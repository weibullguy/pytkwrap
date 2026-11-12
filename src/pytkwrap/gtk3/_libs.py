# pylint: disable=unused-import
"""The pytkwrap GTK3 GObject library module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
import gettext
import sys

try:
    # Third Party Imports
    import gi

    gi.require_version("Gdk", "3.0")
    gi.require_version("GLib", "2.0")
    gi.require_version("Gtk", "3.0")

    # Third Party Imports
    from gi.repository import Gdk  # noqa
    from gi.repository import GdkPixbuf  # noqa
    from gi.repository import Gio  # noqa
    from gi.repository import GLib  # noqa
    from gi.repository import GObject  # noqa
    from gi.repository import Gtk  # noqa
    from gi.repository import Pango  # noqa

except (ImportError, ValueError):
    print("Failed to import package gi; exiting.")
    sys.exit(1)

# Third Party Imports
import cairo as cairo  # noqa: F401 # pylint: disable=useless-import-alias, line-too-long # ruff: ignore[PLC0414]

_ = gettext.gettext
