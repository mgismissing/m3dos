import time
import typing
import color

def slowprint(*values: object, sep: str | None = " ", end: str | None = "\n", flush: typing.Literal[False] = False):
    strvalues = []
    for value in values:
        strvalues.append(str(value))
    toprint = sep.join(strvalues) + end
    toprint = toprint.replace("\n", f"{color.Screen.RESET_STYLE}\n")
    i = 0
    full = ""
    print(end=color.Screen.RESET_STYLE)
    while i < len(toprint):
        if toprint[i] == "\033":
            char = toprint[i:].split("m", 1)[0]+"m"
            i += len(char)-1
        else:
            char = toprint[i]
        full += char
        print(end=char, flush=True)
        if i % 16 == 0:
            time.sleep(0)
        i += 1