from typing import List, Optional
from student import Student
from operations import search_student, sort_students, calculate_average_grade
from grades_fileio import save_to_json, load_from_json, save_to_csv, load_from_csv

class StudentCLI:
    """
    Command Line Interface for the Student Management System.
    """
    
    def __init__(self):
        self.students: List[Student] = []
        self.load_data()
    
    def load_data(self, filename: str = 'students.json'):
        """Attempt to load data from default file on startup."""
        try:
            self.students = load_from_json(filename)
            print(f"Loaded {len(self.students)} students from {filename}")
        except FileNotFoundError:
            self.students = []
        except Exception as e:
            print(f"Error loading data: {e}")
            self.students = []
    
    def display_menu(self):
        """Display the main menu."""
        print("\nSmartStudent Management System")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Edit Student")
        print("5. Delete Student")
        print("6. Calculate Average Grade")
        print("7. Sort Students")
        print("8. Save Data")
        print("9. Load Data")
        print("0. Exit")
    
    def get_user_choice(self) -> int:
        """Get and validate user menu choice."""
        while True:
            try:
                choice = int(input("Enter your choice (0-9): "))
                if 0 <= choice <= 9:
                    return choice
                print("Please enter a number between 0 and 9.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def add_student(self):
        """Add a new student to the system."""
        print("\nAdd New Student")
        student_id = input("Enter Student ID: ").strip()
        name = input("Enter Full Name: ").strip()
        
        # Validate age
        while True:
            try:
                age = int(input("Enter Age: ").strip())
                if age > 0:
                    break
                print("Age must be positive.")
            except ValueError:
                print("Please enter a valid number for age.")
        
        class_name = input("Enter Class Name: ").strip()
        
        # Create student
        student = Student(student_id, name, age, class_name)
        
        # Add subjects
        while True:
            print("\nCurrent Subjects:", student.subjects)
            subject = input("Enter subject name (or leave blank to finish): ").strip()
            if not subject:
                break
            
            # Validate grade
            while True:
                try:
                    grade = float(input(f"Enter grade for {subject} (0-100): ").strip())
                    if 0 <= grade <= 100:
                        student.add_subject(subject, grade)
                        break
                    print("Grade must be between 0 and 100.")
                except ValueError:
                    print("Please enter a valid number for grade.")
        
        self.students.append(student)
        print(f"\nStudent {name} added successfully!")
    
    def view_students(self, students: Optional[List[Student]] = None):
        """Display all students or a provided list of students."""
        students_to_display = students if students is not None else self.students
        
        if not students_to_display:
            print("\nNo students found.")
            return
        
        print("\nStudent List:")
        for i, student in enumerate(students_to_display, 1):
            avg_grade = calculate_average_grade(student)
            print(f"{i}. {student.name} (ID: {student.student_id})")
            print(f"   Age: {student.age}, Class: {student.class_name}")
            print(f"   Subjects: {len(student.subjects)}, Avg Grade: {avg_grade:.2f}")
            print("-" * 40)
    
    def search_student(self):
        """Search for students by name or ID."""
        print("\nSearch Students")
        print("1. Search by Name")
        print("2. Search by ID")
        
        while True:
            try:
                choice = int(input("Enter search method (1-2): "))
                if choice in (1, 2):
                    break
                print("Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        query = input("Enter search term: ").strip()
        results = search_student(self.students, query, by_id=(choice == 2))
        
        if results:
            print(f"\nFound {len(results)} matching students:")
            self.view_students(results)
        else:
            print("\nNo matching students found.")
    
    def edit_student(self):
        """Edit an existing student's information."""
        if not self.students:
            print("\nNo students available to edit.")
            return
        
        self.view_students()
        
        while True:
            try:
                choice = int(input("Enter student number to edit (0 to cancel): "))
                if 0 <= choice <= len(self.students):
                    break
                print(f"Please enter a number between 0 and {len(self.students)}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        if choice == 0:
            return
        
        student = self.students[choice - 1]
        print(f"\nEditing {student.name}:")
        
        # Edit basic info
        name = input(f"Enter new name ({student.name}): ").strip() or student.name
        age = input(f"Enter new age ({student.age}): ").strip()
        age = int(age) if age else student.age
        class_name = input(f"Enter new class ({student.class_name}): ").strip() or student.class_name
        
        student.edit_info(name, age, class_name)
        
        # Edit subjects
        while True:
            print("\nCurrent Subjects:")
            for sub, grade in student.subjects.items():
                print(f"- {sub}: {grade}")
            
            print("\n1. Add/Update Subject")
            print("2. Remove Subject")
            print("3. Finish Editing")
            
            sub_choice = input("Choose subject action (1-3): ").strip()
            
            if sub_choice == '3':
                break
            elif sub_choice == '1':
                subject = input("Enter subject name: ").strip()
                while True:
                    try:
                        grade = float(input(f"Enter grade for {subject} (0-100): ").strip())
                        if 0 <= grade <= 100:
                            student.add_subject(subject, grade)
                            print(f"{subject} grade updated.")
                            break
                        print("Grade must be between 0 and 100.")
                    except ValueError:
                        print("Please enter a valid number for grade.")
            elif sub_choice == '2':
                subject = input("Enter subject name to remove: ").strip()
                if subject in student.subjects:
                    del student.subjects[subject]
                    print(f"{subject} removed.")
                else:
                    print("Subject not found.")
        
        print("\nStudent information updated successfully!")
    
    def delete_student(self):
        """Delete a student from the system."""
        if not self.students:
            print("\nNo students available to delete.")
            return
        
        self.view_students()
        
        while True:
            try:
                choice = int(input("Enter student number to delete (0 to cancel): "))
                if 0 <= choice <= len(self.students):
                    break
                print(f"Please enter a number between 0 and {len(self.students)}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        if choice == 0:
            return
        
        student = self.students.pop(choice - 1)
        print(f"\nStudent {student.name} has been deleted.")
    
    def calculate_average(self):
        """Calculate and display average grade for a student."""
        if not self.students:
            print("\nNo students available.")
            return
        
        self.view_students()
        
        while True:
            try:
                choice = int(input("Enter student number to calculate average (0 to cancel): "))
                if 0 <= choice <= len(self.students):
                    break
                print(f"Please enter a number between 0 and {len(self.students)}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        if choice == 0:
            return
        
        student = self.students[choice - 1]
        avg = calculate_average_grade(student)
        
        print(f"\nAverage grade for {student.name}:")
        if student.subjects:
            for subject, grade in student.subjects.items():
                print(f"- {subject}: {grade}")
            print(f"\nOverall Average: {avg:.2f}")
        else:
            print("No subjects/grades recorded for this student.")
    
    def sort_students(self):
        """Sort and display students by name or grade."""
        if not self.students:
            print("\nNo students available to sort.")
            return
        
        print("\nSort Students By:")
        print("1. Name (A-Z)")
        print("2. Name (Z-A)")
        print("3. Grade (High-Low)")
        print("4. Grade (Low-High)")
        
        while True:
            try:
                choice = int(input("Enter sort method (1-4): "))
                if 1 <= choice <= 4:
                    break
                print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        if choice in (1, 2):
            sorted_students = sort_students(self.students, by='name', descending=(choice == 2))
        else:
            sorted_students = sort_students(self.students, by='grade', descending=(choice == 3))
        
        print("\nSorted Students:")
        self.view_students(sorted_students)
    
    def save_data(self):
        """Save student data to file."""
        if not self.students:
            print("\nNo student data to save.")
            return
        
        print("\nSave Data To:")
        print("1. JSON File")
        print("2. CSV File")
        
        while True:
            try:
                choice = int(input("Enter file format (1-2): "))
                if choice in (1, 2):
                    break
                print("Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        filename = input("Enter filename (without extension): ").strip()
        if not filename:
            filename = "students"
        
        try:
            if choice == 1:
                save_to_json(self.students, f"{filename}.json")
            else:
                save_to_csv(self.students, f"{filename}.csv")
            print("\nData saved successfully!")
        except Exception as e:
            print(f"\nError saving data: {e}")
    
    def load_data_menu(self):
        """Load student data from file."""
        print("\nLoad Data From:")
        print("1. JSON File")
        print("2. CSV File")
        
        while True:
            try:
                choice = int(input("Enter file format (1-2): "))
                if choice in (1, 2):
                    break
                print("Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        filename = input("Enter filename (with extension): ").strip()
        
        try:
            if choice == 1:
                self.students = load_from_json(filename)
            else:
                self.students = load_from_csv(filename)
            print(f"\nLoaded {len(self.students)} students from {filename}")
        except FileNotFoundError:
            print("\nFile not found.")
        except Exception as e:
            print(f"\nError loading data: {e}")
    
    def run(self):
        """Run the CLI application."""
        print("Welcome to SmartStudent Management System!")
        
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            
            if choice == 0:
                print("\nGoodbye!")
                break
            elif choice == 1:
                self.add_student()
            elif choice == 2:
                self.view_students()
            elif choice == 3:
                self.search_student()
            elif choice == 4:
                self.edit_student()
            elif choice == 5:
                self.delete_student()
            elif choice == 6:
                self.calculate_average()
            elif choice == 7:
                self.sort_students()
            elif choice == 8:
                self.save_data()
            elif choice == 9:
                self.load_data_menu()
            
            input("\nPress Enter to continue...")