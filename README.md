
# SmartStudent - Student Management System

A command-line student management system built with Python that allows administrators to manage student records, grades, and academic information.

## Features

- 📝 **Student Management**
  - Add new students with personal and academic details
  - Edit existing student information
  - Delete student records
  - View all students in the system

- 🔍 **Search & Filter**
  - Search students by name or ID
  - Filter students by grade range
  - Sort students by name or average grade

- 📊 **Grade Management**
  - Add/update subject grades
  - Calculate individual student averages
  - View complete grade reports

- 💾 **Data Persistence**
  - Save data to JSON or CSV files
  - Load data from previous sessions
  - Automatic data backup on exit

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JuniorCarti/SmartStudent.git
   cd SmartStudent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python main.py
```

### Main Menu Options:
```
1. Add New Student
2. View All Students
3. Search Student
4. Edit Student
5. Delete Student
6. Calculate Average Grade
7. Sort Students
8. Save Data
9. Load Data
0. Exit
```

## Project Structure

```
SmartStudent/
├── main.py                # Main application entry point
├── student.py             # Student class implementation
├── operations.py          # Search and sort operations
├── grades_fileio.py       # Grade calculations and file I/O
├── cli_interface.py       # Command-line interface
├── tests/                 # Unit tests
│   ├── test_student.py
│   ├── test_operations.py
│   ├── test_grades_fileio.py
│   └── test_cli.py
└── requirements.txt       # Dependencies
```

## Development

### Running Tests
```bash
pytest tests/
```

### Branching Strategy
- `main` - Production-ready code
- `develop` - Integration branch
- `feature/*` - Feature branches (one per team member)

### Team Members
1. **Student Class Core** (`feature/student-class-core`)
2. **Search/Sort Operations** (`feature/search-sort`)
3. **Grades & File I/O** (`feature/grades-fileio`)
4. **CLI Interface** (`feature/cli-interface`)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request
