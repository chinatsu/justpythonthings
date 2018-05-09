# this is actually pointless
def kinda_similar(a, b):
    while a != type(object) and b != type(object):
        a = type(a)
        b = type(b)
    return a == b

print(kinda_similar("a", 1.41))
