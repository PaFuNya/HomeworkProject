#coding = utf-8
#********* Begin *********#
#第一步 请在列表fruits中找出不属于水果一类元素，赋值给变量 a
fruit = ["苹果","梨子","菠萝","黄瓜","香蕉"]
a ="黄瓜"

    
#第二步 将变量 a 的值添加到列表vegetable 的末尾
vegetable = ["土豆","萝卜","茄子","白菜"]
vegetable.append(a)



#第三步 删去列表fruit中不属于水果的元素
fruit.remove("黄瓜")



#第四步 将列表fruit和列表vegetable作为元素按顺序加入到列表food中
food = [fruit+vegetable]



#补充print语句，先打印输出列表food，再打印输出列表food中第1个列表的第3个元素
print(food)
print(food[1][2])
#********* End *********#

















# import collections
# def Func():
#     c = collections.Counter()
#     for i in range(6):
#         data = input()
#         # ********** Begin ********** #
#         if i % 2 == 0:  # 偶数行（行数从0开始）
#             c.update(data)  # 将数据加到计数器中
#         else:  # 奇数行
#             c.subtract(data)  # 将数据从计数器中减去
#         # ********** End ********** #
#     print(c.most_common())








# import collections

# def CreatePoint():
#     # ********** Begin ********** #
#     Point=collections.nametuple("Point",["x,y"])
#     p=Point(x=0,y=0)
#     return p
# 	# ********** End ********** #

# def IncX(p):
#     # ********** Begin ********** #
#     p=p._replace(x=p.x+1)
#     return p
# 	# ********** End ********** #
# def IncY(p):
#     # ********** Begin ********** #
#    p=p._replace(y=p.y+1)
#    return p

# 	# ********** End ********** #

# def PrintPoint(p):
#     print("当前位置:x = %d,y = %d" % (p.x,p.y))























# # 初始化menu1字典，输入两道菜的价格
# menu1 = {}
# menu1['fish']=int(input())
# menu1['pork']=int(input())

# # menu_total列表现在只包含menu1字典
# menu_total = [menu1]

# # 请在此添加代码，实现编程要求
# ########## Begin ##########
# menu2={key:value*2 for key,value in menu1.items()}
# menu_total.append(menu2)
# ########## End ##########

# # 输出menu_total列表
# print(menu_total)


