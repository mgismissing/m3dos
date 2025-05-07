import cmdlib
from logger import Logger
import os
from term import color
import interoperability as io
from term import slowprint as print
from math import ceil

class Exit(cmdlib.Command):
    def __init__(self):
        cmdlib.Command.__init__(self, name="Exit", aliases=["exit"], accolor=color.Fore.YELLOW)
    def run(self, ctx: cmdlib.Context, args: list[str]) -> int:
        ctx.running = False
        return 0

class DirList(cmdlib.Command):
    def __init__(self):
        cmdlib.Command.__init__(self, name="DirectoryList", aliases=["ls", "dir"], accolor=color.Fore.YELLOW)
    def run(self, ctx: cmdlib.Context, args: list[str]) -> int:
        content = os.listdir(ctx.dir+"\\")
        elementw = int((os.get_terminal_size()[0]-12) / 3)
        newline = 3
        for i in range(len(content)):
            element = content[i]
            if element.startswith("."): continue
            elementl = ceil(len(element) / elementw)
            #print(element, elementl)
            if newline - elementl < 0: print()
            print(end=f"{f"{color.Fore.YELLOW} 󰉋" if os.path.isdir(f"{ctx.dir}\\{element}") else f"{color.Fore.GREEN if (os.path.splitext(ctx.dir+"\\"+element)[1][1:] in (io.ext.executable + io.ext.script)) else color.Fore.WHITE} 󰈔"}{content[i].ljust((elementw+3)*elementl-3)}")
            newline -= elementl
            if newline <= 0:
                print()
                newline = 3
        if newline != 3: print()
        return 0
    
class ChangeDirectory(cmdlib.Command):
    class Error:
        PATH_NOT_GIVEN = 1
        PATH_INEXISTENT = 2
        PATH_NOT_DIRECTORY = 3
    def __init__(self):
        cmdlib.Command.__init__(self, name="ChangeDirectory", aliases=["cd"], accolor=color.Fore.YELLOW)
    def run(self, ctx: cmdlib.Context, args: list[str]) -> int:
        logger = Logger(verbose=False)
        try: path = args[0].replace("/", "\\")
        except IndexError:
            logger.close_at_next()
            logger.fatal("Expected path as argument 1")
            return ChangeDirectory.Error.PATH_NOT_GIVEN
        if not path in [".."]:
            if path.startswith("\\"): path = path.replace("\\", io.env.root, 1)
            if not path.startswith(io.env.root): path = f"{ctx.dir}\\{path}"
            if not os.path.exists(path):
                logger.close_at_next()
                logger.fatal("Path doesn't exist")
                return ChangeDirectory.Error.PATH_INEXISTENT
            if not os.path.isdir(path):
                logger.close_at_next()
                logger.fatal("Path is not a directory")
                return ChangeDirectory.Error.PATH_NOT_DIRECTORY
        if path == "..":
            if len(ctx.dir.split("\\")) > 1: ctx.dir = "\\".join(ctx.dir.split("\\")[:-1])
        else:
            ctx.dir = path
        return 0
    
commands: list[cmdlib.Command] = [
    ChangeDirectory(),
    DirList(),
    Exit()
]