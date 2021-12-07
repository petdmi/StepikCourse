# from debugg import anotherfunc
#
# def my_func(a,b,c):
#     print('Хочу поделить')
#     print(c)
#     anotherfunc()
#     c *= 100
#     a *= c
#     return a/b
#
#
#
# print('abc')
# d = 3
# print(my_func(1,1,1))
# m = 4
# l = [1,2,3,4,5]


name1 = "Tom"
height1 = 1.90
weight1 = 80

name2 = "Katy"
height2 = 1.70
weight2 = 60

name3 = "Bob"
height3 = 2
weight3 = 150


def bmi_calc(name,height,weight):
    bmi = weight / height ** 2
    print('Индекс массы тела равен ',bmi)
    if bmi < 25:
        return name + " не имеет лишнего веса"
    else:
        return name + "  имеет лишний вес"


bmi1 = bmi_calc(name1,height1,weight1)
bmi2 = bmi_calc(name2,height2,weight2)
bmi3 = bmi_calc(name3,height3,weight3)

print(bmi1)
print(bmi2)
print(bmi3)


#1 Функция конверта миль в киллометры
def convert(miles):
    return miles*1.609


a = convert(10)
print(a)

#2 area(a,b) функция подсчета плошади прямоугольника
def area(a,b):
    return a*b

square1 = area(5,10)
print(square1)

#Функция is_even(a) четная или нечетная число
def is_even(a):
    if a % 2 == 0:
        print("Четное")
    else:
        print('Нечетное')

chislo = is_even(15)
