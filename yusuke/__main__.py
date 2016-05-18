#!/usr/bin/env python
# Copyright (C) 2016  graypawn <choi.pawn @gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
import sys
from yusuke.notify import notify
from yusuke import __version__


def versionInfo():
    print("Yusuke", __version__)
    print("Copyrig ht (C) 2016 graypawn <choi.pawn @gmail.com>")
    print("GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.")
    print("This is free software: you are free to change and redistribute it.")
    print("There is NO WARRANTY, to the extent permitted by law.")


def helpInfo(name):
    print("Usage: {} [OPTION]".format(name))
    print("pacman update notifier")
    print()
    print("    --help      display this help and exit")
    print("    --version   output version information and exit")
    print()
    print("yusuke@.timer checks periodically for updates.")
    print("    systemctl enable yusuke@{USER}.timer")


def main():
    if len(sys.argv) == 1:
        notify()
    elif sys.argv[1] == '--help':
        helpInfo(sys.argv[0])
        exit(0)
    elif sys.argv[1] == '--version':
        versionInfo()
        exit(0)
    else:
        print("Try '{} --help' for more information.".format(sys.argv[0]),
              file=sys.stderr)
        exit(1)
