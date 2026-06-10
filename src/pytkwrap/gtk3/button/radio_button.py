"""The pytkwrap GTK3RadioButton module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.button.check_button import GTK3CheckButton
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3RadioButton(Gtk.RadioButton, GTK3CheckButton):
    """Wrapper for version 3.0 Gtk.RadioButton."""

    # Define private class attributes.
    _DEFAULT_HEIGHT = 40
    _DEFAULT_WIDTH = 200
    _GTK3_RADIO_BUTTON_PROPERTIES = GTK3WidgetProperties(
        group=None,
    )
    _GTK3_RADIO_BUTTON_SIGNALS = [
        "group-changed",
    ]

    def __init__(self, label="...", group=None) -> None:
        """Initialize an instance of the GTK3RadioButton widget.

        Parameters
        ----------
        label : str
            The text to display in the GTK3RadioButton label.  The default value is
            an ellipsis (...).
        group : Gtk.RadioButton | None
            The group to which the GTK3RadioButton belongs.
        """
        Gtk.RadioButton.__init__(self, label=label)
        GTK3CheckButton.__init__(self, label=label)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_RADIO_BUTTON_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_RADIO_BUTTON_SIGNALS}
        )

        self.join_group(group)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the GTK3RadioButton.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3RadioButton.
        """
        super().do_set_properties(properties)

        self.join_group(self.dic_properties["group"])
