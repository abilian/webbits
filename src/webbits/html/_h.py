from functools import singledispatch


@singledispatch
def h(*args, **kw):
    pass


@h.register
def h_list(list_: list) -> str:
    return "\n".join(list_)


@h.register
def h_other(tag: str, *args, **kw):
    attrs = {}
    children = []

    if len(args) == 0:
        pass

    elif isinstance(args[0], dict):
        attrs = args[0]
        if len(args) == 2:
            children = args[1]

    elif isinstance(args[0], str):
        children = [args[0]]

    elif isinstance(args[0], list):
        children = args[0]

    for k, v in kw.items():
        if k == "_":
            children = v
        else:
            attrs[k] = v

    return f"<{tag}>{h(children)}</{tag}>"
