# Data Structures in Python - Student Grading System
# Complete the tasks below using lists, dictionaries, sets, and tuples

# TODO: Task 1 - Organize sample student data
# Create a list of dictionaries containing student information
# Each student should have: name (string), id (int), grades (dict with subjects as keys and grades as values)

students = [
    # Example:
    # {
    #     "name": "Alice Johnson",
    #     "id": 1001,
    #     "grades": {"Math": 85, "English": 92, "Science": 88, "History": 90}
    # },
    # Add more students here...
]


# TODO: Task 1 - Calculate average grade for a student
def calculate_average(student):
    """
    Calculate the average grade for a student.
    Args:
        student (dict): A student dictionary with a 'grades' key
    Returns:
        float: The average grade rounded to 2 decimal places
    """
    # Hint: Use the sum() function and len() to calculate the average
    pass


# TODO: Task 1 - Display all student grades
def display_grades():
    """
    Print a formatted report of all students and their averages.
    """
    pass


# TODO: Task 2 - Find all unique subjects
def get_all_subjects():
    """
    Find all unique subjects offered using a set.
    Returns:
        set: A set of all unique subject names
    """
    # Hint: Iterate through students and their grades, add each subject to a set
    pass


# TODO: Task 2 - Find students who passed all subjects
def get_passing_students(passing_grade=70):
    """
    Find students who scored at least passing_grade in all subjects.
    Args:
        passing_grade (int): Minimum grade to pass (default: 70)
    Returns:
        set: A set of names of students who passed all subjects
    """
    pass


# TODO: Task 2 - Generate a performance summary
def generate_summary():
    """
    Create an immutable summary of class performance.
    Returns:
        tuple: (total_students, subjects_count, passing_count, class_average)
    """
    pass


# TODO: Task 3 - Analyze subject performance
def analyze_subjects():
    """
    Analyze performance by subject and identify areas needing improvement.
    Returns:
        list: List of tuples with (subject, average_grade, needs_improvement)
              where needs_improvement is True if average < 70
    """
    pass


# Main program
if __name__ == "__main__":
    print("=== Student Grading System ===\n")
    
    # Uncomment as you complete each function:
    # display_grades()
    # print(f"Subjects: {get_all_subjects()}")
    # print(f"Passing Students: {get_passing_students()}")
    # print(f"Summary: {generate_summary()}")
    # print(f"Subject Analysis: {analyze_subjects()}")
