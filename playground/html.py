from __future__ import annotations

from collections.abc import Iterable

# from bs4 import BeautifulSoup
#
#
# def remove_markup(html: str) -> str:
#     return BeautifulSoup(html, "html.parser").text
#     # return BeautifulSoup(html, features="lxml").text

class H:
    def __init__(self) -> None:
        self.elements = []

    def __lshift__(self, other):
        self.elements.append(other)
        return self

    def __str__(self):
        return "".join(str(e) for e in self.elements)

    def __getattr__(self, tag: str) -> ElementFactory:
        return ElementFactory(tag)

    def __call__(self):
        return str(self)


class ElementFactory:
    def __init__(self, tag: str) -> None:
        self.tag = tag

    def __call__(self, *args, **kwargs) -> Element:
        return Element(self.tag, *args, **kwargs)


class Element:
    def __init__(self, tag: str, *args, **kwargs) -> None:
        self.tag = snake_case_to_kebab_case(tag)
        self.children = list(args)
        if kwargs:
            self.children.append(kwargs)

    def __lshift__(self, other: Element) -> Element:
        self.children.append(other)
        return self

    def __str__(self) -> str:
        return self.render()

    def __repr__(self):
        return self.render()

    def render(self) -> str:
        attrs = []
        content = []
        for child in self.children:
            if isinstance(child, dict):
                for k, v in child.items():
                    kk = snake_case_to_kebab_case(k)
                    if v is True:
                        attrs.append(kk)
                    elif v is False:
                        continue
                    else:
                        attrs.append(f'{kk}="{v}"')
            elif isinstance(child, Iterable):
                for subchild in child:
                    content.append(str(subchild))
            else:
                content.append(str(child))
        if attrs:
            opening_tag = f"<{self.tag} {' '.join(attrs)}>"
        else:
            opening_tag = f"<{self.tag}>"
        closing_tag = f"</{self.tag}>"
        return opening_tag + "".join(content) + closing_tag


def snake_case_to_kebab_case(s: str) -> str:
    return "-".join(x for x in s.split("_") if x)
