# python 中函数的定义与使用

print("Usage of function.")


# 函数的的定义
def say_hello():
	# 函数块
	# 尝试文档字符串
	"""This is a python function
	
	output hello world in screen"""
	print("Hello Python")
	# 函数结束
# 函数调用
say_hello()
# 文档字符串的使用
print(say_hello.__doc__)


# 带参数的函数
def print_max(a,b):
	if a>b:
		print(a,"is larger than",b)
	elif a<b:
		print(b,"is larger than",a)
	else:
		print(a,"==",b)
	# 函数结束
# 函数调用
print_max(12,36)


# python变量的global使用
x = 50
def func():
	# 表明这里使用的是全局的变量x
	global x
	print("x is",x)
	x = 6
	print("change global x to",x)
func()
print("Value of x is",x)


# 面向对象的默认参数函数，类似于C++
# 带有默认值得参数只能放在无默认值的参数之后
def say(message,times=1):
	print(message*times)
say("Hello tianmiao")
say("hello tianmiao ,",3)


# 关键字参数函数
def func_key(a, b=5, c=6):
	print("a =",a, "b =",b, "c =",c)
func_key(3)
func_key(3,7)
func_key(3,7,12)
# 注意下面的用法
func_key(c=3,a=7)


# 可变参数函数
def func_varargs(a=5, *numbers, **phbk):
	print("a =",a)
	# 遍历元组中的所有项目
	for single_item in numbers:
		print("single_item =",single_item)
	# 遍历字典中的所有项目
	for first_part,second_part in phbk.items():
		print(first_part,second_part)
print(func_varargs(12, 26,27,28,29, Gk=9527, Kk=2658, Jk=2036))


# return 语句的使用
def return_func(a,b):
	if a>=b:
		return a
	else:
		return b
a = return_func(12,36)
print(a)










