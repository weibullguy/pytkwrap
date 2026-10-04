"""An example program for the GTK3Window widget.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
import sys

# pytkwrap Package Imports
from pytkwrap.gtk3 import (  # pylint: disable=import-error
    GTK3WidgetProperties,
    GTK3Window,
)
from pytkwrap.gtk3._libs import Gtk  # pylint: disable=import-error # noqa: PLC2701


def example_callback(window: GTK3Window):
    """Print some property values when a GTK3Window is realized."""
    # Get the value of a GTK3Window property using the pytkwrap convenience method.
    print(f"Property default_height: {window.do_get_property('default_height')}")
    print(f"Property title: {window.do_get_property('title')}")


def show_window_example(title: str = "pytkwrap Test Window"):
    """Show how to construct a GTK3Window."""
    # Create an instance of the GTK3Window.
    win = GTK3Window()

    # Set GTK3Window properties using the GTK3WidgetProperties TypedDict and the
    # pytkwrap property setting convenience method.
    win.do_set_properties(GTK3WidgetProperties(default_height=500, title=title))

    # Call a Gtk.Window method directly.
    win.maximize()

    # Set a callback function for a GTK3Window signal using the pytkwrap convenience
    # method.
    win.do_set_callbacks("destroy", Gtk.main_quit)
    win.do_set_callbacks("realize", example_callback, True)

    # Show the GTK3Window and enter the main Gtk loop.
    win.show()
    Gtk.main()


if __name__ == "__main__":
    args = sys.argv[1:]
    if args:
        show_window_example(args[0])
    else:
        show_window_example()
