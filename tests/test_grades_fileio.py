import os
import tempfile
from student import Student
from grades_fileio import save_to_json, load_from_json, save_to_csv, load_from_csv

class TestFileIO:
    @pytest.fixture
    def sample_students(self):
        s1 = Student("001", "John Doe", 18, "12A")
        s1.add_subject("Math", 90)
        
        s2 = Student("002", "Jane Smith", 17, "11B")
        s2.add_subject("Math", 85)
        s2.add_subject("Science", 92)
        
        return [s1, s2]
    
    def test_json_roundtrip(self, sample_students):
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            try:
                # Save to JSON
                save_to_json(sample_students, tmp.name)
                
                # Load from JSON
                loaded = load_from_json(tmp.name)
                
                # Verify data
                assert len(loaded) == 2
                assert loaded[0].name == "John Doe"
                assert loaded[0].subjects["Math"] == 90
                assert loaded[1].name == "Jane Smith"
                assert loaded[1].subjects["Science"] == 92
            finally:
                os.unlink(tmp.name)
    
    def test_csv_roundtrip(self, sample_students):
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            try:
                # Save to CSV
                save_to_csv(sample_students, tmp.name)
                
                # Load from CSV
                loaded = load_from_csv(tmp.name)
                
                # Verify data
                assert len(loaded) == 2
                assert loaded[0].name == "John Doe"
                assert loaded[0].subjects["Math"] == 90.0
                assert loaded[1].name == "Jane Smith"
                assert loaded[1].subjects["Science"] == 92.0
                assert loaded[1].subjects["Math"] == 85.0
            finally:
                os.unlink(tmp.name)