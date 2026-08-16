"""The pytkwrap GTK3FileFilter module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Callable

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin


class GTK3FileFilter(Gtk.FileFilter, GTK3GObjectMixin):
    """Wrapper for version 3.0 Gtk.FileFilter."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3FileFilter."""
        Gtk.FileFilter.__init__(self)
        GTK3GObjectMixin.__init__(self)

    def do_set_filter(
        self,
        *data: object | None,
        mime_types: list[str] | None = None,
        patterns: list[str] | None = None,
        needed: Gtk.FileFilterFlags | None = None,
        func: Callable | None = None,
    ):
        """Set the filter ruleset for this file filter.

        This method sets the filter for this file filter to use.  You can set a mime
        type, a shell style glob pattern, or a custom filter function.  The order of
        preference for setting the filter is: mime type, pattern, custom filter.
        Thus, if you pass in a mime type and a pattern, the filter will be set using
        the mime type.

        Parameters
        ----------
        *data : object | None
            Data to pass to the custom filter function.  Defaults to None.
        mime_types : list[str] | None
            A list of mime types to filter on.  Defaults to None.
        patterns : list[str] | None
            A list of shell style glob patterns to use as the filter rule.  Defaults to
            None.
        needed : Gtk.FileFilterFlags | None
            Bitfield of flags indicating the information needed by the custom filter.
            Defaults to None.
        func : Gtk.FileFilterFunc | None
            The callback function to use for filtering.  If the function returns
            True, the file(s) will be displayed.  Defaults to None.
        """
        if mime_types is not None:
            for _mime_type in mime_types:
                self.add_mime_type(_mime_type)
        elif patterns is not None:
            for _pattern in patterns:
                self.add_pattern(_pattern)
        elif func is not None:
            self.add_custom(needed, func, *data)
