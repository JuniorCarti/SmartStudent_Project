# String Processor & Report
def main():
    """
    Main function to process a string and generate a detailed report.
    """
    try:
        # 1. Prompt user to enter a full sentence
        sentence = input("Please enter a full sentence: ").strip()
        
        # Validate input
        if not sentence:
            print("Error: You didn't enter any text!")
            return
        
        # 2. Compute various string metrics
        # a. Number of characters (excluding spaces)
        char_count_no_spaces = len(sentence.replace(" ", ""))
        
        # b. Number of words
        words = sentence.split()
        word_count = len(words)
        
        # c. The sentence in uppercase and lowercase
        uppercase_version = sentence.upper()
        lowercase_version = sentence.lower()
        
        # d. The sentence reversed
        reversed_sentence = sentence[::-1]
        
        # 3. Output a formatted report
        print("\n" + "="*50)
        print("STRING ANALYSIS REPORT")
        print("="*50)
        
        # Format output with aligned indentation
        print(f"{'Original Sentence:':<25} '{sentence}'")
        print(f"{'Character Count (no spaces):':<25} {char_count_no_spaces}")
        print(f"{'Word Count:':<25} {word_count}")
        print(f"{'Uppercase Version:':<25} '{uppercase_version}'")
        print(f"{'Lowercase Version:':<25} '{lowercase_version}'")
        print(f"{'Reversed Sentence:':<25} '{reversed_sentence}'")
        print("="*50)
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()