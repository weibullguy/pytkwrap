"""The pytkwrap GTK3PrintOperation module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin, GTK3WidgetProperties


class GTK3PrintOperation(Gtk.PrintOperation, GTK3GObjectMixin):
    """Wrapper for version 3.0 Gtk.PrintOperation."""

    _GTK3_PRINTOPERATION_PROPERTIES = GTK3WidgetProperties(
        allow_async=False,
        current_page=-1,
        custom_tab_label=None,
        default_page_setup=None,
        embed_page_setup=False,
        export_filename=None,
        has_selection=False,
        job_name="",
        n_pages=-1,
        print_settings=None,
        show_progress=False,
        support_selection=False,
        track_print_status=False,
        unit=Gtk.Unit.NONE,
        use_full_page=False,
    )
    _GTK3_PRINTOPERATION_SIGNALS = [
        "begin-print",
        "create-custom-widget",
        "custom-widget-apply",
        "done",
        "draw-page",
        "end-print",
        "paginate",
        "preview",
        "request-page-setup",
        "status-changed",
        "update-custom-widget",
    ]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3PrintOperation."""
        Gtk.PrintOperation.__init__(self)
        GTK3GObjectMixin.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_PRINTOPERATION_SIGNALS}
        )
        self.dic_properties = dict(self._GTK3_PRINTOPERATION_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3PrintOperation-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3PrintOperation.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_allow_async(self.dic_properties["allow_async"])
        self.set_current_page(self.dic_properties["current_page"])
        self.set_custom_tab_label(self.dic_properties["custom_tab_label"])
        self.set_default_page_setup(self.dic_properties["default_page_setup"])
        self.set_embed_page_setup(self.dic_properties["embed_page_setup"])
        self.set_has_selection(self.dic_properties["has_selection"])
        self.set_job_name(self.dic_properties["job_name"])
        self.set_n_pages(self.dic_properties["n_pages"])
        self.set_print_settings(self.dic_properties["print_settings"])
        self.set_show_progress(self.dic_properties["show_progress"])
        self.set_support_selection(self.dic_properties["support_selection"])
        self.set_track_print_status(self.dic_properties["track_print_status"])
        self.set_unit(self.dic_properties["unit"])
        self.set_use_full_page(self.dic_properties["use_full_page"])

        if self.dic_properties["export_filename"] is not None:
            self.set_export_filename(self.dic_properties["export_filename"])
