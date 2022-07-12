import random

# Напишите программу,
# которая принимает на вход строку, и
# отслеживает, сколько раз
# каждый символ уже встречался


#

# my_dict = {"Hi": 1, "my": 1, "name": 1, "hi": 2}
from pprint import pprint

my_dict = {}
test_str = "Hi my name hi hi"

for l in test_str.split():
    # 1. Если еще нет в словаре
    #    Добавляем в словарь со значением 1
    # 2. Если уже есть в словаре
    #    Увеличиваем значение на 1
    ...

# my_dict[l] = 1


# aaabbc
#
# my_dict["a"] = 3
# my_dict["b"] = 2
# my_dict["c"] = 1
# print(my_dict)


d = {"a": 3, "b": 2, "c": 1}

people_names = ["Алексей", "Анатолий", "Петр", "Иван"]
dogs_names = ["Мартин", "Шарик", "Дружок",
              "Дарман", "Цезарь", "Одиссей", "Эмир",
              "Анда", "Джеки"]

test_data = []
for i in range(30):
    people = random.choice(people_names)
    dog = random.choice(dogs_names)
    test_data.append((dog, random.randint(1, 50), people))
# print(test_data)


data = \
    [
        ('Джеки', 26, 'Петр'),
        ('Одиссей', 21, 'Иван'),
        ('Эмир', 5, 'Анатолий'),
        ('Эмир', 48, 'Алексей'),
        ('Цезарь', 33, 'Иван'),
        ('Дружок', 47, 'Иван'),
        ('Мартин', 46, 'Петр'),
        ('Эмир', 13, 'Алексей'), ('Мартин', 36, 'Анатолий'), ('Одиссей', 17, 'Алексей'), ('Анда', 24, 'Петр'),
        ('Анда', 47, 'Петр'), ('Анда', 31, 'Анатолий'), ('Дружок', 35, 'Анатолий'), ('Шарик', 5, 'Алексей'),
        ('Дарман', 11, 'Анатолий'), ('Шарик', 46, 'Петр'), ('Джеки', 26, 'Петр'), ('Джеки', 47, 'Анатолий'),
        ('Мартин', 28, 'Анатолий'), ('Анда', 43, 'Иван'), ('Цезарь', 20, 'Анатолий'), ('Одиссей', 25, 'Петр'),
        ('Дружок', 13, 'Алексей'), ('Дарман', 25, 'Иван'), ('Дарман', 43, 'Иван'), ('Цезарь', 42, 'Анатолий'),
        ('Дарман', 31, 'Анатолий'), ('Дружок', 26, 'Иван'), ('Цезарь', 23, 'Иван')]

users = {}
# { <Имя пользователя>: [<Имя собаки>,] }
for record in data:
    # record = ('Дарман', 31, 'Анатолий')
    dog = record[0]
    owner = record[2]
    if owner in users:
        users[owner].append(dog)
    else:
        users[owner] = []
        # users = {"Анатолий": []}
        users[owner].append(dog)


print([x for x in range(100)])