import cmdlib

commands: list[cmdlib.Command] = []

class Exit(cmdlib.Command):
    def __init__(self):
        cmdlib.Command.__init__(self, name="exit")
    def run(self, ctx: cmdlib.Context, args: list[str]) -> int:
        ctx.running = False
        return 0
cmdlib.register(commands, Exit())