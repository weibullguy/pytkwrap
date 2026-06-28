"""Test module for the GTK3ColorSelection class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.color import GTK3ColorSelection
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from tests.gtk3.color.constants import (
    EXPECTED_COLORSELECTION_HANDLER_IDS,
    EXPECTED_COLORSELECTION_METHODS,
    EXPECTED_COLORSELECTION_PROPERTIES,
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
    EXPECTED_BOX_METHODS,
    EXPECTED_BOX_PROPERTIES,
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
)


@pytest.mark.usefixtures("skip_if_not_isolated")
@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3ColorSelection(BaseGTK3GObjectTests):
    """Test class for the GTK3ColorSelection class."""

    widget_class = GTK3ColorSelection
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_default_height = -1
    expected_default_width = -1
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_COLORSELECTION_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BOX_METHODS
        + EXPECTED_COLORSELECTION_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_BOX_PROPERTIES
        | EXPECTED_COLORSELECTION_PROPERTIES
    )

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("current_alpha") == 65535
        assert dut.do_get_property("current_rgba") is None
        assert not dut.do_get_property("has_opacity_control")
        assert not dut.do_get_property("has_palette")

    @pytest.mark.unit
    def test_do_set_properties_current_alpha(self):
        """Should set properties to the values passed in the GTK3WidgetProperties.

        Setting the current RGBA will override the current_alpha value.
        """
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                current_alpha=32000,
                current_rgba=None,
                has_opacity_control=True,
                has_palette=True,
            )
        )

        assert dut.get_property("current_alpha") == 32000
        assert dut.get_current_alpha() == 32000
        assert dut.get_property("current_rgba").alpha == pytest.approx(0.488289)
        assert dut.get_current_rgba().alpha == pytest.approx(0.488289)
        assert dut.get_property("has_opacity_control")
        assert dut.get_has_opacity_control()
        assert dut.get_property("has_palette")
        assert dut.get_has_palette()

    @pytest.mark.unit
    def test_do_set_properties_current_rgba(self):
        """Should set properties to the values passed in the GTK3WidgetProperties.

        Setting the current RGBA will override the current_alpha value.
        """
        _rgba = Gdk.RGBA(0.5, 0.5, 0.75, 0.25)

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                current_rgba=_rgba,
                has_opacity_control=True,
            )
        )

        assert dut.get_property("current_alpha") == 16384
        assert dut.get_current_alpha() == 16384
        assert dut.get_property("current_rgba") == _rgba
        assert dut.get_current_rgba() == _rgba
        assert dut.get_property("has_opacity_control")
        assert dut.get_has_opacity_control()
        assert not dut.get_property("has_palette")
        assert not dut.get_has_palette()
