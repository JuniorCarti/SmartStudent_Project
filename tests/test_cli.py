from cli_interface import StudentCLI
from student import Student

class TestCLI:
    def test_add_student(self, monkeypatch, capsys):
        cli = StudentCLI()
        cli.students = []  # Ensure empty list
        
        # Simulate user input
        inputs = [
            "001",         # Student ID
            "Test Student", # Name
            "18",          # Age
            "12A",         # Class
            "Math",        # Subject
            "90",          # Grade
            "",            # No more subjects
        ]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
        
        cli.add_student()
        
        # Verify output
        captured = capsys.readouterr()
        assert "Student Test Student added successfully" in captured.out
        
        # Verify data
        assert len(cli.students) == 1
        assert cli.students[0].name == "Test Student"
        assert "Math" in cli.students[0].subjects
    
    def test_view_students_empty(self, capsys):
        cli = StudentCLI()
        cli.students = []
        cli.view_students()
        
        captured = capsys.readouterr()
        assert "No students found" in captured.out
    
    def test_view_students_with_data(self, capsys):
        cli = StudentCLI()
        s = Student("001", "John Doe", 18, "12A")
        s.add_subject("Math", 90)
        cli.students = [s]
        
        cli.view_students()
        
        captured = capsys.readouterr()
        assert "John Doe" in captured.out
        assert "Math" in captured.out
        assert "90" in captured.out