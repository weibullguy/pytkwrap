"""The pytkwrap GTK3ComboBox module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from datetime import date
from typing import Any

# Third Party Imports
from gi.overrides.GdkPixbuf import Pixbuf  # type: ignore[import-untyped]

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.bin import GTK3BinMixin
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties


class GTK3ComboBoxMixin(GTK3BinMixin):
    """Mixin for GTK3ComboBox."""

    # Define private class attributes.
    _DEFAULT_HEIGHT: int = 30
    _DEFAULT_WIDTH: int = 200
    _GTK3_COMBOBOX_ATTRIBUTES = GTK3WidgetAttributes(
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

    def __init__(self) -> None:
        """Initialize an instance of the GTK3ComboBox mixin."""
        GTK3BinMixin.__init__(self)

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_COMBOBOX_ATTRIBUTES)
        self.dic_properties.update(self._GTK3_COMBOBOX_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_COMBOBOX_SIGNALS}
        )

        self.display_index = 0
        self._n_items = 0

    def do_get_attribute(
        self,
        attribute: str,
    ) -> bool | date | float | int | object | str | None:
        """Get the value of the requested attribute.

        Parameters
        ----------
        attribute : str
            The name of the attribute to retrieve.

        Returns
        -------
        bool | date | float | int | object | str | None
            The value of the requested attribute.
        """
        if attribute in self._GTK3_COMBOBOX_ATTRIBUTES:
            return self.dic_attributes[attribute]
        return super().do_get_attribute(attribute)

    def do_set_properties(
        self, properties: Mapping[str, object] | list[list | tuple]
    ) -> None:
        """Set the values of the GTK3ComboBox-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3ComboBox.
        """
        # Update the property dictionary.
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
        entries: list[
            str | list[str | int | Pixbuf | None] | tuple[str | int | Pixbuf | None],
        ],
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
                for _entry in entries:
                    if isinstance(_entry, (list, tuple)):
                        _model.append(_entry)
                    else:
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
        if isinstance(value, (bool, float, int)):
            self.set_active(int(value))
        else:
            super().do_set_value(value)

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


class GTK3ComboBox(Gtk.ComboBox, GTK3ComboBoxMixin):
    """Wrapper for version 3.0 Gtk.ComboBox."""

    def __init__(
        self,
        has_entry: bool = False,
        model: Gtk.TreeModel | None = None,
    ) -> None:
        """Initialize an instance of the GTK3ComboBox."""
        Gtk.ComboBox.__init__(self, has_entry=has_entry, model=model)
        GTK3ComboBoxMixin.__init__(self)

        # Initialize public instance attributes.
        self.dic_properties["has_entry"] = has_entry
        self.dic_properties["model"] = model

        if model is not None:
            self.n_items = model.get_n_columns()

        self.show()
