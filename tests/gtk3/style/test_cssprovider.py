"""Test module for the GTK3CssProvider class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gio, Gtk
from pytkwrap.gtk3.style.cssprovider import GTK3CssProvider
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)
from tests.gtk3.style.constants import (
    EXPECTED_CSSPROVIDER_HANDLER_IDS,
    EXPECTED_CSSPROVIDER_METHODS,
)

CSS_DATA = """* {
  font-family: "arial";
  font-size: 11pt;
  font-stretch: initial;
  font-style: initial;
  font-variant: initial;
  font-weight: initial;
}

GtkWindow {
  background-color: rgb(18,18,19);
  background-size: 20px 20px;
}

.button {
  border-bottom-style: solid;
  border-left-style: solid;
  border-right-style: solid;
  border-top-style: solid;
  color: rgb(0,0,0);
}

:hover.button {
  background-color: rgb(72,112,188);
  padding-bottom: 12px;
  padding-left: 48px;
  padding-right: 48px;
  padding-top: 12px;
}
"""


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3CssProvider(BaseGTK3GObjectTests):
    """Test class for the GTK3CssProvider class."""

    widget_class = GTK3CssProvider
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS | EXPECTED_CSSPROVIDER_HANDLER_IDS
    )
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_CSSPROVIDER_METHODS

    @pytest.mark.unit
    def test_do_load_styling_from_data(self):
        """Load the CSS information from a string."""
        dut = self.make_dut()

        assert dut.do_load_styling(data=CSS_DATA) is None
        assert dut.to_string() == CSS_DATA

    @pytest.mark.unit
    def test_do_load_styling_from_file(self):
        """Load the CSS information from a Gio.File."""
        _file = Gio.File.new_for_path("tests/data/gtk3/test_theme.css")
        dut = self.make_dut()

        assert dut.do_load_styling(file=_file)

        assert dut.to_string() == CSS_DATA

    @pytest.mark.unit
    def test_do_load_styling_from_path(self):
        """Load the CSS information from a path to a CSS file."""
        dut = self.make_dut()

        assert dut.do_load_styling(path="tests/data/gtk3/test_theme.css")
        assert dut.to_string() == CSS_DATA
