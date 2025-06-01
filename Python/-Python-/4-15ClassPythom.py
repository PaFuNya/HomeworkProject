# # -*- coding: utf-8 -*-
# # coding=utf-8

# # 输入一个整数n
# n = int(input())

# # 请在此添加代码，对输入的整数进行判断，如果是素数则输出为True，不是素数则输出为False
# ########## Begin ##########
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True





# # print(is_prime(n))
# # ########## End ##########1
# # coding=utf-8

# # 输入数字字符串，并转换为数值列表
# a = input()
# num1 = eval(a)
# numbers = list(num1)

# # 请在此添加代码，对数值列表numbers实现从小到大排序
# ########## Begin ##########
# def sort(numbers):
#     for i in range(len(numbers)):
#         for j in range(i+1,len(numbers)):
#             if numbers[i]>numbers[j]:
#                 numbers[i],numbers[j]=numbers[j],numbers[i]
#     return numbers


# print (sort(numbers))


# ########## End ##########




# # coding=utf-8

# from math import pi as PI

# n = int(input())

# # 请在此添加代码，实现圆的面积计算，并输出面积结果
# ########## Begin ##########
# def circle(n):
#     return PI *n**2

# print("{:.2f}".format(circle(n)))




# ########## End ##########




# # coding=utf-8

# # 创建一个空列表numbers
# numbers = []

# # str用来存储输入的数字字符串，lst1是将输入的字符串用空格分割，存储为列表
# str = input()
# lst1 = str.split(' ')

# # 将输入的数字字符串转换为整型并赋值给numbers列表
# for item in lst1:
#     numbers.append(int(item))

# # 请在此添加代码，对输入的列表中的数值元素进行累加求和
# ########## Begin ##########
# def summ(lst):
#     total = 0
#     for num in lst:
#         total += num
#     return total

# d = summ(numbers)
# ########## End ##########

# print(d)


# #输入若干个同学的成绩，计算平均成绩，输入的成绩为负数大于100时表示结束输入。
# scores=[]
#  # coding=utf-8
# while True:
#     score=float(input())
#     if score<0 or score>100:
#         break
#     else:
#         scores.append(score)

# def average(scores):
#     return sum(scores)/len(scores)
# if len(scores)==0:
#     print("没有成绩")
# else:
#     print("{:.2f}".format(average(scores)))



# coding=utf-8

# 输入两个正整数a,b
a = int(input())
b = int(input())

# 请在此添加代码，求两个正整数的最大公约数
########## Begin ##########
def gcd(num1,num2):
    while num2 !=0:
        num1,num2=num2,num1%num2
    return num1



########## End ##########

# 调用函数，并输出最大公约数
print(gcd(a,b))


