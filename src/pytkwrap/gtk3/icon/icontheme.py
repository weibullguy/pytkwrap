"""The pytkwrap GTK3IconTheme module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin


class GTK3IconThemeMixin(GTK3GObjectMixin):
    """Mixin class for GTK3IconTheme.

    Notes
    -----
    GTK3IconTheme passes no widgets to its callback function.
    """

    _GTK3_ICONTHEME_SIGNALS = ["changed"]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3IconTheme mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_ICONTHEME_SIGNALS}
        )


class GTK3IconTheme(Gtk.IconTheme, GTK3IconThemeMixin):
    """Wrapper for version 3.0 Gtk.IconTheme."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3IconTheme."""
        Gtk.IconTheme.__init__(self)
        GTK3IconThemeMixin.__init__(self)

    def do_get_icon(
        self,
        icon_names: list[str],
        size: int,
        flags: Gtk.IconLookupFlags,
        scale: int = 0,
    ) -> Gtk.IconInfo:
        """Return a Gtk.IconInfo object for the icon name(s).

        Parameters
        ----------
        icon_names : list[str]
            A list of icon names to look up.
        size : int
            The desired icon size.
        flags : Gtk.IconLookupFlags
            Flags modifying the behavior of the icon lookup.
        scale : int, optional
            The desired scale factor.  The default is 0.

        Returns
        -------
        A Gtk.IconInfo object for the icon name(s).
        """
        if scale > 0:
            if len(icon_names) > 1:
                return self.choose_icon_for_scale(icon_names, size, scale, flags)
            return self.lookup_icon_for_scale(icon_names[0], size, scale, flags)

        if len(icon_names) > 1:
            return self.choose_icon(icon_names, size, flags)
        return self.lookup_icon(icon_names[0], size, flags)

    @staticmethod
    def do_get_icon_info(icon: Gtk.IconInfo) -> dict[str, bool | int | str | None]:
        """Return a dict of information about the icon.

        Parameters
        ----------
        icon : Gtk.IconInfo
            The icon to get information about.

        Returns
        -------
        A dictionary containing the following keys:
            base_scale : int
            base_size : int
            filename : str
            symbolic : bool
        """
        return {
            "base_scale": icon.get_base_scale(),
            "base_size": icon.get_base_size(),
            "filename": icon.get_filename(),
            "symbolic": icon.is_symbolic(),
        }
