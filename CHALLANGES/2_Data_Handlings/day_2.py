"""
=========================================
Day 2 : Student Marks Analyzer
=========================================

Collect student names and their marks, then
generate a detailed marks report.

Features:
✔ Add multiple students
✔ Prevent duplicate student names
✔ Calculate average marks
✔ Find highest marks and topper(s)
✔ Find lowest marks and student(s)
✔ Display total number of students
✔ Show detailed marks report

Concepts Covered:
✔ Dictionaries
✔ Functions
✔ Loops
✔ List Comprehension
✔ max(), min(), sum()
✔ Exception Handling
✔ String Formatting
"""


# Step 1 : Collect Student Data # 

def collect_student_data():
    """Collects student names and marks from the user."""

    students = {}

    while True:

        name = input(
            "\nEnter student name (or type 'done' to finish): "
        ).strip()

        # Stop collecting data when user types "done".
        if name.lower() == "done":
            break

        # Prevent empty student names.
        if not name:
            print("❌ Student name cannot be empty.")
            continue

        # Prevent duplicate student names.
        if name.lower() in {student.lower() for student in students}:
            print("❌ A student with this name already exists.")
            continue

        # Get and validate marks.
        try:

            marks = float(
                input(f"Enter marks for {name}: ")
            )

            if marks < 0:
                print("❌ Marks cannot be negative.")
                continue

            students[name] = marks

            print(f"✅ {name}'s marks added successfully.")

        except ValueError:

            print("❌ Please enter a valid number for marks.")

    return students


# Step 2 : Generate Marks Report # 

def display_report(students):
    """Calculates and displays the complete marks report."""

    # Handle the case where no students were added.
    if not students:

        print("\n📭 No student data available.")
        return

    # Get all marks from the dictionary.
    marks = list(students.values())

    # Calculate basic statistics.
    total_students = len(students)
    average_marks = sum(marks) / total_students
    highest_marks = max(marks)
    lowest_marks = min(marks)

    # Find all students who achieved the highest marks.
    toppers = [
        name
        for name, score in students.items()
        if score == highest_marks
    ]

    # Find all students who achieved the lowest marks.
    lowest_scorers = [
        name
        for name, score in students.items()
        if score == lowest_marks
    ]


    # Display Summary # 

    print("\n" + "=" * 55)
    print("📊 STUDENT MARKS REPORT".center(55))
    print("=" * 55)

    print(f"👥 Total Students : {total_students}")
    print(f"📈 Average Marks  : {average_marks:.2f}")
    print(
        f"🏆 Highest Marks  : "
        f"{highest_marks:g} - {', '.join(toppers)}"
    )
    print(
        f"📉 Lowest Marks   : "
        f"{lowest_marks:g} - {', '.join(lowest_scorers)}"
    )


    # Display Detailed Marks #

    print("\n" + "-" * 55)
    print("📝 DETAILED MARKS")
    print("-" * 55)

    for name, score in students.items():

        print(f"👤 {name:<20} | Marks: {score:g}")

    print("=" * 55)


# Step 3 : Run the Program # 

students = collect_student_data()

display_report(students)