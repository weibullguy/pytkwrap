"""Test module for the GTK3FontChooserDialog class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, GdkPixbuf, Gtk
from pytkwrap.gtk3.font import GTK3FontChooserDialog
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
from tests.gtk3.dialog.constants import (
    EXPECTED_DIALOG_HANDLER_IDS,
    EXPECTED_DIALOG_METHODS,
    EXPECTED_DIALOG_PROPERTIES,
)
from tests.gtk3.font.constants import EXPECTED_FONTCHOOSERDIALOG_PROPERTIES
from tests.gtk3.window.constants import (
    EXPECTED_WINDOW_HANDLER_IDS,
    EXPECTED_WINDOW_METHODS,
    EXPECTED_WINDOW_PROPERTIES,
)


@pytest.mark.usefixtures("skip_if_not_isolated")
@pytest.mark.usefixtures("filter_stderr")
class TestGTK3FontChooserDialog(BaseGTK3GObjectTests):
    """Test class for the GTK3FontChooserDialog class."""

    widget_class = GTK3FontChooserDialog
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_WINDOW_HANDLER_IDS
        | EXPECTED_DIALOG_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_WINDOW_METHODS
        + EXPECTED_DIALOG_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_WINDOW_PROPERTIES
        | EXPECTED_DIALOG_PROPERTIES
        | EXPECTED_FONTCHOOSERDIALOG_PROPERTIES
    )

    def make_dut(self, title="Choose a Font", transient_for=None):
        """Create a device under test for the GTK3FontChooserDialog."""
        return self.widget_class(title=title, transient_for=transient_for)

    @pytest.mark.unit
    def test_init(self):
        """Should initialize an instance of a GTK3FontChooserDialog."""
        super().test_init()

        dut = self.make_dut()

        assert isinstance(dut, GTK3FontChooserDialog)
        assert dut.do_get_property("title") == "Choose a Font"
        assert dut.get_property("title") == "Choose a Font"
        assert dut.get_title() == "Choose a Font"
        assert dut.get_property("transient_for") is None
        assert dut.get_transient_for() is None

    @pytest.mark.unit
    def test_init_with_title(self):
        """Should initialize an instance of a GTK3FontChooserDialog with a title."""
        dut = self.make_dut(title="Test Font Chooser Dialog Title")

        assert dut.do_get_property("title") == "Test Font Chooser Dialog Title"
        assert dut.get_property("title") == "Test Font Chooser Dialog Title"
        assert dut.get_title() == "Test Font Chooser Dialog Title"

    @pytest.mark.unit
    def test_init_with_transient_for(self):
        """Should initialize an instance of a GTK3FontChooserDialog with a
        transient_for."""
        _window = Gtk.Window()

        dut = self.make_dut(transient_for=_window)

        assert dut.do_get_property("transient_for") == _window
        assert dut.get_property("transient_for") == _window
        assert dut.get_transient_for() == _window
