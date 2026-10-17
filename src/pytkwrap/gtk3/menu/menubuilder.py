"""Build GTK3 menu models and widgets from menu data structures."""

# Standard Library Imports
import gettext

# pytkwrap Package Imports
from pytkwrap.exceptions import MenuError, raise_pytkwrap_exception
from pytkwrap.gtk3._libs import Gio, GLib, Gtk
from pytkwrap.gtk3.menu.menuitem import GTK3MenuItem
from pytkwrap.gtk3.menu.models import (
    GTK3MenuShellAttribute,
    GTK3MenuShellItem,
    GTK3MenuShellMenu,
    GTK3MenuShellSection,
    GTK3MenuShellSubmenu,
    Node,
)

_GIO_ATTRIBUTE_NAMES = {
    "action": "action",
    "action_namespace": "action-namespace",
    "custom": "custom",
    "display_hint": "display-hint",
    "hidden_when": "hidden-when",
    "icon": "icon",
    "label": "label",
    "submenu_action": "submenu-action",
    "target": "target",
    "text_direction": "text-direction",
    "use_markup": "use-markup",
}


def _set_gio_attributes(
    item: Gio.MenuItem,
    attributes: GTK3MenuShellAttribute,
) -> None:
    """Set the attributes on a Gio menu item.

    Parameters
    ----------
    item : Gio.MenuItem
        Gio menu item receiving the attributes.
    attributes : GTK3MenuShellAttribute
        Attributes to copy. Values that are ``None`` are omitted.

    Notes
    -----
    Gio menu attributes are string variants, as they are when parsed from
    Gtk.Builder menu XML. Labels marked translatable are translated using
    the active gettext domain.
    """
    for _field, _gio_name in _GIO_ATTRIBUTE_NAMES.items():
        _value = getattr(attributes, _field)
        if _value is None:
            continue

        if _field == "label" and attributes.translatable == "yes":
            _value = gettext.gettext(_value)

        _value_string = str(_value).lower() if isinstance(_value, bool) else str(_value)
        item.set_attribute_value(_gio_name, GLib.Variant.new_string(_value_string))


def _build_gio_node(node: Node) -> Gio.MenuItem:
    """Build a Gio menu item from an item or submenu node.

    Parameters
    ----------
    node : Node
        Item or submenu definition to render.

    Returns
    -------
    Gio.MenuItem
        The item, with a linked submenu model when ``node`` is a submenu.
    """
    _item = Gio.MenuItem.new(None, None)
    _set_gio_attributes(_item, node.attributes)

    if isinstance(node, GTK3MenuShellSubmenu):
        _submenu = Gio.Menu()
        for _section in node.sections:
            _section_item = Gio.MenuItem.new(None, None)

            if _section.attributes is not None:
                _set_gio_attributes(_section_item, _section.attributes)

            _section_model = Gio.Menu()
            for _child in _section.children:
                _section_model.append_item(_build_gio_node(_child))

            _section_item.set_link(Gio.MENU_LINK_SECTION, _section_model)
            _submenu.append_item(_section_item)

        _item.set_link(Gio.MENU_LINK_SUBMENU, _submenu)

    return _item


def get_gio_menu_model(menu: GTK3MenuShellMenu) -> tuple[str, Gio.MenuModel]:
    """Build a Gio.MenuModel directly from a GTK3MenuShellMenu structure.

    Parameters
    ----------
    menu : GTK3MenuShellMenu
        The menu structure to build.

    Returns
    -------
    tuple[str, Gio.MenuModel]
        The menu ID and its Gio model.

    Notes
    -----
    The model is constructed through Gio's menu APIs rather than serialized
    through XML, so attribute values are passed as data and not interpreted
    as markup.
    """
    _menu_id = menu.id or ""
    _menu_model = Gio.Menu()

    for _submenu in menu.submenus:
        _menu_model.append_item(_build_gio_node(_submenu))

    return _menu_id, _menu_model


def _connect_gtk_callback(item: GTK3MenuItem, node: GTK3MenuShellItem) -> None:
    """Connect a menu item's configured callback to its signal.

    Parameters
    ----------
    item : GTK3MenuItem
        GTK menu item receiving the signal connection.
    node : GTK3MenuShellItem
        Menu node containing the callback and signal configuration.
    """
    if node.attributes.callback is None:
        return

    if node.attributes.signal is None:
        raise_pytkwrap_exception(
            f"Menu item {node.attributes.label!r} has a callback but no signal.",
            error_type=MenuError,
        )

    try:
        item.connect(node.attributes.signal, node.attributes.callback)
    except TypeError as exc:
        raise_pytkwrap_exception(
            f"Could not connect signal {node.attributes.signal!r} for menu item "
            f"{node.attributes.label!r}.",
            cause=exc,
            error_type=MenuError,
        )


def _append_gtk_section(menu: Gtk.Menu, section: GTK3MenuShellSection) -> None:
    """Append every child in a section to a GTK menu.

    Parameters
    ----------
    menu : Gtk.Menu
        GTK menu receiving the child items.
    section : GTK3MenuShellSection
        Section whose child nodes are rendered.
    """
    for _child in section.children:
        menu.append(_build_gtk_node(_child))


def _build_gtk_submenu(node: GTK3MenuShellSubmenu) -> Gtk.Menu:
    """Build a GTK menu from a submenu node.

    Parameters
    ----------
    node : GTK3MenuShellSubmenu
        Submenu definition to render.

    Returns
    -------
    Gtk.Menu
        The rendered submenu and its items.
    """
    _submenu = Gtk.Menu()

    for _section in node.sections:
        _append_gtk_section(_submenu, _section)

    return _submenu


def _build_gtk_node(node: Node) -> GTK3MenuItem:
    """Build a GTK menu item from a node.

    Parameters
    ----------
    node : Node
        Item or submenu definition to render.

    Returns
    -------
    GTK3MenuItem
        The rendered menu item.
    """
    _item = GTK3MenuItem(label=node.attributes.label)

    if isinstance(node, GTK3MenuShellSubmenu):
        _item.set_submenu(_build_gtk_submenu(node))
    else:
        _connect_gtk_callback(_item, node)

    return _item


def get_gtk_menu_items(menu: GTK3MenuShellMenu) -> list[GTK3MenuItem]:
    """Build GTK3MenuItems from the menu tree.

    Parameters
    ----------
    menu : GTK3MenuShellMenu
        The menu structure to render.

    Returns
    -------
    list[GTK3MenuItem]
        The top-level items to append to a menu shell.
    """
    return [_build_gtk_node(_submenu) for _submenu in menu.submenus]
