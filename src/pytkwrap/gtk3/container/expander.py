"""The pytkwrap GTK3Expander module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3ExpanderMixin(GTK3ContainerMixin):
    """Mixin class for GTK3Expander."""

    _GTK_EXPANDER_PROPERTIES = GTK3WidgetProperties(
        expanded=False,
        label=None,
        label_fill=False,
        label_widget=None,
        resize_toplevel=False,
        use_markup=False,
        use_underline=False,
    )
    _GTK3_EXPANDER_SIGNALS = ["activate"]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3Expander mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_EXPANDER_SIGNALS}
        )
        self.dic_properties.update(self._GTK_EXPANDER_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Expander-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Expander.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_expanded(self.dic_properties["expanded"])
        self.set_label(self.dic_properties["label"])
        self.set_label_fill(self.dic_properties["label_fill"])
        self.set_label_widget(self.dic_properties["label_widget"])
        self.set_resize_toplevel(self.dic_properties["resize_toplevel"])
        self.set_use_markup(self.dic_properties["use_markup"])
        self.set_use_underline(self.dic_properties["use_underline"])


class GTK3Expander(Gtk.Expander, GTK3ExpanderMixin):
    """Wrapper for version 3.0 Gtk.Expander."""

    def __init__(self, label: str | None = None) -> None:
        """Initialize an instance of the GTK3Expander.

        Parameters
        ----------
        label : str, optional
            The text to display in the GTK3Expander label.  The default is None.
        """
        Gtk.Expander.__init__(self, label=label)
        GTK3ExpanderMixin.__init__(self)

        self.dic_properties["label"] = label
