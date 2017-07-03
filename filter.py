def find_type(obj):
    t = type(obj)
    if t == type(0):
        if obj >= 100:
            print "That's a big number!"
        else:
            print "That's a small number"
    elif t == type(""):
        if len(obj) >= 50:
            print "Long sentence."
        else:
            print "Short sentence."
    elif t == type([]):
        if len(obj) >= 10:
            print "Big list!"
        else:
            print "Short list."



find_type(45)
find_type(455)
find_type("Rubber baby buggy bumpers")
find_type("Tell me and I forget. Teach me and I remember. Involve me and I learn.")
find_type([4,34,22,68,9,13,3,5,7,9,2,12,45,923])
find_type([1,7,4,21])