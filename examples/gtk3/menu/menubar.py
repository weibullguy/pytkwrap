"""An example program for the GTK3Menu widget.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
import argparse

# pytkwrap Package Imports
from pytkwrap.gtk3 import (  # pylint: disable=import-error
    GTK3MenuBar,
    GTK3WidgetProperties,
    GTK3Window,
)
from pytkwrap.gtk3._libs import Gtk  # pylint: disable=import-error # noqa: PLC2701
from pytkwrap.gtk3.menu import (  # pylint: disable=import-error
    GTK3MenuItem,
    GTK3MenuShellAttribute,
    GTK3MenuShellItem,
    GTK3MenuShellMenu,
    GTK3MenuShellSection,
    GTK3MenuShellSubmenu,
)


def example_callback(menubar: GTK3MenuBar):
    """Print the property values when a GTK3MenuBar item is selected."""
    # Get the value of a GTK3MenuBar property using the pytkwrap convenience method.
    print("List of all the GTK3MenuBar properties:\n")
    for _property in menubar.dic_properties:
        print(f"{_property}: {menubar.do_get_property(_property)}")


def on_open(menu_item: GTK3MenuItem) -> None:
    """Set label to new value when the menu item is opened."""
    print(f"Open: {menu_item.set_label('New Label')}")


MENU_UI = GTK3MenuShellMenu(
    id="menubar",
    submenus=[
        GTK3MenuShellSubmenu(
            attributes=GTK3MenuShellAttribute(
                id="file",
                label="File",
            ),
            sections=[
                GTK3MenuShellSection(
                    children=[
                        GTK3MenuShellItem(
                            attributes=GTK3MenuShellAttribute(
                                action="app.new",
                                callback=on_open,
                                icon="new_icon",
                                label="New",
                                signal="activate",
                            )
                        ),
                        GTK3MenuShellItem(
                            attributes=GTK3MenuShellAttribute(
                                action="app.close",
                                label="Close",
                            )
                        ),
                        GTK3MenuShellSubmenu(
                            attributes=GTK3MenuShellAttribute(
                                id="open",
                                label="Open",
                            ),
                            sections=[
                                GTK3MenuShellSection(
                                    children=[
                                        GTK3MenuShellItem(
                                            attributes=GTK3MenuShellAttribute(
                                                action="app.openrecent",
                                                icon="recent_icon",
                                                label="Recent",
                                            )
                                        ),
                                        GTK3MenuShellItem(
                                            attributes=GTK3MenuShellAttribute(
                                                action="app.fromfile",
                                                icon="from_file_icon",
                                                label="From File",
                                            )
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
        GTK3MenuShellSubmenu(
            attributes=GTK3MenuShellAttribute(
                id="edit",
                label="Edit",
            ),
            sections=[
                GTK3MenuShellSection(
                    children=[
                        GTK3MenuShellItem(
                            attributes=GTK3MenuShellAttribute(
                                action="app.copy",
                                icon="copy_icon",
                                label="Copy",
                            )
                        ),
                        GTK3MenuShellItem(
                            attributes=GTK3MenuShellAttribute(
                                action="app.cut",
                                icon="cut_icon",
                                label="Cut",
                            )
                        ),
                        GTK3MenuShellItem(
                            attributes=GTK3MenuShellAttribute(
                                action="app.paste",
                                label="Paste",
                            )
                        ),
                    ]
                )
            ],
        ),
        GTK3MenuShellSubmenu(
            attributes=GTK3MenuShellAttribute(
                id="view",
                label="View",
            ),
            sections=[
                GTK3MenuShellSection(
                    children=[
                        GTK3MenuShellItem(
                            attributes=GTK3MenuShellAttribute(
                                action="app.zoomin",
                                icon="zoomin_icon",
                                label="Zoom In",
                            )
                        ),
                        GTK3MenuShellItem(
                            attributes=GTK3MenuShellAttribute(
                                action="app.zoomout",
                                icon="zoomout_icon",
                                label="Zoom Out",
                            )
                        ),
                    ]
                )
            ],
        ),
    ],
)


def show_menubar_example(method: str):
    """Show how to construct a GTK3Menu."""
    # Create an instance of the GTK3Window.
    win = GTK3Window()

    # Set GTK3Window properties using the GTK3WidgetProperties TypedDict and the
    # pytkwrap property setting convenience method.
    win.do_set_properties(GTK3WidgetProperties(title="pytkwrap GTK3Menu Example"))

    # Call a Gtk.Window method directly.
    win.maximize()

    # Set a callback function for a GTK3Window signal using the pytkwrap convenience
    # method.
    win.do_set_callbacks("destroy", Gtk.main_quit)

    # Create a new GTK3MenuBar.
    menubar = GTK3MenuBar()
    menubar.do_build_menu(MENU_UI, method=method)

    # Connect the menubar to a callback function.
    menubar.connect("selection-done", example_callback)

    # Add the menubar to the window.
    win.add(menubar)

    # Show the GTK3Window and enter the main Gtk loop.
    win.show_all()
    Gtk.main()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="An example program for the GTK3MenuBar widget."
    )
    parser.add_argument(
        "--method",
        type=str,
        default="gio",
        help="Which method to use to create the menubar.  Options are 'gio' and 'gtk'.",
    )

    args = parser.parse_args()

    show_menubar_example(args.method)
