"""The pytkwrap GTK3Scale module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk, Pango
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.range import GTK3RangeMixin


class GTK3ScaleMixin(GTK3RangeMixin):
    """Mixin class for GTK3Scale.

    Attributes
    ----------
    _GTK3_SCALE_PROPERTIES : GTK3WidgetProperties
        Properties unique to the GTK3Scale class.
    _GTK3_SCALE_SIGNALS : list[str]
        Signals unique to the GTK3Scale class.
    """

    _GTK3_SCALE_PROPERTIES = GTK3WidgetProperties(
        digits=1,
        draw_value=True,
        has_origin=True,
        value_pos=Gtk.PositionType.TOP,
    )
    _GTK3_SCALE_SIGNALS = [
        "format-value",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3Scale mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_SCALE_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_SCALE_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Scale-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Scale.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_digits(self.dic_properties["digits"])
        self.set_draw_value(self.dic_properties["draw_value"])
        self.set_has_origin(self.dic_properties["has_origin"])
        self.set_value_pos(self.dic_properties["value_pos"])

    @property
    def layout(self) -> Pango.Layout | None:
        """Get the layout of the scale.

        Returns
        -------
        Pango.Layout | None
            The layout of the scale.
        """
        return self.get_layout()

    @property
    def layout_offset(self) -> tuple[int, int] | None:
        """Get the coordinates where the scale will draw the text in the scale.

        Returns
        -------
        tuple[int, int] | None
            The layout offset of the scale.
        """
        return self.get_layout_offsets()


class GTK3Scale(Gtk.Scale, GTK3ScaleMixin):
    """Wrapper for version 3.0 Gtk.Scale."""

    def __init__(
        self,
        orientation: Gtk.Orientation = Gtk.Orientation.HORIZONTAL,
        adjustment: Gtk.Adjustment | None = None,
    ) -> None:
        """Initialize an instance of the GTK3Scale.

        Parameters
        ----------
        orientation : Gtk.Orientation
            The orientation of the scale.  The default is Gtk.Orientation.HORIZONTAL.
        adjustment : Gtk.Adjustment | None
            The adjustment to use for the scale.  The default is None.
        """
        Gtk.Scale.__init__(
            self,
            orientation=orientation,
            adjustment=adjustment,
        )
        GTK3ScaleMixin.__init__(self)
