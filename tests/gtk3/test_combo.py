# pylint: skip-file
# type: ignore
#
#       tests.gtk3.test_combo.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""Test class for the GTK3ComboBox module algorithms and models."""

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.exceptions import UnkSignalError
from pytkwrap.gtk3._libs import GObject, Gtk
from pytkwrap.gtk3.combo import GTK3ComboBox
from pytkwrap.gtk3.mixins import GTK3DataWidgetAttributes
from pytkwrap.gtk3.widget import (
    GTK3WidgetProperties,
)

# pytkwrap Local Imports
from .conftest import BaseGTK3DataWidgetTests


SIMPLE_TEST_LIST = [
    "Index 1",
    "Index 2",
    "Index 3",
]
COMPOUND_TEST_LIST = [
    ["This", "is", "a"],
    ["test", "of", "the"],
    ["ComboBox", "not", "simple"],
]



@pytest.mark.order(4)
@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3ComboBox(BaseGTK3DataWidgetTests):
    """Test class for the GTK3ComboBox."""

    widget_class = GTK3ComboBox
    expected_default_height = 30
    expected_default_value = -1
    expected_default_width = 200
    expected_package = {0:{"test_field": "Index 1"},1:{"test_field": "is"}}

    def make_dut(
        self,
        index=0,
        simple=True,
        n_items=1,
        column_types=None,
        has_entry=False,
    ):
        """Create a device under test for the GTK3ComboBox."""
        return self.widget_class(
            index=index,
            simple=simple,
            n_items=n_items,
            column_types=column_types,
            has_entry=has_entry,
        )

    def mock_callback(self, combobox) -> None:
        """Mock callback to attach dut signals to."""
        assert isinstance(combobox, GTK3ComboBox)

    @pytest.fixture
    def compound_combo(self):
        """Create compound GTK3ComboBox device under test."""
        dut = self.make_dut(index=1, simple=False, n_items=3)
        dut.field = "test_field"
        dut.record_id = 1
        dut.send_topic = "combo_changed"
        dut.do_set_callbacks("changed", dut.on_changed)
        dut.do_load_combo(COMPOUND_TEST_LIST)
        return dut

    @pytest.fixture
    def simple_combo(self):
        """Create simple (default) GTK3ComboBox device under test."""
        dut = self.make_dut(column_types=[GObject.TYPE_STRING])
        dut.field = "test_field"
        dut.record_id = 0
        dut.send_topic = "combo_changed"
        dut.do_set_callbacks("changed", dut.on_changed)
        dut.do_load_combo(SIMPLE_TEST_LIST)
        return dut

    @pytest.fixture
    def subscribed_combo(self):
        """Create GTK3ComboBox dut that is subscribed to a pubsub message."""
        dut = self.make_dut(column_types=[GObject.TYPE_STRING])
        dut.field = "test_field"
        dut.do_set_callbacks("changed", dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")
        dut.do_load_combo(SIMPLE_TEST_LIST)
        yield dut
        pub.unsubscribe(dut.do_update, "rootTopic")

    @pytest.mark.unit
    def test_init(self):
        """Create a simple GTK3ComboBox when not passed any arguments."""
        super().test_init()

        dut = self.make_dut()

        assert isinstance(dut, GTK3ComboBox)
        assert self.expected_default_height == dut._DEFAULT_HEIGHT
        assert self.expected_default_width == dut._DEFAULT_WIDTH
        # All handler IDs should start at -1.
        assert all(_hid == -1 for _hid in dut.dic_handler_id.values())
        # ComboBox-specific attributes should be registered.
        for _attribute in GTK3ComboBox._GTK3_COMBO_ATTRIBUTES:
            assert _attribute in dut.dic_attributes
        # ComboBox-specific signals should be registered.
        for _signal in GTK3ComboBox._GTK3_COMBO_SIGNALS:
            assert _signal in dut.dic_handler_id
        # ComboBox-specific properties should be registered.
        for _property in GTK3ComboBox._GTK3_COMBO_PROPERTIES:
            assert _property in dut.dic_properties

        assert not dut.has_entry
        assert dut.index == 0
        assert dut.n_items == 1
        assert dut.simple
        assert dut.column_types == [GObject.TYPE_STRING]
        assert dut.get_model().get_n_columns() == 1
        assert dut.get_model().get_column_type(0) == GObject.TYPE_STRING
        assert dut.edit_signal == "changed"

    @pytest.mark.unit
    def test_init_combobox_compound(self):
        """Create a GTK3ComboBox with three columns when passed simple=False."""
        dut = self.make_dut(
            index=2,
            simple=False,
            n_items=3,
            column_types=[
                GObject.TYPE_STRING,
                GObject.TYPE_STRING,
                GObject.TYPE_STRING,
            ],
        )

        assert isinstance(dut, GTK3ComboBox)
        assert dut._DEFAULT_HEIGHT == 30
        assert dut._DEFAULT_WIDTH == 200
        assert dut.edit_signal == "changed"
        # All handler IDs should start at -1.
        assert all(_hid == -1 for _hid in dut.dic_handler_id.values())
        # ComboBox-specific attributes should be registered.
        for _attribute in GTK3ComboBox._GTK3_COMBO_ATTRIBUTES:
            assert _attribute in dut.dic_attributes
        # ComboBox-specific properties should be registered.
        for _property in GTK3ComboBox._GTK3_COMBO_PROPERTIES:
            assert _property in dut.dic_properties
        # ComboBox-specific signals should be registered.
        for _signal in GTK3ComboBox._GTK3_COMBO_SIGNALS:
            assert _signal in dut.dic_handler_id

        assert not dut.has_entry
        assert dut.index == 2
        assert dut.n_items == 3
        assert not dut.simple
        assert dut.column_types == [
            GObject.TYPE_STRING,
            GObject.TYPE_STRING,
            GObject.TYPE_STRING,
        ]
        assert dut.get_model().get_n_columns() == 3
        assert dut.get_model().get_column_type(0) == GObject.TYPE_STRING
        assert dut.get_model().get_column_type(1) == GObject.TYPE_STRING
        assert dut.get_model().get_column_type(2) == GObject.TYPE_STRING

    @pytest.mark.unit
    def test_init_combobox_custom_column_types(self):
        """Respect custom column_types passed by the caller."""
        dut = self.make_dut(
            n_items=2, column_types=[GObject.TYPE_INT, GObject.TYPE_STRING]
        )

        assert dut.column_types == [GObject.TYPE_INT, GObject.TYPE_STRING]
        assert dut.get_model().get_n_columns() == 2
        assert dut.get_model().get_column_type(0) == GObject.TYPE_INT
        assert dut.get_model().get_column_type(1) == GObject.TYPE_STRING

    @pytest.mark.unit
    def test_do_set_attributes_default(self):
        """Set the default attributes of a GTK3ComboBox when passed an empty
        WidgetAttributes."""
        super().test_do_set_attributes_default()

        dut = self.make_dut()
        dut.do_set_attributes(GTK3DataWidgetAttributes())

        assert dut.column_types == [GObject.TYPE_STRING]

    @pytest.mark.unit
    def test_do_set_attributes(self):
        """Set the GTK3ComboBox attributes to the values passed in a
        WidgetAttributes."""
        super().test_do_set_attributes()

        dut = self.make_dut()
        dut.do_set_attributes(
            GTK3DataWidgetAttributes(
                column_types=[GObject.TYPE_INT],
            )
        )

        assert dut.column_types == [GObject.TYPE_INT]

    @pytest.mark.unit
    def test_do_set_attributes_preserves_column_types(self):
        """Should not override column_types set in __init__ when no column_types key is
        passed in attributes."""
        dut = self.make_dut(
            n_items=2,
            column_types=[GObject.TYPE_INT, GObject.TYPE_STRING],
        )
        dut.do_set_attributes(GTK3WidgetProperties())

        assert dut.column_types == [GObject.TYPE_INT, GObject.TYPE_STRING]

    @pytest.mark.unit
    def test_do_set_attributes_overrides_column_types(self):
        """do_set_attributes() should override column_types when explicitly passed."""
        dut = self.make_dut(
            n_items=2,
            column_types=[GObject.TYPE_INT, GObject.TYPE_STRING],
        )
        dut.do_set_attributes(
            GTK3WidgetProperties(
                column_types=[GObject.TYPE_STRING, GObject.TYPE_STRING]
            )
        )

        assert dut.column_types == [GObject.TYPE_STRING, GObject.TYPE_STRING]

    @pytest.mark.unit
    def test_do_get_attribute(self):
        """Should retrieve the value of the passed attribute."""
        super().test_do_get_attribute()

        dut = self.make_dut()

        assert dut.do_get_attribute("column_types") == [GObject.TYPE_STRING]

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Set the default properties of a GTK3ComboBox when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.get_property("active") == -1
        assert dut.get_property("active-id") is None
        assert not dut.get_property("add-tearoffs")
        assert dut.get_property("border-width") == 0
        assert dut.get_property("button-sensitivity") == Gtk.SensitivityType.AUTO
        assert dut.get_property("can-focus")
        assert dut.get_property("column-span-column") == -1
        assert dut.get_property("entry-text-column") == -1
        assert not dut.get_property("has-entry")
        assert dut.get_property("height-request") == -1
        assert dut.get_property("id-column") == -1
        assert dut.get_property("model") is None
        assert dut.get_property("popup-fixed-width")
        assert dut.get_property("row-span-column") == -1
        assert dut.get_property("sensitive")
        assert dut.get_property("tooltip-markup") == (
            "Missing tooltip, please file an issue to have one added."
        )
        assert dut.get_property("visible")
        assert dut.get_property("width-request") == -1
        assert dut.get_property("wrap-width") == 0

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set the properties of a GTK3ComboBox."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                active=3,
                active_id="Value of the ID column for the active row.",
                border_width=5,
                button_sensitivity=Gtk.SensitivityType.ON,
                column_span_column=2,
                editing_canceled=False,
                entry_text_column=5,
                has_entry=True,
                has_frame=False,
                id_column=3,
                model=Gtk.ListStore(),
                popup_fixed_width=True,
                row_span_column=2,
                wrap_width=10,
                can_focus=True,
                height_request=70,
                sensitive=True,
                tooltip_markup="<b>Test Combo Tooltip</b>",
                tooltip_text="Test Combo Tooltip",
                visible=True,
                width_request=150,
            )
        )

        # Can't set 3 active because there is nothing in the ComboBox.
        assert dut.get_property("active") == -1
        assert dut.get_property("active-id") is None
        assert dut.get_property("column-span-column") == -1
        assert dut.get_property("entry-text-column") == -1
        assert not dut.get_property("has-entry")
        assert not dut.get_property("has-frame")
        assert dut.get_property("id-column") == -1
        assert dut.get_property("row-span-column") == -1

        assert dut.get_property("border-width") == 5
        assert dut.get_property("button-sensitivity") == Gtk.SensitivityType.ON
        assert dut.get_property("can-focus")
        assert not dut.get_property("editing-canceled")
        assert isinstance(dut.get_property("model"), Gtk.ListStore)
        assert dut.get_property("popup-fixed-width")
        assert dut.get_property("wrap-width") == 10
        assert dut.get_property("height-request") == 70
        assert dut.get_property("tooltip-markup") == "Test Combo Tooltip"
        assert dut.get_property("tooltip-text") == "Test Combo Tooltip"
        assert dut.get_property("width-request") == 150

    @pytest.mark.unit
    def test_do_load_combobox_simple(self):
        """Load a list of string values into a simple GTK3ComboBox."""
        dut = self.make_dut()
        dut.do_set_callbacks("changed", self.mock_callback)
        dut.do_load_combo(SIMPLE_TEST_LIST)

    @pytest.mark.unit
    def test_do_load_combobox_compound(self):
        """Load a list of string values into a non-simple GTK3ComboBox."""
        dut = self.make_dut(index=1, simple=False, n_items=3)
        dut.do_set_callbacks("changed", self.mock_callback)
        dut.do_load_combo(COMPOUND_TEST_LIST)

    @pytest.mark.unit
    def test_do_load_combobox_simple_not_string_list(self):
        """Raise a TypeError when passed a list of other than strings to load or a
        single non-string value."""
        _test_list = [0, 1, 2, 3, 4]
        dut = self.make_dut()
        dut.do_set_callbacks("changed", self.mock_callback)

        with pytest.raises(TypeError):
            dut.do_load_combo(_test_list)
        with pytest.raises(TypeError):
            dut.do_load_combo(10)

    @pytest.mark.unit
    def test_do_load_combobox_simple_contents(self):
        """Populate the model with a blank first entry followed by the provided
        entries."""
        dut = self.make_dut()
        dut.do_set_callbacks("changed", self.mock_callback)
        dut.do_load_combo(SIMPLE_TEST_LIST)

        _options = dut.do_get_options()
        assert _options == {0: "", 1: "Index 1", 2: "Index 2", 3: "Index 3"}

    @pytest.mark.unit
    def test_do_load_combobox_compound_contents(self):
        """Populate the model with a blank first row followed by the provided
        entries."""
        dut = self.make_dut(index=1, simple=False, n_items=3)
        dut.do_set_callbacks("changed", self.mock_callback)
        dut.do_load_combo(COMPOUND_TEST_LIST)

        _options = dut.do_get_options()
        assert _options == {0: "", 1: "is", 2: "of", 3: "not"}

    @pytest.mark.unit
    def test_do_load_combobox_clears_previous_entries(self):
        """Clear the model before loading new entries."""
        dut = self.make_dut()
        dut.do_set_callbacks("changed", self.mock_callback)
        dut.do_load_combo(SIMPLE_TEST_LIST)
        dut.do_load_combo(["Only Entry"])

        _options = dut.do_get_options()
        assert len(_options) == 2  # blank + one entry
        assert _options[1] == "Only Entry"

    @pytest.mark.unit
    def test_do_load_combobox_no_model(self):
        """Return None without raising if model is None."""
        dut = self.make_dut()
        dut.set_model(None)
        dut.do_load_combo(SIMPLE_TEST_LIST)

    @pytest.mark.unit
    def test_do_get_options_simple(self):
        """Return a dict of all the options available in a simple GTK3ComboBox."""
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
    def test_do_get_options_compound(self):
        """Return a dict of all the options available in a non-simple GTK3ComboBox."""
        dut = self.make_dut(index=1, simple=False, n_items=3)
        dut.do_set_callbacks("changed", self.mock_callback)
        dut.do_load_combo(COMPOUND_TEST_LIST)

        _options = dut.do_get_options()
        assert isinstance(_options, dict)
        assert _options == {0: "", 1: "is", 2: "of", 3: "not"}

    @pytest.mark.unit
    def test_do_get_options_empty(self):
        """Return an empty dict when the model has no rows."""
        dut = self.make_dut()

        assert dut.do_get_options() == {}

    @pytest.mark.unit
    def test_do_get_options_no_model(self):
        """Return an empty dict when the model is None."""
        dut = self.make_dut()
        dut.set_model(None)

        assert dut.do_get_options() == {}

    @pytest.mark.unit
    def test_get_value_simple(self):
        """Return the value from a simple GTK3ComboBox at index X."""
        dut = self.make_dut(column_types=[GObject.TYPE_STRING])
        dut.field = "test_field"
        dut.do_set_callbacks("changed", dut.on_changed)
        dut.do_load_combo(SIMPLE_TEST_LIST)

        assert not dut.do_get_value()
        for _idx in [1, 2, 3]:
            dut.set_active(_idx)
            assert dut.do_get_value() == f"Index {_idx}"

    @pytest.mark.unit
    def test_get_value_compound(self):
        """Return the value from a compound GTK3ComboBox at index X."""
        dut = self.make_dut(index=1, simple=False, n_items=3)
        dut.edit_signal = "changed"
        dut.field = "test_field"
        dut.do_set_callbacks("changed", dut.on_changed)
        dut.do_load_combo(COMPOUND_TEST_LIST)

        assert not dut.do_get_value(0)
        assert not dut.do_get_value(1)
        assert not dut.do_get_value(2)
        dut.set_active(1)
        assert dut.do_get_value(0) == "This"
        assert dut.do_get_value(1) == "is"
        assert dut.do_get_value(2) == "a"
        dut.set_active(2)
        assert dut.do_get_value(0) == "test"
        assert dut.do_get_value(1) == "of"
        assert dut.do_get_value(2) == "the"
        dut.set_active(3)
        assert dut.do_get_value(0) == "ComboBox"
        assert dut.do_get_value(1) == "not"
        assert dut.do_get_value(2) == "simple"

    @pytest.mark.unit
    def test_get_value_no_model(self):
        """Return an empty string when the model is None."""
        dut = self.make_dut()
        dut.set_model(None)

        assert not dut.do_get_value()

    @pytest.mark.unit
    def test_get_value_no_active_selection(self):
        """Return an empty string when no row is active."""
        dut = self.make_dut()
        dut.do_load_combo(SIMPLE_TEST_LIST)

        assert dut.get_active() == -1
        assert not dut.do_get_value()

    @pytest.mark.unit
    def test_do_update_simple(self, subscribed_combo):
        """Update a simple GTK3ComboBox with the data package value."""
        pub.sendMessage("rootTopic", package={"test_field": 2})

        assert subscribed_combo.get_active() == 2
        assert subscribed_combo.do_get_value() == "Index 2"

    @pytest.mark.unit
    def test_do_update_simple_unknown_signal(self, simple_combo):
        """Raise a key error with an unknown edit signal name."""
        pub.subscribe(self.do_update_error_handler, "do_log_error")
        pub.subscribe(simple_combo.do_update, "rootTopic")
        simple_combo.edit_signal = "edit_signal"

        with pytest.raises(UnkSignalError):
            pub.sendMessage("rootTopic", package={"test_field": 2})

        assert simple_combo.get_active() == -1
        assert not simple_combo.do_get_value()

    @pytest.mark.unit
    def test_do_update_compound(self, compound_combo):
        """Update a compound GTK3ComboBox with the data package value."""
        compound_combo.edit_signal = "changed"
        pub.subscribe(compound_combo.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={"test_field": 2})

        assert compound_combo.get_active() == 2
        assert compound_combo.do_get_value(0) == "test"
        assert compound_combo.do_get_value(1) == "of"
        assert compound_combo.do_get_value(2) == "the"

    @pytest.mark.unit
    def test_do_update_wrong_field(self, subscribed_combo):
        """Do nothing when the package field doesn't match."""
        subscribed_combo.set_active(1)

        pub.sendMessage("rootTopic", package={"wrong_field": 2})

        assert subscribed_combo.get_active() == 1  # unchanged

    @pytest.mark.unit
    def test_do_update_non_int_value(self, subscribed_combo):
        """Do nothing when the value is not an int."""
        subscribed_combo.set_active(1)

        pub.sendMessage("rootTopic", package={"test_field": "Index 2"})

        assert subscribed_combo.get_active() == 1  # unchanged

    @pytest.mark.unit
    def test_do_update_none_value(self, subscribed_combo):
        """Handle a None value via none_to_default."""
        subscribed_combo.default = 0

        pub.sendMessage("rootTopic", package={"test_field": None})

        assert subscribed_combo.get_active() == 0  # falls back to default

    @pytest.mark.unit
    def test_on_changed_simple(self, simple_combo):
        """Call on_changed() when a simple GTK3ComboBox value changes."""
        pub.subscribe(self.mock_handler, simple_combo.send_topic)

        simple_combo.set_active(1)

    @pytest.mark.unit
    def test_on_changed_unknown_signal(self, simple_combo):
        """Raise a KeyError with an unknown edit signal name."""
        pub.subscribe(self.on_changed_error_handler, "do_log_error")
        simple_combo.edit_signal = "edit_signal"
        pub.subscribe(self.mock_handler, simple_combo.send_topic)

        simple_combo.set_active(1)

    @pytest.mark.unit
    def test_on_changed_compound(self, compound_combo):
        """Call on_changed() when a compound GTK3ComboBox value changes."""
        pub.subscribe(self.mock_handler, compound_combo.send_topic)

        compound_combo.set_active(1)
