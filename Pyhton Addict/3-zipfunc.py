students_number = int(input("enter the students number : "))
lesson_number = int(input("enter the lesson number : "))

students = []
notlar = []
for i in range(students_number):
    print(f"{i+1}.incı öğrenci için : ")
    students.append(str(i+1) + " Numaralı Öğrenci :"  )
    grades = []
    for j in range(lesson_number):            
        grades.append(float(input(f"{j + 1}. dersin notunu giriniz : ")))
        
    notlar.append(grades)

ortalama = []
for i in notlar:
    ortalama.append(f"ortalama : {round(sum(i)/3, 2)}")
print('*'*50, '\n')
for i in zip(students, ortalama):
    print(*(i) , "\n")

# student, subject = map(int,input().split())
# # s=[map(float,input().split()) for _ in range(subject)]
# s = []
# for i in range(subject):
#     s.append(map(float, input().split()))

# for i in zip(*s):
#     print(sum(i)/subject)

# student_number, lesson_number = map(int, input("öğrencive ders sayısını boşluk bırakarak giriniz :").split())
# notlar =[]
# for i in range(lesson_number):
#     notlar.append(map(float, input("notları giriniz").split()))

# for i in zip(*notlar):
#     print(sum(i)/lesson_number)




# students_number = int(input("enter the students number : "))
# lesson_number = int(input("enter the lesson number : "))

# students = []
# notlar = []
# for i in range(students_number):
#     print(f"{i+1}.incı öğrenci için : ")
#     students.append(str(i+1) + " Numaralı Öğrenci :"  )
#     grades = []
#     for j in range(lesson_number):            
#         grades.append(float(input(f"{j + 1}. dersin notlarını giriniz : ")))
        
#     notlar.append(grades)

# ortalama = []
# for i in notlar:
#     #print(f"ortalama : {round(sum(i)/3, 2)}")
#     ortalama.append(f"ortalama : {round(sum(i)/3, 2)}")

# #print(* list(zip(students, ortalama)))
# for i in zip (* (students, ortalama)):
#     print(i)


# for i in zip(notlar, students):
#     print(sum(i)/lesson_number)
# print(notlar)
# print(students)

# student, lessons = map(int, input().split())
# print("bu student" ,student)
# print("bu subjetc" ,subject)
# s=[map(float,input().split()) for _ in range(subject)]
# b = list(s)
# print("bu s sayısır" , b)
# for i in zip(*s): print(sum(i)/subject)

# X = map(int, input().split())
# #print("bu x sayısıdır", X)
# grades = []
# for i in range(X):
#     grades.append(list(map(float, input().split())))
# for i in zip(*grades):
#     print(sum(i)/X)

# student, subject = map(int,input().split())
# s=[map(float,input().split()) for _ in range(subject)]
# for i in zip(*s): print(sum(i)/subject)

# for i in list(s):
#     print(i)

# __author__ ="Sirius.Star"
# N, X =list(map(int, input().split()))
# notes=[]
# for i in range(X):
#     notes.append(list(map(float, input().split())))
    
# print(notes)
# notes=list(zip(*notes))
# print(notes)
# notes=[sum(x)/X for x in notes]
# #print(*notes, sep='\n')
# print(notes, sep='\n')

# lista = [[25.0, 26.0, 27.0, 28.0], [35.0, 36.0, 37.0, 38.0]]
# listb = list(zip(*lista))
# print(listb)

# lista = [[25.0, 26.0, 27.0, 28.0], [35.0, 36.0, 37.0, 38.0]]
# listb = [[99.0, 78.0, 58.0, 68.0], [120.0, 136.0, 157.0, 388.0]]
# listc = list(zip(lista, listb))
# print(listc)

# lista = [[28,39], [35.0, 36.0]]
# listb = [[99.0, 78.0], [120.0, 136.0]]
# listc = list(zip(lista, listb))
# print(listc)