"""The pytkwrap GTK3CellView module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3WidgetMixin


class GTK3CellViewMixin(GTK3WidgetMixin):
    """Mixin class for GTK3CellView.

    Attributes
    ----------
    _GTK3_CELLVIEW_PROPERTIES : GTK3WidgetProperties
        Properties unique to GTK3CellView.
    """

    _GTK3_CELLVIEW_PROPERTIES = GTK3WidgetProperties(
        background=None,
        background_rgba=None,
        background_set=False,
        cell_area=None,
        cell_area_context=None,
        draw_sensitive=False,
        fit_model=False,
        model=None,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3CellView mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_CELLVIEW_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3CellView-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3CellView.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        if self.dic_properties["background_rgba"] is not None:
            self.set_background_rgba(self.dic_properties["background_rgba"])

        self.set_draw_sensitive(self.dic_properties["draw_sensitive"])
        self.set_fit_model(self.dic_properties["fit_model"])
        self.set_model(self.dic_properties["model"])

        for _property in ["background"]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )

    @property
    def displayed_row(self) -> Gtk.TreePath | None:
        """Return the displayed row of the cell view."""
        return self.get_displayed_row()


class GTK3CellView(Gtk.CellView, GTK3CellViewMixin):
    """Wrapper for version 3.0 Gtk.CellView."""

    def __init__(
        self,
        cell_area_context: Gtk.CellAreaContext | None = None,
    ) -> None:
        """Initialize an instance of the GTK3CellView.

        Parameters
        ----------
        cell_area_context : Gtk.CellAreaContext | None, optional
            The cell area context to use for the cell view, by default None.
        """
        Gtk.CellView.__init__(
            self,
            cell_area_context=cell_area_context,
        )
        GTK3CellViewMixin.__init__(self)
