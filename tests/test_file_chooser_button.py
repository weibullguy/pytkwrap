# pylint: skip-file
# type: ignore
# -*- coding: utf-8 -*-
#
#       tests.gtk3.test_file_chooser_button.py is part of the pytkwrap project
#
# All rights reserved.
"""Test class for the GTK3 file chooser button module algorithms and models."""

import os

# Third Party Imports
import pytest

from pubsub import pub

# Package Imports
from pytkwrap.exceptions import UnkSignalError
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.buttons import (
    BaseButton,
    FileChooserButton,
)
from pytkwrap.gtk3.widget import WidgetProperties
from .conftest import CommonWidgetTests


@pytest.mark.skip(
    reason=(
        "Gtk.FileChooserButton crashes at the C level in test environments. "
        "Requires manual testing in a running GTK3 application."
        "See examples/file_chooser_button.py for manual test program."
    )
)
@pytest.mark.usefixtures("suppress_stderr")
class TestFileChooserButton(CommonWidgetTests):
    """Test class for the FileChooserButton."""

    widget_class = FileChooserButton
    expected_default_height = 30
    expected_default_width = 200

    def make_dut(self, label="..."):
        return self.widget_class(label=label)

    def do_update_error_handler(self, message):
        assert message == (
            "FileChooserButton.do_update(): Unknown signal name 'edit_signal'."
        )

    def mock_handler(self, node_id, package) -> None:
        if node_id == 0:
            assert package == {"test_field": True}

    def no_signal_error_handler(self, message):
        assert message == (
            "FileChooserButton.do_set_callbacks(): Unknown signal name 'value-changed'."
        )

    def on_changed_error_handler(self, message):
        assert message == (
            "FileChooserButton.on_changed(): Unknown signal name 'edit_signal'."
        )

    @pytest.mark.unit
    def test_set_properties_default(self):
        """do_set_properties() should set the default properties of a FileChooserButton
        when no keywords are passed to the method."""
        dut = self.make_dut()
        dut.do_set_properties(WidgetProperties())

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
        """do_set_properties() should set the properties of a CheckButton."""
        dut = self.make_dut()
        dut.do_set_properties(
            WidgetProperties(
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
        """do_update() should update the ColorButton with the data in the passed
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
        """do_update() should update the ColorButton with the default RGBA values
        when passed None."""
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
