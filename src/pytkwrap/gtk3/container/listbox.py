"""The pytkwrap GTK3ListBox module.

Convenience wrapper for working with Gtk.ListBox.

.. moduleauthor:: Doyle "weibullguy" Rowland
"""

from __future__ import annotations

# Standard Library Imports
from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.adjustment import GTK3Adjustment
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties

if TYPE_CHECKING:
    # pytkwrap Local Imports
    from ._protocols import _ListBoxHost


class GTK3ListBoxMixin(GTK3ContainerMixin):
    """Mixin class for GTK3ListBox.

    Notes
    -----
    The following Gtk.Frame methods are not wrapped in a convenience layer, but may be
    called directly:

        * bind_model(model, widget_func, *user_data)
        * drag_highlight_row(row)
        * drag_unhighlight_row()
        * get_selected_row()
        * invalidate_filter()
        * invalidate_headers()
        * invalidate_sort()
        * selected_foreach(func, *data)
        * set_filter_func(filter_func, *user_data)
        * set_header_func(update_header, *user_data)
        * set_placeholder(placeholder)
        * set_sort_func(sort_func, *user_data)

    Refer to https://lazka.github.io/pgi-docs/#Gtk-3.0/classes/ListBox.html for details
    on these methods.
    """

    _GTK3_LISTBOX_PROPERTIES = GTK3WidgetProperties(
        activate_on_single_click=True,
        adjustment=GTK3Adjustment(),
        selection_mode=Gtk.SelectionMode.SINGLE,
    )
    _GTK3_LISTBOX_SIGNALS = [
        "activate-cursor-row",
        "move-cursor",
        "row-activated",
        "row-selected",
        "select-all",
        "selected-rows-changed",
        "toggle-cursor-row",
        "unselect-all",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3ListBox mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_LISTBOX_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_LISTBOX_PROPERTIES)

    def do_set_properties(
        self: _ListBoxHost,
        properties: (
            Mapping[str, object] | Sequence[list[str | object] | tuple[str, object]]
        ),
    ) -> None:
        """Set the values of the GTK3ListBox-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3ListBox.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)  # type: ignore[safe-super] # ty: ignore[invalid-super-argument] # pylint: disable=line-too-long

        self.set_activate_on_single_click(
            self.dic_properties["activate_on_single_click"]
        )
        self.set_adjustment(self.dic_properties["adjustment"])
        self.set_selection_mode(self.dic_properties["selection_mode"])

    def do_add_child(
        self: _ListBoxHost,
        child: Gtk.Widget,
        position: int | None = None,
    ) -> None:
        """Add a child widget to the GTK3ListBox.

        Parameters
        ----------
        child : Gtk.Widget
            The child widget to add to the GTK3ListBox.
        position : int | None, optional
            The position in the GTK3ListBox to add the child widget.  Pass None to
            add the child to the beginning of the GTK3ListBox.
        """
        if position is None:
            self.prepend(child)
        else:
            self.insert(child, position)

    def do_get_row(
        self: _ListBoxHost,
        index: int | None = None,
        y: int | None = None,
    ) -> Gtk.ListBoxRow | None:
        """Get the requested row from the GTK3ListBox.

        Parameters
        ----------
        index : int | None
            The index of the row in the GTK3ListBox to return.
        y : int | None
            The position of the row in the GTK3ListBox to return.

        Returns
        -------
        Gtk.ListBoxRow | None
            The row requested or None.
        """
        if index is not None:
            return self.get_row_at_index(index)

        if y is not None:
            return self.get_row_at_y(y)

        return None

    def do_get_selected(self: _ListBoxHost) -> list[Gtk.ListBoxRow]:
        """Get the currently selected row or group of rows.

        Returns
        -------
        list[Gtk.ListBoxRow]
            The row or group of rows in the GTK3ListBox that are currently selected.
        """
        return self.get_selected_rows()

    def do_select_row(self: _ListBoxHost, row: Gtk.ListBoxRow | None) -> None:
        """Select one or more rows in the GTK3ListBox.

        Parameters
        ----------
        row : Gtk.ListBoxRow | None
            The row to select.  Pass None to select all rows.
        """
        if row is None:
            self.select_all()
        else:
            self.select_row(row)

    def do_unselect_row(self: _ListBoxHost, row: Gtk.ListBoxRow | None) -> None:
        """Unselect one or more rows in the GTK3ListBox.

        Parameters
        ----------
        row : Gtk.ListBoxRow | None
            The row in the GTK3ListBox to unselect.  Pass None to unselect all rows.
        """
        if row is None:
            self.unselect_all()
        else:
            self.unselect_row(row)


class GTK3ListBox(Gtk.ListBox, GTK3ListBoxMixin):
    """Wrapper for version 3.0 Gtk.ListBox."""

    def __init__(self, adjustment: GTK3Adjustment | None = None) -> None:
        """Initialize an instance of the GTK3ListBox."""
        Gtk.ListBox.__init__(self)
        GTK3ListBoxMixin.__init__(self)

        if adjustment is not None:
            self.dic_properties["adjustment"] = adjustment
            self.do_set_properties(  # ty: ignore[invalid-argument-type]
                self.dic_properties
            )
        else:
            self.dic_properties["adjustment"] = self.get_adjustment()
