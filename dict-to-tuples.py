
def dict_to_tuple(dictionary):
    keys = dictionary.keys()
    vals = dictionary.values()
    zipped = zip(keys, vals)
    print zipped
    return zipped



my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}



dict_to_tuple(my_dict)