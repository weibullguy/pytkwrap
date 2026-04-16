# pylint: skip-file
# type: ignore
#
#       tests.gtk3.test_file_chooser_button.py is part of the pytkwrap project
#
# All rights reserved.
"""Test class for the GTK3FileChooserButton module algorithms and models."""

import os

# Third Party Imports
import pytest

from pubsub import pub

# Package Imports
from pytkwrap.exceptions import UnkSignalError
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.buttons import (
    GTK3BaseButton,
    GTK3FileChooserButton,
)
from pytkwrap.gtk3.widget import GTK3WidgetProperties
from .conftest import BaseGTK3WidgetTests


@pytest.mark.skip(
    reason=(
        "Gtk.FileChooserButton crashes at the C level in test environments. "
        "Requires manual testing in a running GTK3 application."
        "See examples/file_chooser_button.py for manual test program."
    )
)
@pytest.mark.usefixtures("suppress_stderr")
class TestFileChooserButton(BaseGTK3WidgetTests):
    """Test class for the GTK3FileChooserButton."""

    widget_class = GTK3FileChooserButton
    expected_default_height = 30
    expected_default_width = 200

    def make_dut(self, label="..."):
        """Create a device under test for the GTK3FileChooserButton."""
        return self.widget_class(label=label)

    @pytest.mark.unit
    def test_set_properties_default(self):
        """Should set the default properties of a GTK3FileChooserButton when passed an
        empty GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert isinstance(dut.get_property("rgba"), Gdk.RGBA)
        assert dut.get_property("rgba").alpha == 1.0
        assert dut.get_property("rgba").blue == 1.0
        assert dut.get_property("rgba").green == 1.0
        assert dut.get_property("rgba").red == 1.0
        assert not dut.get_property("show-editor")
        assert dut.get_property("title") == "Pick a Color"
        assert dut.get_property("use-alpha")

    @pytest.mark.unit
    def test_set_properties(self):
        """Should set the properties of a GTK3FileChooserButton to the values in the
        passed GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                rgba=Gdk.RGBA(1.0, 1.0, 1.0, 1.0),
                show_editor=True,
                title="Choose a Color",
                use_alpha=False,
            )
        )

        assert isinstance(dut.get_property("rgba"), Gdk.RGBA)
        assert dut.get_property("rgba").alpha == 1.0
        assert dut.get_property("rgba").blue == 1.0
        assert dut.get_property("rgba").green == 1.0
        assert dut.get_property("rgba").red == 1.0
        assert dut.get_property("show-editor")
        assert dut.get_property("title") == "Choose a Color"
        assert not dut.get_property("use-alpha")

    @pytest.mark.unit
    def test_do_update(self):
        """Should update the GTK3FileChooserButton with the data in the passed
        package."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage(
            "rootTopic", package={"test_field": Gdk.RGBA(0.3, 0.1, 0.9, 0.75)}
        )

        assert isinstance(dut.get_property("rgba"), Gdk.RGBA)
        assert isinstance(dut.get_rgba(), Gdk.RGBA)
        assert dut.get_property("rgba").alpha == 0.75
        assert dut.get_property("rgba").blue == 0.9
        assert dut.get_property("rgba").green == 0.1
        assert dut.get_property("rgba").red == 0.3

    @pytest.mark.unit
    def test_do_update_none_value(self):
        """do_update() should update the ColorButton with the default RGBA values when
        passed None."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={"test_field": None})

        assert isinstance(dut.get_property("rgba"), Gdk.RGBA)
        assert isinstance(dut.get_rgba(), Gdk.RGBA)
        assert dut.get_property("rgba").alpha == 1.0
        assert dut.get_property("rgba").blue == 1.0
        assert dut.get_property("rgba").green == 1.0
        assert dut.get_property("rgba").red == 1.0

    @pytest.mark.unit
    def test_do_update_unknown_signal(self):
        """do_update() should raise a key error with an unknown edit signal name."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.do_update)
        pub.subscribe(self.do_update_error_handler, "do_log_error")
        pub.subscribe(dut.do_update, "rootTopic")
        dut.edit_signal = "edit_signal"

        with pytest.raises(UnkSignalError):
            pub.sendMessage("rootTopic", package={"test_field": "Test Package"})

        assert isinstance(dut.get_property("rgba"), Gdk.RGBA)
        assert isinstance(dut.get_rgba(), Gdk.RGBA)
        assert dut.get_property("rgba").alpha == 1.0
        assert dut.get_property("rgba").blue == 0.0
        assert dut.get_property("rgba").green == 0.0
        assert dut.get_property("rgba").red == 0.0

    @pytest.mark.unit
    def test_do_update_wrong_field(self):
        """do_update() should do nothing when the package field doesn't match."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.on_changed)
        pub.subscribe(dut.do_update, "rootTopic")
        dut.set_rgba(Gdk.RGBA(0.5, 0.5, 0.5, 0.88))

        pub.sendMessage("rootTopic", package={"wrong_field": False})

        assert dut.get_rgba().alpha == 0.88
        assert dut.get_rgba().blue == 0.5
        assert dut.get_rgba().green == 0.5
        assert dut.get_rgba().red == 0.5

    @pytest.mark.unit
    def test_on_changed(self):
        """on_changed() is called when the ColorButton color is set."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.record_id = 0
        dut.send_topic = "color_set"
        dut.do_set_callbacks(dut.edit_signal, dut.on_changed)

        pub.subscribe(self.mock_handler, dut.send_topic)

        dut.emit("color-set")

    @pytest.mark.unit
    def test_on_changed_unknown_signal(self):
        """on_changed() should raise a KeyError with an unknown edit signal name."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.record_id = 0
        dut.send_topic = "button_toggled"
        dut.do_set_callbacks(dut.edit_signal, dut.on_changed)
        pub.subscribe(self.on_changed_error_handler, "do_log_error")
        dut.edit_signal = "edit_signal"

        pub.subscribe(self.mock_handler, dut.send_topic)

        dut.emit("color-set")
