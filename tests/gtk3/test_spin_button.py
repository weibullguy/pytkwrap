# pylint: skip-file
# type: ignore
#
#       tests.gtk3.test_spin_button.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""Test class for the GTK3SpinButton module algorithms and models."""

# Third Party Imports
import pytest

from pubsub import pub

# Package Imports
from pytkwrap.exceptions import UnkSignalError
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.buttons import GTK3SpinButton
from pytkwrap.gtk3.widget import GTK3WidgetProperties
from .conftest import BaseGTK3DataWidgetTests


@pytest.mark.usefixtures("suppress_stderr")
class TestSpinButton(BaseGTK3DataWidgetTests):
    """Test class for the GTK3SpinButton."""

    widget_class = GTK3SpinButton
    expected_default_height = 30
    expected_default_edit_signal = "value-changed"
    expected_package = {0:{"test_field": 0.5}}
    expected_default_width = 200

    @pytest.mark.unit
    def test_init(self):
        """Should create a GTK3SpinButton with default attribute values."""
        dut = self.make_dut()

        assert isinstance(dut, GTK3SpinButton)
        assert self.expected_default_height == dut._DEFAULT_HEIGHT
        assert self.expected_default_width == dut._DEFAULT_WIDTH
        assert self.expected_default_edit_signal == dut._DEFAULT_EDIT_SIGNAL
        # GTK3SpinButton-specific properties should be registered.
        for _property in GTK3SpinButton._GTK3_SPIN_BUTTON_PROPERTIES:
            assert _property in dut.dic_properties
        # GTK3SpinButton-specific signals should be registered.
        for _signal in GTK3SpinButton._GTK3_SPIN_BUTTON_SIGNALS:
            assert _signal in dut.dic_handler_id

        assert isinstance(dut.get_adjustment(), Gtk.Adjustment)
        assert dut.get_digits() == 0
        assert dut.get_increments() == (0.0, 0.0)
        assert not dut.get_numeric()
        assert dut.get_range() == (0.0, 0.0)
        assert not dut.get_snap_to_ticks()
        assert dut.get_update_policy() == Gtk.SpinButtonUpdatePolicy.ALWAYS
        assert dut.get_value() == 0.0
        assert dut.get_value_as_int() == 0
        assert not dut.get_wrap()

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set the default properties values of a GTK3SpinButton when passed an
        empty GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert isinstance(dut.get_adjustment(), Gtk.Adjustment)
        assert dut.get_digits() == 0
        assert dut.get_increments() == (0.0, 0.0)
        assert not dut.get_numeric()
        assert dut.get_range() == (0.0, 0.0)
        assert not dut.get_snap_to_ticks()
        assert dut.get_update_policy() == Gtk.SpinButtonUpdatePolicy.ALWAYS
        assert dut.get_value() == 0.0
        assert dut.get_value_as_int() == 0
        assert not dut.get_wrap()

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set the GTKSpinButton properties to the values passed in a
        GTK3WidgetProperties dict."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                adjustment=Gtk.Adjustment(),
                climb_rate=0.1,
                digits=2,
                lower=1.0,
                numeric=True,
                page_increment=0.5,
                snap_to_ticks=True,
                step_increment=0.1,
                update_policy=Gtk.SpinButtonUpdatePolicy.IF_VALID,
                upper=10.0,
                value=5.0,
                wrap=True,
                ),
            )

        assert isinstance(dut.get_adjustment(), Gtk.Adjustment)
        assert dut.get_digits() == 2
        assert dut.get_increments() == (0.1, 0.5)
        assert dut.get_numeric()
        assert dut.get_range() == (1.0, 10.0)
        assert dut.get_snap_to_ticks()
        assert dut.get_update_policy() == Gtk.SpinButtonUpdatePolicy.IF_VALID
        assert dut.get_value() == 5.0
        assert dut.get_value_as_int() == 5
        assert dut.get_wrap()

    @pytest.mark.unit
    def test_do_update(self):
        """Update the GTK3SpinButton with the data package value."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                adjustment=Gtk.Adjustment(),
                lower=0.0,
                upper=5.0,
            ),
        )
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={"test_field": 0.9})

        assert dut.get_value() == 0.9

    @pytest.mark.unit
    def test_do_update_none_value(self):
        """Do NOT update the GTK3SpinButton with the data package value."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                adjustment=Gtk.Adjustment(),
                lower=0.0,
                upper=5.0,
                value=2.5,
            ),
        )
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={"test_field": None})

        assert dut.get_value() == 2.5

    @pytest.mark.unit
    def test_do_update_integer_value(self):
        """Update the GTK3SpinButton with the float of an integer data package value."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                adjustment=Gtk.Adjustment(),
                lower=0.0,
                upper=5.0,
                value=2.5,
            ),
        )
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={"test_field": 2})

        assert dut.get_value() == 2.0

    @pytest.mark.unit
    def test_do_update_unknown_signal(self):
        """Raise an UnkSignalError with an unknown edit signal name."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                adjustment=Gtk.Adjustment(),
                lower=0.0,
                upper=5.0,
                value=2.5,
            ),
        )
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.do_update)
        pub.subscribe(self.do_update_error_handler, "do_log_error")
        pub.subscribe(dut.do_update, "rootTopic")
        dut.edit_signal = "edit_signal"

        with pytest.raises(UnkSignalError):
            pub.sendMessage("rootTopic", package={"test_field": 4.8})

        assert dut.get_value() == 2.5

    @pytest.mark.unit
    def test_do_update_wrong_field(self):
        """Do nothing when the package field doesn't match."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                adjustment=Gtk.Adjustment(),
                lower=0.0,
                upper=5.0,
                value=2.5,
            ),
        )
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.on_changed)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={"wrong_field": 2.89})

        assert dut.get_value() == 2.5

    @pytest.mark.unit
    def test_on_changed(self):
        """Called when the GTK3SpinButton value changes."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                adjustment=Gtk.Adjustment(),
                lower=0.0,
                upper=5.0,
                value=2.5,
            ),
        )
        dut.field = "test_field"
        dut.record_id = 0
        dut.send_topic = "button_toggled"
        dut.do_set_callbacks(dut.edit_signal, dut.on_changed)

        pub.subscribe(self.mock_handler, dut.send_topic)

        dut.set_value(3.8)

    @pytest.mark.unit
    def test_on_changed_unknown_signal(self):
        """Raise a KeyError with an unknown edit signal name."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                adjustment=Gtk.Adjustment(),
                lower=0.0,
                upper=5.0,
                value=2.5,
            ),
        )
        dut.field = "test_field"
        dut.record_id = 0
        dut.send_topic = "button_toggled"
        dut.do_set_callbacks(dut.edit_signal, dut.on_changed)
        pub.subscribe(self.on_changed_error_handler, "do_log_error")
        dut.edit_signal = "toggle_signal"
        pub.subscribe(self.mock_handler, dut.send_topic)

        dut.set_value(3.8)
