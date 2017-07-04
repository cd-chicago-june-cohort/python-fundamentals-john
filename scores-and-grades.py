import random

# Pass in the number of scores 

def scores_and_grades(num):

    print "Scores and Grades"

    scores = []
    
    for i in range(num):
        rand =  random.randint(60, 100)
        scores.append(rand)

    for score in scores:
        string = "Score: "
        string += str(score)
        string += "; Your grade is "
        grade = "D"
        if 70 <= score <= 79:
            grade = "C"
        elif 80 <= score <= 89:
            grade = "B"
        elif score >= 90:
            grade = "A"
        string += grade
        print string

    print "End of the program. Bye!"

scores_and_grades(10)


