"""Test module for the GTK3Label class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk, Pango
from pytkwrap.gtk3.io import GTK3Label
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from tests.gtk3.conftest import BaseGTK3DataWidgetTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)
from tests.gtk3.io.constants import (
    EXPECTED_LABEL_ATTRIBUTES,
    EXPECTED_LABEL_HANDLER_IDS,
    EXPECTED_LABEL_METHODS,
    EXPECTED_LABEL_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3Label(BaseGTK3DataWidgetTests):
    """Test class for the GTK3Label class."""

    widget_class = GTK3Label
    expected_default_height = 30
    expected_default_width = 200
    expected_attributes = (
        EXPECTED_GOBJECT_ATTRIBUTES
        | EXPECTED_WIDGET_ATTRIBUTES
        | EXPECTED_LABEL_ATTRIBUTES
    )
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_LABEL_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS + EXPECTED_WIDGET_METHODS + EXPECTED_LABEL_METHODS
    )
    expected_properties = EXPECTED_WIDGET_PROPERTIES | EXPECTED_LABEL_PROPERTIES

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("angle") == 0.0
        assert dut.do_get_property("attributes") is None
        assert dut.do_get_property("ellipsize") == Pango.EllipsizeMode.NONE
        assert dut.do_get_property("justify") == Gtk.Justification.LEFT
        assert dut.do_get_property("label") == ""
        assert dut.do_get_property("lines") == -1
        assert dut.do_get_property("max_width_chars") == -1
        assert dut.do_get_property("mnemonic_widget") is None
        assert dut.do_get_property("pattern") is None
        assert not dut.do_get_property("selectable")
        assert not dut.do_get_property("single_line_mode")
        assert dut.do_get_property("track_visited_links")
        assert not dut.do_get_property("use_markup")
        assert not dut.do_get_property("use_underline")
        assert dut.do_get_property("width_chars") == -1
        assert not dut.do_get_property("wrap")
        assert dut.do_get_property("wrap_mode") == Pango.WrapMode.WORD

    @pytest.mark.unit
    def test_do_set_properties_wrap_ellipsize(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                angle=45.0,
                ellipsize=Pango.EllipsizeMode.MIDDLE,
                justify=Gtk.Justification.RIGHT,
                label="Test Label",
                lines=2,
                wrap=True,
                wrap_mode=Pango.WrapMode.CHAR,
            )
        )

        assert dut.get_property("angle") == 45.0
        assert dut.get_angle() == 45.0
        assert dut.get_property("ellipsize") == Pango.EllipsizeMode.MIDDLE
        assert dut.get_ellipsize() == Pango.EllipsizeMode.MIDDLE
        assert dut.get_property("justify") == Gtk.Justification.RIGHT
        assert dut.get_justify() == Gtk.Justification.RIGHT
        assert dut.get_property("label") == "Test Label"
        assert dut.get_label() == "Test Label"
        assert dut.get_property("lines") == 2
        assert dut.get_lines() == 2
        assert dut.get_line_wrap()
        assert dut.get_property("wrap_mode") == Pango.WrapMode.CHAR
        assert dut.get_line_wrap_mode() == Pango.WrapMode.CHAR

        assert dut.get_property("attributes") is None
        assert dut.get_property("max_width_chars") == -1
        assert dut.get_property("mnemonic_widget") is None
        assert not dut.get_property("selectable")
        assert not dut.get_property("single_line_mode")
        assert dut.get_property("track_visited_links")
        assert not dut.get_property("use_markup")
        assert not dut.get_property("use_underline")
        assert dut.get_property("width_chars") == -1
        assert dut.get_property("wrap")

    @pytest.mark.unit
    def test_do_get_value(self):
        """Should return the value of the GTK3Label."""
        dut = self.make_dut()
        dut.set_label("Test Label")

        assert dut.do_get_value() == "Test Label"

    @pytest.mark.unit
    def test_do_set_value(self):
        """Should set the value of the GTK3Label."""
        dut = self.make_dut()
        dut.do_set_value("Test Label")

        assert dut.get_label() == "Test Label"

    @pytest.mark.unit
    def test_do_set_value_mnemonic(self):
        """Should set the value of the GTK3Label using a mnemonic."""
        _text = "_Test Label"

        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties(use_underline=True))
        dut.do_set_value(_text)

        assert dut.get_label() == _text

    @pytest.mark.unit
    def test_do_set_value_markup(self):
        """Should set the value of the GTK3Label using markup."""
        _markup = "<span foreground='blue' size='x-large'>Test Label</span>"

        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties(use_markup=True))
        dut.do_set_value(_markup)

        assert dut.get_label() == _markup

    @pytest.mark.unit
    def test_do_set_value_markup_mnemonic(self):
        """Should set the value of the GTK3Label using markup and a mnemonic."""
        _markup = "<span foreground='blue' size='x-large'>_Test Label</span>"

        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties(use_markup=True, use_underline=True))
        dut.do_set_value(_markup)

        assert dut.get_label() == _markup

    @pytest.mark.unit
    def test_do_update_none_value(self):
        """Should not update the GTK3Label when the value is None."""
        dut = self.make_dut()

        pub.subscribe(dut.do_update, "rootTopic")
        pub.sendMessage("rootTopic", package={-1: None})

        assert dut.dic_attributes == self.expected_attributes
