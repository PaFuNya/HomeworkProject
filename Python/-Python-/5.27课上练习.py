with open('abc.txt', 'w') as f:
    f.write('123\n')
count = 0
with open('abc.txt', 'rb') as f:
    while True:
        byte = f.read(1)
        if not byte:
            break
        count += 1
        print(f"第{count}次读取: {byte}")

print(f"\n总共需要读取{count}次才能读完文件")
print("在Windows系统中，文本模式写入'abc\\n'会转换为'abc\\r\\n'(5字节)") 
print("如果是二进制模式写入或非Windows系统，则可能是4字节")  