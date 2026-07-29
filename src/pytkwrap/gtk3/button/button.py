"""The pytkwrap GTK3Button module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GdkPixbuf, Gtk
from pytkwrap.gtk3.container.bin import GTK3Bin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3Button(Gtk.Button, GTK3Bin):
    """Wrapper for version 3.0 Gtk.Button."""

    # Define private class attributes.
    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 200
    _GTK3_BUTTON_PROPERTIES = GTK3WidgetProperties(
        always_show_image=False,
        image=None,
        image_position=Gtk.PositionType.LEFT,
        label="...",
        relief=Gtk.ReliefStyle.NORMAL,
        use_underline=False,
    )
    _GTK3_BUTTON_SIGNALS = [
        "activate",
        "check-resize",
        "clicked",
        # Container signals inherited from Gtk.Bin - callbacks require two arguments
        # (container, widget) rather than the standard single-argument form.  Register
        # these manually via self.connect() if needed:
        # "add", "remove", "set-focus-child"
    ]

    def __init__(
        self,
        label: str | None = "...",
    ) -> None:
        """Initialize an instance of the GTK3Button widget.

        Parameters
        ----------
        label : str | None
            The text to display on the GTK3Button.  The default value is an ellipsis
            (...).
        """
        Gtk.Button.__init__(self, label=label)
        GTK3Bin.__init__(self)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_BUTTON_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_BUTTON_PROPERTIES)

        if label is not None:
            self.set_label(label)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the Button.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Button.
        """
        super().do_set_properties(properties)

        self.set_always_show_image(self.dic_properties["always_show_image"])
        self.set_relief(self.dic_properties["relief"])
        self.set_use_underline(self.dic_properties["use_underline"])

        if self.dic_properties["label"] is not None:
            self.set_label(self.dic_properties["label"])

        if self.dic_properties["image"] is not None:
            self.set_label("")
            _icon = GdkPixbuf.Pixbuf.new_from_file_at_size(
                self.dic_properties["image"],
                self.dic_properties["height_request"],
                self.dic_properties["width_request"],
            )
            _image = Gtk.Image()
            _image.set_from_pixbuf(_icon)
            self.set_image(_image)
            self.set_image_position(self.dic_properties["image_position"])
