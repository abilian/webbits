from xml.sax.saxutils import quoteattr


def h(tag: str, *args, **kw):
    attrs = {}
    children = []

    for arg in args:
        if isinstance(arg, dict):
            for k, v in arg.items():
                attrs[k] = v
        elif isinstance(arg, list):
            children += arg
        else:
            children.append(str(arg))

    for k, v in kw.items():
        if k == "_":
            if isinstance(v, list):
                children += v
            else:
                children.append(v)
        else:
            attr_name = k
            if attr_name.endswith("_"):
                attr_name = attr_name[:-1]
            attr_name = attr_name.replace("_", "-")
            attrs[attr_name] = v

    attrs_str = "".join(f" {k}={quoteattr(v)}" for k, v in attrs.items())

    return f"<{tag}{attrs_str}>{' '.join(children)}</{tag}>"
