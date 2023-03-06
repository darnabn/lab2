# пример входных данных
n = 3  # число элементов в словаре
dictionary = {
    'Россия': ['Волга', 'Обь'],
    'США': ['Миссисипи', 'Колорадо'],
    'Китай': ['Янцзы', 'Хуанхэ']
}
rivers = ['Волга', 'Янцзы', 'Нил']

# 1. Для каждой реки укажите, в какой стране она протекает.
for river in rivers:
    found = False
    for country, rivers_list in dictionary.items():
        if river in rivers_list:
            print(f"{river} протекает в {country}")
            found = True
    if not found:
        print(f"Для реки {river} не найдена страна")

# 2. Проверьте, есть ли введенное название реки в словаре.
river_to_find = 'Волга'
found = False
for rivers_list in dictionary.values():
    if river_to_find in rivers_list:
        found = True
        break
if found:
    print(f"Река {river_to_find} найдена в словаре")
else:
    print(f"Река {river_to_find} не найдена в словаре")

dictionary['Франция'] = ['Сена']
print(dictionary)