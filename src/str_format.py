# 格式化字符串操作

print("Usage of format.")

# 第一种用法
name = "GaoKang"
age  = 25
print("{0} is {1} years old.".format(name, age))

# 第二种用法
print(name + " is " + str(age) + " years old")

# 第三种用法
print("{} is {} years old.".format(name, age))



# 对于浮点数 '0.333' 保留小数点(.)后三位
print("{0:.3f}".format(1.0/3))

# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print("{0:_^11}".format("hello"))

# 基于关键词输出 'Swaroop wrote A Byte of Python'
print("{name} wrote {book}".format(name="Swaroop", book="A Byte of Python"))



# print函数会自动换行，如果不需要换行，这样:
print("a", end="")
print("b", end="")

# 或着以空格结尾
print("")
print("a", end=" ")
print("b", end=" ")
print("c")



# 转义字符
print("This is a exam of \"Hello World.\"")
print("The first line, \n The Second line.")
print("The aaa, \
the bbb.")

# 在字符串前加 r 表示原始字符串，转义序列不会被翻译
print(r"This can show the \n \"")































