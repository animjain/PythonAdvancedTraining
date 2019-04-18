from subprocess import Popen, PIPE
import sys
from time import sleep

COMMAND = "ps -aeo pid,rss,args".split()

MEM_THRESHOLD = int(sys.argv[1])


def ps_command():
    with Popen(COMMAND, stdout=PIPE, encoding="utf8") as process_status:

        headers = process_status.stdout.readline().lower().split()

        for line in process_status.stdout:
            pid, rss, args = line.split(maxsplit=2)
            if int(rss) >= MEM_THRESHOLD:
                print(f"{pid} is using {rss} bytes")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} memory_threshold")
        exit(1)

    try:
        while True:
            ps_command()
            sleep(5)
    except KeyboardInterrupt:
        pass

