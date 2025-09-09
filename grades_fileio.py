import json
import csv
from typing import List
from student import Student
from pathlib import Path

def save_to_json(students: List[Student], filename: str):
    """Save students to JSON file"""
    data = [student.to_dict() for student in students]
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_from_json(filename: str) -> List[Student]:
    """Load students from JSON file"""
    if not Path(filename).exists():
        return []
    
    with open(filename, 'r') as f:
        data = json.load(f)
    
    return [Student.from_dict(item) for item in data]

def save_to_csv(students: List[Student], filename: str):
    """Save students to CSV file"""
    if not students:
        return
        
    fieldnames = ['student_id', 'name', 'age', 'class_name']
    all_subjects = set()
    for student in students:
        all_subjects.update(student.subjects.keys())
    
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames + sorted(all_subjects))
        writer.writeheader()
        for student in students:
            row = student.to_dict()
            row.update(student.subjects)
            writer.writerow(row)

def load_from_csv(filename: str) -> List[Student]:
    """Load students from CSV file"""
    if not Path(filename).exists():
        return []
    
    students = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            student = Student(
                row['student_id'],
                row['name'],
                int(row['age']),
                row['class_name']
            )
            for subject, grade in row.items():
                if subject not in ['student_id', 'name', 'age', 'class_name'] and grade:
                    student.add_subject(subject, float(grade))
            students.append(student)
    
    return students