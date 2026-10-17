"""The pytkwrap GTK3MenuShell module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.exceptions import MenuError, raise_pytkwrap_exception
from pytkwrap.gtk3._libs import Gio, Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.menu.menubuilder import get_gio_menu_model, get_gtk_menu_items
from pytkwrap.gtk3.menu.menuloader import do_build_menu_from_file
from pytkwrap.gtk3.menu.models import GTK3MenuShellMenu
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3MenuShellMixin(GTK3ContainerMixin):
    """Mixin class for GTK3MenuShell.

    Notes
    -----
    GTK3MenuShell passes no widgets to its callback functions.
    """

    _GTK3_MENUSHELL_PROPERTIES = GTK3WidgetProperties(
        take_focus=True,
    )
    _GTK3_MENUSHELL_SIGNALS = [
        "activate-current",
        "cancel",
        "cycle-focus",
        "deactivate",
        "insert",
        "move-current",
        "move-selected",
        "selection-done",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize the menu-shell mixin state."""
        super().__init__(**kwargs)

        # initialize public instance attributes
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_MENUSHELL_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_MENUSHELL_PROPERTIES)

        self.menu_id: str | None = None
        self.menu_model: Gio.MenuModel | None = None

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3MenuShell-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3MenuShell.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_take_focus(self.dic_properties["take_focus"])

    def do_build_menu(
        self,
        menu: GTK3MenuShellMenu | None = None,
        menu_file: str = "",
        method: str = "gio",
    ):
        """Build the GTK3MenuShell menu.

        Parameters
        ----------
        menu : GTK3MenuShellMenu | None
            The GTK3MenuShellMenu to build the menu with.
        menu_file : str
            The path to a file containing the menu structure and attributes.
        method : str
            The builder to use: ``"gio"`` (the default), ``"gtk"``, or
            ``"file"``. The ``"file"`` option loads ``menu_file`` and builds
            a Gio menu model.

        Notes
        -----
        For ``"gio"`` and ``"gtk"``, ``menu`` takes precedence when provided;
        otherwise ``menu_file`` is loaded. The ``"file"`` method always
        requires ``menu_file``.
        """
        _builders = {
            "gio": self._build_gio_menu,
            "gtk": self._build_gtk_menu,
        }

        _build_method = "gio" if method == "file" else method

        if _build_method not in _builders:
            raise_pytkwrap_exception(
                f"Unsupported menu build method {method!r}.",
                error_type=MenuError,
            )

        _menu = self._resolve_menu(menu, menu_file, method)
        _builders[_build_method](_menu)

    @staticmethod
    def _resolve_menu(
        menu: GTK3MenuShellMenu | None,
        menu_file: str,
        method: str,
    ) -> GTK3MenuShellMenu:
        """Return a supplied menu or load the requested menu file.

        Parameters
        ----------
        menu : GTK3MenuShellMenu or None
            Menu structure to return when supplied and ``method`` is not
            ``"file"``.
        menu_file : str
            Path to a TOML file to load when required or when ``menu`` is
            ``None``.
        method : str
            Build method, used to determine whether the file is mandatory.

        Returns
        -------
        GTK3MenuShellMenu
            The supplied menu or the menu loaded from ``menu_file``.

        Notes
        -----
        A non-empty file path is ignored when both a menu is supplied and
        ``method`` is not ``"file"``.
        """
        if method == "file":
            if not menu_file:
                raise_pytkwrap_exception(
                    "menu_file is required when method is 'file'.",
                    error_type=MenuError,
                )

            return do_build_menu_from_file(menu_file)

        if menu is not None:
            return menu

        if menu_file:
            return do_build_menu_from_file(menu_file)

        raise_pytkwrap_exception(
            "A menu or menu_file is required to build a menu.",
            error_type=MenuError,
        )

    def _build_gio_menu(self, menu: GTK3MenuShellMenu) -> None:
        """Build a Gio menu model and bind it to this menu shell.

        Parameters
        ----------
        menu : GTK3MenuShellMenu
            Menu structure used to create the model.
        """
        self.menu_id, self.menu_model = get_gio_menu_model(menu)
        self.bind_model(self.menu_model)

    def _build_gtk_menu(self, menu: GTK3MenuShellMenu) -> None:
        """Build native GTK menu items and append them to this menu shell.

        Parameters
        ----------
        menu : GTK3MenuShellMenu
            Menu structure used to create the items.
        """
        self.menu_id = menu.id
        for _item in get_gtk_menu_items(menu):
            self.append(_item)


class GTK3MenuShell(Gtk.MenuShell, GTK3MenuShellMixin):
    """Wrapper for version 3.0 Gtk.MenuShell."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3MenuShell."""
        Gtk.MenuShell.__init__(self)
        GTK3MenuShellMixin.__init__(self)
