def fizzbuzz(start, end):
    return [
        (
            x, # the number
            # create a dict with all of the fizzbuzz data, and look up what lies at index x.
            dict(
                # fizz
                {str(x): getattr("", "join")(
                    getattr("{3}{2}{1}{1}", "format")(
                        getattr(__import__('random'), 'seed')("wrong"),
                        chr(122),
                        getattr(__import__('random'), "choice")(
                            getattr("a e i o u", "split")()),
                        getattr(getattr(__import__('random'), "choice")(
                            getattr("b c d f g h j k l m n p q r s t v x y z", "split")()), "upper")())) for x in range(start, end+1) if x % 3 == 0},
                # buzz, note that we need `x % 3 != 0` as to not step on fizzbuzz' toes. as far as i understand, each of the **kwargs
                # will get expanded to essentially dict(fizz, str(5)="Buzz", str(10)="Buzz", ...), (except you can't normally have expressions as keyword)
                # and at some point down the line, we'd have 15="Buzz" and 15="FizzBuzz" in the same list of kwargs.
                **{str(x): getattr("", "join")(
                    getattr("{3}{2}{1}{1}", "format")(
                        getattr(__import__('random'), 'seed')("🤷🏻‍"),
                        chr(122),
                        getattr(__import__('random'), "choice")(
                            getattr("a e i o u", "split")()),
                        getattr(getattr(__import__('random'), "choice")(
                            getattr("b c d f g h j k l m n p q r s t v x y z", "split")()), "upper")())) for x in range(start, end+1) if x % 5 == 0 and x % 3 != 0},
                # fizzbuzz
                **{str(x): getattr("", "join")(
                    getattr("{3}{2}{1}{1}{4}{5}{1}{1}", "format")(
                        getattr(__import__('random'), 'seed')("destructibility"),
                        chr(122),
                        getattr(__import__('random'), "choice")(
                            getattr("a e i o u", "split")()),
                        getattr(getattr(__import__('random'), "choice")(
                            getattr("b c d f g h j k l m n p q r s t v x y z", "split")()), "upper")(),
                        getattr(getattr(__import__('random'), "choice")(
                            getattr("b c d f g h j k l m n p q r s t v x y z", "split")()), "upper")(),
                        getattr(__import__('random'), "choice")(
                                getattr("a e i o u", "split")()))) for x in range(start, end+1) if x % 3 == 0 and x % 5 == 0},
                 # numbers
                **{str(x): x for x in range(start, end+1) if x % 3 != 0 and x % 5 != 0}
            )[str(x)] # the fizzbuzz part
        )
        for x in range(start, end+1) # also, make it ordered i guess
    ]

print(getattr("\n", "join")([getattr("{0[0]:>3} {0[1]}", "format")(x) for x in fizzbuzz(1, 100)]))
