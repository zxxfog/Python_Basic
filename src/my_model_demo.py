# 使用自定义模块
# my_model.py 应放在同目录文件夹下

import sys
import my_model

my_model.say_hello()
print("my_model version is",my_model.__version__,"\n\n")


# dir函数的使用

# 列出sys模块中的属性名称
print(dir(sys))
# 模块属性的使用例子
print(sys.__name__)

# 给出当前模块的属性
print(dir())

# 创建一个新的变量a
a = 6
print(dir())

# 删除a
# del用于删除一个变量或名称，使用del后，该变量就如同未存在过
del a
print(dir())





















