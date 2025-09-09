from typing import List, Dict, Tuple, Optional
from student import Student
import matplotlib.pyplot as plt
import seaborn as sns
from colorama import Fore, Style
from dataclasses import dataclass
import statistics

@dataclass
class GradeStats:
    average: float
    median: float
    best_subject: Tuple[str, float]
    worst_subject: Tuple[str, float]

def calculate_average_grade(student: Student) -> float:
    """Basic average grade calculation"""
    if not student.subjects:
        return 0.0
    return sum(student.subjects.values()) / len(student.subjects)

def calculate_grade_stats(student: Student) -> GradeStats:
    """Comprehensive grade statistics"""
    if not student.subjects:
        return GradeStats(0.0, 0.0, ("None", 0), ("None", 0))
    
    grades = list(student.subjects.values())
    subjects = list(student.subjects.items())
    
    return GradeStats(
        average=sum(grades)/len(grades),
        median=statistics.median(grades),
        best_subject=max(subjects, key=lambda x: x[1]),
        worst_subject=min(subjects, key=lambda x: x[1])
    )

def search_student(students: List[Student], query: str, by_id: bool = False) -> List[Student]:
    """Search students by name or ID"""
    results = []
    query = query.lower()
    for student in students:
        target = student.student_id if by_id else student.name
        if query in target.lower():
            results.append(student)
    return results

def sort_students(students: List[Student], by: str = 'name', descending: bool = False) -> List[Student]:
    """Sort students by name or average grade"""
    if by == 'name':
        return sorted(students, key=lambda x: x.name.lower(), reverse=descending)
    elif by == 'grade':
        return sorted(students, key=lambda x: calculate_average_grade(x), reverse=descending)
    else:
        raise ValueError("Invalid sort criteria. Use 'name' or 'grade'")

def visualize_grades(students: List[Student]):
    """Generate grade distribution visualizations"""
    if not students:
        print(f"{Fore.YELLOW}No students to visualize{Style.RESET_ALL}")
        return
    
    grades = [grade for s in students for grade in s.subjects.values()]
    
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    sns.histplot(grades, bins=10, kde=True)
    plt.title("Grade Distribution")
    
    plt.subplot(1, 2, 2)
    sns.boxplot(x=grades)
    plt.title("Grade Spread")
    
    plt.tight_layout()
    plt.savefig("grade_analysis.png")
    plt.show()