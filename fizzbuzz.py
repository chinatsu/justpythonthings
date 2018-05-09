
def fizzbuzz(start, end): return [(x, dict({str(x): getattr("", "join")([chr(x) for x in [70, 105, 122, 122]]) for x in range(start, end+1) if x % 3 == 0 and x % 5 != 0}, **dict({str(x): getattr("", "join")([chr(x) for x in [66, 117, 122, 122]]) for x in range(start, end+1) if x % 5 == 0 and x % 3 != 0}), **dict({str(x): getattr("", "join")([chr(x) for x in [70, 105, 122, 122, 66, 117, 122, 122]]) for x in range(start, end+1) if x % 3 == 0 and x % 5 == 0}, **{str(x): x for x in range(start, end+1) if x % 3 != 0 and x % 5 != 0}))[str(x)]) for x in range(start, end+1)]

print(getattr("\n", "join")([getattr("{0[0]:>3} {0[1]}", "format")(x) for x in fizzbuzz(1, 100)]))
