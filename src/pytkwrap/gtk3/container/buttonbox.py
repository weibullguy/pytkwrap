"""The pytkwrap GTK3ButtonBox module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Callable, Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GdkPixbuf, Gtk
from pytkwrap.gtk3.button.button import GTK3Button
from pytkwrap.gtk3.container.box import GTK3BoxMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3ButtonBoxMixin(GTK3BoxMixin):
    """Mixin class for GTK3ButtonBox."""

    _GTK3_BUTTONBOX_PROPERTIES = GTK3WidgetProperties(
        layout_style=Gtk.ButtonBoxStyle.END,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3ButtonBox mixin."""
        super().__init__(**kwargs)

        self.dic_properties.update(self._GTK3_BUTTONBOX_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3ButtonBox-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3ButtonBox.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_layout(self.dic_properties["layout_style"])


class GTK3ButtonBox(Gtk.ButtonBox, GTK3ButtonBoxMixin):
    """Wrapper for version 3.0 Gtk.ButtonBox."""

    def __init__(
        self,
        orientation: Gtk.Orientation = Gtk.Orientation.HORIZONTAL,
    ) -> None:
        """Initialize an instance of the GTK3ButtonBox."""
        super().__init__(orientation=orientation)
        GTK3ButtonBoxMixin.__init__(self)


def do_make_buttonbox(
    icons: list[str],
    tooltips: list[str],
    callbacks: list[Callable],
    height: int = -1,
    layout: Gtk.ButtonBoxStyle = Gtk.ButtonBoxStyle.START,
    orientation: str = "horizontal",
    width: int = -1,
) -> GTK3ButtonBox:
    """Create a buttonbox for views.

    This method creates the base buttonbox used by all Views.  Use a
    buttonbox for a View if there are only buttons to be added.

    Parameters
    ----------
    icons : list[str]
        List of absolute paths to icon image files for each button.
    tooltips : list[str]
        List of tooltip markup strings for each button.  If fewer tooltips than icons
        are present, the remaining buttons get default tooltips.
    callbacks : list[Callable]
        List of callback functions for each button's 'clicked' signal.  If fewer
        callbacks than icons are provided, the remaining buttons are set insensitive.
    height : int
        The button height in pixels.  The default value is -1 (natural size).
    layout : Gtk.ButtonBoxStyle
        The button layout style.  The default value is Gtk.ButtonBoxStyle.START.
    orientation : str
        'horizontal' or 'vertical'.  The default value is 'horizontal'.
    width : int
        The button width in pixels.  The default value is -1 (natural size).

    Returns
    -------
    _buttonbox : GTK3ButtonBox
        The buttonbox populated with GTK3Buttons.
    """
    _buttonbox = (
        GTK3ButtonBox()
        if orientation == "horizontal"
        else GTK3ButtonBox(Gtk.Orientation.VERTICAL)
    )
    _buttonbox.set_layout(layout)

    for _idx, __ in enumerate(icons):
        _image = Gtk.Image()
        _icon = GdkPixbuf.Pixbuf.new_from_file_at_size(__, height, width)
        _image.set_from_pixbuf(_icon)

        _button = GTK3Button()
        _button.set_image(_image)

        _button.do_set_properties(
            GTK3WidgetProperties(
                height_request=height,
                width_request=width,
            )
        )

        try:
            _button.set_tooltip_markup(tooltips[_idx])
        except IndexError:
            _button.set_tooltip_markup("")

        try:
            _button.connect("clicked", callbacks[_idx])
        except IndexError:
            _button.set_sensitive(False)

        _buttonbox.pack_start(_button, True, True, 0)

    return _buttonbox
