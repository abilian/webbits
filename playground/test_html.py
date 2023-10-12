from playground.html import H


def test_h() -> None:
    h = H()
    el = h.a(href="http://localhost/", class_="h1")
    el <<= h.span("label")
    el <<= h.span(aria_hidden=True)
    expected = '<a href="http://localhost/" class="h1"><span>label</span><span aria-hidden></span></a>'
    assert str(el) == expected


def test_h_alt_syntax() -> None:
    h = H()
    el = h.a(
        {"href": "http://localhost/", "class": "h1"},
        h.span("label"),
        h.span(aria_hidden=True),
    )
    expected = '<a href="http://localhost/" class="h1"><span>label</span><span aria-hidden></span></a>'
    assert str(el) == expected


def test_h_alt_syntax2() -> None:
    h = H()
    el = h.a(
        {"href": "http://localhost/", "class": "h1"},
        [h.span("label"), h.span(aria_hidden=True)],
    )
    expected = '<a href="http://localhost/" class="h1"><span>label</span><span aria-hidden></span></a>'
    assert str(el) == expected
