from types import *

def type_list(lst):
    types = []
    string = ""
    sum = 0
    for item in lst:
        item_type = type(item)
        if item_type not in types:
            types.append(item_type)
        if item_type == type(""):
            string += ""
            string += item
        if item_type == type(0) or item_type == type(0.0):
            sum += item

    list_type = ""  
    #print len(types)


    if len(types) == 1:
        if types[0] == type(True):
            list_type = "Boolean"
        elif types[0] == type(""):
            list_type = "string"
        elif types[0] == type(0):
            list_type = "integer"
        elif types[0] == type(0.0):
            list_type = "float"
        elif types[0] == type([]):
            list_type = "list"
        elif types[0] == type({}):
            list_type = "dictionary"
        elif types[0] == type(()):
            list_type = "tuple"
    else:
        list_type = "mixed"
        
        
        
    print "The list you entered is of " + list_type + " type."

    print string

    print sum


type_list(['magical unicorns',19,'hello',98.98,'world'])