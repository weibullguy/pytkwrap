#
#       pytkwrap.gtk3.buttons.base_button.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""The pytkwrap GTK3BaseButton module."""

# Standard Library Imports
from collections.abc import Callable
from datetime import date

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GdkPixbuf, Gtk
from pytkwrap.gtk3.widget import GTK3BaseDataWidget, GTK3WidgetProperties


def do_make_buttonbox(
    icons: list[str],
    tooltips: list[str],
    callbacks: list[Callable],
    height: int = -1,
    layout: Gtk.ButtonBoxStyle = Gtk.ButtonBoxStyle.START,
    orientation: str = "vertical",
    width: int = -1,
) -> Gtk.HButtonBox | Gtk.VButtonBox:
    """Create a buttonbox for  views.

    This method creates the base buttonbox used by all  Views.  Use a
    buttonbox for a  View if there are only buttons to be added.

    Parameters
    ----------
    icons : list[str]
        List of absolute paths to icon image files for each button.
    tooltips : list[str]
        List of tooltip markup strings for each button.  If fewer tooltips than icons
        are present, remaining buttons get default tooltips.
    callbacks : list[Callable]
        List of callback functions for each button's 'clicked' signal.  If fewer
        callbacks than icons are provided, remaining buttons are set insensitive.
    height : int
        The button height in pixels.  Default is -1 (natural size).
    layout : Gtk.ButtonBoxStyle
        The button layout style.  Default is Gtk.ButtonBoxStyle.START.
    orientation : str
        'horizontal' or 'vertical'. Default is 'vertical'.
    width : int
        The button width in pixels.  Default is -1 (natural size).

    Returns
    -------
    _buttonbox : Gtk.HButtonBox | Gtk.VButtonBox
        The buttonbox populated with GTK3Buttons.
    """
    _buttonbox = Gtk.HButtonBox() if orientation == "horizontal" else Gtk.VButtonBox()
    _buttonbox.set_layout(layout)

    for _idx, __ in enumerate(icons):
        _image = Gtk.Image()
        _icon = GdkPixbuf.Pixbuf.new_from_file_at_size(__, height, width)
        _image.set_from_pixbuf(_icon)

        _button = GTK3BaseButton()
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


class GTK3BaseButton(Gtk.Button, GTK3BaseDataWidget):
    """The GTK3BaseButton class."""

    # Define private class attributes.
    _GTK3_BASE_BUTTON_PROPERTIES = GTK3WidgetProperties(
        action_name=None,
        action_target=None,
        always_show_image=False,
        image=None,
        image_position=Gtk.PositionType.LEFT,
        label=None,
        relief=Gtk.ReliefStyle.NORMAL,
        use_underline=False,
    )
    _GTK3_BASE_BUTTON_SIGNALS = [
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
        """Initialize an instance of the Button widget.

        :param label: the text to display on the Button.  Default is an
            ellipsis (...).
        """
        Gtk.Button.__init__(self)
        GTK3BaseDataWidget.__init__(self)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_BASE_BUTTON_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_BASE_BUTTON_SIGNALS}
        )

        self.set_label(label)
        self.show_all()

    # ----- ----- ----- ----- --- Standard widget methods. --- ----- ----- ----- ----- #
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None:
        """Set the properties of the Button.

        :param properties: the WidgetProperties dict with the property values to set for
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

    def do_get_value(self) -> bool | date | float | int | str | None:
        """Return the current value of the GTK3BaseButton."""

    def do_set_value(self, value: bool | date | float | int | str | None) -> None:
        """Set the current value of the GTK3BaseButton."""
