# Part I

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def print_names(lst):
    for obj in lst:
        print obj["first_name"] + " " + obj["last_name"]

print_names(students)


# Part II
users = {
    'Students': [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
    'Instructors': [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}

def print_users(obj):
    for key, value in obj.iteritems():
        print key
        counter = 1
        for i in range(len(value)):
            name = value[i]["first_name"].upper() + " " + value[i]["last_name"].upper()
            length = len(value[i]["first_name"]) + len(value[i]["last_name"])
            print str(counter) + " - " + name + " - " + str(length)
            counter += 1

print_users(users)