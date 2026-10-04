"""The pytkwrap GTK3MenuShell module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Callable, Mapping
from dataclasses import dataclass, field

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gio, Gtk
from pytkwrap.gtk3.container.container import GTK3ContainerMixin
from pytkwrap.gtk3.menu.menuitem import GTK3MenuItem
from pytkwrap.gtk3.mixins import GTK3WidgetProperties

ATTRIBUTE_ACTION = '<attribute name="action">{action}</attribute>'
ATTRIBUTE_ACTION_NAMESPACE = (
    '<attribute name="action_namespace">{action-namespace}</attribute>'
)
ATTRIBUTE_CUSTOM = '<attribute name="custom">{custom}</attribute>'
ATTRIBUTE_DISPLAY_HINT = '<attribute name="display-hint">{display_hint}</attribute>'
ATTRIBUTE_HIDDEN_WHEN = '<attribute name="hidden-when">{hidden_when}</attribute>'
ATTRIBUTE_ICON = '<attribute name="icon">{icon}</attribute>'
ATTRIBUTE_LABEL = (
    '<attribute name="label" translatable="{translatable}">{label}</attribute>'
)
ATTRIBUTE_SUBMENU_ACTION = (
    '<attribute name="submenu-action">{submenu_action}</attribute>'
)
ATTRIBUTE_TARGET = '<attribute name="target">{target}</attribute>'
ATTRIBUTE_TEXT_DIRECTION = (
    '<attribute name="text-direction">{text_direction}</attribute>'
)
ATTRIBUTE_USE_MARKUP = '<attribute name="use-markup">{use_markup}</attribute>'


@dataclass
class GTK3MenuShellAttribute:  # pylint: disable=too-many-instance-attributes
    """The dataclass for GTK3MenuShell attributes."""

    action: str | None = None
    action_namespace: str | None = None
    callback: Callable | None = None
    custom: str | None = None
    display_hint: str | None = None
    hidden_when: str | None = None
    icon: str | None = None
    id: str | None = None
    label: str | None = None
    signal: str | None = None
    submenu_action: str | None = None
    target: str | None = None
    text_direction: str | None = None
    translatable: str = "yes"
    use_markup: bool = False


@dataclass
class GTK3MenuShellItem:
    """The dataclass for GTK3MenuShell items.

    Notes
    -----
    GTK3MenuShellItem can have any of the following attributes:
        * action
        * custom
        * hidden_when
        * icon
        * label
        * submenu_action
        * target
        * translatable
        * use_markup
    """

    attributes: GTK3MenuShellAttribute


@dataclass
class GTK3MenuShellSection:
    """The dataclass for GTK3MenuShell sections.

    Notes
    -----
    A GTK3MenuShellSection can have any of the following attributes:
        * display_hint
        * label
        * text_direction
        * translatable
    """

    children: list = field(default_factory=list)
    attributes: GTK3MenuShellAttribute | None = None


@dataclass
class GTK3MenuShellSubmenu:
    """The dataclass for GTK3MenuShell submenus.

    Notes
    -----
    A GTK3MenuShellSubmenu can have any of the following attributes:
        * icon
        * id
        * label
        * translatable
    """

    attributes: GTK3MenuShellAttribute
    sections: list[GTK3MenuShellSection] = field(default_factory=list)


@dataclass
class GTK3MenuShellMenu:
    """The dataclass for GTK3MenuShell menus."""

    submenus: list[GTK3MenuShellSubmenu]
    id: str | None = None


Node = GTK3MenuShellItem | GTK3MenuShellSubmenu


def get_gio_menu_model(menu: GTK3MenuShellMenu) -> tuple[str, Gio.MenuModel]:
    """Build a Gio.MenuModel from the given GTK3MenuShellMenu structure..

    Parameters
    ----------
    menu : GTK3MenuShellMenu
        The GTK3MenuShellMenu with the menu structure.

    Returns
    -------
    _menu_id, _model : tuple(str, Gio.MenuModel)
        The ID and the Gio.MenuModel of the menu that was built.
    """
    _menu_id = menu.id if menu.id else ""
    _menu_ui = (
        f"""<?xml version="1.0" encoding="UTF-8"?><interface><menu id="{_menu_id}">"""
    )

    for _submenu in menu.submenus:
        _menu_ui = _do_add_submenu(_submenu, _menu_ui)
    _menu_ui = f"""{_menu_ui}</menu></interface>"""

    _builder = Gtk.Builder.new_from_string(_menu_ui, -1)
    _model = _builder.get_object(_menu_id)

    return _menu_id, _model


def _do_add_attributes(
    attributes: GTK3MenuShellAttribute,
    menu_ui: str,
) -> str:
    """Add attributes to a GTK3Menu submenu, section, or item.

    Parameters
    ----------
    attributes : GTK3MenuShellAttribute
        The attributes to add and their values.
    menu_ui : str
        The existing menu XML string.

    Returns
    -------
    str
        The menu XML string with the attribute elements added.
    """
    _menu_ui = menu_ui

    if attributes.action is not None:
        _menu_ui = f"""{_menu_ui}{ATTRIBUTE_ACTION.format(action=attributes.action)}"""

    if attributes.action_namespace is not None:
        _menu_ui = f"""{_menu_ui}{ATTRIBUTE_ACTION_NAMESPACE.format(
            action_namespace=attributes.action_namespace)}"""

    if attributes.custom is not None:
        _menu_ui = f"""{_menu_ui}{ATTRIBUTE_CUSTOM.format(custom=attributes.custom)}"""

    if attributes.display_hint is not None:
        _menu_ui = f"""{_menu_ui}{ATTRIBUTE_DISPLAY_HINT.format(
            display_hint=attributes.display_hint)}"""

    if attributes.hidden_when is not None:
        _menu_ui = f"""{_menu_ui}{ATTRIBUTE_HIDDEN_WHEN.format(
            hidden_when=attributes.hidden_when)}"""

    if attributes.icon is not None:
        _menu_ui = f"""{_menu_ui}{ATTRIBUTE_ICON.format(icon=attributes.icon)}"""

    if attributes.label is not None:
        _menu_ui = f"""{_menu_ui}{ATTRIBUTE_LABEL.format(
            translatable=attributes.translatable, label=attributes.label,)}"""

    if attributes.submenu_action is not None:
        _menu_ui = f"""{_menu_ui}{ATTRIBUTE_SUBMENU_ACTION.format(
            submenu_action=attributes.submenu_action)}"""

    if attributes.target is not None:
        _menu_ui = f"""{_menu_ui}{ATTRIBUTE_TARGET.format(target=attributes.target)}"""

    if attributes.text_direction is not None:
        _menu_ui = f"""{_menu_ui}{ATTRIBUTE_TEXT_DIRECTION.format(
            text_direction=attributes.text_direction)}"""

    if attributes.use_markup is not None:
        _menu_ui = f"""{_menu_ui}{ATTRIBUTE_USE_MARKUP.format(
            use_markup=attributes.use_markup)}"""

    return _menu_ui


def _do_add_node(
    node: Node,
    menu_ui: str,
) -> str:
    """Add items to a GTK3Menu section.

    Parameters
    ----------
    node : Node
        A Node containing the item to add to the menu.
    menu_ui : str
        The existing menu XML string.

    Returns
    -------
    str
        The menu XML string with the node elements added.
    """
    if isinstance(node, GTK3MenuShellSubmenu):
        return _do_add_submenu(node, menu_ui)

    _menu_ui = f"""{menu_ui}<item>"""
    if node.attributes:
        _menu_ui = _do_add_attributes(node.attributes, _menu_ui)

    return f"""{_menu_ui}</item>"""


def _do_add_section(
    section: GTK3MenuShellSection,
    menu_ui: str,
) -> str:
    """Add a section to the GTK3Menu.

    Parameters
    ----------
    section : GTK3MenuShellSection
        The GTK3MenuShellSection to add to the menu.
    menu_ui : str
        The existing menu XML string.

    Returns
    -------
    str
        The menu XML string with the section elements added.
    """
    _menu_ui = f"""{menu_ui}<section>"""
    if section.attributes:
        _menu_ui = _do_add_attributes(section.attributes, _menu_ui)

    for _node in section.children:
        _menu_ui = _do_add_node(_node, _menu_ui)
    return f"""{_menu_ui}</section>"""


def _do_add_submenu(submenu: GTK3MenuShellSubmenu, menu_ui: str) -> str:
    """Add a submenu to the GTK3Menu section.

    Parameters
    ----------
    submenu : GTK3MenuShellSubmenu
        The GTK3MenuShellSubmenu to add to the menu.
    menu_ui : str
        The existing menu XML string.

    Returns
    -------
    str
        The menu XML string with the submenu elements added.
    """
    _submenu_id = submenu.attributes.id if submenu.attributes.id else ""

    _menu_ui = f"""{menu_ui}<submenu id="{_submenu_id}">"""
    if submenu.attributes:
        _menu_ui = _do_add_attributes(submenu.attributes, _menu_ui)

    for _section in submenu.sections:
        _menu_ui = _do_add_section(_section, _menu_ui)
    return f"""{_menu_ui}</submenu>"""


def get_gtk_menu_items(menu: GTK3MenuShellMenu) -> list[GTK3MenuItem]:
    """Build list of GTK3MenuItems using the passed GTK3MenuShellMenu.

    Parameters
    ----------
    menu : GTK3MenuShellMenu
        The GTK3MenuShellMenu with the structure to build the menu from.

    Returns
    -------
    A list of the top level GTK3MenuItems to add to a menu or menubar.
    """
    _menu_items = []
    for _submenu in menu.submenus:
        _item = GTK3MenuItem(label=_submenu.attributes.label)
        _menu = Gtk.Menu()
        _item.set_submenu(_menu)

        for _section in _submenu.sections:
            for _node in _section.children:
                _leaf_item = GTK3MenuItem(label=_node.attributes.label)
                if _node.attributes.callback is not None:
                    _leaf_item.connect(
                        _node.attributes.signal,
                        _node.attributes.callback,
                    )
                _menu.append(_leaf_item)

        _menu_items.append(_item)

    return _menu_items


class GTK3MenuShellMixin(GTK3ContainerMixin):
    """Mixin class for GTK3MenuShell."""

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
        """Initialize an instance of the GTK3MenuShell mixin."""
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

    def do_build_menu(self, menu: GTK3MenuShellMenu, method: str = "gio"):
        """Build the GTK3MenuShell menu.

        Parameters
        ----------
        menu : GTK3MenuShellMenu
            The GTK3MenuShellMenu to build the menu with.
        method : str
            The method used to build the menu.
        """
        if method == "gio":
            self.menu_id, self.menu_model = get_gio_menu_model(menu)
            self.bind_model(self.menu_model)

        if method == "gtk":
            for _item in get_gtk_menu_items(menu):
                self.append(_item)


class GTK3MenuShell(Gtk.MenuShell, GTK3MenuShellMixin):
    """Wrapper for version 3.0 Gtk.MenuShell."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3MenuShell."""
        Gtk.MenuShell.__init__(self)
        GTK3MenuShellMixin.__init__(self)
