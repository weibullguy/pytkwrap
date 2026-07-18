"""Test module for the GTK3EntryCompletion class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.text import GTK3EntryCompletion
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)
from tests.gtk3.text.constants import (
    EXPECTED_ENTRYCOMPLETION_HANDLER_IDS,
    EXPECTED_ENTRYCOMPLETION_METHODS,
    EXPECTED_ENTRYCOMPLETION_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3EntryCompletion(BaseGTK3GObjectTests):
    """Test class for the GTK3EntryCompletion class."""

    widget_class = GTK3EntryCompletion
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS | EXPECTED_ENTRYCOMPLETION_HANDLER_IDS
    )
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_ENTRYCOMPLETION_METHODS
    expected_properties = EXPECTED_ENTRYCOMPLETION_PROPERTIES

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("cell_area") is None
        assert not dut.do_get_property("inline_completion")
        assert not dut.do_get_property("inline_selection")
        assert dut.do_get_property("minimum_key_length") == 1
        assert dut.do_get_property("model") is None
        assert dut.do_get_property("popup_completion")
        assert dut.do_get_property("popup_set_width")
        assert dut.do_get_property("popup_single_match")
        assert dut.do_get_property("text_column") == -1

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _model = Gtk.ListStore(str)

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                cell_area=None,
                inline_completion=True,
                inline_selection=True,
                minimum_key_length=5,
                model=_model,
                popup_completion=False,
                popup_set_width=False,
                popup_single_match=False,
                text_column=1,
            )
        )

        assert isinstance(dut.get_property("cell_area"), Gtk.CellArea)
        assert dut.get_property("inline_completion")
        assert dut.get_inline_completion()
        assert dut.get_property("inline_selection")
        assert dut.get_inline_selection()
        assert dut.get_property("minimum_key_length") == 5
        assert dut.get_minimum_key_length() == 5
        assert dut.get_property("model") == _model
        assert dut.get_model() == _model
        assert not dut.get_property("popup_completion")
        assert not dut.get_popup_completion()
        assert not dut.get_property("popup_set_width")
        assert not dut.get_popup_set_width()
        assert not dut.get_property("popup_single_match")
        assert not dut.get_popup_single_match()
        assert dut.get_property("text_column") == 1
        assert dut.get_text_column() == 1
