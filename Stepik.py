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
# Alishev LIST
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
##Задача про планировки квартир страны Малевии
##Мой вариант
# pi = 3.14
# room = input()
# if room == 'треугольник':
#     a,b,c = (int(input()),int(input()), int(input()))
#     p = (a + b + c) / 2
#     s = (p*(p-a)*(p-b)*(p-c))**(.5)
# elif room == 'прямоугольник':
#     a,b = (int(input()),int(input()))
#     s = a * b
# elif room == "круг":
#     r = int(input())
#     s  = pi*r**2
# print(float(s))

########################################################################################
##Задача про планировки квартир страны Малевии
##Вариант с степик с лямбдой
# pi = 3.14
# figura = {'треугольник': [3, lambda a, b, c: ((a+b+c)/2*((a+b+c)/2-a)*((a+b+c)/2-c))**0.5],
#           'прямоугольник': [2, lambda a,b: a*b],
#           'круг': [1, lambda r: pi*r**2]}
# f = input()
# print(figura[f][1](*(float(input()) for _ in range(figura[f][0]))))

########################################################################################
# a=int(input())
# b=int(input())
# c=int(input())
# if c<b<a or a==b>c:
#  print(a)
#  print (c)
#  print(b)
# elif b<c<a or a==c>b or b==c<a:
#  print(a)
#  print(b)
#  print(c)
# elif a<c<b or a==c<b or b==c>a:
#  print(b)
#  print(a)
#  print(c)
# elif c<a<b:
#  print(b)
#  print(c)
#  print(a)
# elif b<a<c or a==b<c:
#  print(c)
#  print(b)
#  print(a)


# 123, 213, 321, 132, 111, 112, 211.
# a>b>c
# b>a>c
# a>c>b
# a=b=c
# a=c>b
# b>a=c
#
# 2 2 1 a = b > c
# 2 1 2 a = c > b
# 1 2 2 b = c > a
#
# 2 1 1 a > b = c
# 1 2 1 b > a = c
# 1 1 2 c > a = c
#
# 2 2 2 a = b = c
#
# 1 2 3 b > a
# 3 2 1
# 1 3 2
#
#
# a > b > c
# b > c > a
# c > a > b
# b > c > a
#
#

########################################################################################
##Задача про программистов и их окончания
##Мое решение
# f1, f2, f3 = ("программист","программиста", "программистов")
# n = int(input())
# x = (n % 100) // 10 #Получить вторую с конца цифру Например, 234 - 3
# if x == 1:
#     print(n,f3)
# else:
#     x = n % 10 #Получить первую с конца цифру Например: 234 - 4
#     if x == 0 or x in range(5, 10):
#         print(n, f3)
#     elif x == 1:
#         print(n,f1)
#     elif x in range(2,5):
#         print(n,f2)
########################################################################################
##Задача про программистов и их окончания
##Stepik решение
# n=int(input())
# print(n,'программист'+('ов' if n%10==0 or 4<n%10<10 or 10<n%100<15 else 'а' if 1<n%10<5 else ''))

########################################################################################
##Задача про счастливый билет
##Мое решение
# x1,x2,x3,x4,x5,x6 = input()
# sum1 = int(x1) + int(x2) + int(x3)
# sum2 = int(x4) + int(x5) + int(x6)
# if sum1 == sum2:
# 	print("Счастливый")
# else:
# 	print("Обычный")
########################################################################################
##Задача про счастливый билет
##Stepik решение

# a,b,c,d,e,f=(int(n) for n in input())
# print(('Обычный','Счастливый')[a+b+c == d+e+f])

########################################################################################
##Циклы WHILE
# a = 599
# while a > 0:
# 	print(a, end=" ")
# 	a -= 1

##Вывести все нечетные числа от 5 до 55
##Способ 1
# a = 5
# while a <=55:
# 	print(a)
# 	a+=2

##Способ 2
# a = 5
# while a <= 55:
# 	if a % 2 == 1:
# 		print(a)
# 	a+=2

##Способ 3
# for i in range(5,56):
# 	while i%2 == 1:
# 		print(i)
# 		i+=1

# i = 0
# while i <= 10:
# 	i = i+1
# 	if i > 7:
# 		i = i +2
# print(i)

##Вывести звездочки
# n = int(input())
# c = 3
# while c <= n:
# 	print("*"*c,)
# 	c+=1

##Задание2
# n = int(input())
# stars = "*"
# while len(stars) <= n:
# 	print(stars)
# 	stars+="*"

##Задание 3
##Вычеслить сумму целых чисел на отрезке от a до b
##Пример: сумма чисел на отрезке от 3 до 7 равна: 3+4+5+6+7 = 25
# a = 3
# b = 7
# s = 0
# i = a
# while i <= b:
# 	s += i
# 	i += 1
# print(s)
#######################################################################################
##Напишите программу, которая считыв

# a = int(input())
# s = 0
# while a != 0:
# 	s += a
# 	a = int(input())
# print(s)

#######################################################################################
##Задача про куски торта
# a = int(input())
# b = int(input())
#
# d = 1
# while d%a !=0 or d%b != 0:
# 	d+=1
# print(d)
#######################################################################################
##
# i = 0
# while i < 5:
# 	a,b = input().split()
# 	a = int(a)
# 	b = int(b)
# 	if (a==0) and (b==0):
# 		break  #досрочно завершает цикл
# 	print(a*b)
# 	i+=1

# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         break
#     i = i + 1
# print(i)

######################################################################################
##Мое решение
# a = int(input())
# # while a:
# # 	if a < 10:
# # 		a = int(input())
# # 		continue
# # 	elif a > 100:
# # 		break
# # 	print(a)
# # 	a = int(input())

######################################################################################
# ##Решение Stepik
# while 1==1:
#     a = int(input())
#     if a > 100:
#         break
#     if a < 10:
#         continue
#     print(a)
######################################################################################
##Задача по циклам For сделать таблицу умножения
# a = 7
# b = 10
# c = 5
# d = 6

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# for x in range(c,d+1):
#     print(' ',x, end=' ')
# for i in range(a,b+1):
#     print('\t')
#     print(i,end=' ')
#     for t in range(c, d+1):
#         print(i*t, end=' ')

######################################################################################
# ##Напишите код выводящий 10 звездочек
# for x in range(10):
#     print("*",end =' ')
# print()
# for x in range(5):
#     print("*",end =' ')
# print()
# for x in range(25):
#     print("*",end =' ')

######################################################################################
##Напишите код выводящий 10x10 звездочек
#
# for i in range(10):
#     print()
#     for t in range(10):
#         print("*",end='  ')
##Напишите код, который выведет следующее: 0 1 2 3 4 5 6 7 8 9 по 10 раз в каждой строчке
# for t in range(10):
#     for i in range(0, 10):
#         print(i, end=' ')
#     print()
##Напишите код, который выведет следующее: 0 0 0 0 0 0 0 0 1111 2222 3333 и тд
## по 10 раз в каждой строчке
# for i in range(5):
#     for t in range(10):
#         print(i, end = '')
#     print()
#########################################################################################

# for stroka in range(10):
#     for probel in range(stroka):  #Цикл для вывода пробелов
#         print(' ', end =' ')
#     for numbe in range(10 - stroka): #Цикл для вывода чисел в обратном порядке
#         print(numbe, end=' ')
#
#     print()

#########################################################################################

# for i in range(1, 10):
#     for j in range(1, 10):
#         # Extra space?
#         if i * j < 10:
#             print(" ", end="")
#
#         print(i * j, end=" ")
#
#     # Move down to the next row
#     print()

#########################################################################################
#
# for i in range(10):
#     # Print leading spaces
#     for j in range(10-i):
#         print (" ",end=" ")
#     # Count up
#     for j in range(1,i+1):
#         print (j,end=" ")
#     # Count down
#     for j in range(i-1,0,-1):
#         print (j,end=" ")
#     # Next row
#     print()
#########################################################################################
##Найти сумму всех нечетных чисел от a до b:
# a, b = input().split()
# a = int(a)
# b = int(b)
# s = 0
# for i in range(a, b+1):
#     if i%2 == 1:
#         s+=1
# print(s)

##Вариант2 \ Найдем сумму всех нечетных чисел от а до b:
# a, b = (int(i) for i in input().split())
# s = 0
# if a%2 == 0:
#     a+=1
# for i in range(a,b+1,2):
#     s+=1
# print(s)

#########################################################################################
## Задание вывести среднее арифметическое значение кратное 3
##Мое решение
# a, b = (int(i) for i in input().split())
# a = int(input())
# b = int(input())
# sum  = 0
# count = 0
# for i in range(a, b+1):
#     if i % 3 == 0:
#         sum +=i
#         count +=1
#     else:
#         continue
# sr = sum/count
# print(sr)
#########################################################################################
##Stepik решение
# x = [x for x in range(int(input()),int(input()) + 1) if x % 3 == 0]
# print(sum(x)/len(x))
#########################################################################################

