import colorama
from colorama import Fore, Back, Style, Cursor
colorama.init(autoreset=True)
from logger import Logger
import cmdlib
import cmds

logger = Logger(verbose=False)
logger.close_at_next()

context = cmdlib.Context(startdir="/", verbose=False)

logger.info(f"morph3us daughter-of-satan (m3dos)")
logger.info(f"by 0xDEADC0DE_")

while context.running:
    print(f"{Fore.GREEN}╭@{Fore.MAGENTA}{context.dir}{Fore.GREEN}#")
    print(end=f"{Fore.GREEN}╰╴{Fore.WHITE}")
    prompt = input().split(" ")
    
    context.app_found = False
    for command in cmds.commands:
        if command.name == prompt[0].lower():
            context.app_found = True
            context.returned = command.run(context, prompt[1:])
            break
    
    if context.app_found:
        print(f"{Fore.WHITE}* {Fore.RED if context.returned else Fore.GREEN}App returned code {context.returned}")
    else:
        print(f"{Fore.WHITE}* {Fore.RED}No such command")