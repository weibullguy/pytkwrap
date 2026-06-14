"""The pytkwrap GTK3Window module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.container.bin import GTK3Bin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3Window(Gtk.Window, GTK3Bin):
    """Wrapper for version 3.0 Gtk.Window."""

    _GTK3_WINDOW_PROPERTIES = GTK3WidgetProperties(
        accept_focus=True,
        application=None,
        attached_to=None,
        decorated=True,
        default_height=-1,
        default_width=-1,
        deletable=True,
        destroy_with_parent=False,
        focus_on_map=True,
        focus_visible=True,
        gravity=Gdk.Gravity.NORTH_WEST,
        has_toplevel_focus=False,
        hide_titlebar_when_maximized=False,
        icon=None,
        icon_name=None,
        mnemonics_visible=True,
        modal=False,
        resizable=True,
        role=None,
        screen=None,
        skip_taskbar_hint=False,
        startup_id=None,
        title="pytkwrap GTK3 window",
        transient_for=None,
        type=Gtk.WindowType.TOPLEVEL,
        type_hint=Gdk.WindowTypeHint.NORMAL,
        urgency_hint=False,
        window_position=Gtk.WindowPosition.NONE,
    )
    _GTK3_WINDOW_SIGNALS = [
        "activate-default",
        "activate-focus",
        "enable-debugging",
        "keys-changed",
        "set-focus",
    ]

    def __init__(self, wtype: Gtk.WindowType = Gtk.WindowType.TOPLEVEL) -> None:
        """Initialize an instance of the GTK3Window.

        Parameters
        ----------
        wtype : Gtk.WindowType
            The window type to construct.
        """
        Gtk.Window.__init__(self, type=wtype)
        GTK3Bin.__init__(self)

        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_WINDOW_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_WINDOW_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3Window-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3Window.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_accept_focus(self.dic_properties["accept_focus"])
        self.set_application(self.dic_properties["application"])
        self.set_attached_to(self.dic_properties["attached_to"])
        self.set_decorated(self.dic_properties["decorated"])
        self.set_deletable(self.dic_properties["deletable"])
        self.set_destroy_with_parent(self.dic_properties["destroy_with_parent"])
        self.set_focus_on_map(self.dic_properties["focus_on_map"])
        self.set_focus_visible(self.dic_properties["focus_visible"])
        self.set_gravity(self.dic_properties["gravity"])
        self.set_hide_titlebar_when_maximized(
            self.dic_properties["hide_titlebar_when_maximized"]
        )
        self.set_icon(self.dic_properties["icon"])
        self.set_icon_name(self.dic_properties["icon_name"])
        self.set_mnemonics_visible(self.dic_properties["mnemonics_visible"])
        self.set_modal(self.dic_properties["modal"])
        self.set_resizable(self.dic_properties["resizable"])

        if self.dic_properties["role"] is not None:
            self.set_role(self.dic_properties["role"])

        self.set_skip_taskbar_hint(self.dic_properties["skip_taskbar_hint"])

        if self.dic_properties["startup_id"] is not None:
            self.set_startup_id(self.dic_properties["startup_id"])

        self.set_title(self.dic_properties["title"])
        self.set_transient_for(self.dic_properties["transient_for"])
        self.set_type_hint(self.dic_properties["type_hint"])
        self.set_urgency_hint(self.dic_properties["urgency_hint"])
        self.set_position(self.dic_properties["window_position"])

        for _property in ["default_height", "default_width"]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )
