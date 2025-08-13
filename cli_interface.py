from typing import List, Optional
from student import Student
from operations import search_student, sort_students, calculate_average_grade, visualize_grades
from grades_fileio import save_to_json, load_from_json, save_to_csv, load_from_csv
from colorama import Fore, Back, Style, init

init(autoreset=True)

class StudentCLI:
    def __init__(self):
        self.students: List[Student] = []
        self.load_data()
    
    def load_data(self, filename: str = 'students.json'):
        try:
            self.students = load_from_json(filename)
            print(f"{Fore.GREEN}✓ Loaded {len(self.students)} students{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}✗ Error loading data: {e}{Style.RESET_ALL}")
            self.students = []

    def display_menu(self):
        print(f"\n{Back.BLUE}{Fore.WHITE} SmartStudent Management System {Style.RESET_ALL}")
        print(f"{Fore.CYAN}1.{Style.RESET_ALL} Add New Student")
        print(f"{Fore.CYAN}2.{Style.RESET_ALL} View All Students")
        print(f"{Fore.CYAN}3.{Style.RESET_ALL} Search Student")
        print(f"{Fore.CYAN}4.{Style.RESET_ALL} Edit Student")
        print(f"{Fore.CYAN}5.{Style.RESET_ALL} Delete Student")
        print(f"{Fore.CYAN}6.{Style.RESET_ALL} Calculate Average Grade")
        print(f"{Fore.CYAN}7.{Style.RESET_ALL} Sort Students")
        print(f"{Fore.CYAN}8.{Style.RESET_ALL} Save Data")
        print(f"{Fore.CYAN}9.{Style.RESET_ALL} Load Data")
        print(f"{Fore.MAGENTA}10.{Style.RESET_ALL} Visualize Grades")
        print(f"{Fore.RED}0.{Style.RESET_ALL} Exit")

    def get_user_choice(self) -> int:
        while True:
            try:
                choice = int(input(f"{Fore.YELLOW}Enter your choice (0-10): {Style.RESET_ALL}"))
                if 0 <= choice <= 10:
                    return choice
                print(f"{Fore.RED}Please enter a number between 0 and 10.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Invalid input. Please enter a number.{Style.RESET_ALL}")

    def add_student(self):
        print(f"\n{Back.BLUE}{Fore.WHITE} ADD NEW STUDENT {Style.RESET_ALL}")
        student_id = input(f"{Fore.YELLOW}Enter Student ID:{Style.RESET_ALL} ").strip()
        name = input(f"{Fore.YELLOW}Enter Full Name:{Style.RESET_ALL} ").strip()
        
        while True:
            try:
                age = int(input(f"{Fore.YELLOW}Enter Age:{Style.RESET_ALL} ").strip())
                if age > 0:
                    break
                print(f"{Fore.RED}Age must be positive.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Please enter a valid number for age.{Style.RESET_ALL}")
        
        class_name = input(f"{Fore.YELLOW}Enter Class Name:{Style.RESET_ALL} ").strip()
        student = Student(student_id, name, age, class_name)
        
        while True:
            print(f"\n{Fore.CYAN}Current Subjects:{Style.RESET_ALL}", student.subjects)
            subject = input(f"{Fore.YELLOW}Enter subject name (blank to finish):{Style.RESET_ALL} ").strip()
            if not subject:
                break
            
            while True:
                try:
                    grade = float(input(f"{Fore.YELLOW}Enter grade for {subject} (0-100):{Style.RESET_ALL} ").strip())
                    if 0 <= grade <= 100:
                        student.add_subject(subject, grade)
                        break
                    print(f"{Fore.RED}Grade must be between 0 and 100.{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}Please enter a valid number for grade.{Style.RESET_ALL}")
        
        self.students.append(student)
        print(f"\n{Fore.GREEN}✓ Student {name} added successfully!{Style.RESET_ALL}")

    def view_students(self, students: Optional[List[Student]] = None):
        students_to_display = students if students is not None else self.students
        
        if not students_to_display:
            print(f"\n{Fore.YELLOW}No students found.{Style.RESET_ALL}")
            return
        
        print(f"\n{Back.BLUE}{Fore.WHITE} STUDENT LIST {Style.RESET_ALL}")
        for i, student in enumerate(students_to_display, 1):
            avg_grade = calculate_average_grade(student)
            color = Fore.GREEN if avg_grade >= 75 else Fore.YELLOW if avg_grade >= 50 else Fore.RED
            print(f"{color}{i}. {student.name} (ID: {student.student_id})")
            print(f"   Age: {student.age}, Class: {student.class_name}")
            print(f"   Subjects: {len(student.subjects)}, Avg Grade: {avg_grade:.2f}")
            print("-" * 40 + Style.RESET_ALL)

    def search_student(self):
        if not self.students:
            print(f"\n{Fore.YELLOW}No students available to search.{Style.RESET_ALL}")
            return

        print("\nSearch Options:")
        print("1. By Name")
        print("2. By ID")
        
        while True:
            try:
                search_type = int(input("Enter search method (1-2): "))
                if search_type in (1, 2):
                    break
                print(f"{Fore.RED}Please enter 1 or 2.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Invalid input. Please enter a number.{Style.RESET_ALL}")
        
        query = input("Enter search term: ").strip()
        results = search_student(self.students, query, by_id=(search_type == 2))
        
        if results:
            print(f"\n{Fore.GREEN}Found {len(results)} matching students:{Style.RESET_ALL}")
            self.view_students(results)
        else:
            print(f"\n{Fore.YELLOW}No matching students found.{Style.RESET_ALL}")

    def edit_student(self):
        if not self.students:
            print(f"\n{Fore.YELLOW}No students available to edit.{Style.RESET_ALL}")
            return
        
        self.view_students()
        
        while True:
            try:
                choice = int(input(f"{Fore.YELLOW}Enter student number to edit (0 to cancel): {Style.RESET_ALL}"))
                if 0 <= choice <= len(self.students):
                    break
                print(f"{Fore.RED}Please enter a number between 0 and {len(self.students)}{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Invalid input. Please enter a number.{Style.RESET_ALL}")
        
        if choice == 0:
            return
        
        student = self.students[choice - 1]
        print(f"\n{Back.BLUE}Editing {student.name}{Style.RESET_ALL}")
        
        name = input(f"Enter new name ({student.name}): ").strip() or student.name
        age_input = input(f"Enter new age ({student.age}): ").strip()
        age = int(age_input) if age_input else student.age
        class_name = input(f"Enter new class ({student.class_name}): ").strip() or student.class_name
        
        student.edit_info(name, age, class_name)
        
        while True:
            print(f"\n{Fore.CYAN}Current Subjects:{Style.RESET_ALL}")
            for sub, grade in student.subjects.items():
                print(f"- {sub}: {grade}")
            
            print("\n1. Add/Update Subject")
            print("2. Remove Subject")
            print("3. Finish Editing")
            
            sub_choice = input(f"{Fore.YELLOW}Choose subject action (1-3): {Style.RESET_ALL}").strip()
            
            if sub_choice == '3':
                break
            elif sub_choice == '1':
                subject = input("Enter subject name: ").strip()
                while True:
                    try:
                        grade = float(input(f"Enter grade for {subject} (0-100): ").strip())
                        if 0 <= grade <= 100:
                            student.add_subject(subject, grade)
                            print(f"{Fore.GREEN}✓ {subject} grade updated.{Style.RESET_ALL}")
                            break
                        print(f"{Fore.RED}Grade must be between 0 and 100.{Style.RESET_ALL}")
                    except ValueError:
                        print(f"{Fore.RED}Please enter a valid number for grade.{Style.RESET_ALL}")
            elif sub_choice == '2':
                subject = input("Enter subject name to remove: ").strip()
                if subject in student.subjects:
                    del student.subjects[subject]
                    print(f"{Fore.GREEN}✓ {subject} removed.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Subject not found.{Style.RESET_ALL}")
        
        print(f"\n{Fore.GREEN}✓ Student information updated successfully!{Style.RESET_ALL}")

    def delete_student(self):
        if not self.students:
            print(f"\n{Fore.YELLOW}No students available to delete.{Style.RESET_ALL}")
            return
        
        self.view_students()
        
        while True:
            try:
                choice = int(input(f"{Fore.YELLOW}Enter student number to delete (0 to cancel): {Style.RESET_ALL}"))
                if 0 <= choice <= len(self.students):
                    break
                print(f"{Fore.RED}Please enter a number between 0 and {len(self.students)}{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Invalid input. Please enter a number.{Style.RESET_ALL}")
        
        if choice == 0:
            return
        
        student = self.students.pop(choice - 1)
        print(f"\n{Fore.GREEN}✓ Student {student.name} has been deleted.{Style.RESET_ALL}")

    def calculate_average(self):
        if not self.students:
            print(f"\n{Fore.YELLOW}No students available.{Style.RESET_ALL}")
            return
        
        self.view_students()
        
        while True:
            try:
                choice = int(input(f"{Fore.YELLOW}Enter student number to calculate average (0 to cancel): {Style.RESET_ALL}"))
                if 0 <= choice <= len(self.students):
                    break
                print(f"{Fore.RED}Please enter a number between 0 and {len(self.students)}{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Invalid input. Please enter a number.{Style.RESET_ALL}")
        
        if choice == 0:
            return
        
        student = self.students[choice - 1]
        avg = calculate_average_grade(student)
        
        print(f"\n{Back.BLUE}Average grade for {student.name}{Style.RESET_ALL}")
        if student.subjects:
            for subject, grade in student.subjects.items():
                print(f"- {subject}: {grade}")
            print(f"\nOverall Average: {avg:.2f}")
        else:
            print(f"{Fore.YELLOW}No subjects/grades recorded for this student.{Style.RESET_ALL}")

    def sort_students(self):
        if not self.students:
            print(f"\n{Fore.YELLOW}No students available to sort.{Style.RESET_ALL}")
            return
        
        print("\nSort Students By:")
        print("1. Name (A-Z)")
        print("2. Name (Z-A)")
        print("3. Grade (High-Low)")
        print("4. Grade (Low-High)")
        
        while True:
            try:
                choice = int(input(f"{Fore.YELLOW}Enter sort method (1-4): {Style.RESET_ALL}"))
                if 1 <= choice <= 4:
                    break
                print(f"{Fore.RED}Please enter a number between 1 and 4.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Invalid input. Please enter a number.{Style.RESET_ALL}")
        
        if choice in (1, 2):
            sorted_students = sort_students(self.students, by='name', descending=(choice == 2))
        else:
            sorted_students = sort_students(self.students, by='grade', descending=(choice == 3))
        
        print(f"\n{Back.BLUE}Sorted Students{Style.RESET_ALL}")
        self.view_students(sorted_students)

    def save_data(self):
        if not self.students:
            print(f"\n{Fore.YELLOW}No student data to save.{Style.RESET_ALL}")
            return
        
        print("\nSave Data To:")
        print("1. JSON File")
        print("2. CSV File")
        
        while True:
            try:
                choice = int(input(f"{Fore.YELLOW}Enter file format (1-2): {Style.RESET_ALL}"))
                if choice in (1, 2):
                    break
                print(f"{Fore.RED}Please enter 1 or 2.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Invalid input. Please enter a number.{Style.RESET_ALL}")
        
        filename = input(f"{Fore.YELLOW}Enter filename (without extension): {Style.RESET_ALL}").strip()
        if not filename:
            filename = "students"
        
        try:
            if choice == 1:
                save_to_json(self.students, f"{filename}.json")
            else:
                save_to_csv(self.students, f"{filename}.csv")
            print(f"\n{Fore.GREEN}✓ Data saved successfully!{Style.RESET_ALL}")
        except Exception as e:
            print(f"\n{Fore.RED}✗ Error saving data: {e}{Style.RESET_ALL}")

    def load_data_menu(self):
        print("\nLoad Data From:")
        print("1. JSON File")
        print("2. CSV File")
        
        while True:
            try:
                choice = int(input(f"{Fore.YELLOW}Enter file format (1-2): {Style.RESET_ALL}"))
                if choice in (1, 2):
                    break
                print(f"{Fore.RED}Please enter 1 or 2.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Invalid input. Please enter a number.{Style.RESET_ALL}")
        
        filename = input(f"{Fore.YELLOW}Enter filename (with extension): {Style.RESET_ALL}").strip()
        
        try:
            if choice == 1:
                self.students = load_from_json(filename)
            else:
                self.students = load_from_csv(filename)
            print(f"\n{Fore.GREEN}✓ Loaded {len(self.students)} students from {filename}{Style.RESET_ALL}")
        except FileNotFoundError:
            print(f"\n{Fore.RED}✗ File not found.{Style.RESET_ALL}")
        except Exception as e:
            print(f"\n{Fore.RED}✗ Error loading data: {e}{Style.RESET_ALL}")

    def show_visualization(self):
        if not self.students:
            print(f"\n{Fore.YELLOW}No student data to visualize.{Style.RESET_ALL}")
            return
        
        try:
            visualize_grades(self.students)
            print(f"\n{Fore.GREEN}✓ Visualization generated successfully!{Style.RESET_ALL}")
        except Exception as e:
            print(f"\n{Fore.RED}✗ Error generating visualization: {e}{Style.RESET_ALL}")

    def run(self):
        print(f"{Back.BLUE}{Fore.WHITE} Welcome to SmartStudent Management System {Style.RESET_ALL}")
        
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            
            if choice == 0:
                print(f"\n{Fore.MAGENTA}Goodbye!{Style.RESET_ALL}")
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
            elif choice == 10:
                self.show_visualization()
            
            input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")