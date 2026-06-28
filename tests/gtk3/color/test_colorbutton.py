"""Test module for the GTK3ColorButton class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.color import GTK3ColorButton
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
from tests.gtk3.button.constants import (
    EXPECTED_BUTTON_HANDLER_IDS,
    EXPECTED_BUTTON_METHODS,
    EXPECTED_BUTTON_PROPERTIES,
)
from tests.gtk3.color.constants import (
    EXPECTED_COLORBUTTON_ATTRIBUTES,
    EXPECTED_COLORBUTTON_HANDLER_IDS,
    EXPECTED_COLORBUTTON_METHODS,
    EXPECTED_COLORBUTTON_PROPERTIES,
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
from tests.gtk3.container.constants import (
    EXPECTED_BIN_METHODS,
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3ColorButton(BaseGTK3DataWidgetTests):
    """Test class for the GTK3ColorButton."""

    widget_class = GTK3ColorButton
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | (
        EXPECTED_WIDGET_ATTRIBUTES | EXPECTED_COLORBUTTON_ATTRIBUTES
    )
    expected_default_height = 30
    expected_default_width = 60
    expected_get_value = [
        [
            Gdk.RGBA(1.0, 0.75, 0.5, 0.25),
            Gdk.RGBA(1.0, 0.75, 0.5, 0.25),
        ]
    ]
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_BUTTON_HANDLER_IDS
        | EXPECTED_COLORBUTTON_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_BUTTON_METHODS
        + EXPECTED_COLORBUTTON_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_BUTTON_PROPERTIES
        | EXPECTED_COLORBUTTON_PROPERTIES
    )
    expected_set_value = [
        [Gdk.RGBA(1.0, 0.75, 0.5, 0.25), Gdk.RGBA(1.0, 0.75, 0.5, 0.25)],
        [None, Gdk.RGBA(0.0, 0.0, 0.0, 1.0)],
    ]
    expected_set_value_wrong_types = [
        True,
        8.6,
        3,
        "Red",
        (1, 3, "Blue"),
    ]

    @staticmethod
    def mock_handler(package):
        """Mock handler for on_changed() calls."""
        assert isinstance(package, dict)
        assert isinstance(package[-1], Gdk.RGBA)
        assert package[-1].alpha == 0.0

    @pytest.mark.unit
    def test_do_set_attributes_default(self):
        """Should set attributes to default values when passed an empty
        GTK3WidgetAttributes."""
        dut = self.make_dut()
        dut.do_set_attributes(GTK3WidgetAttributes())

        assert dut.do_get_attribute("default_value") is None
        assert dut.do_get_attribute("edit_signal") == "color-set"

    @pytest.mark.unit
    def test_do_set_attributes(self):
        """Should set attributes to the values passed in the GTK3WidgetAttributes."""
        dut = self.make_dut()
        dut.do_set_attributes(
            GTK3WidgetAttributes(
                default_value=Gdk.RGBA(1.0, 0.5, 0.25, 0.75),
                edit_signal="color_changed",
            )
        )

        assert dut.do_get_attribute("default_value") == Gdk.RGBA(1.0, 0.5, 0.25, 0.75)
        assert dut.do_get_attribute("edit_signal") == "color_changed"

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert isinstance(dut.get_property("rgba"), Gdk.RGBA)
        assert dut.get_property("rgba").alpha == 1.0
        assert dut.get_property("rgba").blue == 0.0
        assert dut.get_property("rgba").green == 0.0
        assert dut.get_property("rgba").red == 0.0
        assert not dut.get_property("show-editor")
        assert dut.get_property("title") == "Pick a Color"
        assert dut.get_property("use-alpha")

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
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
        """Should update the GTK3ColorButton with the data package value."""
        dut = self.make_dut()

        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")
        pub.sendMessage("rootTopic", package={-1: Gdk.RGBA(0.3, 0.1, 0.9, 0.75)})

        assert isinstance(dut.get_property("rgba"), Gdk.RGBA)
        assert isinstance(dut.get_rgba(), Gdk.RGBA)
        assert dut.get_property("rgba").alpha == 0.75
        assert dut.get_property("rgba").blue == 0.9
        assert dut.get_property("rgba").green == 0.1
        assert dut.get_property("rgba").red == 0.3

    @pytest.mark.unit
    def test_on_changed(self):
        """on_changed() is called when the GTK3ColorButton color is set."""
        dut = self.make_dut()

        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
        dut.dic_attributes["send_topic"] = "color_changed"
        pub.subscribe(self.mock_handler, dut.dic_attributes["send_topic"])

        dut.emit("color-set")

        pub.unsubscribe(self.mock_handler, dut.dic_attributes["send_topic"])
