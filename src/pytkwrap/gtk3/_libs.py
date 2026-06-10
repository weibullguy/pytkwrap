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
except ImportError:
    print("Failed to import package gi; exiting.")
    sys.exit(1)
# Third Party Imports
import cairo  # noqa
from gi.repository import Gdk  # noqa
from gi.repository import GdkPixbuf  # noqa
from gi.repository import Gio  # noqa
from gi.repository import GLib  # noqa
from gi.repository import GObject  # noqa
from gi.repository import Gtk  # noqa
from gi.repository import Pango  # noqa

_ = gettext.gettext
