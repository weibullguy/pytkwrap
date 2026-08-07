"""The pytkwrap GTK3 Menu Button module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.button.togglebutton import GTK3ToggleButtonMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3MenuButtonMixin(GTK3ToggleButtonMixin):
    """Mixin for GTK3MenuButton."""

    # Define private class attributes.
    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 200
    _GTK3_MENU_BUTTON_PROPERTIES = GTK3WidgetProperties(
        align_widget=None,
        direction=Gtk.ArrowType.DOWN,
        menu_model=None,
        popover=None,
        popup=None,
        use_popover=True,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3MenuButton mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_MENU_BUTTON_PROPERTIES)

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
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_align_widget(self.dic_properties["align_widget"])
        self.set_direction(self.dic_properties["direction"])
        self.set_menu_model(self.dic_properties["menu_model"])
        self.set_popover(self.dic_properties["popover"])
        self.set_popup(self.dic_properties["popup"])
        self.set_use_popover(self.dic_properties["use_popover"])


class GTK3MenuButton(Gtk.MenuButton, GTK3MenuButtonMixin):
    """The GTK3MenuButton class."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3MenuButton widget."""
        Gtk.MenuButton.__init__(self)
        GTK3MenuButtonMixin.__init__(self)
