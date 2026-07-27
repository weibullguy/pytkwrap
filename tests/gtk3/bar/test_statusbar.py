"""Test module for the GTK3Statusbar class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.exceptions import PytkwrapError

# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.bar import GTK3Statusbar
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from tests.gtk3.bar.constants import (
    EXPECTED_STATUSBAR_HANDLER_IDS,
    EXPECTED_STATUSBAR_METHODS,
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


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3Statusbar(BaseGTK3GObjectTests):
    """Test class for the GTK3Statusbar class."""

    widget_class = GTK3Statusbar
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_default_height = -1
    expected_default_width = -1
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_STATUSBAR_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BOX_METHODS
        + EXPECTED_STATUSBAR_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_BOX_PROPERTIES
    )

    def make_dut(self, contexts=None):
        return self.widget_class(contexts)

    def test_callback(self, widget, context_id, message):
        """Callback method for testing."""
        assert isinstance(widget, GTK3Statusbar)
        assert isinstance(context_id, int)
        assert isinstance(message, str)
        assert message == "Test General Message"

    @pytest.mark.unit
    def test_init(self):
        """Should initialize an instance of a GTK3Statusbar."""
        dut = self.make_dut()

        assert isinstance(dut, GTK3Statusbar)
        assert dut.dic_properties == self.expected_properties
        assert dut.dic_context_id == {}

    @pytest.mark.unit
    def test_init_with_context_id(self):
        """Should initialize an instance of a GTK3Statusbar with a context ID."""
        dut = self.make_dut(contexts=["general", "errors"])

        assert isinstance(dut, GTK3Statusbar)
        assert dut.dic_context_id == {"general": 1, "errors": 2}
        assert dut.get_context_id("general") == 1
        assert dut.get_context_id("errors") == 2

    @pytest.mark.unit
    def test_do_add_message(self):
        """Should push a message to the statusbar."""
        dut = self.make_dut(contexts=["general", "errors"])
        dut.do_set_callbacks("text-pushed", self.test_callback)
        dut.do_add_message("general", "Test General Message")

        assert dut.dic_context_id["general"] == 1
        assert dut.get_context_id("general") == 1
        assert dut.dic_message_id["Test General Message"] == 1

    @pytest.mark.unit
    def test_do_add_message_no_context(self):
        """Should push a message to the statusbar with the default context."""
        dut = self.make_dut()

        with pytest.raises(PytkwrapError):
            dut.do_add_message("general", "Test General Message")

    @pytest.mark.unit
    def test_do_add_message_no_message(self):
        """Should push a message to the statusbar with an empty message."""
        dut = self.make_dut(contexts=["general", "errors"])

        with pytest.raises(PytkwrapError):
            dut.do_add_message("general", None)

    @pytest.mark.unit
    def test_do_remove_message(self):
        """Should remove a message from the statusbar."""
        dut = self.make_dut(contexts=["general", "errors"])
        dut.do_set_callbacks("text-popped", self.test_callback)
        dut.do_add_message("general", "Test General Message")
        dut.do_remove_message("general", "Test General Message")

    @pytest.mark.unit
    def test_do_remove_all_messages(self):
        """Should remove all messages from the statusbar."""
        dut = self.make_dut(contexts=["general", "errors"])
        dut.do_add_message("general", "Test General Message 1")
        dut.do_add_message("general", "Test General Message 2")
        dut.do_remove_message("general", remove_all=True)

    @pytest.mark.unit
    def test_do_remove_first_message(self):
        """Should remove the first message from the statusbar."""
        dut = self.make_dut(contexts=["general", "errors"])
        dut.do_add_message("general", "Test General Message 1")
        dut.do_add_message("general", "Test General Message 2")
        dut.do_remove_message("general")

    @pytest.mark.unit
    def test_do_remove_message_no_context(self):
        """Should raise a PytkwrapError when passed a context that does not exist."""
        dut = self.make_dut(contexts=["general", "errors"])
        dut.do_add_message("general", "Test General Message")

        with pytest.raises(PytkwrapError):
            dut.do_remove_message(None, "Test General Message")

    @pytest.mark.unit
    def test_do_remove_all_messages_no_context(self):
        """Should raise a PytkwrapError when passed a context that does not exist."""
        dut = self.make_dut(contexts=["general", "errors"])
        dut.do_add_message("general", "Test General Message 1")
        dut.do_add_message("general", "Test General Message 2")

        with pytest.raises(PytkwrapError):
            dut.do_remove_message("new_context", remove_all=True)

    @pytest.mark.unit
    def test_do_remove_message_no_message(self):
        """Should raise a PytkwrapError when passed a non-existent message."""
        dut = self.make_dut(contexts=["general", "errors"])
        dut.do_add_message("general", "Test General Message")

        with pytest.raises(PytkwrapError):
            dut.do_remove_message("general", "Non-existent message")

    @pytest.mark.integration
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("baseline_position") == Gtk.BaselinePosition.CENTER
        assert not dut.do_get_property("homogeneous")
        assert dut.do_get_property("spacing") == 0

    @pytest.mark.integration
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                baseline_position=Gtk.BaselinePosition.TOP,
                homogeneous=True,
                spacing=10,
            )
        )

        assert dut.get_property("baseline_position") == Gtk.BaselinePosition.TOP
        assert dut.get_baseline_position() == Gtk.BaselinePosition.TOP
        assert dut.get_property("homogeneous")
        assert dut.get_homogeneous()
        assert dut.get_property("spacing") == 10
        assert dut.get_spacing() == 10
