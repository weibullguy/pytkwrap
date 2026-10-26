"""Test module for the GTK3RadioToolButton class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.gtk3 import GTK3Image

# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.io import GTK3Label
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.tool import GTK3RadioToolButton
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
    EXPECTED_BIN_METHODS,
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
)
from tests.gtk3.tool.constants import (
    EXPECTED_RADIOTOOLBUTTON_HANDLER_IDS,
    EXPECTED_RADIOTOOLBUTTON_METHODS,
    EXPECTED_RADIOTOOLBUTTON_PROPERTIES,
    EXPECTED_TOGGLETOOLBUTTON_HANDLER_IDS,
    EXPECTED_TOGGLETOOLBUTTON_METHODS,
    EXPECTED_TOGGLETOOLBUTTON_PROPERTIES,
    EXPECTED_TOOLITEM_HANDLER_IDS,
    EXPECTED_TOOLITEM_METHODS,
    EXPECTED_TOOLITEM_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3RadioToolButton(BaseGTK3GObjectTests):
    """Test class for the GTK3RadioToolButton class."""

    widget_class = GTK3RadioToolButton
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_TOOLITEM_HANDLER_IDS
        | EXPECTED_TOGGLETOOLBUTTON_HANDLER_IDS
        | EXPECTED_RADIOTOOLBUTTON_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_TOOLITEM_METHODS
        + EXPECTED_TOGGLETOOLBUTTON_METHODS
        + EXPECTED_RADIOTOOLBUTTON_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_TOOLITEM_PROPERTIES
        | EXPECTED_TOGGLETOOLBUTTON_PROPERTIES
        | EXPECTED_RADIOTOOLBUTTON_PROPERTIES
    )

    def make_dut(self, group=None):
        dut = self.widget_class(group=group)
        self.expected_properties["group"] = [dut._radio_button]

        return dut

    @pytest.mark.unit
    def test_init_with_group(self):
        """Should create a GTK3RadioToolButton with a group."""
        _radiobutton = GTK3RadioToolButton()
        dut = self.make_dut(group=[_radiobutton._radio_button])

        assert dut.get_group() == [_radiobutton._radio_button, dut._radio_button]

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("group") == [dut._radio_button]

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _radiotoolbutton = GTK3RadioToolButton()

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                group=[_radiotoolbutton._radio_button],
            )
        )

        assert dut.get_group() == [_radiotoolbutton._radio_button, dut._radio_button]

    @pytest.mark.unit
    def test_get_active(self):
        """Should return the active state of the GTK3RadioToolButton."""
        dut = self.make_dut()

        assert dut.get_active()

    @pytest.mark.unit
    def test_get_icon_name(self):
        """Should return the icon name of the GTK3RadioToolButton."""
        dut = self.make_dut()

        assert dut.get_icon_name() is None

    @pytest.mark.unit
    def test_get_icon_widget(self):
        """Should return the icon widget of the GTK3RadioToolButton."""
        dut = self.make_dut()

        assert dut.get_icon_widget() is None

    @pytest.mark.unit
    def test_get_label(self):
        """Should return the label name of the GTK3RadioToolButton."""
        dut = self.make_dut()

        assert dut.get_label() == ""

    @pytest.mark.unit
    def test_get_label_widget(self):
        """Should return the label widget of the GTK3RadioToolButton."""
        dut = self.make_dut()

        assert dut.get_label_widget() is None

    @pytest.mark.unit
    def test_get_use_underline(self):
        """Should return the underline state of the GTK3RadioToolButton."""
        dut = self.make_dut()

        assert not dut.get_use_underline()

    # TODO: Figure out the set_active() when building example and we can visualize
    #  the group of GTK3RadioToolButton actions.
    @pytest.mark.skip
    def test_set_active(self):
        """Should set the active state of the GTK3RadioToolButton."""
        _radiotoolbutton = GTK3RadioToolButton()
        dut = self.make_dut()
        dut.set_group([_radiotoolbutton._radio_button])

        _radiotoolbutton._radio_button.set_active(True)

        assert not dut.get_active()

        dut.set_active(True)

        assert dut.get_active()

    @pytest.mark.unit
    def test_set_group(self):
        """Should set the group of the GTK3RadioToolButton."""
        _radiotoolbutton = GTK3RadioToolButton()
        dut = self.make_dut()
        dut.set_group([_radiotoolbutton._radio_button])

        assert dut.get_group() == [_radiotoolbutton._radio_button, dut._radio_button]

    @pytest.mark.unit
    def test_set_icon_name(self):
        """Should set the icon to the icon name from the current icon theme."""
        dut = self.make_dut()

        dut.set_icon_name("edit-copy")
        assert dut.get_icon_name() == "edit-copy"

    @pytest.mark.unit
    def test_set_icon_widget(self):
        """Should set the icon widget of the GTK3RadioToolButton."""
        dut = self.make_dut()

        _image = GTK3Image()
        dut.set_icon_widget(_image)

        assert dut.get_icon_widget() == _image

    @pytest.mark.unit
    def test_set_label(self):
        """Should set the label name of the GTK3RadioToolButton."""
        dut = self.make_dut()

        dut.set_label("test")

        assert dut.get_label() == "test"

    @pytest.mark.unit
    def test_set_label_widget(self):
        """Should set the label widget of the GTK3RadioToolButton."""
        _label = GTK3Label()

        dut = self.make_dut()
        dut.set_label_widget(_label)

        assert dut.get_label_widget() == _label

    @pytest.mark.unit
    def test_set_use_underline(self):
        """Should set the use underline of the GTK3RadioToolButton."""
        dut = self.make_dut()

        dut.set_use_underline(True)

        assert dut.get_use_underline() == True
