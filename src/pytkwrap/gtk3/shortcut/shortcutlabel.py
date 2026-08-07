"""The pytkwrap GTK3ShortcutLabel module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.box import GTK3BoxMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3ShortcutLabelMixin(GTK3BoxMixin):
    """Mixin class for GTK3ShortcutLabel."""

    _GTK3_SHORTCUTLABEL_PROPERTIES = GTK3WidgetProperties(
        accelerator=None,
        disabled_text=None,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3ShortcutLabel mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_SHORTCUTLABEL_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3ShortcutLabel-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3ShortcutLabel.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        if self.dic_properties["accelerator"] is not None:
            self.set_accelerator(self.dic_properties["accelerator"])

        if self.dic_properties["disabled_text"] is not None:
            self.set_disabled_text(self.dic_properties["disabled_text"])


class GTK3ShortcutLabel(Gtk.ShortcutLabel, GTK3ShortcutLabelMixin):
    """Wrapper for version 3.0 Gtk.ShortcutLabel."""

    def __init__(self, accelerator: str | None = None) -> None:
        """Initialize an instance of the GTK3ShortcutLabel."""
        Gtk.ShortcutLabel.__init__(self, accelerator=accelerator)
        GTK3ShortcutLabelMixin.__init__(self)
