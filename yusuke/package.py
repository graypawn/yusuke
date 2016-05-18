#!/usr/bin/env python
# Copyright (C) 2016  graypawn <choi.pawn @gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
import os
import subprocess

cache_dir = os.path.expanduser('~')+'/.cache/yusuke'

class CachePermissionException(Exception):
    """
    """


class UpdatePackages:
    """
    A class for pacman update packages
    """
    def __init__(self):
        try:
            self.binary = subprocess.check_output(['pacman', '-Qu'])
            self.items = self.binary.decode("utf-8")
            self.count = self.items.count('\n') - self.items.count('[ignored]')
        except subprocess.CalledProcessError:
            self.binary = 0
            self.items = ""
            self.count = 0

    def isChecked(self):
        """
        Return true if pacman output equal cache.
        """
        try:
            cache = open(cache_dir + '/cache', 'rb')
            if cache.read() == self.binary:
                return True
            else:
                return False
        except (FileNotFoundError, PermissionError):
            return False

    def writeCache(self):
        """
        Write pacman output to a cache file.

        Raise:
        - CachePermissionException
          When trying to run an operation without the adequate access rights.
        """
        try:
            os.makedirs(cache_dir, exist_ok=True)
            with open(cache_dir + '/cache', 'wb') as cache:
                cache.write(self.binary)
        except OSError as e:
            raise CachePermissionException("Permission denied")

    def take(self, n):
        """
        Return a list of the first n items, or all items if there are
        fewer than n.
        """
        if self.count <= n:
            return self.items
        else:
            return "\n".join(self.items.split('\n')[0:n])
