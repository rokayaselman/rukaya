Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import csv
try:
    
    with open('question.csv') as file
        reader=csv.reader(file)
        question=[]
        answer=[]
        for row in reader:
            answer.append(raw[1])
            question.append(raw[0])
except Tes:
    print("الملف",'question.csv',"غير موجود")
    exit()
except Tess:
    print("تحقق من الملف")
    exit()
nam=input("write your name:")

for i in range(len(question)):
    answer=input(question[i]+" ")
    if answer==answer[i]:
        print("ok")