"""The pytkwrap GTK3 menu management package.

NOTE: Sub-modules in this package must import siblings directly
(e.g. from pytkwrap.gtk3.io.combo import GTK3ComboBox)
and never through this __init__.py to avoid circular imports.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Local Imports
from .checkmenuitem import GTK3CheckMenuItem
from .menu import GTK3Menu
from .menubar import GTK3MenuBar
from .menubutton import GTK3MenuButton
from .menuitem import GTK3MenuItem
from .menushell import (
    GTK3MenuShell,
    GTK3MenuShellAttribute,
    GTK3MenuShellItem,
    GTK3MenuShellMenu,
    GTK3MenuShellSection,
    GTK3MenuShellSubmenu,
    get_gio_menu_model,
    get_gtk_menu_items,
)
from .popovermenu import GTK3PopoverMenu
from .radiomenuitem import GTK3RadioMenuItem
from .recentchoosermenu import GTK3RecentChooserMenu
from .separatormenuitem import GTK3SeparatorMenuItem

__all__ = [
    "GTK3CheckMenuItem",
    "GTK3Menu",
    "GTK3MenuBar",
    "GTK3MenuButton",
    "GTK3MenuItem",
    "GTK3MenuShell",
    "GTK3MenuShellAttribute",
    "GTK3MenuShellItem",
    "GTK3MenuShellMenu",
    "GTK3MenuShellSection",
    "GTK3MenuShellSubmenu",
    "get_gio_menu_model",
    "get_gtk_menu_items",
    "GTK3PopoverMenu",
    "GTK3RadioMenuItem",
    "GTK3RecentChooserMenu",
    "GTK3SeparatorMenuItem",
]
