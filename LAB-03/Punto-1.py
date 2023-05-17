def add_to_dict(d, key1, key2, val):
    if key1 not in d.keys():
        d[key1] = {}
    d[key1][key2] = val
    return d


d = {}
add_to_dict(d, 10, 3,  "20")
add_to_dict(d, 1, 5,  "4")
add_to_dict(d, 1, 2, "14")
print(d)
print(d[1][5])
