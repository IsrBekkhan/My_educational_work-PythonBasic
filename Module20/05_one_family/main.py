data = {
    ('Сидоров', 'Никита'): 35,
    ('Сидорова', 'Алина'): 34,
    ('Сидоров', 'Павел'): 10,
    ('Михайлов', 'Алексей'): 40,
    ('Михайлова', 'Алена'): 32,
    ('Дрокин', 'Глеб'): 25,
}

surname = input('Введите фамилию: ').title()
temp_surname = surname[:-1]
print()
for keys, age in data.items():
    if keys[0].startswith(temp_surname):
        print(keys[0], keys[1], age)