#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2025/3/18
# list=[]
# for i in range(3):
#     a=int(input(f"请输入第{i+1}个数:"))
#     list.append(a)
# tuple(list)
# print("最小的数为"+str(min(list)))
#! /usr/bin/env python

# import math
# profit=float(input("Input you Profit(万):"))
# if profit<=10:
#     profit=profit*1.2
# elif profit>10 and profit<20:
#     profit=(profit-10)*0.085
# elif profit>20 and profit<40:
#     profit=(profit-20)*0.06
# elif profit>40 and profit<60:
#     profit=(profit-40)*0.04
# elif profit>60 and profit<100:
#     profit=(profit-60)*0.025
# else:
#     profit=(profit-100)*0.01
# print("Your profit is (万)",profit)
# import math
#
# x=float(input("请输入5个字符/闰年/x坐标"))
# y=float(input("请输入y坐标"))
# # count=x.count("0")
# # print(f"一共有{count}个0")
# if(int(x)%4==0 and int(x)%100!=0)or(int(x)%400==0):
#     print(f"{x}是闰年")
# else:
#     print(f"{x}不是闰年")
# if math.sqrt(math.pow(x-2,2)+math.pow(y-2,2))<=1:
#     print(f"点({x},{y})在圆(2,2)内")
# elif math.sqrt(math.pow(x+2,2)+math.pow(y-2,2))<=1:
#     print(f"点{x},{y}在圆(-2,2)内")
# elif math.sqrt(math.pow(x+2,2)+math.pow(y+2,2))<=1:
#     print(f"点{x},{y}在圆(-2,2)内")
# elif math.sqrt(math.pow(x-2,2)+math.pow(y+2,2))<=1:
#     print(f"点{x},{y}在圆(2,-2)内")
# else:
#     print(f"点{x},{y}不在圆内")














# def decode_morse():
#     # 摩斯密码字典
#     morse_dict = {
#         '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
#         '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
#         '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
#         '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
#         '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
#         '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
#         '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
#         '-----': '0', '.-.-.-': '.', '--..--': ',', '..--..': '?',
#         '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(',
#         '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';',
#         '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
#         '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'
#     }

#     # 将 0 转换为 . ，1 转换为 -
#     encoded = "11 111 010 000 0 1010 111 100 0 00 000 000 111 00 10 1 0 010 0 000 1 00 10 110"
#     morse_text = encoded.replace('0', '.').replace('1', '-')
    
#     # 分割成单个字符的摩斯密码
#     morse_chars = morse_text.split()
    
#     # 解码
#     decoded_text = ''
#     for char in morse_chars:
#         decoded_text += morse_dict.get(char, '?')
    
#     return decoded_text.lower()  # 将结果转换为小写

# # 执行解密
# result = decode_morse()
# print(f"解密结果: {result}")














#


# import math

# t=(input("a=:"))
# low=0
# up=0
# di=0
# b=""
# list(str(t))
# for c in t:
#     if c.islower():
#         low+=1
#         b+=c.upper
#     elif c.isupper():
#         up+=1
#         b+=c.lower
#     elif c.isdigit():
#         di+=1
#     c+=c
# print(f"大写数量为:{up}")
# print(f"小写数量为:{low}")
# print(f"数字有:{di}")
# print(b)














# b = float(input("b=:"))
# c = float(input("c=:"))
# if a + b > c and a + c > b and b + c > a:
#     p = (a + b + c) / 2
#     s = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     print(f"数学学的不错，面积为: {s:.2f}平方米")
# else:
#     print("看看你输了个啥O.o")































# -*-1.4.1运算符-*-
# a=1
# b=2
# c=3
# x=4
# y=3
# print((a+(b>=x+y) and c-a and y-x))
# print(not(x==a) and (y==b) and 0)
# print(not(a+b)+c-1 and b+c/2)
# print(a or str(1)+'a' and b and 'c')

# for i in range(-5,1):
#     print(i)
# x=int(input())
# print(-5 <= x <= 0)







# a=1
# b=2
# c=3
# d=0
# print(a>b and b>c or a+b<c)
# print(a-b<c or b>c and not c)
# print(not d or b>c+a or a)
# print(d and b and c>d and a*b>c)
# print(not(a>b and c>d))
# print(a*b>c or b+c>d and not d)
# print(c+d<=b+d and d<c or 2*b>c)
# print(d<b or c>a+b+d and b<c+a)

# source_string = input()

# # 请在下面添加字符串转换的代码
# ########## Begin ##########
# wow=source_string.strip()
# s=wow.title()
# print(s)
# print(len(s))

