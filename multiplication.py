

lst = ["x", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print lst
for num in range(1, 13):
    new_lst = [0]
    new_lst[0] = num
    for digit in range(1, 13):
        entry = str(num * lst[digit])
        new_lst.append(entry)
    print new_lst