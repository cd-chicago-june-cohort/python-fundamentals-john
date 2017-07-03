
def foo_bar():
    for num in range(1, 1000):
        prime = True
        for value in range((num/2), 1, -1):
            if  num % value == 0:
                prime = False
        if prime == True:
            print str(num) + " - Foo"
        else:
            for integer in range((num/2), 1, -1):
                if integer * integer == num:
                    print str(num) + " - Bar"

foo_bar()


