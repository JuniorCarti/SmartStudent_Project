import json
import base64
import os
from getpass import getpass
from cryptography.fernet import Fernet

class PasswordVault:
    def __init__(self, vault_file="vault.json", key_file="key.key"):
        self.vault_file = vault_file
        self.key_file = key_file
        self.vault = {}
        self.cipher = self._load_or_create_key()
    
    def _load_or_create_key(self):
        """Load encryption key or create a new one if it doesn't exist"""
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as f:
                key = f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as f:
                f.write(key)
        return Fernet(key)
    
    def _encrypt(self, text):
        """Encrypt text using Fernet encryption"""
        return self.cipher.encrypt(text.encode()).decode()
    
    def _decrypt(self, encrypted_text):
        """Decrypt text using Fernet decryption"""
        return self.cipher.decrypt(encrypted_text.encode()).decode()
    
    def _load_vault(self):
        """Load password vault from file"""
        try:
            if os.path.exists(self.vault_file):
                with open(self.vault_file, 'r') as f:
                    encrypted_data = json.load(f)
                    # Decrypt all passwords when loading
                    decrypted_vault = {}
                    for name, entry in encrypted_data.items():
                        decrypted_vault[name] = {
                            'username': entry['username'],
                            'password': self._decrypt(entry['password'])
                        }
                    self.vault = decrypted_vault
        except (json.JSONDecodeError, Exception) as e:
            print(f"Error loading vault: {e}")
            self.vault = {}
    
    def _save_vault(self):
        """Save password vault to file with encrypted passwords"""
        try:
            # Encrypt all passwords before saving
            encrypted_vault = {}
            for name, entry in self.vault.items():
                encrypted_vault[name] = {
                    'username': entry['username'],
                    'password': self._encrypt(entry['password'])
                }
            
            with open(self.vault_file, 'w') as f:
                json.dump(encrypted_vault, f, indent=2)
        except Exception as e:
            print(f"Error saving vault: {e}")
    
    def add_password(self, name, username, password):
        """
        Add a new password entry to the vault
        
        Args:
            name (str): Identifier for the password (e.g., "gmail")
            username (str): Username or email
            password (str): Password to store
        
        Returns:
            bool: True if successful, False otherwise
        """
        if not name or not username or not password:
            print("Error: All fields are required")
            return False
        
        if name in self.vault:
            print(f"Warning: Entry '{name}' already exists. Overwriting.")
        
        self.vault[name] = {'username': username, 'password': password}
        self._save_vault()
        print(f"Password for '{name}' added successfully!")
        return True
    
    def get_password(self, name):
        """
        Retrieve password entry by name
        
        Args:
            name (str): Name of the password entry to retrieve
        
        Returns:
            dict: Dictionary with username and password, or None if not found
        """
        if name not in self.vault:
            print(f"Error: Entry '{name}' not found")
            return None
        
        return self.vault[name]
    
    def delete_password(self, name):
        """
        Delete a password entry
        
        Args:
            name (str): Name of the password entry to delete
        
        Returns:
            bool: True if deleted, False if not found
        """
        if name not in self.vault:
            print(f"Error: Entry '{name}' not found")
            return False
        
        del self.vault[name]
        self._save_vault()
        print(f"Entry '{name}' deleted successfully!")
        return True
    
    def list_entries(self):
        """
        List all password entries in the vault
        
        Returns:
            list: List of entry names
        """
        return list(self.vault.keys())
    
    def search_entries(self, keyword):
        """
        Search for entries containing keyword in their name
        
        Args:
            keyword (str): Keyword to search for
        
        Returns:
            list: List of matching entry names
        """
        return [name for name in self.vault.keys() if keyword.lower() in name.lower()]

def display_menu():
    """Display the main menu options"""
    print("\n" + "="*50)
    print("          PASSWORD VAULT MANAGER")
    print("="*50)
    print("1. Add new password")
    print("2. Retrieve password")
    print("3. Delete password")
    print("4. List all entries")
    print("5. Search entries")
    print("6. Exit")
    print("="*50)

def get_valid_input(prompt, hidden=False):
    """
    Get validated user input
    
    Args:
        prompt (str): Prompt to display
        hidden (bool): Whether to hide input (for passwords)
    
    Returns:
        str: Validated input
    """
    while True:
        try:
            if hidden:
                user_input = getpass(prompt)
            else:
                user_input = input(prompt).strip()
            
            if user_input:
                return user_input
            else:
                print("Input cannot be empty. Please try again.")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

def main():
    """Main function to run the password vault application"""
    vault = PasswordVault()
    vault._load_vault()
    
    print("Welcome to Password Vault!")
    print("Your passwords are stored securely with encryption.")
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                # Add new password
                name = get_valid_input("Enter entry name (e.g., 'gmail'): ")
                if not name:
                    continue
                
                username = get_valid_input("Enter username/email: ")
                if not username:
                    continue
                
                password = get_valid_input("Enter password: ", hidden=True)
                if not password:
                    continue
                
                vault.add_password(name, username, password)
            
            elif choice == '2':
                # Retrieve password
                name = get_valid_input("Enter entry name to retrieve: ")
                if not name:
                    continue
                
                entry = vault.get_password(name)
                if entry:
                    print(f"\nEntry: {name}")
                    print(f"Username: {entry['username']}")
                    print(f"Password: {entry['password']}")
            
            elif choice == '3':
                # Delete password
                name = get_valid_input("Enter entry name to delete: ")
                if not name:
                    continue
                
                vault.delete_password(name)
            
            elif choice == '4':
                # List all entries
                entries = vault.list_entries()
                if entries:
                    print("\nAll password entries:")
                    for i, entry in enumerate(entries, 1):
                        print(f"{i}. {entry}")
                else:
                    print("No entries found in the vault.")
            
            elif choice == '5':
                # Search entries
                keyword = get_valid_input("Enter search keyword: ")
                if not keyword:
                    continue
                
                results = vault.search_entries(keyword)
                if results:
                    print(f"\nFound {len(results)} matching entries:")
                    for i, result in enumerate(results, 1):
                        print(f"{i}. {result}")
                else:
                    print("No matching entries found.")
            
            elif choice == '6':
                print("Thank you for using Password Vault! Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1-6.")
        
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user. Exiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

# Test functions
def test_password_vault():
    """Test the PasswordVault class functionality"""
    # Create a test vault
    test_vault = PasswordVault("test_vault.json", "test_key.key")
    
    # Test adding passwords
    assert test_vault.add_password("test_gmail", "test@gmail.com", "password123") == True
    assert test_vault.add_password("test_facebook", "fb_user", "fbpass456") == True
    
    # Test retrieving passwords
    entry = test_vault.get_password("test_gmail")
    assert entry is not None
    assert entry['username'] == "test@gmail.com"
    assert entry['password'] == "password123"
    
    # Test listing entries
    entries = test_vault.list_entries()
    assert len(entries) == 2
    assert "test_gmail" in entries
    
    # Test searching
    results = test_vault.search_entries("test")
    assert len(results) == 2
    
    # Test deletion
    assert test_vault.delete_password("test_facebook") == True
    assert test_vault.get_password("test_facebook") is None
    
    # Clean up test files
    if os.path.exists("test_vault.json"):
        os.remove("test_vault.json")
    if os.path.exists("test_key.key"):
        os.remove("test_key.key")
    
    print("All tests passed!")

if __name__ == "__main__":
    # Run tests if requested
    if len(os.sys.argv) > 1 and os.sys.argv[1] == "test":
        test_password_vault()
    else:
        main()