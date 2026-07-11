"""Test module for the GTK3SpinButton class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.gtk3 import GTK3Adjustment

# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import GdkPixbuf, Gtk, Pango
from pytkwrap.gtk3.button import GTK3SpinButton
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
from tests.gtk3.button.constants import (
    EXPECTED_SPINBUTTON_ATTRIBUTES,
    EXPECTED_SPINBUTTON_HANDLER_IDS,
    EXPECTED_SPINBUTTON_METHODS,
    EXPECTED_SPINBUTTON_PROPERTIES,
)
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
    EXPECTED_ENTRY_ATTRIBUTES,
    EXPECTED_ENTRY_HANDLER_IDS,
    EXPECTED_ENTRY_METHODS,
    EXPECTED_ENTRY_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3SpinButton(BaseGTK3DataWidgetTests):
    """Test class for the GTK3SpinButton class."""

    widget_class = GTK3SpinButton
    expected_attributes = (
        EXPECTED_GOBJECT_ATTRIBUTES
        | EXPECTED_WIDGET_ATTRIBUTES
        | EXPECTED_ENTRY_ATTRIBUTES
        | EXPECTED_SPINBUTTON_ATTRIBUTES
    )
    expected_default_height = 25
    expected_default_width = 200
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_ENTRY_HANDLER_IDS
        | EXPECTED_SPINBUTTON_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_ENTRY_METHODS
        + EXPECTED_SPINBUTTON_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_ENTRY_PROPERTIES
        | EXPECTED_SPINBUTTON_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_attributes_default(self):
        """Should set the default attributes of a GTK3SpinButton when passed an empty
        WidgetAttributes."""
        super().test_do_set_attributes_default()

        dut = self.make_dut()
        dut.do_set_attributes(GTK3WidgetAttributes())

        assert dut.do_get_attribute("data_type") == float
        assert dut.do_get_attribute("default_value") == 0.0
        assert dut.do_get_attribute("edit_signal") == "value-changed"
        assert dut.do_get_attribute("format") == "{:3.1f}"

    @pytest.mark.unit
    def test_do_set_attributes(self):
        """Should set the GTK3SpinButton attributes to the values passed in a
        GTK3WidgetAttributes dict."""
        super().test_do_set_attributes()

        dut = self.make_dut()
        dut.do_set_attributes(
            GTK3WidgetAttributes(
                default_value=2.5, edit_signal="update-value", format="{:6.4f}"
            )
        )

        assert dut.do_get_attribute("default_value") == 2.5
        assert dut.do_get_attribute("edit_signal") == "update-value"
        assert dut.do_get_attribute("format") == "{:6.4f}"

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Set the default properties of a GTK3SpinButton when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.do_get_property("adjustment") is None
        assert dut.do_get_property("climb_rate") == 0.0
        assert dut.do_get_property("digits") == 0
        assert not dut.do_get_property("numeric")
        assert not dut.do_get_property("snap_to_ticks")
        assert dut.do_get_property("update_policy") == Gtk.SpinButtonUpdatePolicy.ALWAYS
        assert dut.do_get_property("value") == 0.0
        assert not dut.do_get_property("wrap")

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set the properties of a GTK3SpinButton."""
        _adjustment = Gtk.Adjustment(10, 0, 100, 1, 10, 0)

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                adjustment=_adjustment,
                climb_rate=0.25,
                digits=1,
                numeric=True,
                snap_to_ticks=True,
                update_policy=Gtk.SpinButtonUpdatePolicy.IF_VALID,
                value=2.5,
                wrap=True,
            )
        )

        assert dut.get_property("adjustment") == _adjustment
        assert dut.get_adjustment() == _adjustment
        assert dut.get_property("climb_rate") == 0.25
        assert dut.get_property("digits") == 1
        assert dut.get_digits() == 1
        assert dut.get_property("numeric")
        assert dut.get_numeric()
        assert dut.get_property("snap_to_ticks")
        assert dut.get_snap_to_ticks()
        assert dut.get_property("update_policy") == Gtk.SpinButtonUpdatePolicy.IF_VALID
        assert dut.get_update_policy() == Gtk.SpinButtonUpdatePolicy.IF_VALID
        assert dut.get_property("value") == 2.5
        assert dut.get_value() == 2.5
        assert dut.get_property("wrap")
        assert dut.get_wrap()

    @pytest.mark.unit
    def test_do_update(self):
        """Update the GTK3SpinButton with the data package value."""
        _adjustment = GTK3Adjustment(0, 0, 10, 0.5, 1, 0)

        dut = self.make_dut()
        dut.set_adjustment(_adjustment)
        dut.dic_attributes["index"] = 2
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={2: 0.5})

        assert dut.get_value() == 0.5

    @pytest.mark.unit
    def test_on_changed(self):
        """Called when the GTK3SpinButton text changes."""
        dut = self.make_dut()
        dut.dic_attributes["index"] = 2
        dut.dic_attributes["record_id"] = 0
        dut.dic_attributes["send_topic"] = "entry_changed"
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)

        pub.subscribe(self.mock_handler, dut.dic_attributes["send_topic"])

        dut.set_value(0.88)

    @pytest.mark.unit
    def test_do_get_value(self):
        """Return a float value when the datatype attribute is set to 'gfloat'."""
        _adjustment = GTK3Adjustment(0, 0, 100, 1, 10, 0)

        dut = self.make_dut()
        dut.set_adjustment(_adjustment)
        dut.set_value(38.235)

        assert isinstance(dut.do_get_value(), float)
        assert dut.do_get_value() == 38.235

    @pytest.mark.unit
    def test_do_get_value_int(self):
        """Return an integer value when the data_type attribute is set to int."""
        _adjustment = GTK3Adjustment(0, 0, 100, 1, 10, 0)

        dut = self.make_dut()
        dut.set_adjustment(_adjustment)
        dut.dic_attributes["data_type"] = int
        dut.set_value(38.82)

        assert isinstance(dut.do_get_value(), int)
        assert dut.do_get_value() == 38

    @pytest.mark.unit
    def test_do_get_value_str(self):
        """Return an integer value when the data_type attribute is set to str."""
        _adjustment = GTK3Adjustment(0, 0, 100, 1, 10, 0)

        dut = self.make_dut()
        dut.set_adjustment(_adjustment)
        dut.dic_attributes["data_type"] = str
        dut.set_value(38.82)

        assert isinstance(dut.do_get_value(), str)
        assert dut.do_get_value() == "38.82"

    @pytest.mark.unit
    def test_do_set_value_int(self):
        """Set the value of the GTK3SpinButton with int data_type attribute."""
        _adjustment = GTK3Adjustment(0, 0, 10, 1, 10, 0)

        dut = self.make_dut()
        dut.set_adjustment(_adjustment)
        dut.dic_attributes["data_type"] = int
        dut.set_value(2.0)

        assert dut.do_get_value() == 2

    @pytest.mark.unit
    def test_do_set_value_str(self):
        """Set the value of the GTK3SpinButton with str data_type attribute."""
        _adjustment = GTK3Adjustment(0, 0, 10, 1, 10, 0)

        dut = self.make_dut()
        dut.set_adjustment(_adjustment)
        dut.dic_attributes["data_type"] = str
        dut.set_value(2.0)

        assert dut.do_get_value() == "2.0"
