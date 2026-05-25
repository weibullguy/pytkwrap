"""Test module for the GTK3Button class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.buttons import GTK3Button, do_make_buttonbox
from pytkwrap.gtk3.widget import GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3WidgetTests
from .test_constants import (
    EXPECTED_BIN_METHODS,
    EXPECTED_BUTTON_HANDLER_IDS,
    EXPECTED_BUTTON_METHODS,
    EXPECTED_BUTTON_PROPERTIES,
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)


class TestButton(BaseGTK3WidgetTests):
    """Test class for the GTK3Button."""

    widget_class = GTK3Button
    expected_attributes = EXPECTED_WIDGET_ATTRIBUTES
    expected_default_height = 30
    expected_default_width = 200
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_BUTTON_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_BUTTON_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_BUTTON_PROPERTIES
    )

    def make_dut(self, label="..."):
        """Create a device under test for the GTK3Button."""
        return self.widget_class(label)

    @pytest.mark.unit
    def test_init_with_label(self):
        """Should create a GTK3Button with a non-default label."""
        dut = self.make_dut("Test Label")

        assert isinstance(dut, GTK3Button)
        assert dut.get_label() == "Test Label"
        assert dut.get_image() is None

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set the properties of a GTK3Button to the values passed in a
        GTK3WidgetProperties dict."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                always_show_image=True,
                image=None,
                label="Test Label",
                relief=Gtk.ReliefStyle.NONE,
                use_underline=True,
            )
        )

        assert dut.do_get_property("always_show_image")
        assert dut.do_get_property("image") is None
        assert dut.do_get_property("label") == "Test Label"
        assert dut.do_get_property("relief") == Gtk.ReliefStyle.NONE
        assert dut.do_get_property("use_underline")

    @pytest.mark.unit
    def test_do_set_properties_image(self, image_file):
        """Should set the properties of a GTK3Button to the values passed in a
        GTK3WidgetProperties dict."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                always_show_image=True,
                image=image_file,
                label="Test Label",
                relief=Gtk.ReliefStyle.NONE,
                use_underline=True,
            )
        )

        assert dut.get_property("always_show_image")
        assert isinstance(dut.get_property("image"), Gtk.Image)
        assert dut.get_property("label") == ""
        assert dut.get_property("relief") == Gtk.ReliefStyle.NONE
        assert dut.get_property("use_underline")


@pytest.mark.integration
def test_do_make_buttonbox_vertical(image_file):
    """Should make a vertical buttonbox with a single button."""
    _buttonbox = do_make_buttonbox(
        icons=[image_file],
        tooltips=["Test tooltip"],
        callbacks=[],
    )

    assert isinstance(_buttonbox, Gtk.VButtonBox)


@pytest.mark.integration
def test_do_make_buttonbox_horizontal(image_file):
    """Should make a horizontal buttonbox with a single button."""
    _buttonbox = do_make_buttonbox(
        icons=[image_file],
        tooltips=["Test tooltip"],
        callbacks=[],
        orientation="horizontal",
    )

    assert isinstance(_buttonbox, Gtk.HButtonBox)


@pytest.mark.integration
def test_do_make_buttonbox_no_tooltip(image_file):
    """Should make a vertical buttonbox with a single button with no tooltip."""
    _buttonbox = do_make_buttonbox(
        icons=[image_file],
        tooltips=[],
        callbacks=[],
    )

    assert isinstance(_buttonbox, Gtk.VButtonBox)