# genome = 'ATGX'
# #print(genome[-2])
# for i in genome:
# 	print(i)
#
# genome = input()
# cnt = 0
# for i in genome:
# 	if i == 'C':
# 		cnt+=1
# print(cnt)


#########################################################################################
##
# genome = input()
# print(genome.count('C'))

#########################################################################################
##Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин)
# в введенной строке (программа не должна зависеть от регистра вводимых символов).
##Мое решение
#
# genome = input()
# lens = len(genome)
# cnt = 0
#
# for i in genome.lower():
# 	if i == "c" or i == "g":
# 		cnt += 1
# psGC = (cnt / lens) * 100
# print(psGC)
#
# ##Мое решение - короткое
# genome = input()
# print(((genome.lower().count('c')+genome.lower().count('g'))/len(genome))*100)

#####################################################################################
## СРЕЗЫ СТРОК (SLICES)
##Найти палиндром

# stroka = "qwertyxytriwq"
# i = 0
# n = -1
# for x in stroka:
# 	if x == stroka[n]:
# 		n-=1
# 	else:
# 		n = 'False'
# 		break
# if n == 'False':
# 	print('Its not palindrome')
# else:
# 	print('Its palindrome')
####################################################################################
##Находим палиндром методом сравнения с перевернутой строкой

# a = input("")
# if a == a[::-1]:
# 	print('its palindrome')
# else: print("its not palindrome")
#####################################################################################

# s = input() #"aaaabbсaa" aAAaBbCaA
# schetchik = 1
# for x in range(len(s) - 1):
# 	if s[x] == s[x + 1]:
# 		schetchik += 1
# 	else:
# 		print(s[x] + str(schetchik), end='')
# 		schetchik = 1
# print(s[-1] + str(schetchik),end='')

#####################################################################################

# students = ['Ivan','Masha','Sasha']
# students += ['Olga']
# students += 'Olga'
# print(students)
# print(len(students))
# a = int(input())
# b = int(input())
# if a < b:
# 	for i in range(a, b + 1):
# 		print(i)
# else:
# 	for x in range(a+1,b):
# 		print(x)




# students = ['Sasha','Ivan','Masha']
# ordered_stud = sorted(students)
# print(ordered_stud)
#
# students.sort()
# print(students)


# a = [1,2,3]
# b = a
# print(b)
# a[1] = 10
# print(b)
# b[0] = 20
# print(a)
# a = [5,6]
# print(b)

# ##Генерация списоков STEPIK
# a = [0 for i in range(5)]
# print(a)
#
# ##Список генерирует возведение в степень каждого числа из диапазона
# a = [i*i for i in range(5)]
# print(a)

# a = [int(i) for i in input().split()]
# sum = 0
# for x in a:
# 	sum+=x
# print(sum)

# 1 3 5 6 10
# 13 6 9 15 7

# 1 3 + 10 = 13
# 3 1 + 5 = 6
# 5 3 + 6 = 9
# 6 5 + 10 = 15
# 10 6 + 1 = 7

## для каждого элемента этого списка вывести сумму двух его соседей
##Мое решение
# a = [int(i) for i in input().split()]
# n = len(a)
# spisok = []
# for i in range(len(a)):
# 	if len(a) == 1:
# 		print(a[i])
# 	else:
# 		if i == 0:
# 			spisok.append(a[i+1]+a[-1])
# 		elif i == n-1:
# 			spisok.append(a[0]+a[-2])
# 		else:
# 			spisok.append(a[i-1]+a[i+1])
# print(*spisok)

##Решение STEPIK
# numbers = [int(i) for i in input().split()]
# if len(numbers) == 1:
#     print(numbers[0])
# else:
#     for i in range(len(numbers)):
#         print(numbers[i - 1] + numbers[(i + 1) % len(numbers)], end=" ")

#######################################################################################
##Sample Input 1:
##4 8 0 3 4 2 0 3
##1 1 2 2 3 3  -- 1 2 3
#1 1 1 1 1 2 2 2 -- 1 2

# numbers = [int(i) for i in input().split()]
# s=[]
# numbers.sort()
# numbers.append(99999)
#
#
# for i in range(len(numbers)-1):
# 	if numbers[i]==numbers[i+1] and numbers[i+1] != numbers[i+2]:
# 		s.append(numbers[i])
# 	continue
# print(*s)


##Stepik решение
# numbers, spisok = sorted(int(i) for i in input().split()), []
# for i in range(len(numbers)-1):
# 	if numbers[i] == numbers[i+1] and numbers[i] not in spisok:
# 		spisok.append(numbers[i])
# 	continue
# for _ in spisok:
# 	print(_,end =' ')

##Stepik решение 2 метод удаления
# numbers, spisok = sorted(int(i) for i in input().split()),[]
# for i in numbers:
# 	if numbers.count(i) > 1:
# 		while numbers.count(i) != 1:
# 			numbers.remove(i)
# 		print(i, end= " ")

##Stepik решение 3 метод count
# numbers = [int(i) for i in input().split()]
# s = []
# for i in numbers:
# 	if numbers.count(i) > 1 and i not in s:
# 		s.append(i)
# print(*s)
#######################################################################################
##Генерация двухмерных списков
# n = 3
# a = [0]*n
# print(a)
# a = [[0]*n]*n
# print(a)
# a[0][0] = 5
# print(a)
#
# a = [0*n for i in range(n)]
# print(a)
# a = [[0 for j in range(n)]for i in range(n)]
# print(a)
# a[0][0] = 5
# print(a)

##Поиск минимального значения в списке
# a = [int(i) for i in input().split()]
# a - 5,8,4,7,3,8
# m = a[0]
# for x in a:
# 	if m > x:
# 		m = x
# print(m)



##Вывести все элементы из списка
# a = [[1,2,3,4],[5,6,7,],[8,9,10,11,12]]
# for i in range(len(a)):
# 	for j in range(len(a[i])):
# 		print(a[i][j], end = ' ')
# 	print()

##Сложить все элементы из списка (не по индексу, а по значениям)
# a = [[1,2,3,4],[5,6,7,],[8,9,10,11,12]]
# sum = 0
# for row in a:
# 	for elm in row:
# 		sum += elm
# print(sum)

##Создание вложенных списков
# n = 3
# m = 4
# a = [0] * m
# for i in range(n):
# 	a[i] = [0] * m
# 	print()

##Генератор списка
# n = 3
# m = 4
# a = [[0]*m for i in range(n)]
# print(a)

##Ввод двухмерного массива
# n = int(input())
# a = []
# for i in range(n):
# 	a.append([int(j) for j in input().split()])
# print(a)

##с помощью генераторов
# n = int(input())
# a = [[int(j) for j in input().split()] for i in range(n)]
# print(a)
##########################################################################################
##Игра сапер
# n, m , k = (int(i) for i in input().split() #n - ячейки, m - столбцы, k = количество мин
# a = [[0 for j in range(m)] for i in range(n)] # пустая таблица из 0
# for i in range(k):  # перебираем кол-во мин
# 	row, col = (int(i) - 1 for i in input().split()) #записываем строку и столбец одной мины при кажом проходе
# 	a[row][col] = -1 #записываем мину по координатам столбца и колонный
# for i in range(n):
# 	for j in range(m):
# 		if a[i][j] == 0:
# 			for di in range(-1,2):
# 				for dj in range(-1,2)
# 					ai = i + di
# 					aj = j + dj
# 					#(ai, aj)

###########################################################################################


# # print(a)
# a = int(input())
# sum = 0
# sum2 = 0
# while 1 == 1:
# 	sum += a
# 	sum2 += a**2
# 	if sum == 0:
# 		break
# 	else: a = int(input())
# print(sum2)


##Решение Stepik
# s = [int(input())]
# while sum(s) != 0:
# 	s.append(int(input()))
# print(sum([i**2 for i in s]))
#
# a = [sum([x + y for x in range(10)]) for y in range(5)]
# print(a)


##ТРАНСПОНИРОВАНИЕ МАТРИЦЫ
# l, k = 3, 6
# m = [[i for i in range(j, j + k)] for j in range(0, l*k-1, k)]
# print(m)
# print(len(m[0]))
# print(len(m))
# n = [[m[i][j] for i in range(len(m))]for j in range(len(m[0]))]
# print(n,end = '')

# some_dict = {1:"one", "two": 2}
#
# if 1 in some_dict:
# 	print('OK')
# if "one" in some_dict.values():
# 	print('OK2')
# if 'two' in some_dict.keys():
# 	print('OK3')


