# pylint: disable=wrong-import-position
#
#       pytkwrap.gtk3.combo.py is part of the pytkwrap Project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""The pytkwrap GTK3 ComboBox module."""

# Standard Library Imports
from datetime import date
from types import EllipsisType
from typing import Any

# Third Party Imports
from gi.overrides.GdkPixbuf import Pixbuf  # type: ignore[import-untyped]

# pytkwrap Package Imports
from pytkwrap.common import WidgetAttributes
from pytkwrap.gtk3._libs import GObject, Gtk
from pytkwrap.gtk3.mixins import GTK3DataWidgetAttributes
from pytkwrap.gtk3.widget import GTK3BaseDataWidget, GTK3WidgetProperties


class GTK3ComboBox(Gtk.ComboBox, GTK3BaseDataWidget):
    """The GTK3ComboBox class."""

    # Define private class attributes.
    _GTK3_COMBO_BOX_ATTRIBUTES = GTK3DataWidgetAttributes(
        column_types=[GObject.TYPE_STRING]
    )
    _GTK3_COMBO_BOX_PROPERTIES = GTK3WidgetProperties(
        active=-1,
        active_id=None,
        border_width=0,
        button_sensitivity=Gtk.SensitivityType.AUTO,
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
    _GTK3_COMBO_BOX_SIGNALS: list[str] = [
        "changed",
        "editing-done",
        "format-entry-text",
        "move-active",
        "popdown",
        "popup",
        "remove-widget",
    ]
    _DEFAULT_EDIT_SIGNAL: str = "changed"
    _DEFAULT_HEIGHT: int = 30
    _DEFAULT_WIDTH: int = 200

    def __init__(
        self,
        index: int = 0,
        simple: bool = True,
        n_items: int = 1,
        column_types: list[EllipsisType] | list[GObject.GType] | None = None,
        has_entry: bool = False,
    ) -> None:
        """Initialize an instance of the GTK3ComboBox widget.

        Parameters
        ----------
        index : int
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
        GTK3BaseDataWidget.__init__(self)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_COMBO_BOX_ATTRIBUTES)
        self.dic_properties.update(self._GTK3_COMBO_BOX_PROPERTIES)
        self.dic_handler_id.update({
            _signal: -1 for _signal in self._GTK3_COMBO_BOX_SIGNALS
        })

        self.default = -1
        self.has_entry: bool = has_entry
        self.index: int = index
        self.n_items: int = n_items
        self.simple: bool = simple

        if column_types is None:
            column_types = [GObject.TYPE_STRING] * self.n_items
        self.column_types: list[EllipsisType] | list[GObject.GType] | None = (
            column_types
        )

        self.set_model(Gtk.ListStore(*self.column_types))
        for _idx, __ in enumerate(column_types):
            _cell = Gtk.CellRendererText()
            self.pack_end(_cell, True)
            if _idx == self.index:
                self.add_attribute(_cell, "text", self.index)

        self.show()

    # ----- ----- ----- ----- --- Standard widget methods. --- ----- ----- ----- ----- #
    def do_get_attribute(
        self,
        attribute: str,
    ) -> bool | date | float | int | str | None:
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
        if attribute in self._GTK3_COMBO_BOX_ATTRIBUTES:
            return getattr(self, attribute)
        return super().do_get_attribute(attribute)

    def do_set_attributes(self, attributes: WidgetAttributes) -> None:
        """Set the attributes of the GTK3ComboBox.

        Parameters
        ----------
        attributes : GTKDataWidgetAttributes
            The typed dict with the attribute values to set for the GTK3ComboBox.
        """
        super().do_set_attributes(attributes)

        self.column_types = attributes.get("column_types", self.column_types)
        self.font_description = attributes.get(
            "font_description", self.font_description
        )

    def do_set_properties(self, properties: GTK3WidgetProperties) -> None:
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
            self.dic_properties["model"].set_column_types(self.column_types)
        self.set_model(self.dic_properties["model"])

        for _property in [
            "has_frame",
        ]:
            self.set_property(_property, self.dic_properties[_property])

    # ----- ----- ComboBox specific methods. ----- ----- #
    def do_get_options(self) -> dict[int, Any]:
        """Retrieve all the options in the ComboBox.

        Returns
        -------
        _options : dict[int, Any]
            A dict with the GTK3ComboBox index as key and value at that position as
            the value.
        """
        _options = {}

        _model = self.get_model()
        if _model is None:
            return {}

        _iter = _model.get_iter_first()

        i = 0
        while _iter is not None:
            _options[i] = _model.get_value(_iter, self.index)
            _iter = _model.iter_next(_iter)
            i += 1

        return _options

    def do_load_combo(
        self,
        entries: list[list[str | int | Pixbuf | None]],
    ) -> None:
        """Load the ComboBox widget.

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

        _hid = self.dic_handler_id[self.edit_signal]
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
        """Return thw value at the display column (self.index).

        Returns
        -------
        _value : str
        """
        return self.get_value_at_index(self.index)

    def do_set_value(self, value: int) -> None:
        """Set the GTK3ComboBox active selection.

        Parameters
        ----------
        value : int
            The index of the item in the GTK3ComboBox to set active.
        """
        if not isinstance(value, int):
            return

        self.set_active(value)

    def get_value_at_index(self, index: int = -1) -> str:
        """Return the value in the ComboBox model found at <index> position.

        Parameters
        ----------
        index : int
            The column in the GTK3ComboBox model whose value is to be retrieved.
            Defaults to zero which will always read a 'simple' GTK3ComboBox.

        Returns
        -------
        _value : str
            The value displayed in the GTK3ComboBox at position <index>.
        """
        index = self.index if index == -1 else index
        _model = self.get_model()
        if _model is None or not isinstance(_model, Gtk.ListStore):
            return ""

        _row = self.get_active_iter()
        if isinstance(_row, Gtk.TreeIter):
            return _model.get_value(_row, index)

        return ""
