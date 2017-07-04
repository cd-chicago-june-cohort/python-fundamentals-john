
# Part I
def draw_stars(lst):
    for num in lst:
        print "*" * num


# Part II
def draw_stars_modified(lst):
    for item in lst:
        if type(item) == type(0):
            print "*" * item
        elif type(item) == type(""):
            print item[0].lower() * len(item)

draw_stars_modified([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])