#############################################################################################
# a = [str(x) + str(y) for x in range(5) for y in range(5) if x*y != 0 and x != y]
# print(a)

# res = []
# for x in range(5):
# 	for y in range(5):
# 			if x*y !=0 and x != y:
# 				res.append(str(x)+str(y))
#
# print(res)
#############################################################################################

# a = [[str(x) + str(y) for x in range(4) if x != 2] for y in range(4)]
# print(a)


# res = []
# for y in range(4):
# 	rey = []
# 	for x in range(4):
# 		if x != 2:
# 			rey.append(str(x) + str(y))
# 	res.append(rey)
# print(res)


#############################################################################################

# a = [[[str(x) + str(y) + str(z) for x in range(5) if x + y - z > 0]
#                        		  for y in range(5) if y - z > 0]
#                      	       	  for z in range(5) if z != 0]
# print(a)


# res = []
# for z in range(5):
# 	if z != 0:
# 		tez = []
# 		for y in range(5):
# 			if y - z > 0:
# 				tey = []
# 				for x in range(5):
# 					if x + y - z > 0:
# 						tey.append(str(x) + str(y) + str(z))
# 				tez.append(tey)
# 		res.append(tez)
# print(res)
#############################################################################################
# a = [[[x + y + z for x in 'ABC'] for y in '123'] for z in '+-*']
# print(a)

# res = []
# for z in '+-*':
# 	rez = []
# 	for y in '123':
# 		rey = []
# 		for x in "ABC":
# 			rey.append(x+y+z)
# 		rez.append(rey)
# 	res.append(rez)
# print(res)
##########################################################################################
# a = [[x + y for x in 'ABCD'] for y in '123']
# print(a)

# res = []
# for y in "123":
# 	rey = []
# 	for x in "ABCD":
# 		rey.append(x+y)
# 	res.append(rey)
# print(res)
########################################################################################
##Конструкция IF ELIF так же может быть в генераторах
# a = [x*4 if x in 'ACEG' else x*2 for x in 'ABCDEFG']
# print(a)

# res = []
# for x in "ABCDEFG":
# 	if x in "ACEG":
# 		res.append(x*4)
# 	else:
# 		res.append(x*2)
# print(res)
########################################################################################
# a = [x**2 if x % 2 == 0 else x/10 for x in range(10) if x % 3 != 0]
# print(a)

# res  = []
# for x in range(10):
# 	if x % 3 != 0:
# 		if x % 2 == 0:
# 			res.append(x**2)
# 		else:
# 			res.append(x/10)
# print(res)
# ########################################################################################
# a =[str(x) + str(y) if x - y > 0 else str(x)*2 + str(y)*2 for x in range(4) for y in range(4)]
# print(a)
#
# res = []
# for x in range(4):
# 	for y in range(4):
# 		if x - y > 0:
# 			res.append(str(x) + str(y))
# 		else:
# 			res.append(str(x)*2 + str(y)*2)
# print(res)
###################################################################################################
# a = [[x + 10 for x in range(y + 1)] if y % 2 == 0 else [x - 10 for x in range(y + 1)] for y in range(5)]
# print(a)
#
# res = []
# for y in range(5):
# 	rey =[]
# 	if y % 2 == 0:
# 		for x in range(y + 1):
# 			rey.append(x + 10)
# 	else:
# 		for x in range(y + 1):
# 			rey.append(x - 10)
# 	res.append(rey)
# print(res)
#############################################################################################
# ##Мое решение
#
# n, a,s= int(input()),  [],[]
#
# for i in range(1,n+1):
# 	a.append(i)
# for x in a:
# 	s += [x]*x
#
# s = s[0:n]
# print(*s)

# ##Stepik решение (меньше памяти уходит)
# a, b, i = int(input()), [], 1
#
# while len(b) < a:
# 	b += [i]*i
# 	i += 1
# print(*b[0:a])
########################################################################################################

# lst = [int(i) for i in input().split()]
# x = int(input()) # 1, 4, 5
# if x not in lst:
# 	print('Отсутствует')
# for i in range(len(lst)):
# 	if lst[i] == x:
# 		print(i, end = ' ')
#######################################################################################
# n, m, k = (int(i) for i in input().split()) 	# строки, столбцы, кол-во мин
# a = [[0 for j in range(m)] for i in range(n)] 	 # пустая таблица из 0
# # for i in range(k): 	 # перебираем кол-во мин
# #     rw, cl = (int(i) - 1 for i in input().split()) # записываем строку и столбец одной мины при каждом проходе
# #     a[rw][cl] = -1 	# записываем мину по координатам столбца и колонны
#
# print(a)

# a = [
# 	[9,5,3],
# 	[0,7,-1],
# 	[-5,2,9]
# ]
#
# # for i in range(3):
# # 	for j in range(3):
# # 		print(a[i][j], end = ' ')
# # 	print()
# # print('\nNEXT', )
# for j in range(2,-1,-1):
# 	for i in range(3):
#
# 		print(a[i][j], end = ' ')
# 	print()


# a = [
# 	[0,2,4,6],
# 	[1,5,9,13],
# 	[3,10,17,19]
# ]
#
# for
########################################################################################
# a = []
# n = int(input())
# for i in range(n):
# 	a.append([0]*n)
#
# for i in range(n):
# 	for j in range(n):
# 		if i == j :
# 			a[i][j] = 10
# 		elif i > j:
# 			a[i][j] = 3
# 		else:
# 			a[i][j] = 5
# for i in a:
# 	print(i)
########################################################################################

# stroki, stolbci , mines = [int(i) for i in input().split()]
# matrix = [[0 for j in range(stolbci)] for i in range(stroki)]
# for i in range(mines):
# 	rw, cl = (int(i)-1 for i in input().split())
# 	matrix[rw][cl] = -1
#
##########################################################################
# a = int(input())
# b = int(input())
# if a < b:
# 	for i in range(a, b+1):
# 		print(i)
# elif a == b:
# 	print(a)
# else:
# 	for i in range(a, b-1, -1):
# 		print(i)
###########################################################################

# a = int(input())
# b = int(input())
# for i in range(a, b-1,-1):
# 	if i % 2 != 0:
# 		print(i)
#Без использования конструкции if
# a = int(input())
# b = int(input())
# for i in range(a-(a+1)%2, b-b%2, -2):
# 	print(i)

########################################################################################


# n = 10
# sum = 0
# for i in range(n):
# 	sum+=int(input())
# print(sum)

# n = int(input())
# s = 0
# for i in range(n):
# 	s+=i**3
# print(s)

######################################################################
# n = 3
# s = 1
# sumFac = 0
# for i in range(1,n+1):
# 	s *= i
# 	sumFac+=s
#
# print(sumFac)

#####################################################################
# n = int(input())
# count = 0
# for i in range(n):
# 	a = input()
# 	if "0" == a:
# 		count+=1
# print(count)
#####################################################################



# n = int(input())
# cicle = 0
# for i in range(1,n+1):
# 	for j in range(1,i+1):
# 		print(j, sep = '', end = '')
# 	print()
##########################################################################################

# n = 5
# len = n - 1
# sum = 0
# while len > 0:
# 	x = int(input())
# 	sum+=x
# 	len-=1

## ФУНКЦИИ
# def min2(a,b):
# 	if a<=b:
# 		return a
# 	return b
#
# def max2(a,b):
# 	if a>=b:
# 		return a
# 	return b
#
# m = min2(45,30)
# print(m)
# b = max2(56,7)
# print(b)
# m = min2(min2(42,30),25)
# print(f'{m} Минимальное значение из трех')
#
# def min3(*a):
# 	m = a[0]
# 	for x in a:
# 		if m > x:
# 			m = x
# 	return m
# print(min3(5,3,7,8))
#
# ###########################################################################################
# def my_range(start,stop, step = 1):
# 	res = []
# 	if step > 0:
# 		x = start
# 		while x < stop:
# 			res += [x]
# 			x += step
#
# 	elif step < 0:
# 		x = start
# 		while x > stop:
# 			res += [x]
# 			x += step
# 	return res
#
# print(my_range(2,25,3))
#
# ###########################################################################################
#
# def init_values(a):
# 	a = 100
# 	return a
# print(init_values(b),'print B')

###########################################################################################

# def append_zero(xs):
# 	for i in range(10):
# 		xs.append(i)
#
# 	return xs
#
# a = []
# print(append_zero(a))


# def init_b(a):
# 	a = 100
# 	return a
#
# b = 0
# print(init_b(b))
# print(b)

####################################################################################################
# def funr(x):
# 	if x <= -2:
# 		result = 1 - ((x+2)**2)
# 	elif -2 < x <= 2:
# 		result = -x/2
# 	else:
# 		result = 1 + ((x-2)**2)
# 	return result
# print(funr(-4.5))
####################################################################################################

