"""Test module for the GTK3ScaleButton class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.adjustment import GTK3Adjustment
from pytkwrap.gtk3.button import GTK3ScaleButton
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
from tests.gtk3.button.constants import (
    EXPECTED_BUTTON_HANDLER_IDS,
    EXPECTED_BUTTON_METHODS,
    EXPECTED_BUTTON_PROPERTIES,
    EXPECTED_SCALEBUTTON_ATTRIBUTES,
    EXPECTED_SCALEBUTTON_HANDLER_IDS,
    EXPECTED_SCALEBUTTON_METHODS,
    EXPECTED_SCALEBUTTON_PROPERTIES,
)
from tests.gtk3.conftest import BaseGTK3DataWidgetTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
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


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3ScaleButton(BaseGTK3DataWidgetTests):
    """Test class for the GTK3ScaleButton."""

    widget_class = GTK3ScaleButton
    expected_attributes = (
        EXPECTED_GOBJECT_ATTRIBUTES
        | EXPECTED_WIDGET_ATTRIBUTES
        | EXPECTED_SCALEBUTTON_ATTRIBUTES
    )
    expected_default_height = 30
    expected_default_width = 60
    expected_get_value = [
        [8.6, 8.6],
        [5, 5.0],
        ["0.75", 0.75],
    ]
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_BUTTON_HANDLER_IDS
        | EXPECTED_SCALEBUTTON_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_BUTTON_METHODS
        + EXPECTED_SCALEBUTTON_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_BUTTON_PROPERTIES
        | EXPECTED_SCALEBUTTON_PROPERTIES
    )
    expected_set_value = [
        [False, 0.0],
        [8.6, 8.6],
        [5, 5.0],
        ["0.75", 0.75],
    ]
    expected_set_value_wrong_types = [
        ("six", "point", 2),
    ]

    def make_dut(
        self,
        size: int = Gtk.IconSize.SMALL_TOOLBAR,
        min_value: float = 0.0,
        max_value: float = 100.0,
        step: float = 2,
        icons: list | None = None,
    ):
        """Create a device under test for the GTK3ScaleButton."""
        return self.widget_class(size, min_value, max_value, step, icons)

    @pytest.mark.unit
    def test_init_with_size(self):
        """Should initialize an instance of a GTK3ScaleButton with size."""
        dut = self.make_dut(size=Gtk.IconSize.BUTTON)

        assert dut.do_get_property("size") == Gtk.IconSize.BUTTON
        assert dut.get_size() == Gtk.IconSize.BUTTON

    @pytest.mark.unit
    def test_init_with_icons(self):
        """Should initialize an instance of a GTK3ScaleButton with icons."""
        dut = self.make_dut(icons=["gtk-go-up", "gtk-go-down", None])

        assert dut.do_get_property("icons") == ["gtk-go-up", "gtk-go-down", None]
        assert dut.get_icons() == ["gtk-go-up", "gtk-go-down", None]

    @pytest.mark.unit
    def test_do_set_attributes_default(self):
        """Should set attributes to default values when passed an empty
        GTK3WidgetAttributes."""
        dut = self.make_dut()
        dut.do_set_attributes(GTK3WidgetAttributes())

        assert dut.do_get_attribute("default_value") == 0.0
        assert dut.do_get_attribute("edit_signal") == "value-changed"

    @pytest.mark.unit
    def test_do_set_attributes(self):
        """Should set attributes to the values passed in the GTK3WidgetAttributes."""
        dut = self.make_dut()
        dut.do_set_attributes(
            GTK3WidgetAttributes(
                default_value=5.0,
                edit_signal="scale_button_changed",
            )
        )

        assert dut.do_get_attribute("default_value") == 5.0
        assert dut.do_get_attribute("edit_signal") == "scale_button_changed"

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("adjustment") is None
        assert dut.do_get_property("icons") == []
        assert dut.do_get_property("size") == Gtk.IconSize.SMALL_TOOLBAR
        assert dut.do_get_property("value") == 0.0

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _adjustment = GTK3Adjustment(0.0, 0.0, 1.0, 0.1, 0.1, 1.0)

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                adjustment=_adjustment,
                size=Gtk.IconSize.BUTTON,
                value=0.68,
            )
        )

        assert dut.get_property("adjustment") == _adjustment
        assert dut.get_adjustment() == _adjustment
        assert dut.get_property("size") == Gtk.IconSize.BUTTON
        assert dut.get_property("value") == 0.68
        assert dut.get_value() == 0.68

    @pytest.mark.unit
    def test_do_update(self):
        """Should update the GTK3ScaleButton with the data package value."""
        dut = self.make_dut()

        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={-1: 0.75})

        assert dut.do_get_property("value") == 0.75

    @pytest.mark.unit
    def test_on_changed(self):
        """on_changed() is called when the GTK3ScaleButton value is set."""
        dut = self.make_dut()

        dut.dic_attributes["send_topic"] = "scale_changed"
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
        pub.subscribe(self.mock_handler, dut.dic_attributes["send_topic"])

        dut.set_value(5.8)

        pub.unsubscribe(self.mock_handler, dut.dic_attributes["send_topic"])
