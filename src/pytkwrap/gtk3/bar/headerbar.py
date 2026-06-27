"""The pytkwrap GTK3HeaderBar module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container import GTK3Container
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3HeaderBar(Gtk.HeaderBar, GTK3Container):
    """Wrapper for version 3.0 Gtk.HeaderBar."""

    _GTK3_HEADERBAR_PROPERTIES = GTK3WidgetProperties(
        custom_title=None,
        decoration_layout=None,
        decoration_layout_set=False,
        has_subtitle=True,
        show_close_button=False,
        spacing=6,
        subtitle=None,
        title=None,
    )

    def __init__(self) -> None:
        """Initialize an instance of the GTK3HeaderBar."""
        Gtk.HeaderBar.__init__(self)
        GTK3Container.__init__(self)

        self.dic_properties.update(self._GTK3_HEADERBAR_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3HeaderBar-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3HeaderBar.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_custom_title(self.dic_properties["custom_title"])
        self.set_decoration_layout(self.dic_properties["decoration_layout"])
        self.set_has_subtitle(self.dic_properties["has_subtitle"])
        self.set_show_close_button(self.dic_properties["show_close_button"])
        self.set_subtitle(self.dic_properties["subtitle"])
        self.set_title(self.dic_properties["title"])

        for _property in ["decoration_layout_set", "spacing"]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )
