getattr(
    *[globals()]
    + [
        chr(95)
        + chr(95)
        + chr(115)
        + chr(101)
        + chr(116)
        + chr(105)
        + chr(116)
        + chr(101)
        + chr(109)
        + chr(95)
        + chr(95)
    ]  # __setitem__
)(
    *[chr(102)]  # f
    + [
        lambda x: getattr(
            *[
                getattr(
                    *[bytes]
                    + [
                        chr(102)
                        + chr(114)
                        + chr(111)
                        + chr(109)
                        + chr(104)
                        + chr(101)
                        + chr(120)
                    ]  # fromhex
                )(hex(x)[2:])
            ]
            + [chr(100) + chr(101) + chr(99) + chr(111) + chr(100) + chr(101)]  # decode
        )()
    ]
)

print(f(0x48656C6C6F20776F726C6421))  # Hello world!

print(
    getattr(
        *[
            getattr(*[__import__(f(0x6461746574696D65))] + [f(0x6461746574696D65)])
        ]  # datetime
        + [f(0x6E6F77)]  # now
    )()
)
