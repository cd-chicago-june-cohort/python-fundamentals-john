def find_characters(lst, char):
    new_list = []
    for item in lst:
        if char in item:
            new_list.append(item)

    print new_list

find_characters(['hello','world','my','name','is','Anna'], "o")