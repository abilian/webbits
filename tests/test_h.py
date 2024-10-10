"""
Test the h() function.

It will be refactored later for better consistency with the html() builder.

Do not use for now.
"""

from webbits.html import h


def test_without_attrs():
    assert h("h1", "test") == "<h1>test</h1>"
    assert h("h1", ["test", "toto"]) == "<h1>test toto</h1>"
    assert h("h1", "test", "toto") == "<h1>test toto</h1>"
    assert h("h1", 1) == "<h1>1</h1>"
    assert h("h1", _=["test"]) == "<h1>test</h1>"


def test_with_attrs():
    assert h("h1", {"class": "lg"}, _=["test"]) == '<h1 class="lg">test</h1>'
    assert h("h1", {"class": "lg"}, ["test", "toto"]) == '<h1 class="lg">test toto</h1>'
    assert h("h1", **{"class": "lg"}) == '<h1 class="lg"></h1>'
    assert h("h1", class_="lg") == '<h1 class="lg"></h1>'
    assert h("h1", a_b="1") == '<h1 a-b="1"></h1>'