#МОЕ РЕШЕНИЕ
#lst = [1, 2, 3, 4, 5, 6]
# lst = [1, 3, 5, 7]

# def modify_list(l):
# 	for i in reversed(l):
# 		if i%2 == 1:
# 			l.remove(i)
# 			# if len(l) == 0:
# 			# 	break
# 	for key, value in enumerate(l):
# 		l[key] = value // 2


## РЕШЕНИЕ STEPIK МЕТОД СОЗДАНИЯ НОВОГО СПИСКА
#lst = [1, 2, 3, 4, 5, 6]
# def modify_list(l):
#     b = []
#     for x in l:
#         if x % 2 == 0:
#             b.append(x // 2)
#     l[:] = b
# modify_list(lst)
# print(lst)

## РЕШЕНИЕ STEPIK МЕТОД ГЕНЕРАТОРА
# lst = [1, 2, 3, 4, 5, 6]
# def modify_list(l):
# 	"""
#
# 	Docstring
# 	Печатаем Докстринги в Питоне
# 	Тест
#
# 	:param l:
# 	:return:
# 	"""
# 	l[:] = [i//2 for i in l if not i % 2]
#
# modify_list(lst)
# print(lst)
# print(modify_list.__doc__)


##ВЛОЖЕННАЯ ФУНКЦИЯ
# def message(x):
# 	def print_message(y):
# 		return x, y
# 	return print_message
#
# d = message(4)
# print(d(5))
# print(d(8))


#################################################################################################
##МНОЖЕСТВА
# s = set()
# print(type(s))
# print(s)
# s.add('mama')
# s.add('papa')
# s.add('hermana')
# print(s)
# s.remove('hermana')
# print(s)

# basket = {'orange','apple','pear','banana','strawberry','cherry'}
# for x in basket:
# 	print(x)
#
# i = [x for x in basket]
# print(*i)

##СЛОВАРИ
# d = {'C':14,"D":12,"B":13, 'H':15, "K":21}
# for key, value in d.items():
	# print(key,value, end =' ')


# def update_dictionary(d,key,value):
# 	d = {}
# 	if key in d:
# 		d[key] = value
# 	elif key not in d:
# 		key = 2*key
# 		d[] = value
# 	else:
# 		d = dict(key=value)
#
# 		# d = dict(moskva = 495,piter = 812,penza = 8412 )
# 	print(d)
#######################################################################################################
# d = {}
# def update_dictionary(d,key,value):
# 	if key in d:
# 		d[key].append(value)
# 	elif key not in d:
# 		if key*2 in d:
# 			d[key*2].append(value)
# 		else: d[key*2] = [value]
# 	return d
#
# print(update_dictionary(d,1,-1))
# print(update_dictionary(d,2,-2))
# print(update_dictionary(d,1,-3))

#######################################################################################################
# stroka = str(input().lower())
# stroka = stroka.split()
#
# d = {}
# for item in stroka:
# 	x = stroka.count(item)
# 	if item not in d:
# 		d[item] = x
# for key,value in d.items():
# 	print(key,value)

############################################################################################################

# d = {}
# n = int(input())
# for _ in range(1,n+1):
# 	x = int(input())
# 	if x in d:
# 		print(d[x])
#
# 	elif x not in d:
# 		d[x] = f(x)
# 		print(d[x])

###########################################################################################################
# # Sample Input 1:
# #aaaabbcaa
# # Sample Output 1:
# # a4b2c1a2
# s = input()
#
#
# schetchik = 1
# for x in range(len(s) - 1):
# 	if s[x] == s[x + 1]:
# 		schetchik += 1
# 	elif s[x] != s[x + 1]:
# 		print(s[x] + str(schetchik), end='')
# 		schetchik = 1
# print(s[-1] + str(schetchik),end='')
#################################################################################################
# s1 = open(r"C:\\Users\\Дмитрий\\Desktop\\dataset_3363_2.txt",'r').
# s = s1.readline()
#
# # digits = ['0','1','2','3','4','5','6','7','8','9']
# def digits():
# 	a = []
# 	for i in range(0, 100):
# 		a.append(i)
# 	return str(a)
# digits()
# for x in range(len(s)):
# 	if s[x] in digits():
# 		schetchik = (s[x])
# 		print((s[x-1]*int(schetchik)), end='')
#
# s1.close()


# s = 'G17w19J6K11'
# digits = []
# alph = []
# for i in range(len(s)+1):
# 	if s[i].isalpha():
# 		alph.append(s[i])
# 		continue
# 	elif s[i].isdigit():
# 		if s[i+1].isdigit():
# 			digits.append(s[i]+s[i+1])
# 		else: digits.append(s[i])
# print(digits)


# s1 = open(r"C:\\Users\\Дмитрий\\Desktop\\dataset_3363_2.txt",'r')
# s2 = s1.readline()
# l = len(s2)
# s = s2.ljust(l+2,'*')
#
# q = []
# b = []
# n = ''
# bu = ''
# for i in s:
# 	if i.isdigit():
# 		n += i
# 	else:
# 		if n.isdigit():
# 			q.append((n))
# 			n = ''
# for y in s:
# 	if y.isalpha():
# 		bu += y
# 	else:
# 		if bu.isalpha():
# 			b.append(bu)
# 			bu = ''
#
# new = [int(i) for i in q]
#
# last = []
# sch = 0
# for i in b:
# 	last.append(i*new[sch])
# 	sch+=1
# print(''.join(last))


# a, b = input().split()
# print((a+' ')*2 + (b+' ')*3)


# a, b  = input().split()
# print('Переменная a = {0}, переменная b = {1}'.format(a,b))

# a = input()
# print("Строка: "+a+". Длина:" + str(len(a)))

# a,b = input().split()
# print(a in b, a == b, a > b, a < b)

# a,z = input().split()
# print("Коды: "+a+" = "+str(ord(a))+", "+z+ " = " +str(ord(z)))

# a = input()
# print(a[0]+a[-1])

# a = input()
# print(a[:4])

# a = input()
# print(a[-3:])

# a = input()
# print(a[1:len(a):2])

# a = input()
# b = input()
# print(a[0:len(a):2]+" "+b[1:len(b):2])

# a = input()
# print(a[4::-1])

# a,b = input().split()
# print(b[0:len(a)])

# a,b = input().split()
# print(a[1:len(b):2] == b[1:len(b):2])

# a = input()
# x = len(a)
# print(a[0].upper()+a[1:x].lower())

# a = input()
# print(a.count('-'))

# a = input()
# print(a.find('ra'))


# a = input()
# x = a.replace('---','-')
# print(x.replace('--','-'))

# print(input().replace('---','-').replace('--','-'))

# a,b,c = (input().split())
# print(a.rjust(3,'0'),b.rjust(3,'0'),c.rjust(3,'0'), sep = '\n')

# a = input()
# print(a.count(' ')+1)


# print(input().replace(' ',';'))

# print(input().rjust(3,'0'))

# type = """
# hello
# python
# """
# print(type)
#
# a = "Тема занятия \"спецсимволы\""


# a = "Hello Balakirev!"
# print(a.replace(' ','\\'))


# a = "My best friend is Python!"
# print(input().replace(' ','\'',1).replace(' ','\"'))


# print(r'C:\WINDOWS\System32\drivers\etc\hosts')

# a = "language"
# print('\"'+input()+'\"')

# name = input()
# surname = input()
# age = input()
# print(f'Уважаемый {name} {surname}! Поздравляем Вас с {int(age)}-летием!')

# shirina, glubina, vysota = input().split()
# print("Габариты: {a} x {b} x {c}".format(a = shirina,b = glubina,c = vysota))

# a, b = input().split()
# min = min(a,b)
# max = max(a,b)
#
# print(f'{min} {max}')

# city = input()
# street = input()
# house = int(input())
# apt = int(input())
# print(f"г. {city}, ул. {street}, д. {house}, кв. {apt}")

##################################################################################################
# import math
# kurs = float(input())
# sum = input()
# res = int(sum)/int(kurs)
# print(f'Вы можете получить {math.floor(res)}$ за {sum} рублей по курсу {kurs}')


# spisok = [1,3,2,6,5,4,7]
# t_s = sorted(spisok,reverse=True)
#
# print(t_s)
###############################################################################################
##СОЗДАТЬ СПИСОК

# lst = []
# a, b, c = map(int, input().split())
# lst.append(a)
# lst.append(b)
# lst.append(c)
# print(lst)

###############################################################################################

# lst = list(map(int, input().split()))
# print(lst)
# ###############################################################################################

# cities = list(input().split())
# print('Москва' in cities)

##################################################################################################

# cities = list(input().split())
# print(cities[-1])

##################################################################################################
# marks = list(map(int, input().split()))
# print(round(sum(marks)/len(marks),1))

