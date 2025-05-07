import os
from term import color
from logger import Logger
import cmdlib
import cmds
import interoperability as io
from input import acinput
from term import slowprint as print

logger = Logger(verbose=False)

context = cmdlib.Context(startdir=io.env.home, verbose=False)
cmdlib.register_cmds(context, cmds.commands)
commands = len(cmds.commands)
aliases = -commands
for command in cmds.commands:
    aliases += len(command.aliases)

logger.info(f"morph3us daughter-of-satan  (m3dos)")
logger.close_at_next()
logger.info(f"by 0xDEADC0DE_")
logger.debug(f"loaded {commands} command{"s" if commands != 1 else ""} and {aliases} alias{"es" if aliases != 1 else ""}")

while context.running:
    os.chdir(context.dir)
    print(f"{color.Fore.GREEN}╭@{color.Fore.MAGENTA}{("?" + context.dir).replace("?" + io.env.home, "~").replace("?", "")}{color.Fore.GREEN}>")
    prompt = acinput(f"{color.Fore.GREEN}└╴{color.Fore.RED}", context.ac, ignore_empty=True, ignore_ac=True).split(" ")
    
    context.app_found = False
    for command in cmds.commands:
        if prompt == [""]:
            break
        if command.iscommand(prompt[0]):
            context.app_found = True
            context.returned = command.run(context, prompt[1:])
            break
    
    if context.app_found:
        if context.returned == None:
            print(f" {color.Fore.DARK_GRAY} App closed unexpectedly")
        elif context.returned == 0:
            print(f" {color.Fore.GREEN} App returned code {context.returned}")
        else:
            print(f" {color.Fore.RED} App returned code {context.returned}")