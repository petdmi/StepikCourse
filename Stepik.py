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


lst = [5,8,2,7,8,8,2,4]
x = 8
print(lst.count(x))
ind = 0
for i in lst:
	print(lst.index(x,ind))
	while ind < len(lst):
		ind+=1







