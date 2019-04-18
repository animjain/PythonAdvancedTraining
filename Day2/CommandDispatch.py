class CommandDispatch:

    def __init__(self):
        self.commands = {}
        pass

    def for_command(self, name):
        def wrap_command(fn):
            self.commands[name] = fn
            return fn
        return wrap_command

    def invalid(self, fn):
        self.__invalid = fn
        return fn

    def input(self, fn):
        self.__input = fn
        return fn

    def run(self):
        while True:
            c = self.__input()
            self.commands.get(c, self.__invalid)()


shell = CommandDispatch()

@shell.for_command("list")
def list_dir():
    import os
    print(os.listdir("."))

@shell.for_command("pwd")
def show_dir():
    import os
    print(os.getcwd())

@shell.for_command("hostname")
def hostname():
    import os
    print(os.uname().nodename)

@shell.invalid
def invalid_command():
    print("invalid command...")

@shell.input
def getinput():
    return input("Shell> ")

@shell.for_command("exit")
def exit_shell():
    exit(0)

if __name__ == '__main__':
    shell.run()