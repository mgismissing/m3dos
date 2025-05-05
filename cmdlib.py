class Command: pass

class Context:
    def __init__(self, startdir: str = "/", verbose: bool = False, commands: list[Command] = []):
        self.running = True
        self.verbose = verbose
        self.dir = startdir
        self.commands = commands
        self.returned = None
        self.app_found = False

class Command:
    def __init__(self, name: str):
        self.name = name
    def run(self, ctx: Context, args: list[str]) -> int:
        return 0

def register(cmds: list[Command], cmd: Command):
    cmds.append(cmd)