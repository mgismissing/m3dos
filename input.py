import readchar
from term import color

def autocomplete(string: str, ac: dict[str, str]):
    temp = string + " "
    for key in ac:
        if temp.startswith(key + " "):
            temp = temp.replace(key + " ", ac[key]+key+color.Fore.DARK_YELLOW+" ")
            break
    return temp[:-1]

def acinput(prompt: str, ac: dict[str, str], ignore_empty: bool = False, ignore_ac: bool = False):
    char = ""
    string = ""
    while char != readchar.key.ENTER:
        print(end="\r"+color.Screen.CLEAR_LINE+prompt+autocomplete(string, ac), flush=True)
        char = readchar.readchar()
        match char:
            case readchar.key.BACKSPACE: string = string[:-1]
            case _:
                if 0x20 <= ord(char) <= 0xFF: string += char
        if ignore_empty and char == readchar.key.ENTER and string == "":
            char = ""
            continue
        elif ignore_ac and autocomplete(string, ac) == string:
            char = ""
            continue
    print()
    return string