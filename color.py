import colorama
colorama.init(autoreset=False)

class Fore:
    BLACK = colorama.Fore.BLACK
    DARK_RED = colorama.Fore.RED
    DARK_GREEN = colorama.Fore.GREEN
    DARK_YELLOW = colorama.Fore.YELLOW
    DARK_BLUE = colorama.Fore.BLUE
    DARK_MAGENTA = colorama.Fore.MAGENTA
    DARK_CYAN = colorama.Fore.CYAN
    LIGHT_GRAY = colorama.Fore.WHITE

    DARK_GRAY = colorama.Fore.LIGHTBLACK_EX
    RED = colorama.Fore.LIGHTRED_EX
    GREEN = colorama.Fore.LIGHTGREEN_EX
    YELLOW = colorama.Fore.LIGHTYELLOW_EX
    BLUE = colorama.Fore.LIGHTBLUE_EX
    MAGENTA = colorama.Fore.LIGHTMAGENTA_EX
    CYAN = colorama.Fore.LIGHTCYAN_EX
    WHITE = colorama.Fore.LIGHTWHITE_EX

    RESET = colorama.Fore.RESET

class Back:
    BLACK = colorama.Back.BLACK
    DARK_RED = colorama.Back.RED
    DARK_GREEN = colorama.Back.GREEN
    DARK_YELLOW = colorama.Back.YELLOW
    DARK_BLUE = colorama.Back.BLUE
    DARK_MAGENTA = colorama.Back.MAGENTA
    DARK_CYAN = colorama.Back.CYAN
    LIGHT_GRAY = colorama.Back.WHITE

    DARK_GRAY = colorama.Back.LIGHTBLACK_EX
    RED = colorama.Back.LIGHTRED_EX
    GREEN = colorama.Back.LIGHTGREEN_EX
    YELLOW = colorama.Back.LIGHTYELLOW_EX
    BLUE = colorama.Back.LIGHTBLUE_EX
    MAGENTA = colorama.Back.LIGHTMAGENTA_EX
    CYAN = colorama.Back.LIGHTCYAN_EX
    WHITE = colorama.Back.LIGHTWHITE_EX

    RESET = colorama.Back.RESET

class Screen:
    CLEAR_LINE = colorama.ansi.clear_line()
    CLEAR_SCREEN = colorama.ansi.clear_screen()
    RESET_STYLE = colorama.Style.RESET_ALL