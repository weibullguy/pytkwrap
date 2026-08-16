"""The pytkwrap GTK3FileChooserButton module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.box import GTK3BoxMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3FileChooserButtonMixin(GTK3BoxMixin):
    """Mixin class for GTK3FileChooserButton.

    Notes
    -----
    GTK3FileChooserButton passes no widget to its callback function.
    """

    _GTK3_FILECHOOSERBUTTON_PROPERTIES = GTK3WidgetProperties(
        dialog=None,
        title="Select a File",
        width_chars=-1,
    )
    _GTK3_FILECHOOSERBUTTON_SIGNALS = ["file-set"]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3FileChooserButton mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_FILECHOOSERBUTTON_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_FILECHOOSERBUTTON_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3FileChooserButton-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3FileChooserButton.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_title(self.dic_properties["title"])
        self.set_width_chars(self.dic_properties["width_chars"])


class GTK3FileChooserButton(Gtk.FileChooserButton, GTK3FileChooserButtonMixin):
    """Wrapper for version 3.0 Gtk.FileChooserButton."""

    def __init__(
        self,
        title: str = "Select a File",
        action: Gtk.FileChooserAction = Gtk.FileChooserAction.OPEN,
        dialog: Gtk.Dialog | None = None,
    ) -> None:
        """Initialize an instance of the GTK3FileChooserButton.

        Parameters
        ----------
        title : str
            The title of the browse dialog.
        action : Gtk.FileChooserAction
            The open mode for the widget.
        dialog : Gtk.Dialog | None
            The widget to use as the dialog.
        """
        Gtk.FileChooserButton.__init__(self, title=title, action=action, dialog=dialog)
        GTK3FileChooserButtonMixin.__init__(self)

        self.dic_properties["dialog"] = dialog
        self.dic_properties["title"] = title

        self.set_action(action)
