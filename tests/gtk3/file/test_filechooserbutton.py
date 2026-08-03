"""Test module for the GTK3FileChooserButton class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.dialog import GTK3Dialog
from pytkwrap.gtk3.file import GTK3FileChooserButton, GTK3FileChooserDialog
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
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
from tests.gtk3.file.constants import (
    EXPECTED_FILECHOOSERBUTTON_HANDLER_IDS,
    EXPECTED_FILECHOOSERBUTTON_METHODS,
    EXPECTED_FILECHOOSERBUTTON_PROPERTIES,
)


@pytest.mark.usefixtures("skip_if_not_isolated")
@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3FileChooserButton(BaseGTK3GObjectTests):
    """Test class for the GTK3FileChooserButton class."""

    widget_class = GTK3FileChooserButton
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_default_height = -1
    expected_default_width = -1
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_FILECHOOSERBUTTON_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BOX_METHODS
        + EXPECTED_FILECHOOSERBUTTON_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_BOX_PROPERTIES
        | EXPECTED_FILECHOOSERBUTTON_PROPERTIES
    )

    def make_dut(
        self, title="Select a File", action=Gtk.FileChooserAction.OPEN, dialog=None
    ):
        return self.widget_class(title, action, dialog)

    @pytest.mark.unit
    def test_init_with_title(self):
        """Should create a GTK3FileChooserButton with the passed title."""
        dut = self.make_dut(title="Test Title")

        assert dut.get_property("title") == "Test Title"
        assert dut.do_get_property("title") == "Test Title"
        assert dut.get_title() == "Test Title"

    @pytest.mark.unit
    def test_init_with_action(self):
        """Should create a GTK3FileChooserButton with the passed action."""
        dut = self.make_dut(action=Gtk.FileChooserAction.SELECT_FOLDER)

        assert dut.get_action() == Gtk.FileChooserAction.SELECT_FOLDER

    @pytest.mark.unit
    def test_init_with_dialog(self):
        """Should create a GTK3FileChooserButton with the passed dialog."""
        _dialog = GTK3FileChooserDialog()
        dut = self.make_dut(dialog=_dialog)

        assert isinstance(dut, GTK3FileChooserButton)

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("dialog") is None
        assert dut.do_get_property("title") == "Select a File"
        assert dut.do_get_property("width_chars") == -1

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _dialog = GTK3Dialog()

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                dialog=_dialog,
                title="Test Title",
                width_chars=25,
            )
        )

        assert dut.get_property("title") == "Test Title"
        assert dut.get_title() == "Test Title"
        assert dut.get_property("width_chars") == 25
        assert dut.get_width_chars() == 25
