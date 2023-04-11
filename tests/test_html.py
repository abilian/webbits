from datetime import datetime

from dateutil.tz import UTC
from freezegun import freeze_time

from webbits.html import h, html


def test_without_attrs():
    assert h("h1", "test") == "<h1>test</h1>"
    assert h("h1", ["test", "toto"]) == "<h1>test\ntoto</h1>"


def test_with_attrs():
    assert h("h1", {}, _=["test"]) == "<h1>test</h1>"
    assert h("h1", {"class": "large"}, ["test", "toto"]) == "<h1>test\ntoto</h1>"


def test_attrs():
    h = html()
    h.div(class_="test", id="test")
    assert str(h) == "<div class=\"test\" id=\"test\" />"

    h = html()
    h.div(**{"class": "test", "id": "test"})
    assert str(h) == "<div class=\"test\" id=\"test\" />"

    h = html()
    h.div(class_=["test1", "test2"], id="test")
    assert str(h) == "<div class=\"test1 test2\" id=\"test\" />"

    h = html()
    h.div(hidden=True, id="test")
    assert str(h) == "<div hidden id=\"test\" />"

    h = html()
    h.div(hidden=False, id="test")
    assert str(h) == "<div id=\"test\" />"


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
