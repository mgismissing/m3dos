from input import autocomplete

class Command: pass

class Context:
    def __init__(self, startdir: str = "/", verbose: bool = False, commands: list[Command] = [], ac: dict[str, str] = {}):
        self.running = True
        self.verbose = verbose
        self.dir = startdir
        self.commands = commands
        self.returned = None
        self.app_found = False
        self.ac = ac

class Command:
    def __init__(self, name: str, aliases: list[str] = [], accolor: str = ""):
        self.name = name
        self.aliases = aliases
        self.accolor = accolor
    def iscommand(self, command: str) -> bool:
        return (command == self.name) or (command in self.aliases)
    def run(self, ctx: Context, args: list[str]) -> int:
        return 0
    
def register_cmd(ctx: Context, cmd: Command):
    ctx.commands.append(cmd)
    for alias in [cmd.name] + cmd.aliases:
        ctx.ac[alias] = cmd.accolor

def register_cmds(ctx: Context, cmds: list[Command]):
    for cmd in cmds:
        register_cmd(ctx, cmd)