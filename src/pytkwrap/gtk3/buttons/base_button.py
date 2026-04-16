#
#       pytkwrap.gtk3.buttons.base_button.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""The pytkwrap GTK3BaseButton module."""

# Standard Library Imports
from collections.abc import Callable
from typing import Any

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GdkPixbuf, Gtk
from pytkwrap.gtk3.widget import GTK3BaseWidget, GTK3WidgetProperties


def do_make_buttonbox(
    icons: list[str],
    tooltips: list[str],
    callbacks: list[Callable],
    **kwargs: Any,
) -> Gtk.HButtonBox | Gtk.VButtonBox:
    """Create a buttonbox for  views.

    This method creates the base buttonbox used by all  Views.  Use a
    buttonbox for a  View if there are only buttons to be added.

    Parameters
    ----------
    icons: list[str]
    tooltips: list[str]
    callbacks: list[Callable]

    Returns
    -------
    _buttonbox : Gtk.ButtonBox
        The buttonbox populated with GTK3Buttons.
    """
    _height = kwargs.get("height", -1)
    _layout = kwargs.get("layout", Gtk.ButtonBoxStyle.START)
    _orientation = kwargs.get("orientation", "vertical")
    _width = kwargs.get("width", -1)

    _buttonbox = Gtk.HButtonBox() if _orientation == "horizontal" else Gtk.VButtonBox()
    _buttonbox.set_layout(_layout)

    for _idx, __ in enumerate(icons):
        _image = Gtk.Image()
        _icon = GdkPixbuf.Pixbuf.new_from_file_at_size(__, _height, _width)
        _image.set_from_pixbuf(_icon)

        _button = GTK3BaseButton()
        _button.set_image(_image)

        _button.do_set_properties(
            GTK3WidgetProperties(
                height_request=_height,
                width_request=_width,
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


class GTK3BaseButton(Gtk.Button, GTK3BaseWidget):
    """The GTK3BaseButton class."""

    # Define private class attributes.
    _BUTTON_PROPERTIES = GTK3WidgetProperties(
        action_name=None,
        action_target=None,
        always_show_image=False,
        image=None,
        image_position=Gtk.PositionType.LEFT,
        label=None,
        relief=Gtk.ReliefStyle.NORMAL,
        use_underline=False,
    )
    _BUTTON_SIGNALS = [
        "activate",
        # "add", # TODO: The callback for this signal needs to accept two arguments.
        "check-resize",
        "clicked",
        # "remove", # TODO: The callback for this signal needs to accept two arguments.
        # "set-focus-child", # TODO: The callback for this signal needs to accept two
        #  arguments.
    ]
    _DEFAULT_HEIGHT = 30
    _DEFAULT_WIDTH = 200

    def __init__(self, label: str = "...") -> None:
        """Initialize an instance of the Button widget.

        :param label: the text to display on the Button.  Default is an
            ellipsis (...).
        """
        Gtk.Button.__init__(self)
        GTK3BaseWidget.__init__(self)

        # Initialize public instance attributes.
        self.dic_properties.update(self._BUTTON_PROPERTIES)
        self.dic_handler_id.update({_signal: -1 for _signal in self._BUTTON_SIGNALS})

        self.set_label(label)
        self.show_all()

    # ----- ----- Standard widget methods. ----- ----- #
    def do_set_properties(self, properties: GTK3WidgetProperties) -> None:
        """Set the properties of the Button.

        :param properties: the WidgetProperties dict with the property values to set for
            the Button.
        """
        super().do_set_properties(properties)

        self.dic_properties["action_name"] = properties.get("action_name", None)
        self.dic_properties["action_target"] = properties.get("action_target", None)
        self.dic_properties["always_show_image"] = properties.get(
            "always_show_image",
            False,
        )
        self.dic_properties["image"] = properties.get("image", None)
        self.dic_properties["image_position"] = properties.get(
            "image_position",
            Gtk.PositionType.LEFT,
        )
        self.dic_properties["label"] = properties.get("label", None)
        self.dic_properties["relief"] = properties.get("relief", Gtk.ReliefStyle.NORMAL)
        self.dic_properties["use_underline"] = properties.get("use_underline", False)

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
