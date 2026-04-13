# -*- coding: utf-8 -*-
#
#       wrap.examples.matrixview.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2026 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""An example program using the MatrixView."""

# pytkwrap Package Imports
from pytkwrap.gtk3 import ComboBox, Entry, Frame, Label, MatrixView, TextView
from pytkwrap.gtk3._libs import Gtk


class MatrixViewExample(Gtk.Window):
    """An example program using the MatrixView."""

    def __init__(self):
        super().__init__(title="wrap MatrixView Example")

        _frame = Frame()
        _vbox = Gtk.VBox()
        self.matrix = MatrixView()

        self.matrix.do_build_matrix(
            [
                ("Column 1", "Tooltip for column 1"),
                ("Column 2", "Tooltip for column 2"),
            ],
            [
                ("Row 1", "Tooltip for row 1"),
                ("Row 2", "Tooltip for row 2"),
            ],
        )
        self.add_combo_widget()
        self.add_entry_widget()
        self.add_label_widget()
        self.add_textview_widget()

        _frame.add(self.matrix)
        _vbox.pack_start(_frame, True, True, 0)
        self.add(_vbox)

        self.show_all()

    def add_combo_widget(self):
        """Example of how to add a ComboBox widget to the MatrixView.

        This will add a ComboBox widget to the upper left corner of the MatrixView.  It
        attaches on the left at column 1 and to the top at row 1.  It spans 1 row and 1
        column.
        """
        _combobox = ComboBox()
        _combobox.do_set_callbacks("changed", _combobox.on_changed)
        _combobox.do_load_combo(["Example Combo Entry 1", "Example Combo Entry 2"])

        self.matrix.do_add_widget(
            _combobox,
            1,
            1,
            1,
            1,
        )

    def add_entry_widget(self):
        """Example of how to add a Entry widget to the MatrixView.

        This will add a Entry widget to the upper right corner of the MatrixView.  It
        attaches on the left at column 2 and to the top at row 1.  It spans 1 row and 1
        column.
        """
        _entry = Entry()
        _entry.set_text("Example Entry")

        self.matrix.do_add_widget(
            _entry,
            2,
            1,
            1,
            1,
        )

    def add_label_widget(self):
        """Example of how to add a Label widget to the MatrixView.

        This will add a Label widget to the lower left corner of the MatrixView.  It
        attaches on the left at column 1 and to the top at row 2.  It spans 1 row and 1
        column.
        """
        _label = Label("Example Label")

        self.matrix.do_add_widget(
            _label,
            1,
            2,
            1,
            1,
        )

    def add_textview_widget(self):
        """Example of how to add a TextView widget to the MatrixView.

        This will add a TextView widget to the lower right corner of the MatrixView.  It
        attaches on the left at column 2 and to the top at row 2.  It spans 1 row and 1
        column.
        """
        _textview = TextView(Gtk.TextBuffer())
        _textview.field = "example"
        _textview.do_set_callbacks("changed", _textview.do_update)
        _textview.do_update(
            {
                "example": "Example TextView:  You can add alot of text in a "
                "\nTextView widget.  It will wrap and if it gets really long, "
                "\nscrollbars will magically appear.\n\n\n\n\n\n\tPretty cool, huh?\n"
            }
        )

        self.matrix.do_add_widget(
            _textview.scrollwindow,
            2,
            2,
            1,
            1,
        )


win = MatrixViewExample()
win.connect("destroy", Gtk.main_quit)
Gtk.main()
