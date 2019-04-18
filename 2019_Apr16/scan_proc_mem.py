#!/usr/bin/env python
from subprocess import Popen, PIPE
from collections import namedtuple
import sys
from time import sleep

if len(sys.argv) < 2:
    print(f"usage: {sys.argv[0]} memory_threshold")
    exit(1)

COMMAND = "ps -aeo rss,pid,args".split()
MEM_THRESHOLD = int(sys.argv[1])

def run_ps_command():
    with Popen(COMMAND, stdout=PIPE, encoding="utf8") as process_status:

        # capture headers
        headers = process_status.stdout.readline().lower().split()
        Record = namedtuple("ProcessInfo", headers)

        for line in process_status.stdout:
            rss, pid, args = line.split(maxsplit=2)
            rec = Record(int(rss), int(pid), args)
            if rec.rss > MEM_THRESHOLD:
                print(f"{rec.pid} is using {rec.rss} bytes")

try:
    while True:
        run_ps_command()
        sleep(5)
except KeyboardInterrupt:
        pass

