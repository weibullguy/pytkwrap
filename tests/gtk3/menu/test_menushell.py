"""Test module for the GTK3MenuShell class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.exceptions import MenuError

# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gio, Gtk
from pytkwrap.gtk3.menu import (
    GTK3MenuShell,
    GTK3MenuShellAttribute,
    GTK3MenuShellItem,
    GTK3MenuShellMenu,
    GTK3MenuShellSection,
    GTK3MenuShellSubmenu,
    do_build_menu_from_file,
    get_gio_menu_model,
)
from pytkwrap.gtk3.menu.menushell import GTK3MenuShellMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)
from tests.gtk3.container.constants import (
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
)
from tests.gtk3.menu.constants import (
    EXPECTED_MENUSHELL_HANDLER_IDS,
    EXPECTED_MENUSHELL_METHODS,
    EXPECTED_MENUSHELL_PROPERTIES,
    MENU_UI,
)


def on_open(_menu_item):
    """Callback referenced by the menu_ui.toml test fixture."""


@pytest.mark.unit
def test_missing_file_menu_logs_and_raises_menu_error(logged_errors):
    """A missing menu file path should log and raise MenuError."""
    with pytest.raises(MenuError, match="menu_file is required"):
        GTK3MenuShellMixin._resolve_menu(None, "", "file")

    assert logged_errors == ["menu_file is required when method is 'file'."]


@pytest.mark.usefixtures("skip_if_not_isolated")
@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3MenuShell(BaseGTK3GObjectTests):
    """Test class for the GTK3MenuShell class."""

    widget_class = GTK3MenuShell
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_default_height = -1
    expected_default_width = -1
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_MENUSHELL_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_MENUSHELL_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_MENUSHELL_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("take_focus")

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                take_focus=False,
            )
        )

        assert not dut.get_property("take_focus")
        assert not dut.get_take_focus()

    @pytest.mark.unit
    def test_do_build_gio_menu(self):
        """Should build a Gio.MenuModel with the expected structure."""
        dut = self.make_dut()
        dut.do_build_menu(MENU_UI)

        assert dut.menu_id == "menubar"
        assert isinstance(dut.menu_model, Gio.MenuModel)

    @pytest.mark.unit
    def test_gio_menu_preserves_attribute_values(self):
        """Should preserve menu attribute values in the Gio model."""
        _menu = GTK3MenuShellMenu(
            id='menu&"root',
            submenus=[
                GTK3MenuShellSubmenu(
                    attributes=GTK3MenuShellAttribute(
                        action_namespace="app",
                        label='File & "Open"',
                    ),
                    sections=[
                        GTK3MenuShellSection(
                            attributes=GTK3MenuShellAttribute(
                                display_hint="horizontal-buttons",
                            ),
                            children=[
                                GTK3MenuShellItem(
                                    attributes=GTK3MenuShellAttribute(
                                        action="app.open",
                                        custom="data & <value>",
                                        icon="document-open",
                                        label="Open <recent>",
                                        target="'A value' ",
                                        use_markup=True,
                                    )
                                )
                            ],
                        )
                    ],
                )
            ],
        )

        _menu_id, _model = get_gio_menu_model(_menu)

        assert _menu_id == 'menu&"root'
        assert isinstance(_model, Gio.MenuModel)
        _root_item = _model.get_item_attribute_value(0, "label", None)
        assert _root_item.get_string() == 'File & "Open"'
        assert (
            _model.get_item_attribute_value(0, "action-namespace", None).get_string()
            == "app"
        )
        _submenu = _model.get_item_link(0, Gio.MENU_LINK_SUBMENU)
        assert (
            _submenu.get_item_attribute_value(0, "display-hint", None).get_string()
            == "horizontal-buttons"
        )
        _section = _submenu.get_item_link(0, Gio.MENU_LINK_SECTION)
        _menu_item = _section.get_item_attribute_value(0, "label", None)
        assert _menu_item.get_string() == "Open <recent>"
        assert _section.get_item_attribute_value(0, "action", None).get_string() == (
            "app.open"
        )
        assert _section.get_item_attribute_value(0, "custom", None).get_string() == (
            "data & <value>"
        )
        assert _section.get_item_attribute_value(0, "icon", None).get_string() == (
            "document-open"
        )
        assert _section.get_item_attribute_value(0, "target", None).get_string() == (
            "'A value' "
        )
        assert _section.get_item_attribute_value(
            0, "use-markup", None
        ).get_string() == ("true")

    @pytest.mark.unit
    def test_do_build_gtk_menu(self):
        """Should build a Gtk.Menu with the expected structure."""
        dut = self.make_dut()
        dut.do_build_menu(MENU_UI, method="gtk")

        assert dut.menu_id == "menubar"
        assert isinstance(dut.get_children()[0], Gtk.MenuItem)
        assert dut.get_children()[0].get_label() == "File"
        assert isinstance(dut.get_children()[1], Gtk.MenuItem)
        assert dut.get_children()[1].get_label() == "Edit"
        assert isinstance(dut.get_children()[2], Gtk.MenuItem)
        assert dut.get_children()[2].get_label() == "View"
        _file_menu = dut.get_children()[0].get_submenu()
        _open_item = _file_menu.get_children()[2]
        assert _open_item.get_label() == "Open"
        _open_menu = _open_item.get_submenu()
        assert _open_menu.get_children()[0].get_label() == "Recent"

    @pytest.mark.unit
    def test_do_build_menu_from_toml_file(self):
        """Should build a Gio.MenuModel from a TOML file with the expected structure."""
        _menu = do_build_menu_from_file("examples/gtk3/menu/menu_ui.toml")
        _callback = _menu.submenus[0].sections[0].children[0].attributes.callback
        assert _callback is on_open

        dut = self.make_dut()
        dut.do_build_menu(menu_file="examples/gtk3/menu/menu_ui.toml", method="file")

        assert dut.menu_id == "menubar"
        assert isinstance(dut.menu_model, Gio.MenuModel)
