import random

def coin_tosses():

    print "Starting the program. . ."

    head_count = 0
    tail_count = 0

    for i in range(1, 20):

        string = "Attemp #"
        string += str(i) 
        string += ": Throwing a coin... It's a "
        head_or_tails = ""
        rand = random.randint(0, 1)

        if rand == 1:
            head_or_tails = "head"
            head_count += 1
        else:
            head_or_tails = "tail"
            tail_count += 1

        string += head_or_tails
        string += "! ... Got "
        string += str(head_count)
        string += " head(s) so far and "
        string += str(tail_count)
        string += " tail(s) so far"
        
        print string

        print "Ending the program. Thank you!"

coin_tosses()