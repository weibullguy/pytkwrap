"""Test module for the GTK3FileChooserNative class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.file import GTK3FileChooserNative
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)
from tests.gtk3.dialog.constants import (
    EXPECTED_NATIVEDIALOG_HANDLER_IDS,
    EXPECTED_NATIVEDIALOG_METHODS,
    EXPECTED_NATIVEDIALOG_PROPERTIES,
)
from tests.gtk3.file.constants import (
    EXPECTED_FILECHOOSERNATIVE_METHODS,
    EXPECTED_FILECHOOSERNATIVE_PROPERTIES,
)


@pytest.mark.usefixtures("skip_if_not_isolated")
@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3FileChooserNative(BaseGTK3GObjectTests):
    """Test class for the GTK3FileChooserNative class."""

    widget_class = GTK3FileChooserNative
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS | EXPECTED_NATIVEDIALOG_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_NATIVEDIALOG_METHODS
        + EXPECTED_FILECHOOSERNATIVE_METHODS
    )
    expected_properties = (
        EXPECTED_FILECHOOSERNATIVE_PROPERTIES | EXPECTED_NATIVEDIALOG_PROPERTIES
    )

    def make_dut(
        self,
        title: str | None = None,
        action: Gtk.FileChooserAction = Gtk.FileChooserAction.OPEN,
        accept_label: str | None = None,
        cancel_label: str | None = None,
    ):
        return self.widget_class(
            title=title,
            action=action,
            accept_label=accept_label,
            cancel_label=cancel_label,
        )

    @pytest.mark.unit
    def test_init(self):
        """Should create an instance of the widget class with attributes set to default
        values."""
        dut = self.make_dut()
        assert isinstance(dut, self.widget_class)

    @pytest.mark.unit
    def test_init_with_title(self):
        """Should create an instance of the widget class with the passed title."""
        dut = self.make_dut(title="Test Title")

        assert dut.get_property("title") == "Test Title"
        assert dut.do_get_property("title") == "Test Title"
        assert dut.get_title() == "Test Title"

    @pytest.mark.unit
    def test_init_with_action(self):
        """Should create an instance of the widget class with the passed action."""
        dut = self.make_dut(action=Gtk.FileChooserAction.SELECT_FOLDER)

        assert dut.get_action() == Gtk.FileChooserAction.SELECT_FOLDER

    @pytest.mark.unit
    def test_init_with_accept_label(self):
        """Should create an instance of the widget class with the passed accept
        label."""
        dut = self.make_dut(accept_label="Test Accept")

        assert dut.get_property("accept_label") == "Test Accept"
        assert dut.do_get_property("accept_label") == "Test Accept"
        assert dut.get_accept_label() == "Test Accept"

    @pytest.mark.unit
    def test_init_with_cancel_label(self):
        """Should create an instance of the widget class with the passed cancel
        label."""
        dut = self.make_dut(cancel_label="Test Cancel")

        assert dut.get_property("cancel_label") == "Test Cancel"
        assert dut.do_get_property("cancel_label") == "Test Cancel"
        assert dut.get_cancel_label() == "Test Cancel"

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("accept_label") is None
        assert dut.do_get_property("cancel_label") is None

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(accept_label="Test Accept", cancel_label="Test Cancel")
        )

        assert dut.get_property("accept_label") == "Test Accept"
        assert dut.get_accept_label() == "Test Accept"
        assert dut.get_property("cancel_label") == "Test Cancel"
        assert dut.get_cancel_label() == "Test Cancel"
