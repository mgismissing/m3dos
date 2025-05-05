import colorama
from colorama import Fore, Back, Style, Cursor
colorama.init(autoreset=True)

class Logger:
    def __init__(self, verbose: bool = False):
        self.first_log = True
        self.closing = False
        self.verbose = verbose
    
    def _print(self, string: str):
        if self.first_log:
            print(f"{Fore.WHITE}⎡ {string}")
            self.first_log = False
        elif self.closing:
            print(f"{Fore.WHITE}⎣ {string}")
            self.closing = False
            self.first_log = True
        else:
            print(f"{Fore.WHITE}⎢ {string}")
    
    def _print_icon(self, icon: str, string: str):
        self._print(f"{icon} {string}")

    def close_at_next(self):
        self.closing = True

    def debug(self, string: str):
        self._print_icon(f"{Fore.LIGHTBLACK_EX}[◆]", f"{string}")
    
    def info(self, string: str):
        self._print_icon(f"{Fore.CYAN}[◆]", f"{string}")
    
    def warn(self, string: str):
        self._print_icon(f"{Fore.YELLOW}[⚠]", f"{string}")
    
    def error(self, string: str):
        self._print_icon(f"{Fore.RED}[X]", f"{string}")
    
    def fatal(self, string: str):
        self._print_icon(f"{Fore.BLACK}{Back.RED}[X]", f"{string}")