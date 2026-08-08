"""The pytkwrap GTK3ToolItemGroup module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk, Pango
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3ToolItemGroupMixin(GTK3ContainerMixin):
    """Mixin class for GTK3ToolItemGroup."""

    _GTK3_TOOLITEMGROUP_PROPERTIES = GTK3WidgetProperties(
        collapsed=False,
        ellipsize=Pango.EllipsizeMode.NONE,
        header_relief=Gtk.ReliefStyle.NORMAL,
        label="",
        label_widget=None,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3ToolItemGroup mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_TOOLITEMGROUP_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3ToolItemGroup-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3ToolItemGroup.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_collapsed(self.dic_properties["collapsed"])
        self.set_ellipsize(self.dic_properties["ellipsize"])
        self.set_header_relief(self.dic_properties["header_relief"])
        self.set_label(self.dic_properties["label"])

        if self.dic_properties["label_widget"] is not None:
            self.set_label_widget(self.dic_properties["label_widget"])


class GTK3ToolItemGroup(Gtk.ToolItemGroup, GTK3ToolItemGroupMixin):
    """Wrapper for version 3.0 Gtk.ToolItemGroup."""

    def __init__(self, label: str = "") -> None:
        """Initialize an instance of the GTK3ToolItemGroup."""
        Gtk.ToolItemGroup.__init__(self, label=label)
        GTK3ToolItemGroupMixin.__init__(self)

        self.dic_properties["label"] = label
