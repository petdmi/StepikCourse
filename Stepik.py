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


def bmi_calc(name,height,weight):
    bmi = weight / height ** 2
    print('Индекс массы тела равен ',bmi)
    if bmi < 25:
        return name + " не имеет лишнего веса"
    else:
        return name + " человек имеет лишний вес"

print(bmi_calc("Dima", 1.86,72))