##################################################################################################
# name = input()
# author = input()
# quantity_paper = int(input())
# price = float(input())
#
# book = [name,author,quantity_paper,price]
# #book = [input(),input(),int(input()),float(input())]
#
# print(book)
# del book[2] #book.remove(quantity_paper)
# print(book)
# book[1] = 'Пушкин'
# book[-1] *= 2
# print(book)
##################################################################################################
# spisok = list(map(int,input().split()))
# print(max(spisok),min(spisok), (sum(spisok)))
##################################################################################################
# lst = sorted(list(map(int,input().split())),reverse=True)
# print(*lst)
##################################################################################################
# cities = ["Москва", "Тверь", "Вологда"]
# sp = list(input().split())
# lst = cities + sp
# print(*lst)
##################################################################################################
# cities = ["Москва", "Тверь", "Вологда"]
# sp = list(input().split())
# lst = sp + cities
# print(*lst)
# ##################################################################################################
"""
Подвиг 1. Имеется список числа просмотров видео по дням:
v = [1205, 1101, 1434, 1320, 923, 874]
Необходимо выбрать из него первые три значения (используя срезы) и вывести результат на экран.
Sample Input:
v = [1205, 1101, 1434, 1320, 923, 874]
Sample Output:
[1205, 1101, 1434]
"""
# v = [1205, 1101, 1434, 1320, 923, 874]
# print(v[:3])
#################################################################################################3
"""
Подвиг 2. Имеется список числа просмотров видео по дням:
v = [1205, 1101, 1434, 1320, 923, 874]
Необходимо выбрать из него последние четыре значения (используя срезы) и вывести результат на экран.
Sample Input:
v = [1205, 1101, 1434, 1320, 923, 874]
Sample Output:
[1434, 1320, 923, 874]
Решение
"""
# v = [1205, 1101, 1434, 1320, 923, 874]
# print(v[-4:])
####################################################################################################
"""Подвиг 3. Имеется список городов:
c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]
Необходимо с помощью срезов выбрать из него города через один (начиная с первого) и результат вывести на экран.
Sample Input:
Sample Output:
['Москва', 'Самара', 'Вологда', 'Уфа']
РЕШЕНИЕ
"""
# c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]
# print(c[::2])

####################################################################################################
"""
Подвиг 4. Имеется список городов:
c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]
Необходимо с помощью срезов выбрать из него города через один (начиная со второго) и результат вывести на экран.
Sample Output:
['Ульяновск', 'Тверь', 'Омск']
РЕШЕНИЕ
"""
# c = ["Москва", "Ульяновск", "Самара", "Тверь", "Вологда", "Омск", "Уфа"]
# print(c[1::2])
#######################################################################################################
"""
Подвиг 5. Имеется список с оценками студента:
m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
Необходимо с помощью срезов выбрать элементы с 3-го по 7-й (включительно) и вывести их на экран в обратном порядке.
Sample Input:
Sample Output:
[3, 2, 2, 5, 5]
"""
# m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
# print(m[-6:-11:-1])

#########################################################################################################
"""
Подвиг 6. Имеется список с оценками студента:
m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
Необходимо с помощью срезов выбрать элементы через один, начиная с последнего, и вывести результат на экран.
Sample Input:
Sample Output:
[4, 5, 3, 2, 5, 3]
"""
# m = [2, 3, 5, 5, 2, 2, 3, 3, 4, 5, 4, 4]
# print(m[::-2])
#########################################################################################################
# a = [1,2,0,3,4,True,[1,2,3]]
# a.append(100)
# print(a)
# a.remove(True)
# print(a)
# a.pop()
#########################################################################################################
"""
Подвиг 2. Вводится строка из целых чисел через пробел. Если первое число не равно последнему, то нужно добавить значение
 True, а иначе - значение False. Результирующий список lst вывести на экран командой:
print(*lst)
Реализовать задачу без использования условных операторов.
Sample Input:
8 12 2 -10 6
Sample Output:
8 12 2 -10 6 True

РЕШЕНИЕ
"""
######################################################################################################
# lst = list(map(int, input().split()))
# tr = lst[0]!=lst[-1]
# lst.append(tr)
# print(*lst)
######################################################################################################
"""
Подвиг 3. Имеется список городов:
cities = ["Москва", "Казань", "Ярославль"]
Необходимо вставить во вторую позицию этого списка строку "Ульяновск" и вывести список командой:
print(*cities)
Sample Input:
Sample Output:
Москва Ульяновск Казань Ярославль
РЕШЕНИЕ
"""
######################################################################################################
# cities = ["Москва", "Казань", "Ярославль"]
# cities.insert(1,"Ульяновск")
# print(*cities)
######################################################################################################

"""
Подвиг 4. Вводится строка с номером телефона в формате: 
+7(xxx)xxx-xx-xx
Необходимо преобразовать ее в список lst (посимвольно, то есть, элементами списка будут являться 
отдельные символы строки). 
Затем, удалить первый '+', число 7 заменить на 8 и убрать дефисы. 
Отобразить полученный список на экране командой: print("".join(lst))
Sample Input:
+7(912)123-45-67
Sample Output:
8(912)1234567
"""
######################################################################################################
# a = input()
# list_a = list(a)
#
# list_a.remove('+')
# list_a.remove('7')
# list_a.remove('-')
# list_a.remove('-')
# list_a.insert(0,'8')
#
# print("".join(list_a))
######################################################################################################
"""
Подвиг 5. В одну строчку через пробел вводятся: имя, отчество и фамилия. 
Необходимо представить эти данные в виде новой строки в формате: 
Фамилия И.О. (Например, Сергей Михайлович Балакирев -> Балакирев С.М.).
Sample Input:
Сергей Михайлович Балакирев
Sample Output:
Балакирев С.М.
"""
######################################################################################################
# a,b,c = input().split()
# print(f'{c} {a[0]}.{b[0]}.')
######################################################################################################
"""
Подвиг 7. Вводятся целые числа в одну строчку через пробел (не менее четырех). 
Необходимо найти три наименьших числа в этой последовательности чисел и вывести их на экран в порядке возрастания. 
Реализовать программу без использования условного оператора.
Sample Input:
8 11 -5 10 -1 0 7
Sample Output:
-5 -1 0
"""
######################################################################################################
# a = list(map(int,input().split()))
# a.sort()
# print(*a[0:3])
######################################################################################################
"""
Подвиг 8. Вводятся целые числа в одну строчку через пробел. 
Необходимо преобразовать их в список lst 
, затем, удалить последнее значение и если оно нечетное, то в список (в конец) добавить True, иначе - False. 
Отобразить полученный список на экране командой: print(*lst)
Реализовать программу без использования условного оператора.
Sample Input:
8 11 0 3 5 6
Sample Output:
8 11 0 3 5 False
"""
######################################################################################################
# a = list(map(int,input().split()))
# nech = a[-1] %2 == 1
# a.pop()
# a.append(nech)
# print(*a)
######################################################################################################
"""
Подвиг 9. Вводятся оценки студента (числа от 2 до 5) в одну строку через пробел. 
Необходимо определить количество двоек и вывести это значение на экран.
Sample Input:
2 3 5 2 4 2 2 5
Sample Output:
4
"""
######################################################################################################
# a = list(map(int,input().split()))
# print(a.count(2))
######################################################################################################
"""
Подвиг 10. Вводятся названия рек в одну строчку через пробел. 
Необходимо все их отсортировать по именам (по возрастанию) 
и в отсортированном списке удалить первый элемент. 
Результат отобразить на экране в одну строчку через пробел.
Sample Input:
Лена Обь Волга Дон Енисей
Sample Output:
Дон Енисей Лена Обь
"""
######################################################################################################
# a = sorted(list(map(str,input().split())))
# #a.sort()
# del a[0]
# print(*a)
######################################################################################################
"""
Вложенные списки
"""
# line = [1,7,6,11,3]
# img = [line[:],line[:],line[:],line[:],line[:]]
#
# print(img[0])
# img[0]=[0,0,0,0,0]
# print(img)
# img[1] = [1]*5
# print(img)
#
#
# t = [["Люблю", "тебя", "Петра", "творенье"],
# 	["Люблю", "твой", "строгий", "внешний", "вид"],
# 	["Невы", "державное", "теченье"],
# 	["Береговой", "ее", "гранит"]
# 	]

