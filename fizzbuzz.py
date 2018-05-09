def fizzbuzz(start, end):
    return [
        (
            x, # the number
            dict(
                # fizz
                {str(x): getattr("", "join")([chr(x) for x in [70, 105, 122, 122]]) for x in range(start, end+1) if x % 3 == 0},
                # buzz, note that we need `x % 3 != 0` as to not step on fizzbuzz' toes. (type object got multiple values for argument)
                # something weird about the **args here, since `x % 5 != 0` is not needed in the above dict
                **{str(x): getattr("", "join")([chr(x) for x in [66, 117, 122, 122]]) for x in range(start, end+1) if x % 5 == 0 and x % 3 != 0},
                # fizzbuzz
                **{str(x): getattr("", "join")([chr(x) for x in [70, 105, 122, 122, 66, 117, 122, 122]]) for x in range(start, end+1) if x % 3 == 0 and x % 5 == 0},
                 # numbers
                **{str(x): x for x in range(start, end+1) if x % 3 != 0 and x % 5 != 0}
            )[str(x)] # the fizzbuzz part
        )
        for x in range(start, end+1) # also, make it ordered i guess
    ]

print(getattr("\n", "join")([getattr("{0[0]:>3} {0[1]}", "format")(x) for x in fizzbuzz(1, 100)]))
