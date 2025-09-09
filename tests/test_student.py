import pytest
from student import Student

class TestStudent:
    def test_student_creation(self):
        s = Student("001", "John Doe", 18, "12A")
        assert s.name == "John Doe"
        assert s.age == 18
        assert s.class_name == "12A"
        assert s.subjects == {}
    
    def test_add_subject(self):
        s = Student("001", "John Doe", 18, "12A")
        s.add_subject("Math", 90)
        assert "Math" in s.subjects
        assert s.subjects["Math"] == 90
    
    def test_invalid_grade(self):
        s = Student("001", "John Doe", 18, "12A")
        with pytest.raises(ValueError):
            s.add_subject("Math", 150)
        with pytest.raises(ValueError):
            s.add_subject("Math", -10)
    
    def test_edit_info(self):
        s = Student("001", "John Doe", 18, "12A")
        s.edit_info(name="Jane Doe", age=19, class_name="12B")
        assert s.name == "Jane Doe"
        assert s.age == 19
        assert s.class_name == "12B"
    
    def test_to_from_dict(self):
        s = Student("001", "John Doe", 18, "12A")
        s.add_subject("Math", 90)
        data = s.to_dict()
        new_s = Student.from_dict(data)
        assert new_s.name == s.name
        assert new_s.subjects == s.subjects