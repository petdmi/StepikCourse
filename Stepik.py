# # from debugg import anotherfunc
# #
# # def my_func(a,b,c):
# #     print('Хочу поделить')
# #     print(c)
# #     anotherfunc()
# #     c *= 100
# #     a *= c
# #     return a/b
# #
# #
# #
# # print('abc')
# # d = 3
# # print(my_func(1,1,1))
# # m = 4
# # l = [1,2,3,4,5]
#
#
# name1 = "Tom"
# height1 = 1.90
# weight1 = 80
#
# name2 = "Katy"
# height2 = 1.70
# weight2 = 60
#
# name3 = "Bob"
# height3 = 2
# weight3 = 150
#
#
# def bmi_calc(name,height,weight):
#     bmi = weight / height ** 2
#     print('Индекс массы тела равен ',bmi)
#     if bmi < 25:
#         return name + " не имеет лишнего веса"
#     else:
#         return name + "  имеет лишний вес"
#
#
# bmi1 = bmi_calc(name1,height1,weight1)
# bmi2 = bmi_calc(name2,height2,weight2)
# bmi3 = bmi_calc(name3,height3,weight3)
#
# print(bmi1)
# print(bmi2)
# print(bmi3)
#
#
# #1 Функция конверта миль в киллометры
# def convert(miles):
#     return miles*1.609
#
#
# a = convert(10)
# print(a)
#
# #2 area(a,b) функция подсчета плошади прямоугольника
# def area(a,b):
#     return a*b
#
# square1 = area(5,10)
# print(square1)
#
# #Функция is_even(a) четная или нечетная число
# def is_even(a):
#     if a % 2 == 0:
#         print("Четное")
#     else:
#         print('Нечетное')
#
# chislo = is_even(15)
#
#
#
##############################################################################################
#Alishev LIST
#
# a = [3,5,20]
# print(a)
# a.append(15)
# a.append('hi')
# print(a)
# a.append([5,6])
# print(a)
# a.pop()
# print(a)
# a[0] = 100
# print(a)
# a.pop(2)
# print(a)
# b = ['hello', 'goodbye', 'hey']
# print(b)
# temp = b[0]
# b[0] = b[2]
# b[2]  = temp
# print(b)
# b[0],b[2] = b[2], b[0]
# print(b)

##############################################################################################
# #Alishev ЦИКЛЫ FOR
#
# b = [20,30,40,50]
# for num in b:
#     print(num)
#
# total_sum = 0
# for e in b:
#     total_sum += e
# print(total_sum)
#
# x = list(range(1,100))
# print(x)
# for i in range(1,100):
#     print(i)
#
# total_sum2  = 0
# for n in x:
#     total_sum2+=n
# print(total_sum2)


# #Practica
# def my_func(n,k):
#     if n > 20:
#         return 0
#     s = 0
#     for i in range(1,n):
#         if i%2 == 0:
#             s += i**k
#     return s
#
# x = my_func(10,2)
# print(x)
#
# def main():
#     print(my_func(21,5))
#     print(my_func(7,2))
#     print(my_func(20,15))
#
# x = main()
# print(x)
##############################################################################################

