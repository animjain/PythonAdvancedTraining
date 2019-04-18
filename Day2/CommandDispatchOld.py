def list_dir():
    import os
    print(os.listdir("."))


def show_dir():
    import os
    print(os.getcwd())


def hostname():
    import os
    print(os.uname().nodename)


def invalid_command():
    print("invalid command...")


def exit_shell():
    exit(0)


commands = {
    "list": list_dir,
    "pwd": show_dir,
    "hostname": hostname,
    "exit": exit_shell
}
while True:
    c = input("Shell> ")
    commands.get(c, invalid_command)()
