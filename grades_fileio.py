import json
import csv
from typing import List, Dict
from student import Student
from pathlib import Path

def save_to_json(students: List[Student], filename: str) -> None:
    """
    Save student data to a JSON file.
    
    Args:
        students: List of Student objects
        filename: Name of the file to save to
    """
    data = [student.to_dict() for student in students]
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_from_json(filename: str) -> List[Student]:
    """
    Load student data from a JSON file.
    
    Args:
        filename: Name of the file to load from
        
    Returns:
        List of Student objects
    """
    if not Path(filename).exists():
        return []
    
    with open(filename, 'r') as f:
        data = json.load(f)
    
    return [Student.from_dict(item) for item in data]

def save_to_csv(students: List[Student], filename: str) -> None:
    """
    Save student data to a CSV file.
    
    Args:
        students: List of Student objects
        filename: Name of the file to save to
    """
    if not students:
        return
        
    fieldnames = ['student_id', 'name', 'age', 'class_name']
    # Get all unique subject names
    all_subjects = set()
    for student in students:
        all_subjects.update(student.subjects.keys())
    
    fieldnames.extend(sorted(all_subjects))
    
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for student in students:
            row = {
                'student_id': student.student_id,
                'name': student.name,
                'age': student.age,
                'class_name': student.class_name
            }
            row.update(student.subjects)
            writer.writerow(row)

def load_from_csv(filename: str) -> List[Student]:
    """
    Load student data from a CSV file.
    
    Args:
        filename: Name of the file to load from
        
    Returns:
        List of Student objects
    """
    if not Path(filename).exists():
        return []
    
    students = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            student_id = row.pop('student_id')
            name = row.pop('name')
            age = int(row.pop('age'))
            class_name = row.pop('class_name')
            
            student = Student(student_id, name, age, class_name)
            
            # Add subjects (filter out empty grades)
            for subject, grade in row.items():
                if grade:  # Only add if grade exists
                    try:
                        student.add_subject(subject, float(grade))
                    except ValueError:
                        continue
            
            students.append(student)
    
    return students