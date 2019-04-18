#!/usr/bin/env python
from sys import argv
from subprocess import Popen

command = argv.pop(0)

print("Running {} command...".format(command))
cmd = "/bin/" + command
argv.insert(0, cmd)
p = Popen(argv)
ret = p.wait()
print("Command completed with ret = {}".format(ret))


