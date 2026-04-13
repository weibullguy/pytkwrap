# -*- coding: utf-8 -*-
#
#       wrap.examples.file_chooser_button.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2026 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""An example program using the FileChooserButton."""

# pytkwrap Package Imports
from pytkwrap.gtk3 import FileChooserButton
from pytkwrap.gtk3._libs import Gtk

"""
Manual test for FileChooserButton.
Run with: python manual_tests/test_file_chooser_button.py
Requires a running display.
"""


def on_file_set(button):
    print(f"File selected: {button.get_filename()}")


win = Gtk.Window(title="FileChooserButton Test")
win.connect("destroy", Gtk.main_quit)

btn = FileChooserButton(label="Select a file...")
btn.connect("file-set", on_file_set)

win.add(btn)
win.show_all()
Gtk.main()
