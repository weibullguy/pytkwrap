"""The pytkwrap GTK3 ComboBox module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date
from types import EllipsisType
from typing import Any

# Third Party Imports
from gi.overrides.GdkPixbuf import Pixbuf  # type: ignore[import-untyped]

# pytkwrap Package Imports
from pytkwrap.common import PyTkWrapAttributes
from pytkwrap.gtk3._libs import GObject, Gtk
from pytkwrap.gtk3.container.bin import GTK3Bin
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties


class GTK3ComboBox(Gtk.ComboBox, GTK3Bin):
    """The GTK3ComboBox class."""

    # Define private class attributes.
    _DEFAULT_HEIGHT: int = 30
    _DEFAULT_WIDTH: int = 200
    _GTK3_COMBOBOX_ATTRIBUTES = GTK3WidgetAttributes(
        column_types=[GObject.TYPE_STRING],
        default_value=-1,
        edit_signal="changed",
    )
    _GTK3_COMBOBOX_PROPERTIES = GTK3WidgetProperties(
        active=-1,
        active_id=None,
        border_width=0,
        button_sensitivity=Gtk.SensitivityType.AUTO,
        cell_area=None,
        column_span_column=-1,
        editing_canceled=False,
        entry_text_column=-1,
        has_entry=False,
        has_frame=True,
        id_column=-1,
        model=None,
        popup_fixed_width=True,
        popup_shown=False,
        row_span_column=-1,
        wrap_width=0,
    )
    _GTK3_COMBOBOX_SIGNALS: list[str] = [
        "changed",
        "editing-done",
        "format-entry-text",
        "move-active",
        "popdown",
        "popup",
        "remove-widget",
    ]

    def __init__(
        self,
        display_index: int = 0,
        simple: bool = True,
        n_items: int = 1,
        column_types: list[EllipsisType] | list[GObject.GType] | None = None,
        has_entry: bool = False,
    ) -> None:
        """Initialize an instance of the GTK3ComboBox widget.

        Parameters
        ----------
        display_index : int
            The index in the GTK3ComboBox Gtk.ListView to display. Default is 0.
        simple : bool
            Indicates whether to make a simple (one item) or complex (n_item)
            GTK3ComboBox. Default is True.
        n_items : int
            The number of items (columns) to add.
        column_types : list
            The column types to add to the GTK3ComboBox model.
        has_entry : bool
            Indicates whether GTK3ComboBox will have an entry.
        """
        Gtk.ComboBox.__init__(self)
        GTK3Bin.__init__(self)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_COMBOBOX_ATTRIBUTES)
        self.dic_properties.update(self._GTK3_COMBOBOX_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_COMBOBOX_SIGNALS}
        )
        self.dic_attributes["column_types"] = column_types
        self.dic_properties["has_entry"] = has_entry

        self.display_index: int = display_index
        self.n_items: int = n_items
        self.simple: bool = simple

        if self.dic_attributes["column_types"] is None:
            self.dic_attributes["column_types"] = [GObject.TYPE_STRING] * self.n_items

        self.set_model(Gtk.ListStore(*self.dic_attributes["column_types"]))
        for _idx, __ in enumerate(self.dic_attributes["column_types"]):
            _cell = Gtk.CellRendererText()
            self.pack_end(_cell, True)
            if _idx == self.display_index:
                self.add_attribute(_cell, "text", self.display_index)

        self.show()

    def do_get_attribute(
        self,
        attribute: str,
    ) -> bool | date | float | int | object | str | None:
        """Get the value of the requested BaseWidget attribute.

        Parameters
        ----------
        attribute : str
            The name of the attribute to retrieve.

        Returns
        -------
        bool | date | float | int | str | None
            The value of the requested attribute.
        """
        if attribute in self._GTK3_COMBOBOX_ATTRIBUTES:
            return self.dic_attributes[attribute]
        return super().do_get_attribute(attribute)

    def do_set_attributes(self, attributes: PyTkWrapAttributes) -> None:
        """Set the GTK3ComboBox attributes.

        Parameters
        ----------
        attributes : GTK3WidgetAttributes
            Typed dict with the attribute values to set for the widget.
        """
        super().do_set_attributes(attributes)

        for _attr in ["column_types"]:
            self.dic_attributes[_attr] = attributes.get(
                _attr,
                self.dic_attributes[_attr],
            )

    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None:
        """Set the properties of the GTK3ComboBox.

        Parameters
        ----------
        properties : GTK3WidgetProperties
            The typed dict with the property values to set for the GTK3ComboBox.
        """
        super().do_set_properties(properties)

        self.set_active(self.dic_properties["active"])
        self.set_active_id(self.dic_properties["active_id"])
        self.set_border_width(self.dic_properties["border_width"])
        self.set_button_sensitivity(self.dic_properties["button_sensitivity"])
        self.set_column_span_column(self.dic_properties["column_span_column"])
        self.set_entry_text_column(self.dic_properties["entry_text_column"])
        self.set_id_column(self.dic_properties["id_column"])
        self.set_popup_fixed_width(self.dic_properties["popup_fixed_width"])
        self.set_row_span_column(self.dic_properties["row_span_column"])
        self.set_wrap_width(self.dic_properties["wrap_width"])

        if self.dic_properties["model"]:
            self.dic_properties["model"].set_column_types(  # type: ignore[attr-defined]
                self.dic_attributes["column_types"]
            )
        self.set_model(self.dic_properties["model"])

        for _property in [
            "has_frame",
        ]:
            self.set_property(_property, self.dic_properties[_property])

    def do_get_options(self) -> dict[int, Any]:
        """Retrieve all the options in the GTK3ComboBox.

        Returns
        -------
        _options : dict[int, Any]
            A dict with the GTK3ComboBox index as the key and value at that position as
            the value.
        """
        _options = {}

        _model = self.get_model()
        if _model is None:
            return {}

        _iter = _model.get_iter_first()

        i = 0
        while _iter is not None:
            _options[i] = _model.get_value(_iter, self.display_index)
            _iter = _model.iter_next(_iter)
            i += 1

        return _options

    def do_load_combo(
        self,
        entries: list[str | list[str | int | Pixbuf | None]],
    ) -> None:
        """Load the GTK3ComboBox.

        Parameters
        ----------
        entries : list
            The information to load into the GTK3ComboBox. This is always a list of
            lists where each internal list contains the information to be displayed,
            and there is one internal list for each ComboBox line.
        """
        _model = self.get_model()
        if _model is None or not isinstance(_model, Gtk.ListStore):
            return

        _model.clear()

        _hid = self.dic_handler_id[self.dic_attributes["edit_signal"]]
        if _hid != -1:
            with self.handler_block(_hid):
                _model.append([""] * self.n_items)
                if not self.simple:
                    for _entry in entries:
                        _model.append(list(_entry))
                else:
                    for _entry in entries:
                        _model.append([_entry])

    def do_get_value(self) -> str:
        """Return the value at the display column (self.index).

        Returns
        -------
        _value : str
        """
        return self.get_value_at_index(self.display_index)

    def do_set_value(
        self,
        value: bool | date | float | int | object | str | tuple | None,
    ) -> None:
        """Set the GTK3ComboBox active selection.

        Parameters
        ----------
        value : bool | date | float | int | object | str | tuple | None
            The index of the item in the GTK3ComboBox to set active.
        """
        if not isinstance(value, (float, int)):
            super().do_set_value(value)
        self.set_active(int(value))

    def get_value_at_index(self, display_index: int = -1) -> str:
        """Return the value in the ComboBox model found at <index> position.

        Parameters
        ----------
        display_index : int
            The column in the GTK3ComboBox model whose value is to be retrieved.
            Defaults to zero which will always read a 'simple' GTK3ComboBox.

        Returns
        -------
        _value : str
            The value displayed in the GTK3ComboBox at position <index>.
        """
        display_index = self.display_index if display_index == -1 else display_index
        _model = self.get_model()
        if _model is None or not isinstance(_model, Gtk.ListStore):
            return ""

        _row = self.get_active_iter()
        if isinstance(_row, Gtk.TreeIter):
            return _model.get_value(_row, display_index)

        return ""
