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
    *[chr(97)] # a
    + [
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
        )
    ]
)

a(
    *[chr(98)] # b
    + [
        lambda l: getattr(*[str()] + [chr(106) + chr(111) + chr(105) + chr(110)])(
            chr(c) for c in l
        )
    ]
)

a(
    *[chr(102)]  # f
    + [
        lambda x: getattr(
            *[
                getattr(
                    *[bytes]
                    + [
                        b([102] + [114] + [111] + [109] + [104] + [101] + [120])
                    ]  # fromhex
                )(hex(x)[2:])
            ]
            + [b([100] + [101] + [99] + [111] + [100] + [101])]  # decode
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
