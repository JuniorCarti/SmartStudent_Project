 """
    A class to represent a student with personal and academic information.
   
    Attributes:
        student_id (str): Unique identifier for the student
        name (str): Full name of the student
        age (int): Age of the student
        class_name (str): Class/grade level of the student
        subjects (dict): Dictionary of subjects and their grades
    """
   
    def __init__(self, student_id: str, name: str, age: int, class_name: str):
        """
        Initialize a new Student instance.
       
        Args:
            student_id: Unique identifier for the student
            name: Full name of the student
            age: Age of the student
            class_name: Class/grade level of the student
        """
        self.student_id = student_id
        self.name = name
        self.age = age
        self.class_name = class_name
        self.subjects = {}
   
    def add_subject(self, subject_name: str, grade: float):
        """
        Add a subject and its grade to the student's record.
       
        Args:
            subject_name: Name of the subject
            grade: Grade received in the subject
        """
        if not isinstance(grade, (int, float)) or grade < 0 or grade > 100:
            raise ValueError("Grade must be a number between 0 and 100")
        self.subjects[subject_name] = grade
   
    def edit_info(self, name: str = None, age: int = None, class_name: str = None):
        """
        Edit basic student information.
       
        Args:
            name: New name (optional)
            age: New age (optional)
            class_name: New class name (optional)
        """
        if name:
            self.name = name
        if age:
            self.age = age
        if class_name:
            self.class_name = class_name
   
    def to_dict(self):
        """
        Convert student information to a dictionary.
       
        Returns:
            dict: Dictionary representation of the student
        """
        return {
            'student_id': self.student_id,
            'name': self.name,
            'age': self.age,
            'class_name': self.class_name,
            'subjects': self.subjects
        }
   
    @classmethod
    def from_dict(cls, data: dict):
        """
        Create a Student instance from a dictionary.
       
        Args:
            data: Dictionary containing student information
           
        Returns:
            Student: New Student instance
        """
        student = cls(
            student_id=data['student_id'],
            name=data['name'],
            age=data['age'],
            class_name=data['class_name']
        )
        student.subjects = data.get('subjects', {})
        return student
   
    def __str__(self):
        """String representation of the student."""
        return (f"Student ID: {self.student_id}\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Class: {self.class_name}\n"
                f"Subjects: {', '.join(self.subjects.keys())}")
