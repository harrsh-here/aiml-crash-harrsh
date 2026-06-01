# Description: Manages writing and processing student metrics using the csv module and DictWriter.

import csv

def generate_student_data(filename: str) -> None:
    fieldnames = ['name', 'math', 'science', 'english']
    students = [
        {'name': 'Govind', 'math': '85', 'science': '92', 'english': '88'},
        {'name': 'Gaurav', 'math': '70', 'science': '65', 'english': '78'},
        {'name': 'Dheeraj', 'math': '95', 'science': '98', 'english': '92'}
    ]
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

def calculate_grade(avg: float) -> str:
    if avg >= 90: return 'A'
    elif avg >= 80: return 'B'
    elif avg >= 70: return 'C'
    elif avg >= 60: return 'D'
    return 'F'

def process_results(source_csv: str, output_csv: str) -> None:
    results = []
    with open(source_csv, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['name']
            math = float(row['math'])
            science = float(row['science'])
            english = float(row['english'])
            avg = (math + science + english) / 3
            results.append({
                'name': name,
                'average': f"{avg:.2f}",
                'grade': calculate_grade(avg)
            })

    with open(output_csv, mode='w', newline='') as file:
        fieldnames = ['name', 'average', 'grade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

if __name__ == "__main__":
    generate_student_data('Day_3_Tasks/students.csv')
    process_results('Day_3_Tasks/students.csv', 'Day_3_Tasks/results.csv')
    
    with open('Day_3_Tasks/results.csv', mode='r') as f:
        print(f.read())