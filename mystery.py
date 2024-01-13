import re

def my_func(x):
    a = x.split(" ")
    y = []
    for x in a:
        x2 = re.sub("[.!?]", "", x)
        y.append(x2)
    z = {}
    for stuff in y:
        if len(stuff) in z: 
            z[len(stuff)] = z[len(stuff)] + [stuff]
        else:
            z[len(stuff)]=[stuff]
    a = {}
    for y in z:
        for x in z[y]:
            if len(x) % 2 == 1:
                a[y] = z[y]
        else:
            continue
    return a




# Tests
assert(my_func("This is a sentence. And yet another one!") == {1: ['a'], 3: ['And', 'yet', 'one'], 7: ['another']})
assert(my_func("Miscollated alphabetic superimposition") == {11: ['Miscollated'], 15: ['superimposition']})
print(my_func("a a a a bb bb bb ccc ccc") == {1: ['a', 'a', 'a', 'a'], 3: ['ccc', 'ccc']})