# # #Alishev ЦИКЛЫ WHILE
# total = 0
# for i in range (1,5):
#     total += i
# print(total)
#
# total2 = 0
# i1 = 0
# while i1 < 5:
#     total2+=i1
#     i1+=1
##############################################################################################
# my_list = [7,5,4,3,2,1,-5,-10,-15]
# total3 = 0
# i3 = 0
# while my_list[i3] > 0:       #Вообще не рассматривает остальные числа, если доходит до отрицательного
#     total3+=my_list[i3]
#     i3+=1
#
##############################################################################################
# total4 = 0
# for element in my_list:       #Перебером циклом FOR будем проверять каждый элемент (займет больше времени)
#     if element > 0:
#         total4+=element
#
# print(total3)
# print(total4)
##############################################################################################
#
# total6 = 0
# for element1 in my_list:
#     if element1 <=0:
#         break
#     total6+=element1
#
# print(total6,'total6')
##############################################################################################
# ##Мы хотим суммировать все числа списка , пока их сумма меньше 10. Как только сумма чисел > 10 - выходим
# total5 = 0
# i5 = 0
# while total5 < 10 and my_list[i5] > 0:
#     total5+=my_list[i5]
#     i5+=1
# print(total5)
##############################################################################################
# ##Мы хотим суммировать все числа списка , пока их сумма меньше 10. Как только сумма чисел > 10 - выходим
# total7 = 0
# i7 = 0
# for element in my_list:
#     if total7>10:
#         break
#     total7+=element
#     i7+=1
# print(total7, 'total7')
# ##############################################################################################
# my_list = [7,5,4,3,2,1]
# total8 = 0
# i8 = 0
# while i8 < len(my_list) and my_list[i8] > 0:
#     total8+=my_list[i8]
#     i8+=1
# print(total8,'total8')
##############################################################################################
##Practica Alishev
##Найти сумму отрицательных чисел двумя методами
##РЕШЕНИЕ ЗАДАЧИ
##ЧЕРЕЗ ЦИКЛ WHILE
##МОЙ МЕТОД
# my_list = [7,5,4,3,2,1,-5,-10,-15, -20, -30]
# total = 0
# i = 0
# while my_list[i]>0:
#     i+=1
#     pass
# else:
#     while i<len(my_list) and my_list[i]<0:
#         total+=my_list[i]
#         i+=1
# print(total,'total While')
# ##############################################################################################
# ##Найти сумму отрицательных чисел двумя методами
# ##РЕШЕНИЕ ЗАДАЧИ
# ##ЧЕРЕЗ ЦИКЛ WHILE
# ## МЕТОД АВТОРА
# numbers = [7,5,4,3,2,1,-5,-10,-15, -20, -30]
# total = 0
# i = len(numbers) - 1
# while i >= 0 and numbers[i] < 0:
#         # суммируем очередное отрицательное число
#         total += numbers[i]
#         # ДЕКРЕМЕНТИРУЕМ (отнимаем 1) переменную счетчик
#         i -= 1
#
# print(total)
#
#
# ##############################################################################################
# ##Practica Alishev
# ##Найти сумму отрицательных чисел двумя методами
# ##РЕШЕНИЕ ЗАДАЧИ
# ##ЧЕРЕЗ ЦИКЛ FOR
# ##МОЙ МЕТОД
# my_list = [7,5,4,3,2,1,-5,-10,-15, -20, -30]
# total = 0
# i = 0
# for element in my_list:
#     if element < 0:
#         total+=my_list[i]
#         i+=1
#     else:
#         i+=1
#         pass
# print(total, 'total FOR')
# ##############################################################################################
# ##Practica Alishev
# ##Найти сумму отрицательных чисел двумя методами
# ##РЕШЕНИЕ ЗАДАЧИ
# ##ЧЕРЕЗ ЦИКЛ FOR
# ##МЕТОД АВТОРА
# numbers = [7,5,4,3,2,1,-5,-10,-15, -20, -30]
#     # Диапазон - от последнего индекса в списке numbers до 0
#     # Третий аргумент для функции range - число, на которое надо инкрементировать переменную счетчик
#     # В данном случае третий аргумент для range() - отрицательное число, поэтому счетчик будет декрементироваться
#     # Значение третьего аргумента по-умолчанию - 1
#     # Об этой особенности функции range() не говорилось в уроке,
#     # Вам необходимо было найти эту информацию самостоятельно в интернете (в идеале)
# total2 = 0
# for i in range(len(numbers) - 1, -1, -1):  #in range(10,-1,-1) = 10,9,8,7,6,5,4,3,2,1,0
#     if numbers[i] > 0:
#         break
#
#     total2 += numbers[i]
#
# print(total2)
#
# ##############################################################################################
# ##Задание: Выводить все слова , пока не увидишь слово STOP
# ##Вариант 1 через FOR
# wordss = ['apple', 'orange', 'banana','stop', 'mango']
# for element in wordss:
#     if element == 'stop':
#         break
#     print(element,'FOR')
# ##############################################################################################
# ##Задание: Выводить все слова , пока не увидишь слово STOP
# ##Вариант 2 через WHILE
# words = ['apple', 'orange', 'banana','stop', 'mango']
# i = 0
#     # Итерируем, пока не наткнемся на слово "stop"
# while wordss[i] != "stop":
#     print(wordss[i],'While')
#     i += 1

##############################################################################################

