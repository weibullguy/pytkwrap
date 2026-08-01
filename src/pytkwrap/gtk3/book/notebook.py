"""The pytkwrap GTK3Notebook module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.exceptions import PytkwrapError
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.io.label import GTK3Label
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3NotebookMixin(GTK3ContainerMixin):
    """Mixin for GTK3Notebook."""

    _GTK3_NOTEBOOK_PROPERTIES = GTK3WidgetProperties(
        enable_popup=False,
        group_name=None,
        page=-1,
        scrollable=False,
        show_border=True,
        show_tabs=True,
        tab_pos=Gtk.PositionType.TOP,
    )
    _GTK3_NOTEBOOK_SIGNALS = [
        "change-current-page",
        "create-window",
        "focus-tab",
        "move-focus-out",
        "page-added",
        "page-removed",
        "page-reordered",
        "reorder-tab",
        "select-page",
        "switch-page",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Notebook mixin."""
        GTK3ContainerMixin.__init__(self)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_NOTEBOOK_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_NOTEBOOK_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Notebook-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Notebook.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_group_name(self.dic_properties["group_name"])
        self.set_current_page(self.dic_properties["page"])
        self.set_scrollable(self.dic_properties["scrollable"])
        self.set_show_border(self.dic_properties["show_border"])
        self.set_show_tabs(self.dic_properties["show_tabs"])
        self.set_tab_pos(self.dic_properties["tab_pos"])

        for _property in ["enable_popup"]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )

    def do_add_page(
        self,
        child: Gtk.Widget,
        tab_label: str | None = None,
        position: int = -1,
    ) -> None:
        """Add a page to the notebook.

        Parameters
        ----------
        child : Gtk.Widget
            The Gtk.Widget to use as the contents of the page.
        tab_label : str
            The label to display for the page.
        position : int, optional
            The position at which to add the page.  Defaults to the end (-1).  To
            prepend a page, pass 0.
        """
        _tab_label = None
        if tab_label is not None:
            _tab_label = GTK3Label()
            _tab_label.do_set_value(tab_label)

        self.insert_page(child, _tab_label, position)

    def do_remove_page(self, position: int) -> None:
        """Remove a page from the notebook.

        Parameters
        ----------
        position : int
            The position of the page to remove.

        Raises
        ------
        PytkwrapError
            If the page number is invalid.
        """
        if position > self.get_n_pages():
            raise PytkwrapError(
                f"Invalid GTK3Notebook page number: {position}.  There are only "
                f"{self.get_n_pages()} pages."
            )
        self.remove_page(position)


class GTK3Notebook(Gtk.Notebook, GTK3NotebookMixin):
    """Wrapper for version 3.0 Gtk.Notebook."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Notebook."""
        Gtk.Notebook.__init__(self)
        GTK3NotebookMixin.__init__(self)
