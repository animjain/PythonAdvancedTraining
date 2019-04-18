def style(s):
    def decorate(fn):
        if s == "upper":
            def wrap():
                return fn().upper()
        elif s == "italics":
            def wrap():
                return "<italics>" + fn() + "</italics>"
        else:
            wrap = fn
        return wrap
    return decorate


@style("upper")
@style("italics")
def greet():
    return "Hello world"


greet()