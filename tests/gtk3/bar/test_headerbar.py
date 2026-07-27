"""Test module for the GTK3HeaderBar class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.bar import GTK3HeaderBar
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from tests.gtk3.bar.constants import (
    EXPECTED_HEADERBAR_METHODS,
    EXPECTED_HEADERBAR_PROPERTIES,
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
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3HeaderBar(BaseGTK3GObjectTests):
    """Test class for the GTK3HeaderBar class."""

    widget_class = GTK3HeaderBar
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_default_height = -1
    expected_default_width = -1
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_HEADERBAR_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_HEADERBAR_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("border_width") == 0
        assert dut.do_get_property("custom_title") is None
        assert dut.do_get_property("decoration_layout") is None
        assert not dut.do_get_property("decoration_layout_set")
        assert dut.do_get_property("has_subtitle")
        assert not dut.do_get_property("show_close_button")
        assert dut.do_get_property("spacing") == 6
        assert dut.do_get_property("subtitle") is None
        assert dut.do_get_property("title") is None

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _custom_title = Gtk.Label(label="Test Custom Title")

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                border_width=25,
                custom_title=_custom_title,
                decoration_layout="close:minimize:maximize",
                decoration_layout_set=True,
                has_subtitle=False,
                show_close_button=True,
                spacing=16,
                subtitle="Test Subtitle",
                title="Test Title",
            )
        )

        assert dut.get_property("border_width") == 25
        assert dut.get_property("custom_title") == _custom_title
        assert dut.get_custom_title() == _custom_title
        assert dut.get_property("decoration_layout") == "close:minimize:maximize"
        assert dut.get_decoration_layout() == "close:minimize:maximize"
        assert dut.get_property("decoration_layout_set")
        assert not dut.get_property("has_subtitle")
        assert not dut.get_has_subtitle()
        assert dut.get_property("show_close_button")
        assert dut.get_show_close_button()
        assert dut.get_property("spacing") == 16
        assert dut.get_property("subtitle") == "Test Subtitle"
        assert dut.get_subtitle() == "Test Subtitle"
        assert dut.get_property("title") == "Test Title"
        assert dut.get_title() == "Test Title"
