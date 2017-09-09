#  python控制流例程
print("Usage of  if / for / while.")


# if-else- demo
keyval = 25
guss = int(input("input a integer:"))
if guss == keyval:
	print("Wonderful, just do it")
# 注意：这里不是else if
elif guss < keyval:
	print("Your number is little")
else:
	print("Your number is large")
print("Done")


# while demo
keyval = 25
runflag = True

while runflag:
	guss = int(input("input a integer:"))
	if guss == keyval:
		print("Wonderful, just do it")
		runflag = False
	elif guss < keyval:
		print("Your number is little")
	else:
		print("Your number is large")
# while还可以匹配else，神奇不神奇
else:
	print("The while loop is finished.")
		
print("Done")


# for demo
for i in range(1,6):
	print(i)
else:
	print("The for loop is finished.")

# 使用len可以获得字符串长度
st = "0gaokang_tianmiao"
print("len is",len(st))















