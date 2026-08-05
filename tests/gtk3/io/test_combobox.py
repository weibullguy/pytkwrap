"""Test module for the GTK3ComboBox class.

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
from pytkwrap.gtk3.io import GTK3ComboBox
from pytkwrap.gtk3.mixins import GTK3WidgetAttributes, GTK3WidgetProperties
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
    COMPOUND_TEST_LIST,
    EXPECTED_COMBOBOX_ATTRIBUTES,
    EXPECTED_COMBOBOX_HANDLER_IDS,
    EXPECTED_COMBOBOX_METHODS,
    EXPECTED_COMBOBOX_PROPERTIES,
    SIMPLE_TEST_LIST,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3ComboBox(BaseGTK3DataWidgetTests):
    """Test class for the GTK3ComboBox."""

    widget_class = GTK3ComboBox
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
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_COMBOBOX_PROPERTIES
    )

    def make_dut(self, has_entry=False, model=None):
        """Create a device under test for the GTK3ComboBox."""
        return self.widget_class(has_entry=has_entry, model=model)

    @pytest.fixture
    def compound_combo(self):
        """Create compound GTK3ComboBox device under test."""
        _model = Gtk.ListStore(
            GObject.TYPE_STRING, GObject.TYPE_STRING, GObject.TYPE_STRING
        )
        dut = self.make_dut(model=_model)
        dut.index = 1
        dut.dic_attributes["send_topic"] = "combo_changed"
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
        dut.do_load_combo(COMPOUND_TEST_LIST)
        return dut

    @pytest.fixture
    def simple_combo(self):
        """Create simple (default) GTK3ComboBox device under test."""
        _model = Gtk.ListStore(GObject.TYPE_STRING)
        dut = self.make_dut(model=_model)
        dut.index = 1
        dut.dic_attributes["send_topic"] = "combo_changed"
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
        dut.do_load_combo(SIMPLE_TEST_LIST)
        return dut

    @pytest.fixture
    def subscribed_combo(self):
        """Create GTK3ComboBox dut that is subscribed to a pubsub message."""
        _model = Gtk.ListStore(GObject.TYPE_STRING)
        dut = self.make_dut(model=_model)
        dut.index = 1
        dut.dic_attributes["send_topic"] = "combo_changed"
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.do_update)
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
        for _attribute in GTK3ComboBox._GTK3_COMBOBOX_ATTRIBUTES:
            assert _attribute in dut.dic_attributes
        # ComboBox-specific properties should be registered.
        for _property in GTK3ComboBox._GTK3_COMBOBOX_PROPERTIES:
            assert _property in dut.dic_properties
        # ComboBox-specific signals should be registered.
        for _signal in GTK3ComboBox._GTK3_COMBOBOX_SIGNALS:
            assert _signal in dut.dic_handler_id

        assert not dut.dic_properties["has_entry"]

    @pytest.mark.unit
    def test_init_with_entry(self):
        """Create a GTK3ComboBox with an entry when passed has_entry=True."""
        dut = self.make_dut(has_entry=True)

        assert isinstance(dut, GTK3ComboBox)
        assert dut.dic_properties["has_entry"]
        assert dut.get_has_entry()

    @pytest.mark.unit
    def test_init_with_model(self):
        """Create a GTK3ComboBox with a model when passed a Gtk.TreeModel."""
        _model = Gtk.ListStore(GObject.TYPE_INT, GObject.TYPE_STRING)
        dut = self.make_dut(model=_model)

        assert isinstance(dut, GTK3ComboBox)
        assert not dut.dic_properties["has_entry"]
        assert not dut.get_has_entry()
        assert dut.get_model() == _model
        assert dut.get_model().get_n_columns() == 2
        assert dut.get_model().get_column_type(0) == GObject.TYPE_INT
        assert dut.get_model().get_column_type(1) == GObject.TYPE_STRING

    @pytest.mark.unit
    def test_init_with_model_and_entry(self):
        """Create a GTK3ComboBox with an entry and a model when passed a Gtk.TreeModel
        and has_entry=True."""
        _model = Gtk.ListStore(GObject.TYPE_INT, GObject.TYPE_STRING)
        dut = self.make_dut(has_entry=True, model=_model)

        assert isinstance(dut, GTK3ComboBox)
        assert dut.dic_properties["has_entry"]
        assert dut.get_has_entry()
        assert dut.get_model() == _model
        assert dut.get_model().get_n_columns() == 2
        assert dut.get_model().get_column_type(0) == GObject.TYPE_INT
        assert dut.get_model().get_column_type(1) == GObject.TYPE_STRING

    @pytest.mark.unit
    def test_do_get_attribute(self):
        """Should return the value of the attribute name."""
        super().test_do_get_attribute()

        dut = self.make_dut()

        assert dut.do_get_attribute("default_value") == -1
        assert dut.do_get_attribute("edit_signal") == "changed"

    @pytest.mark.unit
    def test_do_set_attributes_default(self):
        """Should set attributes to default values when passed an empty
        GTK3WidgetAttributes."""
        dut = self.make_dut()
        dut.do_set_attributes(GTK3WidgetAttributes())

        assert dut.do_get_attribute("default_value") == -1
        assert dut.do_get_attribute("edit_signal") == "changed"

    @pytest.mark.unit
    def test_do_set_attributes(self):
        """Should set attributes to the values passed in the GTK3WidgetAttributes."""
        dut = self.make_dut()
        dut.do_set_attributes(
            GTK3WidgetAttributes(
                default_value=1,
                edit_signal="combobox_changed",
            )
        )

        assert dut.do_get_attribute("default_value") == 1
        assert dut.do_get_attribute("edit_signal") == "combobox_changed"

    @pytest.mark.unit
    @pytest.mark.filterwarnings("ignore:gtk_combo_box_set_entry_text_column")
    def test_do_set_properties_default(self, filter_stderr):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.do_get_property("active") == -1
        assert dut.do_get_property("active_id") is None
        assert dut.do_get_property("column_span_column") == -1
        assert dut.do_get_property("entry_text_column") == -1
        assert not dut.do_get_property("has_entry")
        assert dut.do_get_property("has_frame")
        assert dut.do_get_property("id_column") == -1
        assert dut.do_get_property("row_span_column") == -1
        assert dut.do_get_property("border_width") == 0
        assert dut.do_get_property("button_sensitivity") == Gtk.SensitivityType.AUTO
        assert not dut.do_get_property("can_focus")
        assert not dut.do_get_property("editing_canceled")
        assert dut.do_get_property("model") is None
        assert dut.do_get_property("popup_fixed_width")
        assert dut.do_get_property("wrap_width") == 0
        assert dut.do_get_property("height_request") == -1
        assert (
            dut.do_get_property("tooltip_markup")
            == "Missing tooltip, please file an issue to have one added."
        )
        assert (
            dut.do_get_property("tooltip_text")
            == "Missing tooltip, please file an issue to have one added."
        )
        assert dut.do_get_property("width_request") == -1

    @pytest.mark.unit
    @pytest.mark.filterwarnings("ignore:gtk_combo_box_set_entry_text_column")
    def test_do_set_properties(self, filter_stderr):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
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

        assert dut.do_get_property("active") == 3
        assert (
            dut.do_get_property("active_id")
            == "Value of the ID column for the active row."
        )
        assert dut.do_get_property("column_span_column") == 2
        assert dut.do_get_property("entry_text_column") == 5
        assert dut.do_get_property("has_entry")
        assert not dut.do_get_property("has_frame")
        assert dut.do_get_property("id_column") == 3
        assert dut.do_get_property("row_span_column") == 2
        assert dut.do_get_property("border_width") == 5
        assert dut.do_get_property("button_sensitivity") == Gtk.SensitivityType.ON
        assert dut.do_get_property("can_focus")
        assert not dut.do_get_property("editing_canceled")
        assert isinstance(dut.do_get_property("model"), Gtk.ListStore)
        assert dut.do_get_property("popup_fixed_width")
        assert dut.do_get_property("wrap_width") == 10
        assert dut.do_get_property("height_request") == 70
        assert dut.do_get_property("tooltip_markup") == "<b>Test Combo Tooltip</b>"
        assert dut.do_get_property("tooltip_text") == "Test Combo Tooltip"
        assert dut.do_get_property("width_request") == 150

    @pytest.mark.unit
    def test_do_load_combobox(self):
        """Load a list of string values into a simple GTK3ComboBox."""
        _model = Gtk.ListStore(GObject.TYPE_STRING)
        dut = self.make_dut(model=_model)
        dut.do_set_callbacks("changed", self.mock_callback)
        dut.do_load_combo(SIMPLE_TEST_LIST)

    @pytest.mark.unit
    def test_do_load_combobox_compound(self):
        """Load a list of string values into a non-simple GTK3ComboBox."""
        _model = Gtk.ListStore(
            GObject.TYPE_STRING, GObject.TYPE_STRING, GObject.TYPE_STRING
        )
        dut = self.make_dut(model=_model)
        dut.do_set_callbacks("changed", self.mock_callback)
        dut.do_load_combo(COMPOUND_TEST_LIST)

    @pytest.mark.unit
    def test_do_load_combobox_clears_previous_entries(self):
        """Clear the model before loading new entries."""
        _model = Gtk.ListStore(GObject.TYPE_STRING)
        dut = self.make_dut(model=_model)
        dut.do_set_callbacks("changed", self.mock_callback)
        dut.do_load_combo(SIMPLE_TEST_LIST)
        dut.do_load_combo(["Only Entry"])

        _options = dut.do_get_options()
        assert len(_options) == 2  # blank + one entry
        assert _options[1] == "Only Entry"

    @pytest.mark.unit
    def test_do_load_combobox_no_model(self):
        """Return None without raising and exception if model is None."""
        dut = self.make_dut()

        assert dut.do_load_combo(SIMPLE_TEST_LIST) is None

    @pytest.mark.unit
    def test_do_get_options_simple(self):
        """Return a dict of all the options available in a simple GTK3ComboBox."""
        _model = Gtk.ListStore(GObject.TYPE_STRING)
        dut = self.make_dut(model=_model)
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
        _model = Gtk.ListStore(
            GObject.TYPE_STRING, GObject.TYPE_STRING, GObject.TYPE_STRING
        )
        dut = self.make_dut(model=_model)
        dut.display_index = 1
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], self.mock_callback)
        dut.do_load_combo(COMPOUND_TEST_LIST)

        _options = dut.do_get_options()
        assert isinstance(_options, dict)
        assert _options == {0: "", 1: "is", 2: "of", 3: "not"}

    @pytest.mark.unit
    def test_do_get_options_no_model(self):
        """Return an empty dict when the model is None."""
        dut = self.make_dut()

        assert dut.do_get_options() == {}

    @pytest.mark.unit
    def test_do_set_value_wrong_type(self):
        """Should raise a WrongTypeError when passed a wrong data type."""
        _model = Gtk.ListStore(GObject.TYPE_INT)
        dut = self.make_dut(model=_model)

        with pytest.raises(WrongTypeError):
            dut.do_set_value("2")

    @pytest.mark.unit
    def test_get_value_simple(self):
        """Return the value from a simple GTK3ComboBox at index X."""
        _model = Gtk.ListStore(GObject.TYPE_STRING)
        dut = self.make_dut(model=_model)
        dut.dic_attributes["index"] = 1
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
        dut.do_load_combo(SIMPLE_TEST_LIST)

        assert not dut.do_get_value()
        for _idx in [1, 2, 3]:
            dut.set_active(_idx)
            assert dut.do_get_value() == f"Index {_idx}"

    @pytest.mark.unit
    def test_get_value_compound(self):
        """Return the value from a compound GTK3ComboBox at index X."""
        _model = Gtk.ListStore(
            GObject.TYPE_STRING, GObject.TYPE_STRING, GObject.TYPE_STRING
        )
        dut = self.make_dut(model=_model)
        dut.display_index = 1
        dut.dic_attributes["edit_signal"] = "changed"
        dut.dic_attributes["index"] = 1
        dut.do_set_callbacks(dut.dic_attributes["edit_signal"], dut.on_changed)
        dut.do_load_combo(COMPOUND_TEST_LIST)

        assert not dut.get_value_at_index(0)
        assert not dut.do_get_value()
        assert not dut.get_value_at_index(2)
        dut.set_active(1)
        assert dut.get_value_at_index(0) == "This"
        assert dut.do_get_value() == "is"
        assert dut.get_value_at_index(2) == "a"
        dut.set_active(2)
        assert dut.get_value_at_index(0) == "test"
        assert dut.do_get_value() == "of"
        assert dut.get_value_at_index(2) == "the"
        dut.set_active(3)
        assert dut.get_value_at_index(0) == "ComboBox"
        assert dut.do_get_value() == "not"
        assert dut.get_value_at_index(2) == "simple"

    @pytest.mark.unit
    def test_get_value_no_model(self):
        """Return an empty string when the model is None."""
        dut = self.make_dut()

        assert not dut.do_get_value()

    @pytest.mark.unit
    def test_get_value_no_active_selection(self):
        """Return an empty string when no row is active."""
        _model = Gtk.ListStore(GObject.TYPE_STRING)
        dut = self.make_dut(model=_model)
        dut.do_load_combo(SIMPLE_TEST_LIST)

        assert dut.get_active() == -1
        assert not dut.do_get_value()

    @pytest.mark.unit
    def test_do_update_simple(self, subscribed_combo):
        """Update a simple GTK3ComboBox with the data package value."""
        subscribed_combo.set_active(2)
        pub.sendMessage("rootTopic", package={"test_field": 2})

        assert subscribed_combo.get_active() == 2
        assert subscribed_combo.do_get_value() == "Index 2"

    @pytest.mark.unit
    def test_do_update_compound(self, compound_combo):
        """Update a compound GTK3ComboBox with the data package value."""
        compound_combo.set_active(2)
        compound_combo.dic_attributes["index"] = "test_field"
        pub.subscribe(compound_combo.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={"test_field": 2})

        assert compound_combo.get_active() == 2
        assert compound_combo.get_value_at_index(0) == "test"
        assert compound_combo.do_get_value() == "test"
        assert compound_combo.get_value_at_index(2) == "the"

    @pytest.mark.unit
    def test_do_update_non_int_value(self, subscribed_combo):
        """Do nothing when the value is not an int."""
        subscribed_combo.set_active(1)

        pub.sendMessage("rootTopic", package={"test_field": "Index 2"})

        assert subscribed_combo.get_active() == 1  # unchanged

    @pytest.mark.unit
    def test_on_changed_simple(self, simple_combo):
        """Call on_changed() when a simple GTK3ComboBox value changes."""
        pub.subscribe(self.mock_handler, simple_combo.dic_attributes["send_topic"])

        simple_combo.set_active(1)

    @pytest.mark.unit
    def test_on_changed_compound(self, compound_combo):
        """Call on_changed() when a compound GTK3ComboBox value changes."""
        pub.subscribe(self.mock_handler, compound_combo.dic_attributes["send_topic"])

        compound_combo.set_active(1)
