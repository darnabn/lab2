# Создание словаря для хранения информации о студентах
students = {
    'John': {
        'email': 'john@example.com',
        'phone': '555-555-5555',
        'major': 'Computer Science'
    },
    'Mary': {
        'email': 'mary@example.com',
        'phone': '555-123-4567',
        'major': 'Biology'
    },
    'Bob': {
        'email': 'bob@example.com',
        'phone': '555-987-6543',
        'major': 'Mathematics'
    }
}

# Функция для добавления нового студента в словарь
def add_student(name, email, phone, major):
    students[name] = {'email': email, 'phone': phone, 'major': major}

# Функция для удаления студента из словаря
def remove_student(name):
    del students[name]

# Функция для изменения контактной информации студента
def update_contact_info(name, email=None, phone=None):
    student = students[name]
    if email:
        student['email'] = email
    if phone:
        student['phone'] = phone

# Функция для поиска студента по имени
def search_student(name):
    if name in students:
        return students[name]
    else:
        return None

# Функция для вывода всех студентов в словаре
def print_students():
    for name, info in students.items():
        print(f"Name: {name}, Email: {info['email']}, Phone: {info['phone']}, Major: {info['major']}")

# Добавление нового студента в словарь
add_student('Alice', 'alice@example.com', '555-111-2222', 'Chemistry')

# Изменение контактной информации студента
update_contact_info('Bob', phone='555-444-4444')

# Поиск студента по имени
print(search_student('Mary'))

# Удаление студента из словаря
remove_student('John')

# Вывод всех студентов в словаре
print_students()
