#  数据结构：List 例子

shoplist = ["banana", "apple", "mango"]

print("I have",len(shoplist),"items to purchase")

# 使用end参数，可以通过一个空格结束，而不是换行
print("This items are:",end=" ")
for item in shoplist:
	print(item, end=" ")

print("\nI also have to buy rice")
# append方法添加项
shoplist.append("rice")
print("My shoplist is now : ",shoplist)

print("I will sort my shoplist now")
# sort方法会影响列表本身
shoplist.sort()
print("Sorted result is :",shoplist)

print("The first item i will buy is",shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print("I bought the",olditem)
print("My shoplist now is",shoplist)
























