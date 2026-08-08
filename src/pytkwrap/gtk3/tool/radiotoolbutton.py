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
from pytkwrap.gtk3._libs import GObject, Gtk
from pytkwrap.gtk3.button.radiobutton import GTK3RadioButton
from pytkwrap.gtk3.io.label import GTK3Label
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.tool.toggletoolbutton import GTK3ToggleToolButtonMixin


class GTK3RadioToolButtonMixin(GTK3ToggleToolButtonMixin):
    """Mixin class for GTK3RadioToolButton."""

    _GTK3_RADIOTOOLBUTTON_PROPERTIES = GTK3WidgetProperties(
        group=None,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3RadioToolButton mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
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

        self._group = []

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

        # Create a GTK3Label.  This presents the text of the Gtk.RadioToolButton.
        self._label = GTK3Label()
        self._box.pack_end(self._label, True, True, 0)
        self._label.show()

        # Handle grouping logic manually.
        if group is not None:
            self._group = group
            self._group.append(self)
            # Sync with other radio button in the group.
            for _other in group:
                if isinstance(_other, GTK3RadioToolButton):
                    self._radio_button.set_group([_other._radio_button])
        else:
            self._group = [self]

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
        return self._group

    def get_icon_name(self) -> None:
        """Return the icon name of the GTK3RadioToolButton."""

    def get_icon_widget(self) -> None:
        """Return the icon widget of the GTK3RadioToolButton."""

    def get_label(self) -> str:
        """Return the label of the GTK3RadioToolButton.

        Returns
        -------
        The label text currently displayed in the GTK3RadioToolButton.
        """
        return self._radio_button.get_label()

    def get_label_widget(self) -> GTK3Label:
        """Return the label widget of the GTK3RadioToolButton.

        Returns
        -------
        The GTK3Label widget currently displayed in the GTK3RadioToolButton.
        """
        return self._label

    def get_use_underline(self) -> bool:
        """Return the use_underline of the GTK3RadioToolButton.

        Returns
        -------
        Whether the GTK3RadioToolButton label currently uses an underline.
        """
        return self._radio_button.get_use_underline()

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
            self._group = group
            self._group.append(self)

            # Sync with other radio button in the group.
            for _other in group:
                if isinstance(_other, GTK3RadioToolButton):
                    self._radio_button.set_group(
                        [_other._radio_button]  # pylint: disable=protected-access
                    )
                else:
                    self._group = [self]

    def set_icon_name(self, icon_name: str) -> None:
        """Set the icon name of the GTK3RadioToolButton."""

    def set_icon_widget(self, icon_widget: Gtk.Widget) -> None:
        """Set the icon widget of the GTK3RadioToolButton."""

    def set_label(self, text: str) -> None:
        """Set the label of the GTK3RadioToolButton.

        Parameters
        ----------
        text : str
            The text to display in the GTK3RadioToolButton.
        """
        if text is None:
            return self._label.set_text("")
        return self._label.set_text(text)

    def set_label_widget(self, label_widget: Gtk.Widget) -> None:
        """Set the label widget of the GTK3RadioToolButton.

        Parameters
        ----------
        label_widget : Gtk.Widget
            The widget to display in the GTK3RadioToolButton.
        """
        if label_widget is not None:
            self.remove(self._label)
            self._label = label_widget
            self.add(self._label)

    def set_use_underline(self, use_underline: bool) -> None:
        """Set the use_underline of the GTK3RadioToolButton.

        Parameters
        ----------
        use_underline : bool
            Whether to use an underline for the label.
        """
        return self._radio_button.set_use_underline(use_underline)

    def _on_toggled(self, widget: Gtk.ToggleToolButton) -> None:
        """Enforce exclusivity of radio buttons in a group.

        Parameters
        ----------
        widget : Gtk.ToggleToolButton
        """
        if widget.get_active():
            for _other in self._group:
                if _other is not widget:
                    _other.handler_block_by_func(self._on_toggled)
                    _other.set_active(False)
                    _other.handler_unblock_by_func(self._on_toggled)

    @classmethod
    def create_group(cls, count: int = 2) -> list["GTK3RadioToolButton"]:
        """Create a group of radio tool buttons.

        This method is a convenience factory method designed to simplify the creation
        of a set of mutually exclusive buttons.

        Its specific purposes are:

        #. Bulk Instantiation: It automates the creation of N buttons in a loop,
        saving you from writing repetitive instantiation code.
        #. Shared State Initialization: It ensures every button in the set receives
        the same list reference (self._group) during initialization. This shared list
        is critical because the _on_toggled handler iterates over this specific list to
        deactivate other buttons.
        #. Encapsulation: It keeps the internal grouping logic (the list management)
        contained within the class, so the rest of your application just receives a
        ready-to-use list of buttons.

        Parameters
        ----------
        count : int
            The number of GTK3RadioToolButtons to create.

        Returns
        -------
        The list of GTK3RadioToolButtons created.
        """
        group: list[GTK3RadioToolButton] = []
        for _ in range(count):
            btn = cls(group=group)  # Pass the list as it grows.
            group.append(btn)
        return group

    @GObject.Signal
    def clicked(self):
        """Add the 'clicked' signal."""

    @GObject.Signal
    def toggled(self):
        """Add the 'toggled' signal."""
