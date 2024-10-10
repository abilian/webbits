class H:
    def __init__(self):
        self._stack = []
        self._result = []

    def __lshift__(self, other):
        self._result.append(other)

    def __getattr__(self, name):
        self._stack.append(name)
        return self

    def __enter__(self):
        return self

    def __exit__(self, *args):
        name = self._stack.pop()
        self._result.append(f"</{name}>")

    def __str__(self):
        return "".join(self._result)


def test_1():
    h = H()
    h << h.h1("title")
    with h.p.ul as ul:
        for i in range(3):
            ul << h.li(f"li {i}")
    result = str(h)
    assert (
        result
        == "<h1>title</h1><p><ul><li>li 0</li><li>li 1</li><li>li 2</li></ul></p>"
    )


# Or


def test_2():
    h = H()
    h << h.h1("title")
    with h.p.ul:
        for i in range(3):
            h << h.li(f"li {i}")
    result = str(h)
    assert (
        result
        == "<h1>title</h1><p><ul><li>li 0</li><li>li 1</li><li>li 2</li></ul></p>"
    )
