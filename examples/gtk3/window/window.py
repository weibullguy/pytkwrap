"""An example program for the GTK3Window widget.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
import argparse

# pytkwrap Package Imports
from pytkwrap.gtk3 import (  # pylint: disable=import-error
    GTK3WidgetProperties,
    GTK3Window,
)
from pytkwrap.gtk3._libs import Gtk  # pylint: disable=import-error # noqa: PLC2701


def example_callback(window: GTK3Window):
    """Print the property values when a GTK3Window is realized."""
    # Get the value of a GTK3Window property using the pytkwrap convenience method.
    print("List of all the GTK3Window properties:\n")
    for _property in window.dic_properties:
        print(f"{_property}: {window.do_get_property(_property)}")


def show_window_example(title: str):
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
    parser = argparse.ArgumentParser(
        description="An example program for the GTK3Window widget."
    )
    parser.add_argument(
        "--title",
        type=str,
        default="pytkwrap Test Window",
        help="Text to use as the window title.",
    )

    args = parser.parse_args()

    show_window_example(args.title)
