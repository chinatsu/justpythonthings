import datetime

getattr(
    *list(globals() for _ in range(1))
    + list(
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
        for _ in range(1)
    )  # __setitem__
)(
    *list(chr(97))  # a
    + list(
        getattr(
            *list(globals() for _ in range(1))
            + list(
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
                for _ in range(1)
            )
        )
        for _ in range(1)
    )
)


a(
    *list(chr(102))  # f
    + list(
        lambda x: getattr(
            *list(
                getattr(
                    *list(bytes for _ in range(1))
                    + list(
                        chr(102)
                        + chr(114)
                        + chr(111)
                        + chr(109)
                        + chr(104)
                        + chr(101)
                        + chr(120)
                        for _ in range(1)
                    )  # fromhex
                )(
                    str(
                        getattr(
                            *list(hex(x) for _ in range(1))
                            + list(
                                chr(114)
                                + chr(101)
                                + chr(109)
                                + chr(111)
                                + chr(118)
                                + chr(101)
                                + chr(112)
                                + chr(114)
                                + chr(101)
                                + chr(102)
                                + chr(105)
                                + chr(120)
                                for _ in range(1)
                            )  # removeprefix
                        )(chr(48) + chr(120))
                    )
                )
                for _ in range(1)
            )
            + list(
                chr(100) + chr(101) + chr(99) + chr(111) + chr(100) + chr(101)
                for _ in range(1)
            )  # decode
        )()
        for _ in range(1)
    )
)

print(f(0x48656C6C6F20776F726C6421))  # Hello world!

print(
    getattr(
        *list(
            getattr(
                *list(datetime for _ in range(1))
                + list(f(0x6461746574696D65) for _ in range(1))
            )
            for _ in range(1)
        )  # datetime
        + list(f(0x6E6F77) for _ in range(1))  # now
    )()
)
