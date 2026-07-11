"""Test module for the GTK3LevelBar class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.bar import GTK3LevelBar
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from tests.gtk3.bar.constants import (
    EXPECTED_LEVELBAR_HANDLER_IDS,
    EXPECTED_LEVELBAR_METHODS,
    EXPECTED_LEVELBAR_PROPERTIES,
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


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3LevelBar(BaseGTK3GObjectTests):
    """Test class for the GTK3LevelBar class."""

    widget_class = GTK3LevelBar
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_LEVELBAR_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS + EXPECTED_WIDGET_METHODS + EXPECTED_LEVELBAR_METHODS
    )
    expected_properties = EXPECTED_WIDGET_PROPERTIES | EXPECTED_LEVELBAR_PROPERTIES

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert not dut.do_get_property("inverted")
        assert dut.do_get_property("max_value") == 1.0
        assert dut.do_get_property("min_value") == 0.0
        assert dut.do_get_property("mode") == Gtk.LevelBarMode.CONTINUOUS
        assert dut.do_get_property("value") == 0.0

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                inverted=True,
                max_value=5.0,
                min_value=1.0,
                mode=Gtk.LevelBarMode.DISCRETE,
                value=2.6,
            )
        )

        assert dut.get_property("inverted")
        assert dut.get_inverted()
        assert dut.get_property("max_value") == 5.0
        assert dut.get_max_value() == 5.0
        assert dut.get_property("min_value") == 1.0
        assert dut.get_min_value() == 1.0
        assert dut.get_property("mode") == Gtk.LevelBarMode.DISCRETE
        assert dut.get_mode() == Gtk.LevelBarMode.DISCRETE
        assert dut.get_property("value") == 2.6
        assert dut.get_value() == 2.6

    @pytest.mark.unit
    def test_do_set_value(self):
        """Should set the value of the GTK3LevelBar."""
        dut = self.make_dut()
        dut.do_set_value(0.5)

        assert dut.get_value() == 0.5

    @pytest.mark.unit
    def test_do_get_value(self):
        """Should return the current value of the GTK3LevelBar."""
        dut = self.make_dut()
        dut.set_value(0.5)

        assert dut.do_get_value() == 0.5
