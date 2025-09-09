from student import Student
from operations import search_student, sort_students, calculate_average_grade

class TestOperations:
    @pytest.fixture
    def sample_students(self):
        s1 = Student("001", "John Doe", 18, "12A")
        s1.add_subject("Math", 90)
        
        s2 = Student("002", "Jane Smith", 17, "11B")
        s2.add_subject("Math", 85)
        s2.add_subject("Science", 92)
        
        s3 = Student("003", "Alice Johnson", 19, "12A")
        s3.add_subject("History", 88)
        
        return [s1, s2, s3]
    
    def test_search_by_name(self, sample_students):
        results = search_student(sample_students, "john")
        assert len(results) == 2  # John Doe and Alice Johnson
        assert results[0].name == "John Doe"
        assert results[1].name == "Alice Johnson"
    
    def test_search_by_id(self, sample_students):
        results = search_student(sample_students, "002", by_id=True)
        assert len(results) == 1
        assert results[0].name == "Jane Smith"
    
    def test_sort_by_name(self, sample_students):
        sorted_students = sort_students(sample_students, by='name')
        assert sorted_students[0].name == "Alice Johnson"
        assert sorted_students[1].name == "Jane Smith"
        assert sorted_students[2].name == "John Doe"
    
    def test_sort_by_grade(self, sample_students):
        sorted_students = sort_students(sample_students, by='grade')
        # Jane has highest average (88.5)
        assert sorted_students[0].name == "Jane Smith"
        assert sorted_students[1].name == "John Doe"  # 90
        assert sorted_students[2].name == "Alice Johnson"  # 88
    
    def test_calculate_average(self, sample_students):
        assert calculate_average_grade(sample_students[0]) == 90.0
        assert calculate_average_grade(sample_students[1]) == 88.5
        assert calculate_average_grade(sample_students[2]) == 88.0