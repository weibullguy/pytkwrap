"""The pytkwrap GTK3Tooltip module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import GdkPixbuf, Gio, Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin


class GTK3TooltipMixin(GTK3GObjectMixin):
    """Mixin for GTK3Tooltip."""

    def do_set_icon(
        self,
        icon: GdkPixbuf.Pixbuf | None,
        gicon: Gio.Icon | None,
        icon_name: str | None,
        icon_size: int,
    ) -> None:
        """Set the icon for the tooltip.

        Parameters
        ----------
        icon : GdkPixbuf.Pixbuf | None
            The icon to set.
        gicon : Gio.Icon | None
            The GIcon to set.
        icon_name : str | None
            The name of the icon to set.
        icon_size : int
            The size of the icon to set.
        """
        if icon is not None:
            self.set_icon(icon)

        if gicon is not None:
            self.set_icon_from_gicon(gicon, icon_size)

        if icon_name is not None:
            self.set_icon_from_icon_name(icon_name, icon_size)

    def do_set_tooltip(self, tooltip: str | None, markup: bool) -> None:
        """Set the tooltip text.

        Parameters
        ----------
        tooltip : str
            The tooltip text to set.
        markup : bool
            Whether the tooltip text is markup or plain text.
        """
        if markup:
            self.set_markup(tooltip)
        else:
            self.set_text(tooltip)


class GTK3Tooltip(Gtk.Tooltip, GTK3TooltipMixin):
    """Wrapper for version 3.0 Gtk.Tooltip."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Tooltip."""
        Gtk.Tooltip.__init__(self)
        GTK3TooltipMixin.__init__(self)


def do_construct_tooltip(
    tooltip: str | None,
    markup: bool,
    icon: GdkPixbuf.Pixbuf | None,
    gicon: Gio.Icon | None,
    icon_name: str | None,
    icon_size: int,
) -> GTK3Tooltip:
    """Create a new tooltip for the given widget.

    Parameters
    ----------
    tooltip : str | None
        The tooltip text to set.
    markup : bool
        Whether the tooltip text is markup or plain text.
    icon : GdkPixbuf.Pixbuf | None
        The icon to set.
    gicon : Gio.Icon | None
        The GIcon to set.
    icon_name : str | None
        The name of the icon to set.
    icon_size : int
        The size of the icon to set.

    Returns
    -------
    GTK3Tooltip
        The newly created tooltip.
    """
    _tooltip = GTK3Tooltip()
    _tooltip.do_set_tooltip(tooltip, markup)
    _tooltip.do_set_icon(icon, gicon, icon_name, icon_size)

    return _tooltip
