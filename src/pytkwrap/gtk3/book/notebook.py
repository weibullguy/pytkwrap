"""The pytkwrap GTK3Notebook module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# Third Party Imports
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.exceptions import PytkwrapError, PytkwrapWarning
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3NotebookMixin(GTK3ContainerMixin):
    """Mixin for GTK3Notebook.

    Attributes
    ----------
    _GTK3_NOTEBOOK_PROPERTIES : GTK3WidgetProperties
        GTK3Notebook-specific properties.
    _GTK3_NOTEBOOK_SIGNALS : list[str]
        List of GTK3Notebook-specific signals.

    Notes
    -----
    The following Gtk.Notebook methods are not wrapped in a convenience layer,
    but may be called directly:

        * detach_tab(child)
        * get_action_widget(pack_type)
        * get_menu_label(child)
        * get_menu_label_text(child)
        * get_nth_page(page_num)
        * get_tab_detachable(child)
        * get_tab_label(child)
        * get_tab_label_text(child)
        * get_tab_reorderable(child)
        * next_page()
        * page_num(child)
        * popup_disable()
        * popup_enable()
        * prev_page()
        * reorder_child(child, position)
        * set_action_widget(widget, pack_type)
        * set_menu_label(child, menu_label)
        * set_menu_label_text(child, menu_text)
        * set_tab_detachable(child, detachable)
        * set_tab_label(child, tab_label)
        * set_tab_label_text(child, tab_text)
        * set_tab_reaorderable(child, reorderable)

    Refer to https://lazka.github.io/pgi-docs/#Gtk-3.0/classes/Notebook.html for
    details on these methods.
    """

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

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3Notebook mixin."""
        super().__init__(**kwargs)

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

        self.set_current_page(self.dic_properties["page"])
        self.set_group_name(self.dic_properties["group_name"])
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
        tab_label: Gtk.Widget | None = None,
        menu_label: Gtk.Widget | None = None,
        position: int = -1,
    ) -> None:
        """Add a page to the notebook.

        Parameters
        ----------
        child : Gtk.Widget
            The Gtk.Widget to use as the contents of the page.
        tab_label : Gtk.Widget | None
            The widget to use as the label for the page.
        menu_label : Gtk.Widget | None
            The widget to use as the label for the page-switch menu.
        position : int, optional
            The position at which to add the page.  Defaults to the end (-1).  To
            prepend a page, pass 0.
        """
        if menu_label is None:
            if position == -1:
                self.append_page(child, tab_label)
            elif position == 0:
                self.prepend_page(child, tab_label)
            else:
                self.insert_page(child, tab_label, position)
        elif position == -1:
            self.append_page_menu(child, tab_label, menu_label)
        elif position == 0:
            self.prepend_page_menu(child, tab_label, menu_label)
        else:
            self.insert_page_menu(child, tab_label, menu_label, position)

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

    @property
    def n_pages(self) -> int:
        """Get the total number of pages in the GTK3Notebook.

        Returns
        -------
        int
            The total number of pages in the GTK3Notebook.
        """
        return self.get_n_pages()


class GTK3Notebook(Gtk.Notebook, GTK3NotebookMixin):
    """Wrapper for version 3.0 Gtk.Notebook."""

    def __init__(
        self,
        child_widgets: list[Gtk.Widget] | None,
        tab_labels: list[str] | None = None,
    ) -> None:
        """Initialize an instance of the GTK3Notebook.

        Parameters
        ----------
        child_widgets : list[Gtk.Widget] | None
            List of Gtk.Widgets to use as contents of each page.
        tab_labels : list[str] | None
            List of tab labels to add to the notebook.
        """
        Gtk.Notebook.__init__(self)
        GTK3NotebookMixin.__init__(self)

        if child_widgets is not None and tab_labels is not None:
            self.do_build_notebook(child_widgets, tab_labels)

    def do_build_notebook(
        self, child_widgets: list[Gtk.Widget], tab_labels: list[str]
    ) -> None:
        """Add pages to the GTK3Notebook.

        Parameters
        ----------
        child_widgets : list[Gtk.Widget] | None
            List of Gtk.Widgets to use as contents of each page.
        tab_labels : list[str] | None
            List of tab labels to add to the notebook.

        Raises
        ------
        PytkwrapWarning
            if the number of child widgets does not match the number of tab labels.
        """
        _n_pages = min(len(child_widgets), len(tab_labels))

        try:
            # Warn the user that the number of child widgets does not match the number
            # of tab labels and that only the first _n_pages will be added.
            if len(child_widgets) != len(tab_labels):
                _warning_message = (
                    f"GTK3Notebook: The number of child widgets ({len(child_widgets)}) "
                    f"does not match the number of tab labels ({len(tab_labels)}).  "
                    f"Only {_n_pages} pages will be added."
                )
                pub.sendMessage("do_log_warning", message=_warning_message)
                raise PytkwrapWarning(_warning_message)
        except PytkwrapWarning:
            # But still add the minimum number of pages.
            for _page in range(_n_pages):
                self.do_add_page(child_widgets[_page], tab_labels[_page])
            raise

        for _page in range(_n_pages):
            self.do_add_page(child_widgets[_page], tab_labels[_page])
