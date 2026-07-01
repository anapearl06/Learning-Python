# Student Grading System

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"


def generate_student_report(name, score):
    grade = calculate_grade(score)
    return f"{name} has scored {score} and received grade {grade}"


# Take input from the user
name = input("Enter student name: ")
score = int(input("Enter student score: "))

# Print the report
print(generate_student_report(name, score))