# names = ['Dima', 'Nomin', 'Alina', "Inna"]
# for name in names:
#     print(name)
#
# for i in range(len(names)):
#     print(names[i],'RANGE')

##############################################################################################
##Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована;
# x = 0
# y = 1
# for i in range(5):
#     print(y,'0000')
#     y+=1

##Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран
# x = 0
# for i in range(1,101):
#     x+=i
# print(x)
##Даны три числа. Вывести на экран «yes«, если среди них есть одинаковые, иначе вывести “ERROR”
# a = int(input())
# b = int(input())
# c = int(input())
# if a==b and b==c and a==c:
#     print('Yes')
# print("Error")

##Даны три числа. Вывести на экран «yes>, если можно взять какие-то два из них и в сумме получить третье;
# a = int(input())
# b = int(input())
# c = int(input())
# if a+b==c or b+c==a or a+c==b:
#     print('yes')
# else: print('error')


##Дано три числа. Найти количество положительных чисел среди них
# chisla = [1,2,-2]
# total = 0
# for elem in chisla:
#     if elem>0:
#         total+=1
# print(total)


##Вывести на экран все чётные значения в диапазоне от 1 до 497;
# for i in range(1,498):
#     if i%2==0:
#         print(i)

##Посчитать сумму числового ряда от 0 до 14 включительно. Например, 0+1+2+3+…+14
# x=0
# for i in range(0,15):
#     x+=i
# print(x)

##Перемножить все нечётные значения в диапазоне от 0 до 9435
# x = 1
# for i in range(0,4):
#     if i%2 !=0:
#        x*=i
# print(x)
##############################################################################################
##Требуется определить, является ли данный год високосным.
# a = int(input())
# x = []
# x.append(a)
# for i in x:
#     if i % 400 == 0:
#         print(i, "Високосный")
#     elif i%4 == 0 and i%100 != 0:
#         print(i, "Високосный")
#
#     else:
#         print(i, "Обычный")
##############################################################################################



# print("First stroke",'\n','Second Stroke' )
# '''
# Мультипликаторный коммент
#
# '''

##############################################################################################
###Формула Герона
# a = int(input())
# b = int(input())
# c = int(input())
#
# p = (a+b+c)/2
# s = (p*(p-a)*(p-b)*(p-c))**(.5)
# print(s)

##############################################################################################

# a = int(input())
# if -16 > a >= 12 or 14 > a > 17 or a >= 19:
#     print('True')
# else: print("False")

##############################################################################################
##Stepik Задача сделать калькулятор
## Мой вариант

# a = float(input())
# b = float(input())
# c = input()
# if c == "+":
#     print(a+b)
# elif c == "-":
#     print(a-b)
# elif c == "/":
#     if b == 0:
#         print('Деление на 0!')
#         pass
#     else: print(a/b)
#
# elif c == "*":
#     print(a*b)
# elif c == "mod":
#     if b == 0:
#         print('Деление на 0!')
#         pass
#     else: print(a%b)
#
# elif c == "pow":
#     print(a**b)
# elif c == "div" or '//':
#     if b == 0:
#         print('Деление на 0!')
#         pass
#     else: print(a//b)


#############################################################################################
##Stepik Задача сделать калькулятор
## Вариант с сайта
# a = float(input())
# b = float(input())
# act = input()
#
# if (act == "/" or act == 'div' or act == 'mod') and b == 0:
#     c = 'Деление на 0!'
# elif act == "+" : c = a + b
# elif act == "-" : c = a - b
# elif act == "/" : c = a / b
# elif act == "*" : c = a * b
# elif act == "mod" : c = a % b
# elif act == "pow" : c = a ** b
# elif act == "div" : c = a // b
# print(c)

# ##Вариант #2 с помощью словаря с методами
# operations  = {
#     "+": lambda x,y: x + y,
#     "-": lambda x,y: x - y,
#     "/": lambda x,y: x / y,
#     "*": lambda x,y: x * y,
#     "mod": lambda x,y: x % y,
#     "pow": lambda x,y: x ** y,
#     "div": lambda x,y: x // y,
# }
#
# x,y = float(input()),float(input())
# operation = input()
# if operation in ['mod','div','/'] and y == 0:
#     print('Деление на 0!')
# else: print(operations[operation](x,y))

########################################################################################







