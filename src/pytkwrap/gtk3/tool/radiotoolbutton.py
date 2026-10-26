"""The pytkwrap GTK3RadioToolButton module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.

GTK3 Radio Tool Button Implementation Notes
-------------------------------------------

This module implements `GTK3RadioToolButton` by composing a `Gtk.ToolItem`
containing a native `Gtk.RadioButton` and `Gtk.Label`, rather than subclassing
`Gtk.RadioToolButton` directly. This architecture is required due to critical
defects in PyGObject 3's introspection bindings for `Gtk.RadioToolButton`:

1. **Introspection Type Errors**: `Gtk.RadioToolButton.get_group()` incorrectly
returns lists typed as `[Gtk.RadioButton]`, causing identity and type
assertion failures even when only tool buttons are present.

2. **Constructor & Memory Bugs**: Passing a `group` argument to the constructor
fails to link widgets correctly, while manual linking via `set_group()`
triggers segmentation faults due to improper marshaling of Python lists to
C `GSList` structures.

3. **Visual Fidelity**: Direct subclassing often results in visual artifacts or
requires complex CSS overrides to restore the standard radio (circle) indicator.
Using a native `Gtk.RadioButton` ensures the correct UI appearance automatically.

4. **Deprecation**: `Gtk.RadioToolButton` is deprecated (GTK 3.10+) and removed
in GTK 4. The composition pattern used here aligns with GTK 4's philosophy of
flexible widget composition over rigid specialized classes.

By embedding a standard `Gtk.RadioButton` within a `Gtk.ToolItem`, this
implementation achieves full API compatibility, memory safety, and correct
visual rendering without relying on the broken `RadioToolButton` bindings.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3 import GTK3Image
from pytkwrap.gtk3._libs import GObject, Gtk
from pytkwrap.gtk3.button.radiobutton import GTK3RadioButton
from pytkwrap.gtk3.io.label import GTK3Label
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.tool.toggletoolbutton import GTK3ToggleToolButtonMixin


class GTK3RadioToolButtonMixin(GTK3ToggleToolButtonMixin):
    """Mixin class for GTK3RadioToolButton."""

    _GTK3_RADIOTOOLBUTTON_PROPERTIES = GTK3WidgetProperties(
        group=[],
        icon_name=None,
        icon_widget=None,
        label="",
        label_widget=None,
        use_underline=False,
    )
    _GTK3_RADIOTOOLBUTTON_SIGNALS = ["clicked", "toggled"]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3RadioToolButton mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_RADIOTOOLBUTTON_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_RADIOTOOLBUTTON_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3RadioToolButton-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3RadioToolButton.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        if self._radio_button not in self.dic_properties["group"]:
            self.set_group(self.dic_properties["group"])


class GTK3RadioToolButton(Gtk.ToolItem, GTK3RadioToolButtonMixin):
    """Wrapper for version 3.0 Gtk.RadioToolButton."""

    def __init__(self, group: list | None = None) -> None:
        """Initialize an instance of the GTK3RadioToolButton.

        Parameters
        ----------
        group : list | None
            The group to add the GTK3RadioToolButton to.
        """
        Gtk.ToolItem.__init__(self)
        GTK3RadioToolButtonMixin.__init__(self)

        # TODO: Update this after updating GTK3Box to accept orientation and spacing
        #  in it's __init__ method.
        # Create a STANDARD Gtk.Box to pack the radio button and label.
        self._box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.add(self._box)
        self._box.show()

        # Create a GTK3RadioButton.  This presents the visual of a Gtk.RadioToolButton
        # (filled or unfilled circle).
        self._radio_button = GTK3RadioButton(group=None)
        self._box.pack_start(self._radio_button, False, False, 0)
        self._radio_button.show()

        self.set_group(group)

        # Connect toggled signal to enforce exclusivity.
        self._radio_button.connect("toggled", self._on_toggled)

    def get_active(self) -> bool:
        """Return the active state of the GTK3RadioToolButton.

        Returns
        -------
        The current state of the GTK3RadioToolButton.
        """
        return self._radio_button.get_active()

    def get_group(self) -> list | None:
        """Return the group of the GTK3RadioToolButton.

        Returns
        -------
        A list containing all the GTK3RadioToolButton instances in the same group as
        self.
        """
        return self.dic_properties["group"]

    def get_icon_name(self) -> str:
        """Return the icon name of the GTK3RadioToolButton.

        Returns
        -------
        The name of the icon currently displayed in the GTK3RadioToolButton.
        """
        return self.dic_properties["icon_name"]

    def get_icon_widget(self) -> GTK3Image:
        """Return the icon widget of the GTK3RadioToolButton.

        Returns
        -------
        The GTK3Image widget currently displayed as the icon in the GTK3RadioToolButton.
        """
        return self.dic_properties["icon_widget"]

    def get_label(self) -> str:
        """Return the label of the GTK3RadioToolButton.

        Returns
        -------
        The label text currently displayed in the GTK3RadioToolButton.
        """
        return self.dic_properties["label"]

    def get_label_widget(self) -> GTK3Label:
        """Return the label widget of the GTK3RadioToolButton.

        Returns
        -------
        The GTK3Label widget currently displayed in the GTK3RadioToolButton.
        """
        return self.dic_properties["label_widget"]

    def get_use_underline(self) -> bool:
        """Return the use_underline of the GTK3RadioToolButton.

        Returns
        -------
        Whether the GTK3RadioToolButton label currently uses an underline.
        """
        return self.dic_properties["use_underline"]

    def set_active(self, active: bool) -> None:
        """Set the active state of the GTK3RadioToolButton.

        Parameters
        ----------
        active : bool
            Whether the GTK3RadioToolButton should be active or not.
        """
        return self._radio_button.set_active(active)

    def set_group(self, group: list | None = None) -> None:
        """Set the group of the GTK3RadioToolButton.

        Parameters
        ----------
        group : list | None
            The group to add for the GTK3RadioToolButton instance to or None to
            remove it from the group.
        """
        if group is not None:
            self.dic_properties["group"] = group
            self.dic_properties["group"].append(self._radio_button)

            # Sync with other radio button in the group.
            for _other in group:
                if isinstance(_other, GTK3RadioButton):
                    _other.set_group(self.dic_properties["group"])
        else:
            self.dic_properties["group"] = [self._radio_button]

    def set_icon_name(self, icon_name: str | None) -> None:
        """Set the icon name of the GTK3RadioToolButton.

        Parameters
        ----------
        icon_name : str | None
            The name of the icon in a current icon theme to display in the
            GTK3RadioToolButton.  Pass None to remove the label.
        """
        self.dic_properties["icon_name"] = icon_name
        if self.dic_properties["icon_name"] is not None:
            _icon_widget = GTK3Image(icon_name=self.dic_properties["icon_name"])
            self.set_icon_widget(_icon_widget)

    def set_icon_widget(self, icon_widget: GTK3Image | None) -> None:
        """Set the icon widget of the GTK3RadioToolButton.

        Parameters
        ----------
        icon_widget : GTK3Image | None
            The GTK3Image to display in the GTK3RadioToolButton.  Pass None to remove
            any existing GTK3Image.
        """
        self.dic_properties["icon_widget"] = icon_widget

        if self.dic_properties["icon_widget"] is not None:
            self._box.pack_end(self.dic_properties["icon_widget"], False, False, 0)
            self.dic_properties["icon_name"] = self.dic_properties[
                "icon_widget"
            ].get_icon_name()[0]

    def set_label(self, text: str | None) -> None:
        """Set the label of the GTK3RadioToolButton.

        Parameters
        ----------
        text : str | None
            The text to display in the GTK3RadioToolButton.  Pass None to remove any
            existing label text.
        """
        self.dic_properties["label"] = "" if text is None else text

        if self.dic_properties["label_widget"] is not None:
            self.dic_properties["label_widget"].set_text("" if text is None else text)

    def set_label_widget(self, label_widget: GTK3Label | None) -> None:
        """Set the label widget of the GTK3RadioToolButton.

        Parameters
        ----------
        label_widget : GTK3Label | None
            The GTK3Label to display in the GTK3RadioToolButton.  Pass None to remove
            any existing GTK3Label.
        """
        # Remove any existing GTK3Label.
        if self.dic_properties["label_widget"] is not None:
            self.remove(self.dic_properties["label_widget"])

        self.dic_properties["label_widget"] = label_widget

        # If a GTK3Image was passed, make it the new label widget.
        if self.dic_properties["label_widget"] is not None:
            self._box.pack_end(self.dic_properties["label_widget"], True, True, 0)
            self.dic_properties["label_widget"].show()

    def set_use_underline(self, use_underline: bool) -> None:
        """Set the use_underline of the GTK3RadioToolButton.

        Parameters
        ----------
        use_underline : bool
            Whether to use an underline for the label.
        """
        self.dic_properties["use_underline"] = use_underline
        return self._radio_button.set_use_underline(use_underline)

    def _on_toggled(self, widget: Gtk.ToggleToolButton) -> None:
        """Enforce exclusivity of radio buttons in a group.

        Parameters
        ----------
        widget : Gtk.ToggleToolButton
        """
        if widget.get_active():
            for _other in self.dic_properties["group"]:
                if _other is not widget:
                    _other.handler_block_by_func(self._on_toggled)
                    _other.set_active(False)
                    _other.handler_unblock_by_func(self._on_toggled)

    @GObject.Signal
    def clicked(self):
        """Add the 'clicked' signal."""

    @GObject.Signal
    def toggled(self):
        """Add the 'toggled' signal."""
