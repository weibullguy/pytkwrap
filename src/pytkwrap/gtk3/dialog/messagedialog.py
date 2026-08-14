"""The pytkwrap GTK3MessageDialog module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.dialog.dialog import GTK3DialogMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3MessageDialogMixin(GTK3DialogMixin):
    """Mixin class for GTK3MessageDialog."""

    _GTK3_MESSAGEDIALOG_PROPERTIES = GTK3WidgetProperties(
        buttons=Gtk.ButtonsType.NONE,
        message_area=None,
        message_type=Gtk.MessageType.INFO,
        secondary_text=None,
        secondary_use_markup=False,
        text="",
        use_markup=False,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3MessageDialog mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_MESSAGEDIALOG_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3MessageDialog-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3MessageDialog.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        if self.dic_properties["use_markup"]:
            self.set_markup(self.dic_properties["text"])

        for _property in [
            "message_type",
            "secondary_text",
            "secondary_use_markup",
            "use_markup",
        ]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )


class GTK3MessageDialog(Gtk.MessageDialog, GTK3MessageDialogMixin):
    """Wrapper for version 3.0 Gtk.MessageDialog."""

    def __init__(
        self,
        buttons: Gtk.ButtonsType = Gtk.ButtonsType.NONE,
        message_type: Gtk.MessageType = Gtk.MessageType.INFO,
    ) -> None:
        """Initialize an instance of the GTK3MessageDialog.

        Parameters
        ----------
        buttons : Gtk.ButtonsType
            The buttons to display on the message dialog.  The default is none.
        message_type : Gtk.MessageType
            The type of message to display.  The default is Gtk.MessageType.INFO.
        """
        Gtk.MessageDialog.__init__(self, buttons=buttons, message_type=message_type)
        Gtk.Widget.set_has_window(self, False)
        GTK3MessageDialogMixin.__init__(self)

        self.dic_properties["buttons"] = buttons
        self.dic_properties["message_type"] = message_type
