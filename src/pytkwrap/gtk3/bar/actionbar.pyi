# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.widget import GTK3WidgetMixin as GTK3WidgetMixin

class GTK3ActionBar(Gtk.ActionBar, GTK3WidgetMixin):
    def __init__(self) -> None: ...
