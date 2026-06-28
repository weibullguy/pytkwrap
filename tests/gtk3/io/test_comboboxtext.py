"""Test module for the GTK3ComboBoxText class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.exceptions import WrongTypeError

# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import GObject, Gtk
from pytkwrap.gtk3.io import GTK3ComboBoxText
from tests.gtk3.conftest import BaseGTK3DataWidgetTests
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
from tests.gtk3.io.constants import (
    EXPECTED_COMBOBOX_ATTRIBUTES,
    EXPECTED_COMBOBOX_HANDLER_IDS,
    EXPECTED_COMBOBOX_METHODS,
    EXPECTED_COMBOBOX_PROPERTIES,
    EXPECTED_COMBOBOXTEXT_METHODS,
    SIMPLE_TEST_LIST,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3ComboBoxText(BaseGTK3DataWidgetTests):
    """Test class for the GTK3ComboBoxText."""

    widget_class = GTK3ComboBoxText
    expected_attributes = (
        EXPECTED_GOBJECT_ATTRIBUTES
        | EXPECTED_WIDGET_ATTRIBUTES
        | EXPECTED_COMBOBOX_ATTRIBUTES
    )
    expected_default_height = 30
    expected_default_width = 200
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_COMBOBOX_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_COMBOBOX_METHODS
        + EXPECTED_COMBOBOXTEXT_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_COMBOBOX_PROPERTIES
    )

    def make_dut(
        self,
        has_entry=False,
    ):
        """Create a device under test for the GTK3ComboBox."""
        return self.widget_class(
            has_entry=has_entry,
        )

    @pytest.mark.unit
    def test_init(self):
        """Create a simple GTK3ComboBox when not passed any arguments."""
        super().test_init()

        dut = self.make_dut()

        assert isinstance(dut, GTK3ComboBoxText)
        assert self.expected_default_height == dut._DEFAULT_HEIGHT
        assert self.expected_default_width == dut._DEFAULT_WIDTH

        assert dut.dic_attributes["column_types"] == [GObject.TYPE_STRING]
        assert not dut.dic_properties["has_entry"]
        assert dut.display_index == 0
        assert dut.n_items == 1
        assert dut.simple
        assert dut.get_model().get_n_columns() == 1
        assert dut.get_model().get_column_type(0) == GObject.TYPE_STRING

    @pytest.mark.unit
    def test_init_with_entry(self):
        """Initiate a GTK3ComboBoxText with an entry."""
        dut = self.make_dut(True)

        assert isinstance(dut, GTK3ComboBoxText)
        assert dut.dic_attributes["column_types"] == [GObject.TYPE_STRING]
        assert dut.dic_properties["has_entry"]
        assert dut.display_index == 0
        assert dut.n_items == 1
        assert dut.simple
        assert dut.get_model().get_n_columns() == 1
        assert dut.get_model().get_column_type(0) == GObject.TYPE_STRING

    @pytest.mark.unit
    def test_do_load(self):
        """Load a list of string values into a simple GTK3ComboBox."""
        dut = self.make_dut()
        dut.do_set_callbacks("changed", self.mock_callback)
        dut.do_load_combo(SIMPLE_TEST_LIST)

        dut.set_active(0)
        assert dut.get_active_text() == ""
        dut.set_active(1)
        assert dut.get_active_text() == "Index 1"
        dut.set_active(2)
        assert dut.get_active_text() == "Index 2"
        dut.set_active(3)
        assert dut.get_active_text() == "Index 3"

    @pytest.mark.unit
    def test_do_load_not_string_list(self):
        """Raise a WrongTypeError when passed a list of other than strings to load."""
        dut = self.make_dut()
        dut.do_set_callbacks("changed", self.mock_callback)

        with pytest.raises(WrongTypeError):
            dut.do_load_combo([0, 1, 2, 3, 4])

    @pytest.mark.unit
    def test_do_load_clears_previous_entries(self):
        """Clear the GTK3ComboBoxText before loading new entries."""
        dut = self.make_dut()
        dut.do_set_callbacks("changed", self.mock_callback)
        dut.do_load_combo(SIMPLE_TEST_LIST)
        dut.do_load_combo(["Only Entry"])

        dut.set_active(0)
        assert dut.get_active_text() == ""
        dut.set_active(1)
        assert dut.get_active_text() == "Only Entry"

    @pytest.mark.unit
    def test_do_get_options(self):
        """Return a dict of all the options available in a simple GTK3ComboBoxText."""
        dut = self.make_dut()
        dut.do_set_callbacks("changed", self.mock_callback)
        dut.do_load_combo(SIMPLE_TEST_LIST)

        _options = dut.do_get_options()
        assert isinstance(_options, dict)
        assert _options == {
            0: "",
            1: "Index 1",
            2: "Index 2",
            3: "Index 3",
        }

    @pytest.mark.unit
    def test_do_get_options_empty(self):
        """Return an empty dict when the GTK3ComboBoxText has no entries."""
        dut = self.make_dut()

        assert dut.do_get_options() == {}

    @pytest.mark.unit
    def test_do_set_value_wrong_type(self):
        """Should raise a WrongTypeError when passed a wrong data type."""
        dut = self.make_dut()

        with pytest.raises(WrongTypeError):
            dut.do_set_value("2")

    @pytest.mark.unit
    def test_get_value(self):
        """Return the value from a simple GTK3ComboBoxText at index X."""
        dut = self.make_dut()
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
        dut.do_load_combo(SIMPLE_TEST_LIST)

        assert not dut.do_get_value()
        for _idx in [1, 2, 3]:
            dut.set_active(_idx)
            assert dut.do_get_value() == f"Index {_idx}"

    @pytest.mark.unit
    def test_get_value_no_active_selection(self):
        """Return an empty string when no row is active."""
        dut = self.make_dut()
        dut.do_load_combo(SIMPLE_TEST_LIST)

        assert dut.get_active() == -1
        assert not dut.do_get_value()

    @pytest.mark.unit
    def test_do_update(self):
        """Update a simple GTK3ComboBoxText with the data package value."""
        dut = self.make_dut()
        dut.dic_attributes["send_topic"] = "combo_changed"
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")
        dut.do_load_combo(SIMPLE_TEST_LIST)

        dut.set_active(2)
        pub.sendMessage("rootTopic", package={"test_field": 2})

        assert dut.get_active() == 2
        assert dut.do_get_value() == "Index 2"

        pub.unsubscribe(dut.do_update, "rootTopic")

    @pytest.mark.unit
    def test_do_update_non_int_value(self):
        """Do nothing when the value is not an int."""
        dut = self.make_dut()
        dut.dic_attributes["send_topic"] = "combo_changed"
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")
        dut.do_load_combo(SIMPLE_TEST_LIST)
        dut.set_active(1)
        pub.sendMessage("rootTopic", package={"test_field": "Index 2"})

        assert dut.get_active() == 1  # unchanged

        pub.unsubscribe(dut.do_update, "rootTopic")

    @pytest.mark.unit
    def test_on_changed(self):
        """Call on_changed() when a simple GTK3ComboBox value changes."""
        dut = self.make_dut()
        dut.index = 1
        dut.dic_attributes["send_topic"] = "combo_changed"
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
        dut.do_load_combo(SIMPLE_TEST_LIST)

        pub.subscribe(self.mock_handler, dut.dic_attributes["send_topic"])

        dut.set_active(1)

        pub.unsubscribe(self.mock_handler, dut.dic_attributes["send_topic"])
