"""Workshop CODING STANDARDS"""


class Student:
    """Functions with the requirements"""
    def __init__(self, student_id, name):
        """Init process"""
        if not student_id.strip() or not name.strip():
            raise ValueError("Student ID and name cannot be empty.")

        self.student_id = student_id.strip()
        self.name = name.strip()
        self.grades = []
        self.passed = False
        self.honor_roll = False
        self.letter_grade = "N/A"

    def add_grade(self, grade):
        """Adding grades function"""
        if not isinstance(grade, (int, float)):
            print(f"Invalid grade '{grade}': must be a number.")
            return
        if not 0 <= grade <= 100:
            print(f"Invalid grade '{grade}': must be between 0 and 100.")
            return
        self.grades.append(grade)

    def calculate_average(self):
        """Calculate average fucntion"""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def determine_letter_grade(self):
        """Determine Letter Grade fucntion"""
        avg = self.calculate_average()
        if avg >= 90:
            self.letter_grade = 'A'
        elif avg >= 80:
            self.letter_grade = 'B'
        elif avg >= 70:
            self.letter_grade = 'C'
        elif avg >= 60:
            self.letter_grade = 'D'
        else:
            self.letter_grade = 'F'

    def evaluate_pass_status(self):
        """Evaluate Pass Status"""
        self.passed = self.calculate_average() >= 60

    def evaluate_honor_roll(self):
        """Evaluate Honor rolls"""
        self.honor_roll = self.calculate_average() >= 90

    def delete_grade_by_index(self, index):
        """Delete Grade Index"""
        try:
            removed = self.grades[index]
            del self.grades[index]
            print(f"Removed grade at index {index}: {removed}")
        except IndexError:
            print(f"Error: No grade found at index {index}.")

    def delete_grade_by_value(self, value):
        """Delete Grade Value"""
        try:
            self.grades.remove(value)
            print(f"Removed grade with value: {value}")
        except ValueError:
            print(f"Error: Grade with value {value} not found.")

    def generate_summary_report(self):
        """Generate Summary Report"""
        self.determine_letter_grade()
        self.evaluate_pass_status()
        self.evaluate_honor_roll()

        report = (
            f"=== Student Summary ===\n"
            f"ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Grades Count: {len(self.grades)}\n"
            f"Average Grade: {self.calculate_average():.2f}\n"
            f"Letter Grade: {self.letter_grade}\n"
            f"Passed: {'Yes' if self.passed else 'No'}\n"
            f"Honor Roll: {'Yes' if self.honor_roll else 'No'}\n"
        )
        return report


def start_run():
    """Run the class and fucntions"""
    try:
        student = Student("001", "Raúl León")

        student.add_grade(95)
        student.add_grade(89.5)
        student.add_grade("Quedado")    # Invalid
        student.add_grade(-9)          # Invalid
        student.add_grade(74)

        student.delete_grade_by_index(10)   # Invalid index
        student.delete_grade_by_value(100) # Not in list

        student.delete_grade_by_index(2)    # Valid index
        student.delete_grade_by_value(89.5) # Valid value

        print(student.generate_summary_report())

    except ValueError as e:
        print(f"Failed to create student: {e}")


if __name__ == "__main__":
    start_run()
