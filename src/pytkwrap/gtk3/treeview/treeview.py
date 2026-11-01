"""The pytkwrap GTK3TreeView module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk, GObject, Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.treeview.cellrenderer import GTK3CellRenderer
from pytkwrap.gtk3.treeview.cellrenderercombo import GTK3CellRendererCombo
from pytkwrap.gtk3.treeview.cellrendererpixbuf import GTK3CellRendererPixbuf
from pytkwrap.gtk3.treeview.cellrendererprogress import GTK3CellRendererProgress
from pytkwrap.gtk3.treeview.cellrendererspin import GTK3CellRendererSpin
from pytkwrap.gtk3.treeview.cellrendererspinner import GTK3CellRendererSpinner
from pytkwrap.gtk3.treeview.cellrenderertext import GTK3CellRendererText
from pytkwrap.gtk3.treeview.cellrenderertoggle import GTK3CellRendererToggle
from pytkwrap.gtk3.treeview.liststore import GTK3ListStore
from pytkwrap.gtk3.treeview.treestore import GTK3TreeStore
from pytkwrap.gtk3.treeview.treeviewcolumn import GTK3TreeViewColumn


class GTK3TreeViewMixin(GTK3ContainerMixin):
    """Mixin class for GTK3TreeView.

    Attributes
    ----------
    _GTK3_TREEVIEW_PROPERTIES : GTK3WidgetProperties
        Properties unique to the GTK3TreeView.
    _GTK3_TREEVIEW_SIGNALS : list[str]
        Signals unique to the GTK3TreeView.
    """

    _GTK3_TREEVIEW_PROPERTIES = GTK3WidgetProperties(
        activate_on_single_click=False,
        enable_grid_lines=Gtk.TreeViewGridLines.NONE,
        enable_search=True,
        enable_tree_lines=False,
        expander_column=None,
        fixed_height_mode=False,
        headers_clickable=True,
        headers_visible=True,
        hover_expand=False,
        hover_selection=False,
        level_indentation=0,
        model=None,
        reorderable=False,
        rubber_banding=False,
        search_column=-1,
        show_expanders=True,
        tooltip_column=-1,
    )
    _GTK3_TREEVIEW_SIGNALS = [
        "columns-changed",
        "cursor-changed",
        "expand-collapse-cursor-row",
        "move-cursor",
        "row-activated",
        "row-collapsed",
        "row-expanded",
        "select-all",
        "select-cursor-parent",
        "select-cursor-row",
        "start-interactive-search",
        "test-collapse-row",
        "test-expand-row",
        "toggle-cursor-row",
        "unselect-all",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3TreeView mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_TREEVIEW_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_TREEVIEW_PROPERTIES)

        self.attr_map: dict[GTK3CellRenderer, dict[str, int]] = {}

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3TreeView-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3TreeView.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_activate_on_single_click(
            self.dic_properties["activate_on_single_click"]
        )
        self.set_grid_lines(self.dic_properties["enable_grid_lines"])
        self.set_enable_search(self.dic_properties["enable_search"])
        self.set_enable_tree_lines(self.dic_properties["enable_tree_lines"])
        self.set_fixed_height_mode(self.dic_properties["fixed_height_mode"])
        self.set_headers_clickable(self.dic_properties["headers_clickable"])
        self.set_headers_visible(self.dic_properties["headers_visible"])
        self.set_hover_expand(self.dic_properties["hover_expand"])
        self.set_hover_selection(self.dic_properties["hover_selection"])
        self.set_level_indentation(self.dic_properties["level_indentation"])
        self.set_model(self.dic_properties["model"])
        self.set_reorderable(self.dic_properties["reorderable"])
        self.set_rubber_banding(self.dic_properties["rubber_banding"])
        self.set_search_column(self.dic_properties["search_column"])
        self.set_show_expanders(self.dic_properties["show_expanders"])
        self.set_tooltip_column(self.dic_properties["tooltip_column"])

    def do_add_column(
        self,
        column: GTK3TreeViewColumn | None = None,
        position: int = -1,
        title: str | None = None,
        cell: GTK3CellRenderer | None = None,
        **kwargs,
    ) -> int:
        """Add a column to the GTK3TreeView.

        Parameters
        ----------
        column : GTK3TreeViewColumn | None, optional
            The GTK3TreeViewColumn to add to the GTK3TreeView.  If None is passed,
            then a GTK3TreeViewColumn will be created and added.
        position : int, optional
            The position to insert the new column.  Pass -1 to append the column to
            the end (right) of the GTK3TreeView.
        title : str | None, optional
            The title for the header of the new column.
        cell : GTK3CellRenderer | None, optional
            The GTK3CellRenderer for the new GTK3TreeViewColumn.

        Returns
        -------
        int
            The number of columns in the GTK3TreeView after inserting the column.

        Note
        ----
        This method does not wrap insert_column_with_data_func.
        """
        if column is None:
            column = GTK3TreeViewColumn()

        if title is None:
            if position == -1:
                return self.append_column(column)
            return self.insert_column(column, position)

        if cell is None:
            cell = GTK3CellRenderer()

        return self.insert_column_with_attributes(position, title, cell, **kwargs)

    def do_add_row(
        self,
        values: list[object],
        position: int | None = None,
        columns: list[int] | None = None,
        parent: Gtk.TreeIter | None = None,
        sibling: Gtk.TreeIter | None = None,
        after: bool | None = None,
    ) -> Gtk.TreeIter:
        """Add a new row with values to the GTK3TreeView.

        Parameters
        ----------
        values : list[object]
            The values to apply to the newly inserted row.
        position : int | None, optional
            The position to insert the new row.  Pass 0 to prepend the row, pass -1
            to append the row.
        columns : list[int] | None, optional
            The list of column numbers to insert the values.
        parent : Gtk.TreeIter | None, optional
            The Gtk.TreeIter that will be the parent of the newly inserted row.
        sibling : Gtk.TreeIter | None, optional
            The Gtk.TreeIter to insert the new row before or after.
        after : bool | None, optional
            Whether to insert the new row after the sibling or before it.

        Returns
        -------
        Gtk.TreeIter
            The Gtk.TreeIter of the newly added row.
        """
        return self.get_model().do_insert_row(
            values=values,
            position=position,
            columns=columns,
            parent=parent,
            sibling=sibling,
            after=after,
        )

    def do_collapse_row(self, path: Gtk.TreePath | None = None) -> bool | None:
        """Collapse one or more rows.

        Parameters
        ----------
        path : Gtk.TreePath | None, optional
            The path of the row to collapse.

        Returns
        -------
        bool | None
            True if the row pointed to by path was collapsed.  None if all rows were
            collapsed.
        """
        if path is None:
            return self.collapse_all()
        return self.collapse_row(path)

    def do_expand_row(
        self,
        path: Gtk.TreePath | None = None,
        open_all: bool = False,
    ) -> bool | None:
        """Expand one or more rows.

        Parameters
        ----------
        path : Gtk.TreePath | None, optional
            The path of the row to expand.
        open_all : bool
            Indicates whether to recursively expand or just the immediate children

        Returns
        -------
        int | None
            True if the expanded row existed and had children.  None if expanding all
            or expanding to a path.
        """
        if path is None:
            return self.expand_all()

        if open_all:
            return self.expand_row(path, open_all)

        return self.expand_to_path(path)

    def do_move_column(
        self,
        column: GTK3TreeViewColumn,
        base_column: GTK3TreeViewColumn | None,
    ) -> None:
        """Move a column after the base column.

        Parameters
        ----------
        column : GTK3TreeViewColumn
            The GTK3TreeViewColumn to move.
        base_column : GTK3TreeViewColumn | None
            The GTK3TreeViewColumn to move column relative to.  If None, then column
            is moved to the first position.
        """
        return self.move_column_after(column, base_column)

    def do_remove_column(self, column: GTK3TreeViewColumn) -> int:
        """Remove one or more columns.

        Parameters
        ----------
        column : GTK3TreeViewColumn
            The GTK3TreeViewColumn to remove.

        Returns
        -------
        int
            The number of columns in the GTK3TreeView after removing column.
        """
        return self.remove_column(column)

    def do_scroll(
        self,
        path: Gtk.TreePath | None,
        column: GTK3TreeViewColumn | None,
        use_align: bool,
        row_align: float,
        col_align: float,
        tree_x: int = -1,
        tree_y: int = -1,
    ) -> None:
        """Scroll the GTK3TreeView.

        Parameters
        ----------
        path : Gtk.TreePath | None
            The path of the row to move vertically to.  If None, then no vertical
            scrolling occurs.
        column : GTK3TreeViewColumn | None
            The column to move horizontally to.  If None, the no horizontal scrolling
            occurs.
        use_align : bool
            Indicates whether to use alignment arguments.
        row_align : float
            The vertical alignment of the row specified by path.
        col_align : float
            The horizontal alignment of the column specified by column.
        tree_x : int
            The X coordinate, in tree coordinates, of the new top-left pixel of the
            visible area.
        tree_y : int
            The Y coordinate, in tree coordinates, of the new top-left pixel of the
            visible area.
        """
        if path is not None and column is not None:
            return self.scroll_to_cell(path, column, use_align, row_align, col_align)
        return self.scroll_to_point(tree_x, tree_y)

    @property
    def columns(self) -> list[Gtk.TreeViewColumn]:
        """Return a list of all the Gtk.TreeViewColumns in the GTK3TreeView."""
        return self.get_columns()

    @property
    def n_columns(self) -> int:
        """Return the number of columns in the GTK3TreeView."""
        return self.get_n_columns()

    @property
    def selection(self) -> Gtk.TreeSelection:
        """Return the currently selected Gtk.TreeSelection (row)."""
        return self.get_selection()

    @property
    def visible_range(self) -> tuple[Gtk.TreePath, Gtk.TreePath] | None:
        """Return the first and last visible paths."""
        return self.get_visible_range()

    @property
    def visible_rect(self) -> Gdk.Rectangle:
        """Return the currently visible region, in tree coordinates."""
        return self.get_visible_rect()


class GTK3TreeView(Gtk.TreeView, GTK3TreeViewMixin):
    """Wrapper for version 3.0 Gtk.TreeView."""

    def __init__(self, model: Gtk.TreeModel = None) -> None:
        """Initialize an instance of the GTK3TreeView."""
        Gtk.TreeView.__init__(self, model=model)
        GTK3TreeViewMixin.__init__(self)

        self.dic_properties["model"] = model


def do_construct_treeview(
    column_types: list[GObject.GType],
    renderer_types: list[str],
    attributes: list[dict[str, int]],
    headers: list[str],
    tree: bool = True,
) -> GTK3TreeView:
    """Construct a GTK3TreeView.

    Parameters
    ----------
    column_types : list[GObject.GType]
        A list with the data type to be displayed in each column.
    renderer_types : list[str]
        A list with the name of the type of GTK3CellRenderer to use for each column.
        Options are:
            * Combo
            * Pixbuf
            * Progress
            * Spin
            * Spinner
            * Text
            * Toggle
    attributes : list[dict[str, int]]
        A list of dicts where each dict contains the attributes for the
        GTK3TreeViewColumn to bind to the underlying GTK3TreeModel.
    headers : list[str]
        A list with the titles for each columns' header.
    tree : bool
        Indicates whether to construct with a GTK3TreeStore, default,
        or a GTK3ListStore.

    Returns
    -------
    GTK3TreeView
        A GTk3TreeView with the appropriate GTK3TreeModel.
    """
    _n_columns = len(column_types)
    if tree:
        _model = GTK3TreeStore(column_types, n_columns=_n_columns, n_rows=0)
    else:
        _model = GTK3ListStore(column_types, n_columns=_n_columns, n_rows=0)

    _treeview = GTK3TreeView(model=_model)
    _treeview.attr_map.clear()

    for _idx, _title in enumerate(headers):
        match renderer_types[_idx].lower():
            case "combo":
                _cell = GTK3CellRendererCombo()
            case "pixbuf":
                _cell = GTK3CellRendererPixbuf()
            case "progress":
                _cell = GTK3CellRendererProgress()
            case "spin":
                _cell = GTK3CellRendererSpin()
            case "spinner":
                _cell = GTK3CellRendererSpinner()
            case "text":
                _cell = GTK3CellRendererText()
            case "toggle":
                _cell = GTK3CellRendererToggle()
            case _:
                _cell = GTK3CellRenderer()

        _attributes = attributes[_idx]
        _treeview.attr_map[_cell] = _attributes
        _treeview.do_add_column(
            column=None,
            position=-1,
            title=_title,
            cell=_cell,
            **_attributes,
        )

    return _treeview
