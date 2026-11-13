"""The pytkwrap GTK3RadioButton module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

from __future__ import annotations

# Standard Library Imports
from collections.abc import Mapping
from typing import TYPE_CHECKING

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.button.checkbutton import GTK3CheckButtonMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties

if TYPE_CHECKING:
    # pytkwrap Local Imports
    from ._protocols import _RadioButtonHost


class GTK3RadioButtonMixin(GTK3CheckButtonMixin):
    """Mixin for GTK3RadioButton.

    Attributes
    ----------
    _DEFAULT_HEIGHT : int
        The default height of the GTK3RadioButton.
    _DEFAULT_WIDTH : int
        The default width of the GTK3RadioButton.
    _GTK3_RADIOBUTTON_PROPERTIES : GTK3WidgetProperties
        GTK3RadioButton-specific properties.
    _GTK3_RADIOBUTTON_SIGNALS : list[str]
        List of GTK3RadioButton-specific signals.

    Notes
    -----
    The following Gtk.RadioButton methods are not wrapped in a convenience layer,
    but may be called directly:

        * set_group(group)

    Refer to https://lazka.github.io/pgi-docs/#Gtk-3.0/classes/RadioButton.html for
    details on these methods.
    """

    # Define private class attributes.
    _DEFAULT_HEIGHT = 40
    _DEFAULT_WIDTH = 200
    _GTK3_RADIOBUTTON_PROPERTIES = GTK3WidgetProperties(
        group=None,
    )
    _GTK3_RADIOBUTTON_SIGNALS = [
        "group-changed",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3RadioButton mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_RADIOBUTTON_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_RADIOBUTTON_SIGNALS}
        )

    def do_set_properties(
        self: _RadioButtonHost,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the properties of the GTK3RadioButton.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3RadioButton.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)  # type: ignore[safe-super] # ty: ignore[invalid-super-argument] # pylint: disable=line-too-long

        self.join_group(self.dic_properties["group"])

    @property
    def group(self: _RadioButtonHost) -> list[Gtk.RadioButton]:
        """Get the list of GTK3RadioButtons in the same group as self.

        Returns
        -------
        list[Gtk.RadioButton]
            The list of GTK3RadioButtons belonging to the same group as self.
        """
        return self.get_group()


class GTK3RadioButton(Gtk.RadioButton, GTK3RadioButtonMixin):
    """Wrapper for version 3.0 Gtk.RadioButton."""

    def __init__(
        self,
        label: str = "...",
        group: Gtk.RadioButton | None = None,
    ) -> None:
        """Initialize an instance of the GTK3RadioButton widget.

        Parameters
        ----------
        label : str
            The text to display in the GTK3RadioButton label.  The default value is
            an ellipsis (...).
        group : Gtk.RadioButton | None
            The group to which the GTK3RadioButton belongs.
        """
        Gtk.RadioButton.__init__(self, label=label)
        GTK3RadioButtonMixin.__init__(self)

        self.dic_properties["label"] = label
        self.join_group(group)
