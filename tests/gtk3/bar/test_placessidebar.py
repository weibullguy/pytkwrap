"""Test module for the GTK3PlacesSidebar class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
import os

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gio, Gtk

# noinspection PyProtectedMember
from pytkwrap.gtk3.bar import GTK3PlacesSidebar
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from tests.gtk3.bar.constants import (
    EXPECTED_PLACESSIDEBAR_HANDLER_IDS,
    EXPECTED_PLACESSIDEBAR_METHODS,
    EXPECTED_PLACESSIDEBAR_PROPERTIES,
)
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
    EXPECTED_BIN_METHODS,
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
)
from tests.gtk3.window.constants import (
    EXPECTED_SCROLLEDWINDOW_HANDLER_IDS,
    EXPECTED_SCROLLEDWINDOW_METHODS,
    EXPECTED_SCROLLEDWINDOW_PROPERTIES,
)


@pytest.mark.usefixtures("skip_if_not_isolated")
@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3PlacesSidebar(BaseGTK3GObjectTests):
    """Test class for the GTK3PlacesSidebar."""

    widget_class = GTK3PlacesSidebar
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_SCROLLEDWINDOW_HANDLER_IDS
        | EXPECTED_PLACESSIDEBAR_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_SCROLLEDWINDOW_METHODS
        + EXPECTED_PLACESSIDEBAR_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_SCROLLEDWINDOW_PROPERTIES
        | EXPECTED_PLACESSIDEBAR_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert not dut.do_get_property("local_only")
        assert dut.do_get_property("location") is None
        assert dut.do_get_property("open_flags") == Gtk.PlacesOpenFlags.NORMAL
        assert not dut.do_get_property("populate_all")
        assert dut.do_get_property("show_desktop")
        assert not dut.do_get_property("show_enter_location")
        assert not dut.do_get_property("show_other_locations")
        assert dut.do_get_property("show_recent")
        assert not dut.do_get_property("show_starred_location")
        assert dut.do_get_property("show_trash")

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _gfile = Gio.File.new_for_path(f"{os.getcwd()}/tests/data")

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                local_only=True,
                location=_gfile,
                open_flags=Gtk.PlacesOpenFlags.NEW_TAB,
                populate_all=True,
                show_desktop=False,
                show_enter_location=True,
                show_other_locations=True,
                show_recent=False,
                show_starred_location=True,
                show_trash=False,
            )
        )

        assert dut.get_property("local_only")
        assert dut.do_get_property("location").get_path() == f"{os.getcwd()}/tests/data"
        assert dut.get_property("open_flags") == Gtk.PlacesOpenFlags.NEW_TAB
        assert dut.get_property("populate_all")
        assert not dut.get_property("show_desktop")
        assert dut.get_property("show_enter_location")
        assert dut.get_property("show_other_locations")
        assert not dut.get_property("show_recent")
        assert dut.get_property("show_starred_location")
        assert not dut.get_property("show_trash")
