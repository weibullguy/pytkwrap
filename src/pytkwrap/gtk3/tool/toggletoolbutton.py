"""The pytkwrap GTK3ToggleToolButton module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.tool.toolbutton import GTK3ToolButtonMixin


class GTK3ToggleToolButtonMixin(GTK3ToolButtonMixin):
    """Mixin class for GTK3ToggleToolButton."""

    _GTK3_TOGGLETOOLBUTTON_PROPERTIES = GTK3WidgetProperties(
        active=False,
    )
    _GTK3_TOGGLETOOLBUTTON_SIGNALS = ["toggled"]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3ToggleToolButton mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_TOGGLETOOLBUTTON_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_TOGGLETOOLBUTTON_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3ToggleToolButton-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3ToggleToolButton.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_active(self.dic_properties["active"])


class GTK3ToggleToolButton(Gtk.ToggleToolButton, GTK3ToggleToolButtonMixin):
    """Wrapper for version 3.0 Gtk.ToggleToolButton."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ToggleToolButton."""
        Gtk.ToggleToolButton.__init__(self)
        GTK3ToggleToolButtonMixin.__init__(self)
