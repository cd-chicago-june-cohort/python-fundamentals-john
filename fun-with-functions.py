# Odd/Even:
def odd_even():
    for num in range(1, 2001):
        string = "Number is "
        string += str(num)
        string += ". This is an "
        even_or_odd = "odd number."
        if num % 2 == 0:
            even_or_odd = "even number."
        string += even_or_odd
        print string



# Multiply:
def multiply(lst, num):
    for i in range(len(lst)):
        lst[i] = lst[i] * num
    return lst



# Hacker Challenge
def layered_multiples(arr):
    new_arr = []
    for i in range(len(arr)):
        sub_arr = []
        j = 1
        while j <= arr[i]:
            sub_arr.append(1)
            j += 1
        new_arr.append(sub_arr)
    return new_arr

x = layered_multiples(multiply([2,4,5],3))
print x