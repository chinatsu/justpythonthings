import datetime

getattr(
    *list(globals() for _ in range(1)).__add__(
        list(
            chr(95)
            .__add__(chr(95))
            .__add__(chr(115))
            .__add__(chr(101))
            .__add__(chr(116))
            .__add__(chr(105))
            .__add__(chr(116))
            .__add__(chr(101))
            .__add__(chr(109))
            .__add__(chr(95))
            .__add__(chr(95))
            for _ in range(1)
        )
    )  # __setitem__
)(
    *list(chr(97)).__add__(  # a
        list(
            getattr(
                *list(globals() for _ in range(1)).__add__(
                    list(
                        chr(95)
                        .__add__(chr(95))
                        .__add__(chr(115))
                        .__add__(chr(101))
                        .__add__(chr(116))
                        .__add__(chr(105))
                        .__add__(chr(116))
                        .__add__(chr(101))
                        .__add__(chr(109))
                        .__add__(chr(95))
                        .__add__(chr(95))
                        for _ in range(1)
                    )
                )
            )
            for _ in range(1)
        )
    )
)


a(
    *list(chr(102)).__add__(  # f
        list(
            lambda x: getattr(
                *list(
                    getattr(
                        *list(bytes for _ in range(1)).__add__(
                            list(
                                chr(102)
                                .__add__(chr(114))
                                .__add__(chr(111))
                                .__add__(chr(109))
                                .__add__(chr(104))
                                .__add__(chr(101))
                                .__add__(chr(120))
                                for _ in range(1)
                            )
                        )  # fromhex
                    )(
                        str(
                            getattr(
                                *list(hex(x) for _ in range(1)).__add__(
                                    list(
                                        chr(114)
                                        .__add__(chr(101))
                                        .__add__(chr(109))
                                        .__add__(chr(111))
                                        .__add__(chr(118))
                                        .__add__(chr(101))
                                        .__add__(chr(112))
                                        .__add__(chr(114))
                                        .__add__(chr(101))
                                        .__add__(chr(102))
                                        .__add__(chr(105))
                                        .__add__(chr(120))
                                        for _ in range(1)
                                    )
                                )  # removeprefix
                            )(chr(48).__add__(chr(120)))
                        )
                    )
                    for _ in range(1)
                ).__add__(
                    list(
                        chr(100)
                        .__add__(chr(101))
                        .__add__(chr(99))
                        .__add__(chr(111))
                        .__add__(chr(100))
                        .__add__(chr(101))
                        for _ in range(1)
                    )
                )  # decode
            )()
            for _ in range(1)
        )
    )
)

print(f(0x48656C6C6F20776F726C6421))  # Hello world!

print(
    getattr(
        *list(
            getattr(
                *list(datetime for _ in range(1)).__add__(
                    list(f(0x6461746574696D65) for _ in range(1))
                )
            )
            for _ in range(1)
        ).__add__(  # datetime
            list(f(0x6E6F77) for _ in range(1))
        )  # now
    )()
)
