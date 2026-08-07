"""The pytkwrap GTK3TextMark module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin, GTK3WidgetProperties


class GTK3TextMarkMixin(GTK3GObjectMixin):
    """Mixin class for GTK3TextMark."""

    _GTK3_TEXTMARK_PROPERTIES = GTK3WidgetProperties(
        left_gravity=False,
        name=None,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3TextMark."""
        super().__init__(**kwargs)

        self.dic_properties = dict(self._GTK3_TEXTMARK_PROPERTIES)


class GTK3TextMark(Gtk.TextMark, GTK3TextMarkMixin):
    """Wrapper for version 3.0 Gtk.TextMark."""

    def __init__(self, name: str | None = None, left_gravity: bool = False) -> None:
        """Initialize an instance of the GTK3TextMark.

        Parameters
        ----------
        name : str | None
            The name of the text mark.
        left_gravity : bool, optional
            Whether the text mark should have left-gravity.
        """
        Gtk.TextMark.__init__(self, name=name, left_gravity=left_gravity)
        GTK3TextMarkMixin.__init__(self)

        self.dic_properties["left_gravity"] = left_gravity
        self.dic_properties["name"] = name
