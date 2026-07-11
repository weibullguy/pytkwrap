"""The pytkwrap GTK3GLArea module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3Widget


class GTK3GLArea(Gtk.GLArea, GTK3Widget):
    """Wrapper for version 3.0 Gtk.GLArea."""

    _GTK3_GLAREA_PROPERTIES = GTK3WidgetProperties(
        auto_render=True,
        has_alpha=False,
        has_depth_buffer=False,
        has_stencil_buffer=False,
        use_es=False,
    )
    _GTK3_GLAREA_SIGNALS = [
        "create-context",
        "render",
        "resize",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3GLArea."""
        Gtk.GLArea.__init__(self)
        GTK3Widget.__init__(self)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_GLAREA_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_GLAREA_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3GLArea-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3GLArea.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        # Set the value of each of the mixin properties.
        self.set_auto_render(self.dic_properties["auto_render"])
        self.set_has_alpha(self.dic_properties["has_alpha"])
        self.set_has_depth_buffer(self.dic_properties["has_depth_buffer"])
        self.set_has_stencil_buffer(self.dic_properties["has_stencil_buffer"])
        self.set_use_es(self.dic_properties["use_es"])
