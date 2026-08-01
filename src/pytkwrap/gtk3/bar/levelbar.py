"""The pytkwrap GTK3LevelBar module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GObject, Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3WidgetMixin
from pytkwrap.utilities import clamp


class GTK3LevelBarMixin(GTK3WidgetMixin):
    """Mixin for GTK3LevelBar."""

    _GTK3_LEVELBAR_ATTRIBUTES = GTK3WidgetAttributes(
        default_value=0.0,
        edit_signal="changed",
    )
    _GTK3_LEVELBAR_PROPERTIES = GTK3WidgetProperties(
        inverted=False,
        max_value=1.0,
        min_value=0.0,
        mode=Gtk.LevelBarMode.CONTINUOUS,
        value=0.0,
    )
    _GTK3_LEVELBAR_SIGNALS = [
        "offset-changed",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3LevelBar mixin."""
        GTK3WidgetMixin.__init__(self)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_LEVELBAR_ATTRIBUTES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_LEVELBAR_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_LEVELBAR_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3LevelBar-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3LevelBar.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_inverted(self.dic_properties["inverted"])
        self.set_max_value(self.dic_properties["max_value"])
        self.set_min_value(self.dic_properties["min_value"])
        self.set_mode(self.dic_properties["mode"])
        self.set_value(self.dic_properties["value"])

    def do_get_value(self) -> float | int | str | None:
        """Retrieve the value of the GTK3LevelBar.

        Returns
        -------
        float
            The value displayed in the GTK3LevelBar.
        """
        return float(self.get_value())

    def do_set_value(
        self, value: bool | date | float | int | object | str | tuple | None
    ) -> None:
        """Set the GTK3LevelBar active value.

        Parameters
        ----------
        value : float | int | str
            The value to display in the GTK3LevelBar.
        """
        if not isinstance(value, (float, int, str)):
            super().do_set_value(value)

        # Clamp the value to the min and max values.
        value = clamp(
            float(value),  # type: ignore[arg-type] # ty: ignore[invalid-argument-type] # pylint: disable=line-too-long
            self.dic_properties["min_value"],
            self.dic_properties["max_value"],
        )

        self.set_value(float(value))  # type: ignore[arg-type]
        self.dic_properties["value"] = float(value)  # type: ignore[arg-type]
        self.emit("changed")


class GTK3LevelBar(Gtk.LevelBar, GTK3LevelBarMixin):
    """Wrapper for version 3.0 Gtk.LevelBar."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3LevelBar."""
        Gtk.LevelBar.__init__(self)
        GTK3LevelBarMixin.__init__(self)

    @GObject.Signal
    def changed(self):
        """Add the 'changed' signal."""
