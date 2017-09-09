# 使用模块的例子

import sys

print("The command line args are:")
for i in sys.argv:
	print(i)
print("\n The pyton path is",sys.path,"\n\n\n")



# __name__属性的使用
if __name__ == "__main__":
	print("This program is being run by itself")
else:
	print("I am being imported by other.")


















