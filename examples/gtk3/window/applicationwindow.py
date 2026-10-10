"""An example program for the GTK3ApplicationWindow widget.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
import argparse

# pytkwrap Package Imports
from pytkwrap.gtk3 import (  # pylint: disable=import-error
    GTK3ApplicationWindow,
    GTK3WidgetProperties,
)
from pytkwrap.gtk3._libs import Gtk  # pylint: disable=import-error # noqa: PLC2701


def example_callback(window: GTK3ApplicationWindow):
    """Print some property values when a GTK3ApplicationWindow is realized."""
    # Get the value of a GTK3ApplicationWindow property using the pytkwrap convenience
    # method.
    print("List of all the GTK3ApplicationWindow properties:\n")
    for _property in window.dic_properties:
        print(f"{_property}: {window.do_get_property(_property)}")


def show_application_window_example(
    application: Gtk.Application | None = None,
    title: str = "pytkwrap Test Application Window",
):
    """Show how to construct a GTK3ApplicationWindow."""
    # Create an instance of the GTK3ApplicationWindow.
    win = GTK3ApplicationWindow(application=application)

    # Set GTK3Window properties using the GTK3WidgetProperties TypedDict and the
    # pytkwrap property setting convenience method.
    win.do_set_properties(
        GTK3WidgetProperties(default_height=500, show_menubar=True, title=title)
    )

    # Call a Gtk.Window method directly.
    win.maximize()

    # Set a callback function for a GTK3ApplicationWindow signal using the pytkwrap
    # convenience method.
    win.do_set_callbacks("destroy", Gtk.main_quit)
    win.do_set_callbacks("realize", example_callback, True)

    # Show the GTK3ApplicationWindow and enter the main Gtk loop.
    win.show()
    Gtk.main()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="An example program for the GTK3ApplicationWindow widget."
    )
    parser.add_argument(
        "--title",
        type=str,
        default="pytkwrap Test Application Window",
        help="Text to use as " "the window title.",
    )
    parser.add_argument(
        "--application",
        type=bool,
        default=False,
        help="Create the " "GTK3ApplicationWindow with a Gtk.Application object.",
    )

    args = parser.parse_args()

    if args.application:
        _application = Gtk.Application()
        _application.connect("activate", show_application_window_example, args.title)
        _application.run()
    else:
        show_application_window_example(title=args.title)
