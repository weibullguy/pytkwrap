"""The pytkwrap GTK3 Menu Button module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.buttons.toggle_button import GTK3ToggleButton
from pytkwrap.gtk3.widget import GTK3WidgetProperties


class GTK3MenuButton(Gtk.MenuButton, GTK3ToggleButton):
    """The GTK3MenuButton class."""

    # Define private class attributes.
    _GTK3_MENU_BUTTON_PROPERTIES = GTK3WidgetProperties(
        align_widget=None,
        direction=Gtk.ArrowType.DOWN,
        menu_model=None,
        popover=None,
        popup=None,
        use_popover=True,
    )
    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 200

    def __init__(self) -> None:
        """Initialize an instance of the GTK3MenuButton widget."""
        Gtk.MenuButton.__init__(self)
        GTK3ToggleButton.__init__(self)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_MENU_BUTTON_PROPERTIES)

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
        if property_name in self._GTK3_MENU_BUTTON_PROPERTIES:
            return self.dic_properties.get(property_name)
        return super().do_get_property(property_name)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the GTK3MenuButton.

        Parameters
        ----------
        properties : GTK3WidgetProperties
            The typed dict with the property values to set for the GTK3MenuButton.
        """
        super().do_set_properties(properties)

        self.set_align_widget(self.dic_properties["align_widget"])
        self.set_direction(self.dic_properties["direction"])
        self.set_menu_model(self.dic_properties["menu_model"])
        self.set_popover(self.dic_properties["popover"])
        self.set_popup(self.dic_properties["popup"])
        self.set_use_popover(self.dic_properties["use_popover"])
