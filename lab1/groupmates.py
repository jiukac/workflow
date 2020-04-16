def print_students(students):
    print (u"Имя студента".ljust(15), \
           u"Группа".ljust(8), \
          u"Возраст".ljust(8), \
          u"Оценки".ljust(20))
    for student in students:
        print (
                student["name"].ljust(15),\
                student["group"].ljust(8), \
                str(student["age"]).ljust(8), \
                str(student["marks"]).ljust(20))
        print ("\n")

mas_stud = []
groupmates = [
    {"name": u"Дарья",
     "group": "БАП-1952",
     "age": 18,
     "marks": [4, 4, 5, 5, 5]
     },
    {"name": u"Анна",
     "group": "БАП-1952",
     "age": 23,
     "marks": [3, 4, 3, 4, 4]
     },
    {"name": u"Игорь",
     "group": "БАП-1952",
     "age": 21,
     "marks": [4, 4, 4, 3, 5]
     },
    {"name": u"Сергей",
     "group": "БАП-1952",
     "age": 28,
     "marks": [4, 4, 5, 4, 5]
    }
]
print_students(groupmates)