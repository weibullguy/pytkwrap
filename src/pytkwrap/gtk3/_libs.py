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
from gi.repository import Gdk, GdkPixbuf, Gio, GLib, GObject, Gtk, Pango

_ = gettext.gettext
