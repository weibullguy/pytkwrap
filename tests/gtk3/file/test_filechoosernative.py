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

        assert dut.do_get_property("accept_label") == "Test Accept"
        assert dut.do_get_property("cancel_label") == "Test Cancel"
