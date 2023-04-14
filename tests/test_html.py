from datetime import datetime
from unittest import skip

from dateutil.tz import UTC
from freezegun import freeze_time
from markupsafe import Markup

from webbits.html import html


def test_attrs():
    h = html()
    h.div(class_="test", id="test")
    assert str(h) == '<div class="test" id="test" />'

    h = html()
    h.div(**{"class": "test", "id": "test"})
    assert str(h) == '<div class="test" id="test" />'

    h = html()
    h.div(class_=["test1", "test2"], id="test")
    assert str(h) == '<div class="test1 test2" id="test" />'

    h = html()
    h.div(hidden=True, id="test")
    assert str(h) == '<div hidden id="test" />'

    h = html()
    h.div(hidden=False, id="test")
    assert str(h) == '<div id="test" />'

    h = html()
    h.div(count=1, id="test")
    assert str(h) == '<div count="1" id="test" />'


def test_nested():
    h = html()
    with h.ul():
        h.li("Blah")
    assert str(h) == "<ul>\n <li>Blah</li>\n</ul>"


def test_non_str():
    h = html()
    h.div(1)
    assert str(h) == "<div>1</div>"

    h = html()
    h.div([1, 2, 3])
    assert str(h) == "<div>[1, 2, 3]</div>"

    h = html()
    h.div(1, 2, 3)
    assert str(h) == "<div>1 2 3</div>"


@skip
def test_nested_fail():
    h = html()
    h.ul(h.li())
    assert str(h) == '<div count="1" id="test" />'


def test_attrs_as_dict():
    h = html()
    h.div({"class": "test", "id": "test"})
    assert str(h) == '<div class="test" id="test" />'


def test_markup():
    inner = "<span>123</span>"
    h = html()
    h.div(inner)
    assert str(h) == "<div>&lt;span&gt;123&lt;/span&gt;</div>"

    h = html()
    h.div(Markup(inner))
    assert str(h) == f"<div>{inner}</div>"


@freeze_time("2023-03-14")
def test_advanced():
    h = html()
    with h.html:
        with h.head():
            h.title("Hello world")
            h.meta(charset="utf-8")
        with h.body():
            h.h1("Hello world")
            h.p("This is a paragraph.")

            today = datetime.now(tz=UTC).date()
            h.p(f"Today is {today}.")

            if today.month == 3 and today.day == 14:
                h.p("Happy Pi Day!")

    result = str(h)

    expected = (
        "<html>\n"
        " <head>\n"
        "  <title>Hello world</title>\n"
        '  <meta charset="utf-8" />\n'
        " </head>\n"
        " <body>\n"
        "  <h1>Hello world</h1>\n"
        "  <p>This is a paragraph.</p>\n"
        "  <p>Today is 2023-03-14.</p>\n"
        "  <p>Happy Pi Day!</p>\n"
        " </body>\n"
        "</html>"
    )
    assert result == expected
