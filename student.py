class Student:
    """
    A class to represent a student with personal and academic information.
    """
    
    def __init__(self, student_id: str, name: str, age: int, class_name: str):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.class_name = class_name
        self.subjects = {}  # {subject_name: grade}
    
    def add_subject(self, subject_name: str, grade: float):
        """Add a subject with grade validation (0-100)"""
        if not isinstance(grade, (int, float)) or grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100")
        self.subjects[subject_name] = grade
    
    def edit_info(self, name: str = None, age: int = None, class_name: str = None):
        """Edit basic student information"""
        if name: self.name = name
        if age: self.age = age
        if class_name: self.class_name = class_name
    
    def to_dict(self):
        """Convert student to dictionary for serialization"""
        return {
            'student_id': self.student_id,
            'name': self.name,
            'age': self.age,
            'class_name': self.class_name,
            'subjects': self.subjects
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Create Student from dictionary"""
        student = cls(
            data['student_id'],
            data['name'],
            data['age'],
            data['class_name']
        )
        student.subjects = data.get('subjects', {})
        return student
    
    def __str__(self):
        return (f"Student(ID: {self.student_id}, Name: {self.name}, "
                f"Class: {self.class_name}, Subjects: {len(self.subjects)})")