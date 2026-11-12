"""The pytkwrap GTK3Button module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

from __future__ import annotations

# Standard Library Imports
from collections.abc import Mapping
from typing import TYPE_CHECKING

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GdkPixbuf, Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties

if TYPE_CHECKING:
    # pytkwrap Local Imports
    from ._protocols import _ButtonHost


class GTK3ButtonMixin(GTK3ContainerMixin):
    """Mixin class for GTK3Button.

    Attributes
    ----------
    _DEFAULT_HEIGHT : int
        The default height of the GTK3Button.
    _DEFAULT_WIDTH : int
        The default width of the GTK3Button.
    _GTK3_BUTTON_PROPERTIES : GTK3WidgetProperties
        GTK3Button-specific properties.
    _GTK3_BUTTON_SIGNALS : list[str]
        List of GTK3Button-specific signals.

    Notes
    -----
    The following Gtk.Button methods are not wrapped in a convenience layer,
    but may be called directly:

        * clicked()

    Refer to https://lazka.github.io/pgi-docs/#Gtk-3.0/classes/Button.html for
    details on these methods.

    Container signals inherited from Gtk.Container require two arguments
    (container, widget) rather than the standard single-argument form.  Register these
    manually via self.connect() if needed:
        * add
        * remove
        * set-focus-child
    """

    # Define private class attributes.
    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 200
    _GTK3_BUTTON_PROPERTIES = GTK3WidgetProperties(
        always_show_image=False,
        file=None,
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
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3Button widget."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_BUTTON_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_BUTTON_PROPERTIES)

    def do_set_properties(
        self: _ButtonHost,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the Button.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Button.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)  # type: ignore[safe-super] # ty: ignore[invalid-super-argument] # pylint: disable=line-too-long

        self.set_always_show_image(self.dic_properties["always_show_image"])
        self.set_relief(self.dic_properties["relief"])
        self.set_use_underline(self.dic_properties["use_underline"])

        # Allow None to be used to clear the label.
        if self.dic_properties["label"] is None:
            self.dic_properties["label"] = ""
        self.set_label(self.dic_properties["label"])

        if self.dic_properties["file"] is not None:
            _icon = GdkPixbuf.Pixbuf.new_from_file_at_size(
                self.dic_properties["file"],
                self.dic_properties["height_request"],
                self.dic_properties["width_request"],
            )
            _image = Gtk.Image()
            _image.set_from_pixbuf(_icon)
            self.set_image(_image)
            self.set_image_position(self.dic_properties["image_position"])


class GTK3Button(Gtk.Button, GTK3ButtonMixin):
    """Wrapper for version 3.0 Gtk.Button."""

    def __init__(
        self,
        label: str = "...",
    ) -> None:
        """Initialize an instance of the GTK3Button widget.

        Parameters
        ----------
        label : str
            The text to display on the GTK3Button.  The default value is an ellipsis
            (...).  Pass an empty string to clear the label.
        """
        Gtk.Button.__init__(self, label=label)
        GTK3ButtonMixin.__init__(self)

        self.dic_properties["label"] = label
