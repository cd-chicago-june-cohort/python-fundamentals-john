
# Print all odd numbers from 1 to 1000:
for x in range(1, 1000, 2):
    print x

# Print all multiples of 5 from 5 to 1,000,000:
for x in range(5, 1000000, 5):
    print x

# Sum a list:
a = [1, 2, 5, 10, 255, 3]
sum = 0
for item in a:
    sum += item
print sum

# Average that list:
avg = sum//len(a)
print avg