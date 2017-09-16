#coding = utf-8

### 字典例子

print("Usage of dict.")

ab = {"gaokang":"17601219718", "zhangxixi":"18603536289", "tianmiao":"18803362359"}

print("gaokang number is",ab["gaokang"])

# 删除一对键值-值
del ab["zhangxixi"]

print("There are {} contacts in the address book".format(len(ab)))

for name,phone in ab.items():
	print("Contact {} is {}".format(name,phone))

# 添加一对键值-值
ab["haha"] = "18603321569"

if "haha" in ab:
	print("\nhaha phone is ",ab["haha"])




