"""
Подвиг 1. В список:
a = [5.4, 6.7, 10.4]
добавить в конец вложенный список со значениями, вводимыми в программу (целые числа вводятся в строчку через пробел).
Результирующий список lst вывести на экран командой:print(lst)
Sample Input:
8 11
Sample Output:
[5.4, 6.7, 10.4, [8, 11]]
"""
######################################################################################################
# a = [5.4, 6.7, 10.4]
# i = list(map(int, input().split()))
# a.append(i)
# print(a)
######################################################################################################
"""
Подвиг 2. Вводятся три строчки стихотворения (каждая с новой строки).
Сохранить его в виде вложенного списка с разбивкой по строкам и словам (слова разделяются пробелом).
Результирующий список lst вывести на экран командой:print(lst)
Sample Input:
Мороз и солнце день чудесный
Еще ты дремлешь друг прелестный
Пора красавица проснись
Sample Output:

[['Мороз', 'и', 'солнце', 'день', 'чудесный'], ['Еще', 'ты', 'дремлешь', 'друг', 'прелестный'], ['Пора', 'красавица', 'проснись']]
"""
######################################################################################################
# n = []
# a = list(map(str,input().split()))
# b = list(map(str,input().split()))
# c = list(map(str,input().split()))
# n.append(a)
# n.append(b)
# n.append(c)
# print(n)
######################################################################################################
"""
Подвиг 3. Вводится  матрица чисел из трех строк. В каждой строке числа разделяются пробелом. 
Необходимо вывести на экран последний столбец этой матрицы в виде строки из трех чисел через пробел.
Sample Input:
8 11 12 1
9 4 36 -4
1 12 49 5
Sample Output:
1 -4 5
"""
######################################################################################################
# a, b, c = [input().split(),input().split(),input().split()]
# print(a[-1],b[-1],c[-1])
######################################################################################################
"""
Подвиг 6. Имеется вложенный список из трех строк:
t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
    ["Я", "Python", "выучил", "с", "каналом"],
    ["Балакирев", "что", "раздавал?"]]
Необходимо реализовать проверку на наличие в этом списке введенного слова. 
Результат (True или False) вывести на экран. Решить задачу необходимо без применения условного оператора.
Sample Input:
дядя
Sample Output:
True
"""
######################################################################################################
# t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
#     ["Я", "Python", "выучил", "с", "каналом"],
#     ["Балакирев", "что", "раздавал?"]]
# x = input()
# a = x in str(t)
# print(a)
######################################################################################################
"""
Подвиг 1. Вводятся два вещественных числа в одну строку через пробел. 
Вывести на экран наибольшее из чисел. Задачу решить с помощью условного оператора.
Sample Input:
8.7 11.0
Sample Output:
11.0
"""
######################################################################################################
# a, b = map(float,(input().split()))
# if a > b:
# 	print(a)
# else:
# 	print(b)
######################################################################################################
"""
Подвиг 2. Вводится слово. Необходимо определить, является ли это слово палиндромом 
(одинаково читается вперед и назад, например, АННА). 
Регистр букв не учитывать. Если введенное слово палиндром, на экран вывести ДА, иначе - НЕТ.
Sample Input:
Шалаш
Sample Output:
ДА
"""
######################################################################################################
# a = input()
# print('ДА 'if a[::-1].lower() == a[:].lower() else "НЕТ" )
######################################################################################################
"""
Подвиг 3. Вводятся два целых положительных числа m и n в одну строку через пробел. 
Если число m делится нацело на число n, 
то вывести на экран частное от деления (результат деления) в виде целого числа.
В противном случае вывести сообщение «m на n нацело не делится» (без кавычек)
и вместо m и n подставить соответствующие числа, например: «13 на 2 нацело не делится».
Sample Input 1:
8 4
Sample Output 1:
2
Sample Input 2:
11 2
Sample Output 2:
11 на 2 нацело не делится
"""
######################################################################################################
# m,n = map(int, input().split())
# if m%n == 0:
# 	print(m//n)
# else:
# 	print(f'{m} на {n} нацело не делится')
# #print(m//n if m%n == 0 else f'{m} на {n} нацело не делится')
######################################################################################################
"""
Подвиг 4. Вводятся три целых положительных числа в одну строку через пробел.
Убедиться, что первые два числа - это катеты прямоугольного треугольника, а третье - его гипотенуза.
(Подсказка: проверка делается по теореме Пифагора ).
Если проверка проходит (истинна), то вывести на экран ДА, иначе - НЕТ.
Sample Input:
3 4 5
Sample Output:
ДА
"""
######################################################################################################
# a, b, c = map(int, input().split())
# print("ДА" if (a**2+b**2 == c**2) else "НЕТ")
######################################################################################################
"""
Подвиг 5. Вводится четырехзначное число. Проверить, что оно оканчивается на цифру 7.
Вывести на экран ДА, если это так и НЕТ - в противном случае.
Sample Input:
8117
Sample Output:
ДА
"""
######################################################################################################
# a = input()
# print("ДА" if a[-1]== '7' else "НЕТ")
######################################################################################################
"""
Подвиг 6. Вводится слово. Проверить, что в этом слове присутствуют все три буквы: t, h и o (в произвольном порядке).
Реализовать программу с помощью одного условного оператора. Если проверка проходит, вывести ДА, иначе - НЕТ.
Sample Input:
Python
Sample Output:
ДА
"""
######################################################################################################
# a = input()
# print('ДА' if "t" in a and "h" in a and "o" in a else 'НЕТ')
######################################################################################################
"""
Подвиг 7. Вводится список городов в одну строку через пробел.
Если в этом списке присутствует город Москва, то удалить его.
Вывести на экран результирующий список в виде строки с городами через пробел.
Sample Input:
Уфа Астрахань Москва Самара Казань
Sample Output:
Уфа Астрахань Самара Казань
"""
######################################################################################################
# a  = list(map(str,input().split()))
# if "Москва" in a:
# 	a.remove('Москва')
# print(*a)
######################################################################################################
"""
Подвиг 8. Вводятся четыре целых числа a, b, c, d в одну строку через пробел. 
Определить, войдет ли в конверт с внутренними размерами a и b мм прямоугольная открытка с размерами с и d мм. 
Для размещения открытки в конверте необходим зазор в 1 мм с каждой стороны. 
Открытку можно поворачивать на 90 градусов. 
Вывести ДА, если входит и НЕТ - если не входит.
Sample Input:
12 5 7 2
Sample Output:
ДА
"""
######################################################################################################
# a, b, c, d  = map(int,input().split())
# if a-1 > (c) and b-1 > (d) or a-1 > (d) and b-1 > (c):
# 	print("ДА")
# else:
# 	print("НЕТ")
# # print('ДА' if a >= c-1 and b >= d-1 else 'НЕТ')
######################################################################################################
"""
Подвиг 9. Вводится шестизначное число. Определить, является ли оно счастливым. 
(Счастливым называют такое шестизначное число, в котором сумма его первых трех цифр равна сумме его последних трех цифр.).
 Вывести ДА, если счастливое и НЕТ - в противном случае.
Sample Input:
811235
Sample Output:
ДА
"""
######################################################################################################
# a = input()
# print('ДА' if int(a[0])+int(a[1])+int(a[2]) == int(a[3])+int(a[4])+int(a[5]) else 'НЕТ')
######################################################################################################
"""
Подвиг 10. Работа светофора для пешеходов запрограммирована следующим образом:
 в начале каждого часа в течение трех минут горит зеленый сигнал, затем в течение двух минут – красный, 
 в течение трех минут – опять зеленый и т. д. Дано вещественное число t, означающее время в минутах, 
 прошедшее с начала очередного часа. Определить, сигнал какого цвета горит для пешеходов в этот момент. 
 На экран вывести сообщение (без кавычек) "green" - для зеленого и "red" - для красного.
Sample Input:
12.5
Sample Output:
green
"""

