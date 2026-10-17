"""An example program for the GTK3Menu widget.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3 import (  # pylint: disable=import-error
    GTK3Menu,
    GTK3MenuButton,
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


def do_show_menu_example() -> None:
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

    # Build a native GTK menu and display it from a menu button.
    menu = GTK3Menu()
    menu.do_build_menu(MENU_UI, method="gtk")

    # Create a GTK3MenuButton and set its properties using the pytkwrap convenience
    # method.
    menu_button = GTK3MenuButton()
    menu_button.do_set_properties(GTK3WidgetProperties(label="Menu", popup=menu))

    win.add(menu_button)

    # Show the GTK3Window and enter the main Gtk loop.
    win.show_all()
    Gtk.main()


if __name__ == "__main__":
    do_show_menu_example()
