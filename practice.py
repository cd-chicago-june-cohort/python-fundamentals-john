# Find and Replace
words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
print words.replace("day", "month")


# Min and Max
x = [2,54,-2,7,12,98]
print min(x)
print max(x)


# First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[len(x) - 1]
newArr = []
newArr.append(x[0])
newArr.append(x[len(x) - 1])
print newArr


# New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
list_a = x[:len(x)/2]
list_b = x[len(x)/2:]
list_c = [list_a]
for item in list_b:
    list_c.append(item)
print list_c
