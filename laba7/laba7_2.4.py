n = int(input())  # количество сотрудников
vacations = {}  # словарь с графиком отпусков

# заполнение словаря
for i in range(n):
    surname, day, month = input().split()
    if month not in vacations:
        vacations[month] = [surname]
    else:
        vacations[month].append(surname)

# запрос месяца и вывод результата
requested_month = input()
if requested_month in vacations:
    print(' '.join(vacations[requested_month]))
else:
    print()