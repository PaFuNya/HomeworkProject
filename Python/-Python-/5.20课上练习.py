# class parentClass:
#     def __init__(self):
#         self.name = "parent"
#     def tell(self):
#         print("this is parentClass")
# class subClass(parentClass):
#     def tell(self):
#         print("this is subClass")
#         parentClass.tell(self)
# sc = subClass()
# sc.tell()

# class parentClass:
#     def __init__(self):
#         self.name = "parent"
#     def tell(self):
#         print("this is parentClass")
# class subClass(parentClass):
#     def tell(self):
#         print("this is subClass")
#         super(subClass,self).tell()
# sc = subClass()
# sc.tell()
# import Bagtest
# price = int(input())
# bag = Bagtest.Bag(price)
# # 请在下面填入输出Bag类中变量__price的代码
# ########## Begin ##########
# print(bag._Bag__price)
# ########## End ##########
# # 请在下面填入输出Bag类中变量_price的代码
# ########## Begin ##########
# print(bag._price)

# class MyWrapper:
#     def __init__(self, obj):
#         self.__obj = obj  # 包装原始对象

#     def append(self, item):  # 新增一个功能：添加时打印
#         print(f"我添加了元素: {item}")
#         self.__obj.append(item)  # 原来 list 的 append 功能

#     def __getattr__(self, name):
#         # 如果我没定义的属性，自动授权给 list 对象
#         return getattr(self.__obj, name)

#     def __str__(self):
#         return str(self.__obj)  # 让 print() 显示原来的 list 内容


# # 使用这个包装器
# mylist = MyWrapper([1, 2, 3])
# mylist.append(4)       # 调用我们包装过的 append
# mylist.pop()           # 调用原始 list 的 pop（通过授权）
# print(mylist)          # 打印包装后的 list


#建立一个普通人员类person，包含姓名(m_name)，年龄(m_gen)_，性别(m_age),
# 且name和性别以及年龄为Private
class Person:
    #建立person的构造函数
    def __init__(self, m_name, m_age, m_sex):
        self.__name = m_name
        self.__age = m_age
        self.__sex = m_sex
    #建立一个显示过程Show(),显示该对象的数据
    def Show(self):
        print("姓名：", self.__name)
        print("年龄：", self.__age)
        print("性别：", self.__sex)
#派生一个学生类Student，增加班级（m_class），专业（m_major），设计这些类的构造函数
class Student(Person):
    def __init__(self,m_class,m_major,m_name,m_age,m_sex):
        super().__init__(m_name,m_age,m_sex)
        self.__m_class=m_class
        self.__m_major=m_major
#建立m_class和m_major对应的属性函数sClass和sMajor
    def sClass(self):
        return self.__m_class
    def sMajor(self):
        return self.__m_major
#建立显示成员函数Show()，显示该对象的数据
    def Show(self):
        print("班级：", self.__m_class)
        print("专业：", self.__m_major)


#建立一个时间类time，包含hour，min，sec的实列属性
class Time:
    def __init__(self,hour,min,sec):
        self.__hour=hour
        self.__min=min
        self.__sec=sec
#设置时间显示函数show（self）
    def show(self):
        print("时间：",self.__hour,":",self.__min,":",self.__sec)
#设置两个时间大小比较函数compare（self，t）,其中t是另外一个时间。
    def compare(self,t):
        if self.__hour>t.__hour:
            print("第一个时间大于第二个时间")
        elif self.__hour<t.__hour:
            print("第一个时间小于第二个时间")
        else:
            if self.__min>t.__min:
                print("第一个时间大于第二个时间")
            elif self.__min<t.__min:
                print("第一个时间小于第二个时间")
            else:
                if self.__sec>t.__sec:
                    print("第一个时间大于第二个时间")
                elif self.__sec<t.__sec:
                    print("第一个时间小于第二个时间")
                else:
                    print("两个时间相等")

s = Student("软件1班", "计算机科学", "张三", 20, "男")
s.Show() 

# 测试 Time 类
t1 = Time(10, 20, 30)
t2 = Time(11, 15, 10)

t1.show()
t2.show()     
t1.compare(t2)  # 比较 t1 和 t2 的大小
