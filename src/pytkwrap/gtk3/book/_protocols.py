# pylint: disable=missing-function-docstring
"""The pytkwrap book protocols module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping
from typing import Protocol

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class _NotebookHost(Protocol):
    """Methods the mixin expects the concrete widget to provide."""

    dic_handler_id: dict[str, int]
    dic_properties: GTK3WidgetProperties

    # pytkwrap methods.
    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None: ...
    def do_add_page(
        self,
        child: Gtk.Widget,
        tab_label: Gtk.Widget | None = None,
        menu_label: Gtk.Widget | None = None,
        position: int = -1,
    ) -> None: ...
    def do_remove_page(self, position: int) -> None: ...
    def do_build_notebook(
        self,
        child_widgets: list[Gtk.Widget],
        tab_labels: list[Gtk.Widget],
    ) -> None: ...

    # pytkwrap managed attributes.
    @property
    def n_pages(self) -> int: ...

    # Native Gtk3 API methods.
    def set_current_page(self, page: int) -> None: ...
    def set_group_name(self, group_name: str | None) -> None: ...
    def set_scrollable(self, scrollable: bool) -> None: ...
    def set_show_border(self, show_border: bool) -> None: ...
    def set_show_tabs(self, show_tabs: bool) -> None: ...
    def set_tab_pos(self, tab_pos) -> None: ...
    def set_property(self, property_name: str, value) -> None: ...
    def append_page(self, child: Gtk.Widget, tab_label: Gtk.Widget | None) -> int: ...
    def prepend_page(self, child: Gtk.Widget, tab_label: Gtk.Widget | None) -> int: ...
    def insert_page(
        self, child: Gtk.Widget, tab_label: Gtk.Widget | None, position: int
    ) -> int: ...
    def append_page_menu(
        self,
        child: Gtk.Widget,
        tab_label: Gtk.Widget | None,
        menu_label: Gtk.Widget | None,
    ) -> int: ...
    def prepend_page_menu(
        self,
        child: Gtk.Widget,
        tab_label: Gtk.Widget | None,
        menu_label: Gtk.Widget | None,
    ) -> int: ...
    def insert_page_menu(
        self,
        child: Gtk.Widget,
        tab_label: Gtk.Widget | None,
        menu_label: Gtk.Widget | None,
        position: int,
    ) -> int: ...
    def remove_page(self, position: int) -> None: ...
    def get_n_pages(self) -> int: ...
