from term import color
from term import slowprint as print

class Logger:
    def __init__(self, verbose: bool = False):
        self.first_log = True
        self.closing = False
        self.verbose = verbose
    
    def _print(self, string: str, no_notch: bool = False):
        if not no_notch:
            if self.first_log and self.closing:
                print(f"{color.Fore.WHITE} {string}")
                self.closing = False
                self.first_log = False
            elif self.first_log:
                print(f"{color.Fore.WHITE}⎡{string}")
                self.first_log = False
            elif self.closing:
                print(f"{color.Fore.WHITE}⎣{string}")
                self.closing = False
                self.first_log = True
            else:
                print(f"{color.Fore.WHITE}⎢{string}")
        else:
            print(f"{color.Fore.WHITE} {string}")
    
    def _print_icon(self, icon: str, string: str, no_notch: bool = False):
        self._print(f"{icon} {string}", no_notch=no_notch)

    def close_at_next(self):
        self.closing = True

    def debug(self, string: str):
        if self.verbose:
            self._print_icon(f"{color.Fore.DARK_GRAY}", f"{string}", no_notch=True)
    
    def info(self, string: str):
        self._print_icon(f"{color.Fore.CYAN}", f"{string}")
    
    def warn(self, string: str):
        self._print_icon(f"{color.Fore.YELLOW}", f"{string}")
    
    def error(self, string: str):
        self._print_icon(f"{color.Fore.RED}", f"{string}")
    
    def fatal(self, string: str):
        self._print_icon(f"{color.Fore.WHITE}{color.Back.DARK_RED}", f"{string} ")