"""Test module for the GTK3RecentChooserMenu class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.menu import GTK3RecentChooserMenu
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
    EXPECTED_MENU_HANDLER_IDS,
    EXPECTED_MENU_METHODS,
    EXPECTED_MENU_PROPERTIES,
    EXPECTED_MENUSHELL_HANDLER_IDS,
    EXPECTED_MENUSHELL_METHODS,
    EXPECTED_MENUSHELL_PROPERTIES,
    EXPECTED_RECENTCHOOSERMENU_METHODS,
    EXPECTED_RECENTCHOOSERMENU_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3RecentChooserMenu(BaseGTK3GObjectTests):
    """Test class for the GTK3RecentChooserMenu class."""

    widget_class = GTK3RecentChooserMenu
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_default_height = -1
    expected_default_width = -1
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_MENUSHELL_HANDLER_IDS
        | EXPECTED_MENU_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_MENUSHELL_METHODS
        + EXPECTED_MENU_METHODS
        + EXPECTED_RECENTCHOOSERMENU_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_MENUSHELL_PROPERTIES
        | EXPECTED_MENU_PROPERTIES
        | EXPECTED_RECENTCHOOSERMENU_PROPERTIES
    )

    def make_dut(
        self, manager: Gtk.RecentManager | None = None
    ) -> GTK3RecentChooserMenu:
        """Make a new instance of the GTK3RecentChooserMenu class.

        Parameters
        ----------
        manager : Gtk.RecentManager | None
            The Gtk.RecentManager to use for the GTK3RecentChooserMenu. If None, a new
            Gtk.RecentManager will be created.

        Returns
        -------
        GTK3RecentChooserMenu
            A new instance of the GTK3RecentChooserMenu class.
        """
        return self.widget_class(manager=manager)

    @pytest.mark.unit
    def test_init(self):
        """Should initialize the GTK3RecentChooserMenu with a default
        Gtk.RecentManager."""
        dut = self.make_dut()

        assert isinstance(dut, GTK3RecentChooserMenu)
        assert isinstance(dut.recent_manager, Gtk.RecentManager)

    @pytest.mark.unit
    def test_init_with_manager(self):
        """Should initialize the GTK3RecentChooserMenu with a Gtk.RecentManager."""
        manager = Gtk.RecentManager.get_default()
        dut = self.make_dut(manager=manager)

        assert isinstance(dut, GTK3RecentChooserMenu)
        assert dut.recent_manager == manager

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert not dut.do_get_property("show_numbers")

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                show_numbers=True,
            )
        )

        assert dut.get_property("show_numbers")
        assert dut.get_show_numbers()
