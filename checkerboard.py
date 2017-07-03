def checker_board():
    for turn in range(0, 9):
        row = "* * * * *"
        if turn % 2 == 0:
            print row
        else:
            print " " + row


checker_board()