######################################################################################################
# t = float(input())
# if 0<= t%5 <= 3:
#     print("green")
# else:
#     print("red")
######################################################################################################
"""
Подвиг 1. Имеется следующее меню:

m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''
В программе вводится целое число от 1 до 6. Нужно вывести пункт меню, связанный с этим числом. 
Реализовать программу с использованием операторов if-elif
Sample Input:
2
Sample Output:
2. Строки и списки
"""
######################################################################################################
# x = int(input())
# if x == 1:
#     print("1. Введение в Python")
# elif x == 2:
#     print("2. Строки и списки")
# elif x == 3:
#     print("3. Условные операторы")
# elif x == 4:
#     print("4. Циклы")
# elif x == 5:
#     print("5. Словари, кортежи и множества")
# else:
#     print("6. Выход")
######################################################################################################
"""
Подвиг 2. Вводятся три целых числа в одну строку через пробел.
Необходимо определить наименьшее среди них и вывести его на экран.
Реализовать программу, используя условный оператор, без использования функции min.
Sample Input:
8 11 -1
Sample Output:
-1
"""
######################################################################################################
# a, b, c = map(int,input().split())
# if a <= b:
#     if a <= c:
#         print(a)
#     else:
#         print(c)
# elif b <= a:
#     if b <= c:
#         print(b)
#     else:
#         print(c)
######################################################################################################
"""
Подвиг 3. Вводится вес боксера-любителя (в кг, в виде вещественного числа).
Известно, что вес таков, что боксер может быть отнесен к одной из весовых категорий:

1) легкий вес – до 60 кг (включительно);
2) первый полусредний вес – до 64 кг (включительно);
3) полусредний вес – до 69 кг (включительно);
4) остальные - более 69 кг.

Вывести на экран номер категории, в которой будет выступать боксер.
Sample Input:
62.4
Sample Output:
2
"""
######################################################################################################
# weight = float(input())
# if int(weight) <= 60:
#     print("1")
# elif int(weight) <= 64:
#     print("2")
# elif int(weight) <= 69:
#     print("3")
# else:
#     print("4")
######################################################################################################
"""
Подвиг 4. Вводится порядковый номер дня недели (1, 2, ..., 7).
Вывести на экран его название (понедельник, вторник, среда, четверг, пятница, суббота, воскресенье).
Программу реализовать с использованием операторов if-elif.

Sample Input:
2
Sample Output:
вторник
"""
######################################################################################################
# dn = int(input())
# if dn == 1:
#     print('понедельник')
# elif dn == 2:
#     print('вторник')
# elif dn == 3:
#     print('среда')
# elif dn == 4:
#     print('четверг')
# elif dn == 5:
#     print('пятница')
# elif dn == 6:
#     print('суббота')
# elif dn == 7:
#     print('воскресенье')
######################################################################################################

# week = ['понедельник',"вторник","среда","четверг","пятница","суббота","воскресенье"]
# day = int(input())
# if 1 <= day <= 7:
#     print(week[day-1])
######################################################################################################
"""
Подвиг 5. Вводится порядковый номер месяца (1, 2, ..., 12). 
Вывести на экран количество дней в этом месяце. Принять, что год не является високосным. 
Реализовать через условный оператор, в котором следует использовать не более трех ветвей (блоков).
P.S. Число дней в месяцах не високосного года, начиная с января: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

Sample Input:
2
Sample Output:
28
"""
######################################################################################################
# months = ["31", "28", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"]
# x = int(input())
# if 1 <= x <= 12:
#     print(months[x-1])

######################################################################################################
"""
Подвиг 6. Дата некоторого дня характеризуется двумя натуральными числами: m (порядковый номер месяца) и n (число). 
По введенным m и n (в одну строку через пробел) определить:

а) дату предыдущего дня (принять, что m и n не характеризуют 1 января);
б) дату следующего дня (принять, что m и n не характеризуют 31 декабря).

В задаче принять, что год не является високосным. 
Вывести предыдущую дату и следующую дату (в формате: mm.dd, где m - число месяца; d - номер дня) 
в одну строчку через пробел.

P.S. Число дней в месяцах не високосного года, начиная с января: 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

Sample Input:
8 31
Sample Output:
08.30 09.01
"""
######################################################################################################
# m,n = map(int,input().split())
# months = ["31", "28", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"]
# if 2 <= m <= 8:
#     if n == int(months[m-1]):
#         print(f'0{m}.{n-1} 0{m + 1}.01')
#     elif 10 <= n < int(months[m-1]):
#         print(f'0{m}.{n-1} 0{m}.{n+1}')
#     elif 1<= n <= 9:
#         print(f'0{m-1}.{(int(months[m+1]))} 0{m}.0{n+1}')
# if  m == 9:
#     if n == int(months[m-1]):
#         print(f'0{m}.{n-1} {m + 1}.01')
#     elif 10 <= n < int(months[m-1]):
#         print(f'0{m}.{n-1} 0{m}.{n+1}')
#     elif 1<= n <= 9:
#         print(f'0{m-1}.{(int(months[m+1]))} 0{m}.0{n+1}')
# elif 10 <= m <= 11:
#     if n == int(months[m-1]):
#         print(f'{m}.{n-1} {m + 1}.01')
#     elif 10 <= n < int(months[m-1]):
#         print(f'{m}.{n-1} {m}.{n+1}')
#     elif 1<= n <= 9:
#         print(f'0{m-1}.{(int(months[m+1]))} 0{m}.0{n+1}')
# elif m == 12:
#     if n == int(months[m - 1]):
#         print(f'{m}.{n - 1} 0{m-11}.01')
#     elif 10 <= n < int(months[m - 1]):
#         print(f'{m}.{n - 1} {m}.{n + 1}')
#     elif 1 <= n <= 9:
#         print(f'0{m - 1}.{(int(months[m + 1]))} 0{m}.0{n + 1}')
# elif m == 1:
#     if n == int(months[m-1]):
#         print(f'0{m}.{n-1} 0{m + 1}.01')
#     elif 10 <= n < int(months[m-1]):
#         print(f'0{m}.{n-1} 0{m}.{n+1}')
#     elif 1 < n <= 9:
#         print(f'0{m}.0{n-1} 0{m}.0{n+1}')
#     elif n == 1:
#         print(f'{(int(months[m+11]))}.{n-1} 0{m + 1}.01')

######################################################################################################
"""
Подвиг 7. Вводится целое число k (1 <= k <= 365). 
Определить, каким днем недели (понедельник, вторник, среда, четверг, пятница, суббота или воскресенье)
является k-й день не високосного года, в котором 1 января является понедельником.

Sample Input:
121
Sample Output:
вторник
"""
######################################################################################################
# k = int(input())
# if 1 <= k <= 365:
# 	if k in range(1,366,7):
# 		print('понедельник')
# 	elif k in range(2,360,7):
# 		print('вторник')
# 	elif k in range(3,361,7):
# 		print('среда')
# 	elif k in range(4, 362, 7):
# 		print('четверг')
# 	elif k in range(5, 363, 7):
# 		print('пятница')
# 	elif k in range(6, 364, 7):
# 		print('суббота')
# 	else:
# 		print('воскресенье')

######################################################################################################
"""
Подвиг 1. Вводится два вещественных числа, каждое с новой строки. 
Необходимо с помощью тернарного условного оператора наибольшее значение присвоить переменной d и вывести ее на экран.
Sample Input:
5.4
-3.8
Sample Output:
5.4
"""
######################################################################################################
# a = float(input())
# b = float(input())
#
# d  = (a if a > b else b)
# print(d)
######################################################################################################

"""
Подвиг 2. Вводится целое число. Необходимо переменной msg присвоить строку "кратно 3", 
если введенное число кратно 3, а иначе присвоить строку "не кратно 3". 
Реализовать программу с использованием тернарного оператора. Переменную msg отобразить на экране.

Sample Input:
9
Sample Output:
кратно 3
"""
######################################################################################################
# a  = int(input())
# msg = ('кратно 3' if a % 3 == 0 else "не кратно 3")
# print(msg)
######################################################################################################
"""
Подвиг 3. Вводится слово. Переменной msg присвоить строку "палиндром", если введенное слово является палиндромом
(одинаково читается и вперед и назад), а иначе присвоить строку "не палиндром".
Проверку проводить без учета регистра. Программу реализовать с помощью тернарного условного оператора.
Значение переменной msg отобразить на экране.

Sample Input:
Казак
Sample Output:
палиндром
"""
######################################################################################################
# a = str(input().lower())
# msg = ('палиндром' if a == a[::-1] else 'не палиндром')
# print(msg)
######################################################################################################
"""
Подвиг 4. Вводится целое число 0 или 1. Необходимо преобразовать их в строки: 0 - в "False", 1 - в "True".
Реализовать это с помощью тернарного условного оператора. Результат отобразить на экране.
Sample Input:
1
Sample Output:
True"""

######################################################################################################
# a  = int(input())
# msg = ('False' if a == 0 else "True")
# print(msg)

