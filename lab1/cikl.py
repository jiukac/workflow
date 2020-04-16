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
    },
    {"name": u"Владимир",
     "group": "БАП-1952",
     "age":21,
     "marks":[3,4,5,4,5]
     }
]
def shitaloshka():
    Lush=[]
    a = []
    x=int((len(groupmates)))
    for i in range(x):
        a.append(groupmates[i])
    chisla = a[0].get('marks')
    sum=0
    sr=0
    d=0
    summ=0
    for i in range(len(a)):
        chisla = a[i].get('marks')
        for i in range(len(chisla)):
            sum+= chisla[i]
            sr += 1
        sred=sum/sr
    for i in range(len(chisla)):
            summ+= chisla[i]
            d+=1
            sr_o_stu=summ/d
            sravnenie=sred
            if sravnenie > sr_o_stu :
             Lush.append(groupmates[i])
    print ((Lush))
z=shitaloshka()
print(z)

