john = {
    "name": "JohnPaul Doherty",
    "age": "26",
    "country of birth": "the U.S.A.",
    "favorite language": "JavaScript"
}

def  print_dict_info(dictionary):
    for key, value in dictionary.iteritems():
        print "My " + key + " is " + value + "."

print_dict_info(john)
