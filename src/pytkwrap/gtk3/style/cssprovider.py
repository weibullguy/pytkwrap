"""The pytkwrap GTK3CssProvider module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gio, Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin


class GTK3CssProviderMixin(GTK3GObjectMixin):
    """Mixin class for GTK3CssProvider.

    Notes
    -----
    GTK3CssProvider passes no widgets to its callback functions.
    """

    _GTK3_CSSPROVIDER_SIGNALS = [
        "parsing-error",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3CssProvider mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_CSSPROVIDER_SIGNALS}
        )

    def do_load_styling(
        self,
        data: str | None = None,
        file: Gio.File | None = None,
        path: str | None = None,
        resource: str | None = None,
    ) -> bool | None:
        """Load styling information into the provider.

        Parameters
        ----------
        data : str | None, optional
            A byte-string containing the styling information.
        file : Gio.File | None, optional
            The Gio.File pointing to the file to load.
        path : str | None, optional
            The path to the filename to load.
        resource : str | None, optional
            The Gio.Resource path to load.

        Returns
        -------
        True or None.  Only when loading from data will this method return None on
        success.

        The return value is deprecated and False will only be returned
        for backwards compatibility reasons if an error is not None and a loading error
        occurred.  To track errors while loading CSS, connect to the `::parsing-error``
        signal.
        """
        if data is not None:
            return self.load_from_data(data)

        if file is not None:
            return self.load_from_file(file)

        if path is not None:
            return self.load_from_path(path)

        if resource is not None:
            return self.load_from_resource(resource)

        return True


class GTK3CssProvider(Gtk.CssProvider, GTK3CssProviderMixin):
    """Wrapper for version 3.0 Gtk.CssProvider."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3CssProvider."""
        Gtk.CssProvider.__init__(self)
        GTK3CssProviderMixin.__init__(self)
