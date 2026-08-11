"""The pytkwrap GTK3AppChooserButton module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.io.combobox import GTK3ComboBoxMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3AppChooserButtonMixin(GTK3ComboBoxMixin):
    """Mixin for GTK3AppChooserButton."""

    # Define private class attributes.
    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 200
    _GTK3_APPCHOOSERBUTTON_PROPERTIES = GTK3WidgetProperties(
        heading=None,
        show_default_item=False,
        show_dialog_item=False,
    )
    _GTK3_APPCHOOSERBUTTON_SIGNALS = [
        "custom-item-activated",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3AppChooserButton mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_APPCHOOSERBUTTON_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_APPCHOOSERBUTTON_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the GTK3AppChooserButton.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3AppChooserButton.
        """
        super().do_set_properties(properties)

        if self.dic_properties["heading"] is not None:
            self.set_heading(self.dic_properties["heading"])
        self.set_show_default_item(self.dic_properties["show_default_item"])
        self.set_show_dialog_item(self.dic_properties["show_dialog_item"])


class GTK3AppChooserButton(Gtk.AppChooserButton, GTK3AppChooserButtonMixin):
    """Wrapper for version 3.0 Gtk.AppChooserButton."""

    def __init__(self, heading="Choose an application") -> None:
        """Initialize an instance of the GTK3AppChooserButton widget.

        Parameters
        ----------
        heading : str
            The text to show at the top of the dialog.
        """
        Gtk.AppChooserButton.__init__(self, heading=heading)
        GTK3AppChooserButtonMixin.__init__(self)

        self.dic_properties["heading"] = heading
