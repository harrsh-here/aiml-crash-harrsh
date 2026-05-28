# Program to classify a student's grade based on obtained marks.

students = [
    {"name": "Amit", "score": 94},
    {"name": "Bhavna", "score": 78}, 
    {"name": "Chetan", "score": 62}, 
    {"name": "Divya", "score": 45}, 
    {"name": "Naman", "score": 88}]


def classify(s): 
    return "A" if s>=90 else "B" if s>=80 else "C" if s>=70 else "D" if s>=60 else "F"

for s in sorted(students, key=lambda x: x["score"], reverse=True):
     print(f"{s['name']}: {classify(s['score'])}")
