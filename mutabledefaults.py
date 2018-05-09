# http://effbot.org/zone/default-values.htm

def hm(a=[]):
    a.append("lol")
    print(a)
    hm()

hm() # ends up hitting recursion depth limit
