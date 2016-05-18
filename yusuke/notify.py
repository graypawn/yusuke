#!/usr/bin/env python
# Copyright (C) 2016  graypawn <choi.pawn @gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
import sys
import gi
gi.require_version('Notify', '0.7')
gi.require_version('Gtk', '3.0')
from gi.repository import Notify
from gi.repository import Gtk
import yusuke.package as pkg

ICON = 'system-software-update'

def closedCallback(notify_object):
    Gtk.main_quit()


def moreMessageCallback(notify_object, action_name, user_data):
    notify_object.update(
        user_data['title'],
        user_data['items'],
        ICON
    )
    notify_object.show()


def checkCallback(notify_object, action_name, update_packages):
    try:
        update_packages.writeCache()
    except pkg.CachePermissionException:
        print("yusuke: {}: {}".format(cache_dir + '/cache', e.args[1]),
              file=sys.stderr)
        exit(1)
    notify_object.close()
    Gtk.main_quit()


def notify():
    packages = pkg.UpdatePackages()
    if packages.count is 0:
        print("Already up-to-date")
        return

    if packages.isChecked():
        print("These packages have been checked")
        return

    Notify.init('yusuke')
    title = "{} Update(s) Available".format(packages.count)
    message = packages.take(10)

    yusuke_notify = Notify.Notification.new(title, message, ICON)
    yusuke_notify.connect('closed', closedCallback)

    # Pressing the 'more' button to show full packages.
    yusuke_notify.add_action(
        'more_message',
        'more',
        moreMessageCallback,
        {'title': title, 'items': packages.items}
    )
    # If all packages are checked, then don't show this message again.
    yusuke_notify.add_action(
        'no_more',
        "Don't show this message again",
        checkCallback,
        packages
    )
    yusuke_notify.show()
    Gtk.main()
