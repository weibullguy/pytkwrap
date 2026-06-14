"""The pytkwrap GTK3ToolButton module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.tool.toolitem import GTK3ToolItem


class GTK3ToolButton(Gtk.ToolButton, GTK3ToolItem):
    """Wrapper for version 3.0 Gtk.ToolButton."""

    _GTK3_TOOLBUTTON_PROPERTIES = GTK3WidgetProperties(
        icon_name=None,
        icon_widget=None,
        label=None,
        label_widget=None,
        use_underline=False,
    )
    _GTK3_TOOLBUTTON_SIGNALS = ["clicked"]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ToolButton."""
        Gtk.ToolButton.__init__(self)
        GTK3ToolItem.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_TOOLBUTTON_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_TOOLBUTTON_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3ToolButton-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3ToolButton.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        # Set the value of each of the mixin properties.
        self.set_icon_name(self.dic_properties["icon_name"])
        self.set_icon_widget(self.dic_properties["icon_widget"])
        self.set_label(self.dic_properties["label"])
        self.set_label_widget(self.dic_properties["label_widget"])
        self.set_use_underline(self.dic_properties["use_underline"])
