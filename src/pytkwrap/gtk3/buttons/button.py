"""The pytkwrap GTK3 Button module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Callable, Mapping
from datetime import date

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GdkPixbuf, Gtk
from pytkwrap.gtk3.bin import GTK3Bin
from pytkwrap.gtk3.widget import GTK3WidgetProperties


def do_make_buttonbox(
    icons: list[str],
    tooltips: list[str],
    callbacks: list[Callable],
    height: int = -1,
    layout: Gtk.ButtonBoxStyle = Gtk.ButtonBoxStyle.START,
    orientation: str = "vertical",
    width: int = -1,
) -> Gtk.ButtonBox:
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
        'horizontal' or 'vertical'.  The default value is 'vertical'.
    width : int
        The button width in pixels.  The default value is -1 (natural size).

    Returns
    -------
    _buttonbox : Gtk.ButtonBox
        The buttonbox populated with GTK3Buttons.
    """
    # TODO: Change this to a GTK3ButtonBox once that wrapper is done.
    _buttonbox = Gtk.HButtonBox() if orientation == "horizontal" else Gtk.VButtonBox()
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


class GTK3Button(Gtk.Button, GTK3Bin):
    """The GTK3Button class."""

    # Define private class attributes.
    _GTK3_BUTTON_PROPERTIES = GTK3WidgetProperties(
        action_name=None,
        action_target=None,
        always_show_image=False,
        image=None,
        image_position=Gtk.PositionType.LEFT,
        label=None,
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
    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 200

    def __init__(self, label: str = "...") -> None:
        """Initialize an instance of the GTK3Button widget.

        Parameters
        ----------
        label : str
            The text to display on the GTK3Button.  The default value is an ellipsis
            (...).
        """
        Gtk.Button.__init__(self)
        GTK3Bin.__init__(self)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_BUTTON_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_BUTTON_SIGNALS}
        )

        self.set_label(label)
        self.show_all()

    def do_get_property(
        self, property_name: str
    ) -> bool | date | float | int | object | str | None:
        """Get the value of the requested property.

        Parameters
        ----------
        property_name : str
            The name of the property to retrieve.

        Returns
        -------
        bool | date | float | int | object | str | None
        """
        if property_name in self._GTK3_BUTTON_PROPERTIES:
            return self.dic_properties.get(property_name)
        return super().do_get_property(property_name)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the Button.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
         the WidgetProperties dict with the property values to set for
            the Button.
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
