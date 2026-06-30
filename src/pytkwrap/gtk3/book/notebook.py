"""The pytkwrap GTK3Notebook module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.container import GTK3Container
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3Notebook(Gtk.Notebook, GTK3Container):
    """Wrapper for version 3.0 Gtk.Notebook."""

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
        """Initialize an instance of the GTK3Notebook."""
        Gtk.Notebook.__init__(self)
        GTK3Container.__init__(self)

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
