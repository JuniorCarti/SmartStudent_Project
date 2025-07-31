
from typing import List, Dict, Union
from student import Student

def search_student(students: List[Student], query: str, by_id: bool = False) -> List[Student]:
    """
    Search for students by name or ID.
    
    Args:
        students: List of Student objects
        query: Search term
        by_id: If True, search by student ID; otherwise search by name
        
    Returns:
        List of matching Student objects
    """
    results = []
    query = query.lower()
    
    for student in students:
        if by_id:
            if query in student.student_id.lower():
                results.append(student)
        else:
            if query in student.name.lower():
                results.append(student)
    
    return results

def sort_students(students: List[Student], by: str = 'name', descending: bool = False) -> List[Student]:
    """
    Sort students by name or average grade.
    
    Args:
        students: List of Student objects
        by: Attribute to sort by ('name' or 'grade')
        descending: If True, sort in descending order
        
    Returns:
        Sorted list of Student objects
    """
    if by == 'name':
        return sorted(students, key=lambda x: x.name.lower(), reverse=descending)
    elif by == 'grade':
        return sorted(students, key=lambda x: calculate_average_grade(x), reverse=descending)
    else:
        raise ValueError("Invalid sort criteria. Use 'name' or 'grade'")

def calculate_average_grade(student: Student) -> float:
    """
    Calculate the average grade for a student.
    
    Args:
        student: Student object
        
    Returns:
        Average grade (float) or 0 if no subjects
    """
    if not student.subjects:
        return 0.0
    return sum(student.subjects.values()) / len(student.subjects)

def filter_students_by_grade(students: List[Student], min_grade: float = 0, max_grade: float = 100) -> List[Student]:
    """
    Filter students by grade range.
    
    Args:
        students: List of Student objects
        min_grade: Minimum average grade threshold
        max_grade: Maximum average grade threshold
        
    Returns:
        List of Student objects within the grade range
    """
    return [student for student in students 
            if min_grade <= calculate_average_grade(student) <= max_grade]
