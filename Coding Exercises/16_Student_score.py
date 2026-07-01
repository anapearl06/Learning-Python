# Student Scores Report

def generate_score_report(names, scores):
    report = []

    for name, score in zip(names, scores):
        report.append(f"{name} scored {score} marks")

    return report

# Example data
names = ["Amit", "Priya", "Rahul"]
scores = [85, 92, 78]

result = generate_score_report(names, scores)

for line in result:
    print(line)