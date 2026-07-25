"""Test module for the GTK3TreeModelSort class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.treeview import GTK3TreeModelSort
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)
from tests.gtk3.treeview.constants import (
    EXPECTED_TREEMODELSORT_METHODS,
    EXPECTED_TREEMODELSORT_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3TreeModelSort(BaseGTK3GObjectTests):
    """Test class for the GTK3TreeModelSort class."""

    widget_class = GTK3TreeModelSort
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_TREEMODELSORT_METHODS
    expected_properties = EXPECTED_TREEMODELSORT_PROPERTIES

    def make_dut(self, model=None):
        """Override in subclass if constructor needs arguments."""
        return self.widget_class(model)

    @pytest.mark.unit
    def test_init_with_child_model(self):
        dut = self.make_dut(model=Gtk.ListStore())

        assert isinstance(dut.get_property("model"), Gtk.TreeModel)
        assert isinstance(dut.get_model(), Gtk.TreeModel)

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("model") is None
