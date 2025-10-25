import csv
all_students = []

with open('dataset.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        all_students.append(row)

for student in all_students:
    grades = [
        float (student['Основи програмування']),
        float (student['Лінійна алгебра']),
        float (student['Проекційна геометрія']),
        float (student['Математичний аналіз']),
    ]
    s=sum(grades)
    l=len(grades)
    student['Середня оцінка'] = round(s//l, 2)

