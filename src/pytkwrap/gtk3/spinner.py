"""The pytkwrap GTK3Spinner module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3WidgetMixin


class GTK3SpinnerMixin(GTK3WidgetMixin):
    """Mixin class for GTK3Spinner."""

    _GTK3_SPINNER_PROPERTIES = GTK3WidgetProperties(
        active=False,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3Spinner mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_SPINNER_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Spinner-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Spinner.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        for _property in ["active"]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )


class GTK3Spinner(Gtk.Spinner, GTK3SpinnerMixin):
    """Wrapper for version 3.0 Gtk.Spinner."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Spinner."""
        Gtk.Spinner.__init__(self)
        GTK3SpinnerMixin.__init__(self)
