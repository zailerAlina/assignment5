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

target_group = input("Введіть назву ОДНІЄЇ групи для експорту: ")

fieldnames = ['Id', 'Прізвище', 'Ім\'я', 'Група',
              'Основи програмування', 'Лінійна алгебра',
              'Проекційна геометрія', 'Математичний аналіз',
              'Середня оцінка']

filename = f"{target_group}.csv"

with open(filename, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for student in all_students:
        if student["Група"] == target_group:
            writer.writerow(student)

print(f"Завершено. Створено файл {filename}.")