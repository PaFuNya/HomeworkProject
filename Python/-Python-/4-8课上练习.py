# a=input("0-你输入的和的大小")
# b=input("1/N+2-你输入的和的大小")
# def digit(a):
#     for i in range(0,a,2):
#         i+=i
#     return i
# def digite(b):
#     sum=1
#     for i in range(1,b,2):
#         sum=1/i
#         sum+=sum
# print(digit(a))
# print(digit(b))
# Input a string from the keyboard
# string = input("输入字符 ")
# uppercount = 0
# lowercount = 0
# for char in string:
#     if char.isupper():
#         uppercount += 1
#     elif char.islower():
#         lowercount += 1
#
# print(f"大写字母有 {uppercount}")
# print(f"小写字母有 {lowercount}")

def isExactMatch(phrase, word):
    """
    检查phrase是否完全等于word
    phrase: 要检查的字符串
    word: 要匹配的字符串
    返回: 如果phrase等于word返回True，否则返回False
    """
    print(f"\n开始精确匹配检查: phrase='{phrase}', word='{word}'")
    
    # 首先检查长度是否相同
    if len(word) != len(phrase):
        print(f"长度不同: phrase长度({len(phrase)}), word长度({len(word)})，返回False")
        return False
        
    # 逐个字符比较
    for i in range(len(word)):
        print(f"比较位置{i}: phrase[{i}]='{phrase[i]}' vs word[{i}]='{word[i]}'")
        if word[i] != phrase[i]:
            print(f"字符不匹配: '{word[i]}' != '{phrase[i]}'，返回False")
            return False
    
    print(f"所有{len(word)}个字符完全匹配，返回True")
    return True

# 跟随名字以"Mac"开头的本地向导
guides = ["MacDonald", "MacKenzie", "Smith", "Johnson"]
for guide in guides:
    if startsWith(guide, "Mac"):
        print(f"找到以Mac开头的向导: {guide}")
