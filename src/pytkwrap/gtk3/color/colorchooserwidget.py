"""The pytkwrap GTK3ColorChooserWidget module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.box import GTK3Box
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3ColorChooserWidget(Gtk.ColorChooserWidget, GTK3Box):
    """Wrapper for version 3.0 Gtk.ColorChooserWidget."""

    _GTK3_COLORCHOOSERWIDGET_PROPERTIES = GTK3WidgetProperties(
        show_editor=False,
    )

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ColorChooserWidget."""
        Gtk.ColorChooserWidget.__init__(self)
        GTK3Box.__init__(self)

        self.dic_properties.update(self._GTK3_COLORCHOOSERWIDGET_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3ColorChooserWidget-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3ColorChooserWidget.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        for _property in ["show_editor"]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )
