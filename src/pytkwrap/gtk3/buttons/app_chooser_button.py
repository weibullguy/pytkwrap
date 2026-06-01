"""The pytkwrap GTK3 App Chooser Button module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.combobox import GTK3ComboBox
from pytkwrap.gtk3.widget import GTK3WidgetProperties


class GTK3AppChooserButton(Gtk.AppChooserButton, GTK3ComboBox):
    """The GTK3AppChooserButton class."""

    # Define private class attributes.
    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 200
    _GTK3_APP_CHOOSER_BUTTON_PROPERTIES = GTK3WidgetProperties(
        heading=None,
        show_default_item=False,
        show_dialog_item=False,
    )
    _GTK3_APP_CHOOSER_BUTTON_SIGNALS = [
        "custom-item-activated",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3AppChooserButton widget."""
        Gtk.AppChooserButton.__init__(self)
        GTK3ComboBox.__init__(self)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_APP_CHOOSER_BUTTON_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_APP_CHOOSER_BUTTON_SIGNALS}
        )

        self.show_all()

    def do_get_property(
        self, property_name: str
    ) -> bool | date | float | int | object | str | None:
        """Get the value of the requested property.

        Parameters
        ----------
        property_name : str
            The name of the property to retrieve.

        Returns
        -------
        bool | date | float | int | object | str | None
        """
        if property_name in self._GTK3_APP_CHOOSER_BUTTON_PROPERTIES:
            return self.dic_properties.get(property_name)
        return super().do_get_property(property_name)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the AppChooserButton.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
         the WidgetProperties dict with the property values to set for
            the AppChooserButton.
        """
        super().do_set_properties(properties)

        if self.dic_properties["heading"] is not None:
            self.set_heading(self.dic_properties["heading"])
        self.set_show_default_item(self.dic_properties["show_default_item"])
        self.set_show_dialog_item(self.dic_properties["show_dialog_item"])
