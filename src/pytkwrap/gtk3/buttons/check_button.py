"""The pytkwrap GTK3 Check Button module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.buttons.toggle_button import GTK3ToggleButton


class GTK3CheckButton(Gtk.CheckButton, GTK3ToggleButton):
    """The GTK3CheckButton class."""

    # Define private class attributes.
    _DEFAULT_EDIT_SIGNAL = "toggled"
    _DEFAULT_HEIGHT = 40
    _DEFAULT_WIDTH = 200

    def __init__(self, label="...") -> None:
        """Initialize an instance of the GTK3CheckButton widget.

        Parameters
        ----------
        label : str
            The text to display in the GTK3CheckButton label.  The default value is
            an ellipsis (...).
        """
        Gtk.CheckButton.__init__(self, label=label)
        GTK3ToggleButton.__init__(self)