######################################################################################################
"""
Подвиг 5. Вводится текущее время (секунды) в диапазоне [0; 59]. Если значение равно 59, то следующее должно быть 0. 
И так по кругу. Необходимо  вычислить следующее значение с проверкой граничного значения 59. 
Реализуйте это с помощью тернарного условного оператора. Результат отобразите на экране.
P.S. Попробуйте также реализовать эту же задачу с использованием только арифметических операций.
Sample Input:
55
Sample Output:
56
"""
######################################################################################################
# a  = int(input())
# msg  = (a+1 if a in range(0,59) else 0)
# print(msg)
######################################################################################################
"""
Подвиг 6. Имеется список базовых нот:
m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
Вводятся три целых числа в диапазоне от 1 до 7 - номера нот, в одну строчку через пробел.
Необходимо отобразить указанные ноты в виде строки через пробел, 
но перед нотами до и фа дополнительно ставить символ диеза '#'. 
Реализовать эту программу с использованием тернарного условного оператора (он может использоваться несколько раз).
Sample Input:
1 6 7
Sample Output:
#до ля си
"""
######################################################################################################
# a, b, c = map(int, input().split())
# m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
# print(
# 	(f'#{m[a-1]}' if a == 1 or a == 4 else f'{m[a-1]}'),
# 	(f'#{m[b-1]}' if b == 1 or b == 4 else f'{m[b-1]}'),
# 	(f'#{m[c-1]}' if c == 1 or c == 4 else f'{m[c-1]}')
# 	 )
######################################################################################################
# #Оператор WHILE
# N = 1000
# s = 0
# i = 1
# while i <= N and i <= 50:
# 	s += i
# 	i += 1
# print(s)
######################################################################################################
# password = 'password'
# ps = ''
#
# while ps != password:
# 	ps = input('Введите пароль: ')
# print("Вход в систему")
######################################################################################################
# N = 20
# i = 1
# while i <= N:
# 	if i %3 == 0:
# 		print(i)
# 	i += 1
######################################################################################################
"""
Подвиг 2. Вводятся два целых положительных числа n и m, причем, n < m. 
Вывести в строку через пробел квадраты целых чисел в диапазоне [n; m].
Программу реализовать при помощи цикла while.
Sample Input:
2 4
Sample Output:
4 9 16
"""
######################################################################################################
# n, m = map(int, (input().split()))
# a = [] #список , куда закидывать квадраты чисел
# i = 0 #будущее число в квадрате , которое будет записано в список а
# s = n #создаем s чтобы не изменять n по мере прохождения цикла
#
# while s <= m: #пока n <= m
# 	i = s**2
# 	a.append(i)
# 	s += 1
# print(*a)
######################################################################################################
"""
Подвиг 3. Вводится стоимость одной книги x рублей (вещественное число).
Необходимо вывести на экран в строчку через пробел стоимости 2, 3, ... 10 таких книг с точностью до десятых.
Программу реализовать при помощи цикла while.
Sample Input:
34.6
Sample Output:
69.2 103.8 138.4 173.0 207.6 242.2 276.8 311.4 346.0
"""
######################################################################################################
# x = float(input('Введите стоимость книги: '))
# a = []
# i = 0
# y = 2
#
# s = x
# while i <= 10:
# 	s *= y
# 	a.append(round(s,2))
# 	y+=1
# 	i+=1
# 	s = x
# print(*a)
######################################################################################################
"""
Подвиг 4. Вводится целое положительное число n. Вычислить и вывести на экран сумму: 
1 + 1/2 + 1/3 + ... + 1/n с точностью до тысячных (три знака после запятой). 
Программу реализовать при помощи цикла while.
Sample Input:
8
Sample Output:
2.718
"""
######################################################################################################
# n = int(input())
# i = 1
# k = 1
# sum = 0
# while i <= n:
# 	x = 1/k
# 	i+=1
# 	sum += x
# 	k += 1
# print(round(sum,3))
######################################################################################################
# n = int(input())
# res = 0
# while n > 0:
#     res += 1 / n
#     n -=1
# print(round(res, 3))
######################################################################################################
"""
Подвиг 5. На каждой итерации цикла пользователь вводит целое число.
Цикл продолжается, пока не встретится число 0.
Необходимо вычислить сумму введенных в цикле чисел и вывести результат на экран.
Программу реализовать при помощи цикла while.
Sample Input:
8
11
2
-4
0
Sample Output:
17
"""
######################################################################################################
# n = int(input())
# res = 0
# while n != 0:
# 	res += n
# 	n = int(input())
# print(res)
######################################################################################################
"""
Подвиг 6. Вводится строка (слаг). Замените в этой строке все подряд идущие дефисы
(--, ---, ---- и т.д.) на одинарные (-).
Результат преобразования строки выведите на экран.
Программу реализовать при помощи цикла while.

Sample Input:
osnovnye--metody-----slovarey
Sample Output:
osnovnye-metody-slovarey
"""
######################################################################################################
# n = input()
# while '--' in n:
# 	n = n.replace('--','-')
# print(n)
######################################################################################################
"""
Подвиг 7. Вводится натуральное (то есть, целое положительное) число (от трехзначного и более). 
Найти произведение всех его цифр. Результат вывести на экран. 
Программу реализовать при помощи цикла while.

Sample Input:
821
Sample Output:
16
"""
######################################################################################################
# n = input()
# dlina = len(n)
# res = 1
# index = 0
#
# while dlina > 0:
# 	res *= int(n[index]) # произведение каждого индекса записываем в переменную res
# 	index += 1 #увеличиваем индекс
# 	dlina -=1 #уменьшаем длинну
# print(res)
######################################################################################################
"""
Подвиг 8. Последовательность Фибоначчи образуется так: первые два числа равны 1 и 1, 
а каждое последующее равно сумме двух предыдущих.
Имеем такую последовательность чисел: 1, 1, 2, 3, 5, 8, 13, ... 
Постройте последовательность Фибоначчи длиной n (n вводится с клавиатуры).
Результат отобразите в виде строки полученных чисел, записанных через пробел.
Программу реализовать при помощи цикла while.

Sample Input:
8
Sample Output:
1 1 2 3 5 8 13 21
"""
######################################################################################################
# n = int(input())
# f1 = 1
# f2 = 1
#
# f_sum = 0
# i = 0
#
# res  = [f1,f2]
# while n - 2 > i:
# 	f_sum = f1 + f2
# 	f1 = f2
# 	f2 = f_sum
# 	res.append(f2)
# 	i += 1
#
# print(*res)
######################################################################################################
"""
Подвиг 9. Одноклеточная амеба каждые 3 часа делится на 2 клетки. Определить, сколько клеток будет через n часов
(n - целое положительное число, вводимое с клавиатуры). Считать, что изначально была одна амеба.
Результат вывести на экран. Задачу необходимо решить с использованием цикла while.
Sample Input:
11
Sample Output:
8
"""
######################################################################################################
# n = float(input())
# a = 1
# step = 3
#
# while n > step:
# 	a *= 2
# 	step+=3
#
# print(a)
######################################################################################################
"""
Подвиг 10. Гражданин 1 января открыл счет в банке, вложив 1000 руб. 
Каждый год размер вклада увеличивается на 5% от имеющейся суммы.
Определить сумму вклада через n лет (n - целое положительное число, вводимое с клавиатуры).
Результат округлить до сотых и вывести на экран. Программу реализовать при помощи цикла while.

Sample Input:
5
Sample Output:
1276.28
"""
######################################################################################################
# n = int(input())
# sum = 1000
# year = 1
# while year <= n:
# 	year += 1
# 	sum = sum + (sum * 0.05)
#
# print(round(sum,2))
######################################################################################################
"""
Подвиг 11. Вводятся два натуральных четных числа n и m в одну строчку через пробел, причем n < m. 
Напечатать все нечетные числа из интервала [n, m]. 
Задачу решить без применения условного оператора. 
Результат вывести на экран в виде строки чисел, записанных через пробел.
Программу реализовать при помощи цикла while.

Sample Input:
2 10
Sample Output:
3 5 7 9
"""
######################################################################################################
###Мое решение с применением условного оператора if
# n, m = map(int, input().split())
# i = 0
# s = n
# while s <= m:
# 	while s%2 == 1:
# 		print(s, end = ' ')
# 		s += 1
# 	s += 1
######################################################################################################
###Решение Без применения условного оператора  (метод поиска нечетных чисел)
# n, m = map(int, input().split())
# while n < m:
#     print(n + (n + 1) % 2, end=' ')
#     n += 2
######################################################################################################
"""
Подвиг 12. Составить программу поиска всех трехзначных чисел, которые при делении на 47 дают
в остатке 43 и кратны 3. 
Вывести найденные числа в строчку через пробел. Программу реализовать при помощи цикла while.
Sample Input:
Sample Output:
231 372 513 654 795 936
"""
######################################################################################################
# a = 100
# while a < 1000:
# 	if a % 47 == 43 and a%3 == 0:
# 		print(a, end = ' ')
# 		a+=1
# 	else:
# 		a+=1
######################################################################################################
n, m = map(int, input().split())
a = []
kv = 0
while n <= m:
	kv = n ** 2
	a.append()
	n += 1
print(*a)

######################################################################################################


######################################################################################################


######################################################################################################


######################################################################################################


######################################################################################################


######################################################################################################


######################################################################################################


######################################################################################################


######################################################################################################


######################################################################################################


######################################################################################################


######################################################################################################


######################################################################################################


######################################################################################################


######################################################################################################


######################################################################################################


######################################################################################################


######################################################################################################


######################################################################################################


######################################################################################################


######################################################################################################



######################################################################################################


######################################################################################################


######################################################################################################


######################################################################################################



