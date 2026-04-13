# pylint: skip-file
# type: ignore
#
#       pytkwrap.gtk3.test_entry.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""Test class for the GTK3 entry module algorithms and models."""

# Standard Library Imports
from datetime import datetime

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.common.mixins import WidgetAttributes
from pytkwrap.exceptions import UnkSignalError
from pytkwrap.gtk3._libs import GdkPixbuf, Gtk, Pango
from pytkwrap.gtk3.entry import GTK3Entry
from pytkwrap.gtk3.widget import GTK3WidgetProperties

# pytkwrap Local Imports
from .conftest import BaseGTK3DataWidgetTests


def do_update_error_handler(message) -> None:
    """Error handler for do_update() errors."""
    assert message == "GTK3Entry.do_update(): Unknown signal name 'edit_signal'."


def mock_handler(node_id, package) -> None:
    """Mock message handler."""
    if node_id == 0:
        assert package == {"test_field": "Test Text"}


def on_changed_error_handler(message):
    """Error handler for on_changed() errors."""
    assert message == "GTK3Entry.on_changed(): Unknown signal name 'edit_signal'."


@pytest.mark.order(4)
@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3Entry(BaseGTK3DataWidgetTests):
    """Test class for the GTK3Entry."""

    widget_class = GTK3Entry
    expected_default_height = 25
    expected_default_value = ""
    expected_default_width = 200

    def make_dut(self, font_description=None):
        """Create a device under test for the GTK3Entry."""
        return self.widget_class(font_description)

    @staticmethod
    def no_signal_error_handler(message):
        """Error handler for do_set_callbacks() errors."""
        assert (
            message
            == "GTK3Entry.do_set_callbacks(): Unknown signal name 'value-changed'."
        )

    @pytest.mark.unit
    def test_init(self):
        """Should create a GTK3Entry with default values for attributes."""
        super().test_init()

        dut = self.make_dut()

        assert isinstance(dut, GTK3Entry)
        assert dut._DEFAULT_HEIGHT == 25
        assert dut._DEFAULT_WIDTH == 200
        assert dut.edit_signal == "changed"
        # All handler IDs should start at -1.
        assert all(_hid == -1 for _hid in dut.dic_handler_id.values())
        # Entry-specific attributes should be registered.
        for _attribute in GTK3Entry._GTK3_ENTRY_ATTRIBUTES:
            assert _attribute in dut.dic_attributes
        # Entry-specific properties should be registered.
        for _property in GTK3Entry._GTK3_ENTRY_PROPERTIES:
            assert _property in dut.dic_properties
        # Entry-specific signals should be registered.
        for _signal in GTK3Entry._GTK3_ENTRY_SIGNALS:
            assert _signal in dut.dic_handler_id
        assert dut.font_description is None

    @pytest.mark.unit
    def test_do_set_attributes_default(self):
        """Should set the default attributes of a GTK3Entry when passed an empty
        WidgetAttributes.
        """
        super().test_do_set_attributes_default()

        dut = self.make_dut()
        dut.do_set_attributes(WidgetAttributes())

        assert dut.font_description is None

    @pytest.mark.unit
    def test_do_set_attributes(self):
        """Should set the GTKEntry attributes to the values passed in a WidgetAttributes
        dict.
        """
        super().test_do_set_attributes()

        dut = self.make_dut()
        dut.do_set_attributes(
            WidgetAttributes(
                font_description=Pango.FontDescription(
                    "Sans,Serif,Monospace Normal Not-Rotated Bold 10"
                ),
            )
        )

        assert dut.font_description.get_family() == "Sans,Serif,Monospace"
        assert dut.font_description.get_features() is None
        assert dut.font_description.get_gravity() == Pango.Gravity.SOUTH
        assert dut.font_description.get_size() == 10240
        assert dut.font_description.get_stretch() == Pango.Stretch.NORMAL
        assert dut.font_description.get_style() == Pango.Style.NORMAL
        assert dut.font_description.get_variant() == Pango.Variant.NORMAL
        assert dut.font_description.get_weight() == Pango.Weight.BOLD

    @pytest.mark.unit
    def test_do_set_attributes_preserves_font_description(self):
        """Should not override column_types set in __init__ when no column_types key is
        passed in WidgetAttributes.
        """
        dut = self.make_dut(
            Pango.FontDescription("Sans,Serif,Monospace Normal Not-Rotated Bold 10")
        )
        dut.do_set_attributes(WidgetAttributes())

        assert dut.font_description.get_family() == "Sans,Serif,Monospace"
        assert dut.font_description.get_features() is None
        assert dut.font_description.get_gravity() == Pango.Gravity.SOUTH
        assert dut.font_description.get_size() == 10240
        assert dut.font_description.get_stretch() == Pango.Stretch.NORMAL
        assert dut.font_description.get_style() == Pango.Style.NORMAL
        assert dut.font_description.get_variant() == Pango.Variant.NORMAL
        assert dut.font_description.get_weight() == Pango.Weight.BOLD

    @pytest.mark.unit
    def test_do_set_attributes_overrides_font_description(self):
        """Should override column_types when explicitly passed."""
        dut = self.make_dut(
            Pango.FontDescription("Sans,Serif,Monospace Normal Not-Rotated Bold 10")
        )
        dut.do_set_attributes(
            WidgetAttributes(
                font_description=Pango.FontDescription(
                    "Helvetica Italic Not-Rotated Demi-Bold 16"
                )
            )
        )

        assert dut.font_description.get_family() == "Helvetica"
        assert dut.font_description.get_features() is None
        assert dut.font_description.get_gravity() == Pango.Gravity.SOUTH
        assert dut.font_description.get_size() == 16384
        assert dut.font_description.get_stretch() == Pango.Stretch.NORMAL
        assert dut.font_description.get_style() == Pango.Style.ITALIC
        assert dut.font_description.get_variant() == Pango.Variant.NORMAL
        assert dut.font_description.get_weight() == Pango.Weight.SEMIBOLD

    @pytest.mark.unit
    def test_do_get_attribute(self):
        """Should retrieve the value of the passed attribute."""
        super().test_do_get_attribute()

        dut = self.make_dut()

        assert dut.do_get_attribute("font_description") is None

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Set the default properties of a GTK3Entry when passed an empty
        GTK3WidgetProperties.
        """
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert not dut.get_property("activates_default")
        assert dut.get_property("attributes") is None
        assert isinstance(dut.get_property("buffer"), Gtk.EntryBuffer)
        assert dut.get_property("caps_lock_warning")
        assert dut.get_property("completion") is None
        assert dut.get_property("editable")
        assert not dut.get_property("editing_canceled")
        assert not dut.get_property("enable_emoji_completion")
        assert dut.get_property("has_frame")
        assert dut.get_property("height-request") == -1
        assert dut.get_property("im_module") is None
        assert dut.get_property("inner_border") is None
        assert dut.get_property("input_hints") == Gtk.InputHints.NONE
        assert dut.get_property("input_purpose") == Gtk.InputPurpose.FREE_FORM
        assert dut.get_property("invisible_char") == "•"
        assert not dut.get_property("invisible_char_set")
        assert dut.get_property("max_length") == 0
        assert dut.get_property("max_width_chars") == -1
        assert not dut.get_property("overwrite_mode")
        assert dut.get_property("placeholder_text") is None
        assert not dut.get_property("populate_all")
        assert dut.get_property("primary_icon_activatable")
        assert dut.get_property("primary_icon_gicon") is None
        assert dut.get_property("primary_icon_name") is None
        assert dut.get_property("primary_icon_pixbuf") is None
        assert dut.get_property("primary_icon_sensitive")
        assert dut.get_property("primary_icon_storage_type") == Gtk.ImageType.EMPTY
        assert dut.get_property("primary_icon_tooltip_markup") is None
        assert dut.get_property("primary_icon_tooltip_text") is None
        assert dut.get_property("progress_fraction") == 0.0
        assert dut.get_property("progress_pulse_step") == 0.1
        assert dut.get_property("scroll_offset") == 0
        assert dut.get_property("secondary_icon_activatable")
        assert dut.get_property("secondary_icon_gicon") is None
        assert dut.get_property("secondary_icon_name") is None
        assert dut.get_property("secondary_icon_pixbuf") is None
        assert dut.get_property("secondary_icon_sensitive")
        assert dut.get_property("secondary_icon_storage_type") == Gtk.ImageType.EMPTY
        assert dut.get_property("secondary_icon_tooltip_markup") is None
        assert dut.get_property("secondary_icon_tooltip_text") is None
        assert dut.get_property("selection_bound") == 0
        assert dut.get_property("shadow_type") == Gtk.ShadowType.IN
        assert not dut.get_property("show_emoji_icon")
        assert dut.get_property("tabs") is None
        assert dut.get_property("text") == ""
        assert dut.get_property("text_length") == 0
        assert dut.get_property("tooltip-markup") == (
            "Missing tooltip, please file an issue to have one added."
        )
        assert not dut.get_property("truncate_multiline")
        assert dut.get_property("visibility")
        assert dut.get_property("width_chars") == -1
        assert dut.get_property("width-request") == -1
        assert dut.get_property("xalign") == 0.0

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set the properties of a GTK3Entry."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                activates_default=True,
                attributes=Pango.AttrList(),
                buffer=Gtk.EntryBuffer.new("New Buffer", 10),
                caps_lock_warning=False,
                completion=Gtk.EntryCompletion(),
                editable=False,
                editing_canceled=True,
                enable_emoji_completion=True,
                has_frame=False,
                height_request=70,
                im_module="im-ibus",
                inner_border=Gtk.Border(),
                input_hints=Gtk.InputHints.SPELLCHECK,
                input_purpose=Gtk.InputPurpose.PASSWORD,
                invisible_char=":",
                invisible_char_set=True,
                max_length=30,
                max_width_chars=100,
                overwrite_mode=True,
                placeholder_text="Test Placeholder Text",
                populate_all=True,
                primary_icon_activatable=False,
                primary_icon_gicon=None,
                primary_icon_name="network-server",
                primary_icon_pixbuf=GdkPixbuf.Pixbuf(),
                primary_icon_sensitive=False,
                primary_icon_storage_type=Gtk.ImageType.EMPTY,
                primary_icon_tooltip_markup="<span foreground='blue'>Primary Icon Tooltip Text</span>",
                primary_icon_tooltip_text="Primary Icon Tooltip Text",
                progress_fraction=0.1,
                progress_pulse_step=0.5,
                scroll_offset=0,
                secondary_icon_activatable=False,
                secondary_icon_gicon=None,
                secondary_icon_name=None,
                secondary_icon_pixbuf=None,
                secondary_icon_sensitive=False,
                secondary_icon_storage_type=Gtk.ImageType.EMPTY,
                secondary_icon_tooltip_markup=None,
                secondary_icon_tooltip_text=None,
                selection_bound=3,
                shadow_type=Gtk.ShadowType.ETCHED_IN,
                show_emoji_icon=True,
                tabs=Pango.TabArray.from_string("100px 200px center:300px right:400px"),
                text="Test Entry Text",
                text_length=20,
                tooltip_markup="Test Entry Tooltip.",
                tooltip_text="Test Entry Tooltip.",
                truncate_multiline=True,
                visibility=False,
                width_chars=20,
                width_request=150,
                xalign=0.6,
            )
        )

        assert dut.get_property("activates_default")
        assert isinstance(dut.get_property("attributes"), Pango.AttrList)
        assert dut.get_property("attributes").get_attributes() == []
        assert isinstance(dut.get_property("buffer"), Gtk.EntryBuffer)
        assert not dut.get_property("caps_lock_warning")
        assert isinstance(dut.get_property("completion"), Gtk.EntryCompletion)
        assert not dut.get_property("editable")
        assert not dut.get_property("editing_canceled")
        assert dut.get_property("enable_emoji_completion")
        assert not dut.get_property("has_frame")
        assert dut.get_property("height-request") == 70
        assert dut.get_property("im_module") == "im-ibus"
        assert isinstance(dut.get_property("inner_border"), Gtk.Border)
        assert dut.get_property("inner_border").bottom == 0
        assert dut.get_property("inner_border").left == 0
        assert dut.get_property("inner_border").right == 0
        assert dut.get_property("inner_border").top == 0
        assert dut.get_property("input_hints") == Gtk.InputHints.SPELLCHECK
        assert dut.get_property("input_purpose") == Gtk.InputPurpose.PASSWORD
        assert dut.get_property("invisible_char") == ":"
        assert dut.get_property("invisible_char_set")
        assert dut.get_property("max_length") == 30
        assert dut.get_property("max_width_chars") == 100
        assert dut.get_property("overwrite_mode")
        assert dut.get_property("placeholder_text") == "Test Placeholder Text"
        assert dut.get_property("populate_all")
        assert not dut.get_property("primary_icon_activatable")
        assert dut.get_property("primary_icon_gicon") is None
        assert dut.get_property("primary_icon_name") is None
        assert isinstance(dut.get_property("primary_icon_pixbuf"), GdkPixbuf.Pixbuf)
        assert not dut.get_property("primary_icon_sensitive")
        assert dut.get_property("primary_icon_storage_type") == Gtk.ImageType.PIXBUF
        assert (
            dut.get_property("primary_icon_tooltip_markup")
            == "Primary Icon Tooltip Text"
        )
        assert (
            dut.get_property("primary_icon_tooltip_text") == "Primary Icon Tooltip Text"
        )
        assert dut.get_property("progress_fraction") == 0.1
        assert dut.get_property("progress_pulse_step") == 0.5
        assert dut.get_property("scroll_offset") == 0
        assert dut.get_property("secondary_icon_activatable")
        assert dut.get_property("secondary_icon_gicon") is None
        assert dut.get_property("secondary_icon_name") == "face-smile-symbolic"
        # assert isinstance(dut.get_property("secondary_icon_pixbuf"), GdkPixbuf.Pixbuf)
        assert dut.get_property("secondary_icon_sensitive")
        assert (
            dut.get_property("secondary_icon_storage_type") == Gtk.ImageType.ICON_NAME
        )
        assert dut.get_property("secondary_icon_tooltip_markup") == "Insert Emoji"
        assert dut.get_property("secondary_icon_tooltip_text") == "Insert Emoji"
        assert dut.get_property("selection_bound") == 0
        assert dut.get_property("shadow_type") == Gtk.ShadowType.ETCHED_IN
        assert dut.get_property("show_emoji_icon")
        assert isinstance(dut.get_property("tabs"), Pango.TabArray)
        assert dut.get_property("tabs").get_size() == 4
        assert dut.get_property("text") == "Test Entry Text"
        assert dut.get_property("text_length") == 15
        assert dut.get_property("tooltip-markup") == "Test Entry Tooltip."
        assert dut.get_property("truncate_multiline")
        assert not dut.get_property("visibility")
        assert dut.get_property("width_chars") == 20
        assert dut.get_property("width-request") == 150
        assert dut.get_property("xalign") == pytest.approx(0.6)

    @pytest.mark.unit
    def test_do_update(self):
        """Update the GTK3Entry with the data package value."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={"test_field": "Test Package"})

        assert dut.get_text() == "Test Package"

    @pytest.mark.unit
    def test_do_update_date_value(self):
        """Update the GTK3Entry with the stringified version of a date."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={"test_field": datetime.today()})

        assert dut.get_text() == datetime.strftime(datetime.today(), "%Y-%m-%d")

    @pytest.mark.unit
    def test_do_update_none_value(self):
        """Update the GTK3Entry with a blank string."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.do_update)
        pub.subscribe(dut.do_update, "rootTopic")

        pub.sendMessage("rootTopic", package={"test_field": None})

        assert dut.get_text() == ""

    @pytest.mark.unit
    def test_do_update_unknown_signal(self):
        """Raise a KeyError with an unknown edit signal name."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.do_update)
        pub.subscribe(do_update_error_handler, "do_log_error")
        pub.subscribe(dut.do_update, "rootTopic")
        dut.edit_signal = "edit_signal"

        with pytest.raises(UnkSignalError):
            pub.sendMessage("rootTopic", package={"test_field": "Test Package"})

        assert dut.get_text() == ""

    @pytest.mark.unit
    def test_do_update_wrong_field(self):
        """Do nothing when the package field doesn't match."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.do_set_callbacks(dut.edit_signal, dut.on_changed)
        pub.subscribe(dut.do_update, "rootTopic")
        dut.set_text("Test Text")

        pub.sendMessage("rootTopic", package={"wrong_field": "Test Package"})

        assert dut.get_text() == "Test Text"

    @pytest.mark.unit
    def test_on_changed(self):
        """Called when the GTK3Entry text changes."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.record_id = 0
        dut.send_topic = "entry_changed"
        dut.do_set_callbacks(dut.edit_signal, dut.on_changed)

        pub.subscribe(mock_handler, dut.send_topic)

        dut.set_text("Test Text")

    @pytest.mark.unit
    def test_on_changed_unknown_signal(self):
        """Raise a KeyError with an unknown edit signal name."""
        dut = self.make_dut()
        dut.field = "test_field"
        dut.record_id = 0
        dut.send_topic = "entry_changed"
        dut.do_set_callbacks(dut.edit_signal, dut.on_changed)
        pub.subscribe(on_changed_error_handler, "do_log_error")
        dut.edit_signal = "edit_signal"
        pub.subscribe(mock_handler, dut.send_topic)

        dut.set_text("Test Text")

    @pytest.mark.unit
    def test_do_get_value_float(self):
        """Return a float value when the datatype attribute is set to 'gfloat'."""
        dut = self.make_dut()
        dut.datatype = "gfloat"
        dut.set_text("38.235")

        assert isinstance(dut.do_get_value(), float)
        assert dut.do_get_value() == 38.235

    @pytest.mark.unit
    def test_do_get_value_int(self):
        """Return an integer value when the datatype attribute is set to 'gint'."""
        dut = self.make_dut()
        dut.datatype = "gint"
        dut.set_text("38")

        assert isinstance(dut.do_get_value(), int)
        assert dut.do_get_value() == 38

    @pytest.mark.unit
    def test_do_get_value_string(self):
        """Return a string value when the datatype attribute is set to 'gchararray'."""
        dut = self.make_dut()
        dut.datatype = "gchararray"
        dut.set_text("Some Text")

        assert isinstance(dut.do_get_value(), str)
        assert dut.do_get_value() == "Some Text"

    @pytest.mark.unit
    def test_do_set_font_description_default(self):
        """Set a new font description with default values when no arguments are
        passed.
        """
        dut = self.make_dut()
        dut.do_set_font_description()

        assert isinstance(dut.font_description, Pango.FontDescription)
        assert dut.font_description.get_family() == "Sans,Serif,Monospace Not Rotated"
        assert dut.font_description.get_features() is None
        assert dut.font_description.get_gravity() == Pango.Gravity.SOUTH
        assert dut.font_description.get_size() == 10240
        assert dut.font_description.get_stretch() == Pango.Stretch.NORMAL
        assert dut.font_description.get_style() == Pango.Style.NORMAL
        assert dut.font_description.get_variant() == Pango.Variant.NORMAL
        assert dut.font_description.get_weight() == Pango.Weight.NORMAL

    @pytest.mark.unit
    def test_do_set_font_description(self):
        """Set a new font description with values passed as arguments."""
        dut = self.make_dut()
        dut.do_set_font_description(
            family="Helvetica",
            size=16,
            style="Roman",
            variant="All-Caps",
            weight="Demi Bold",
        )

        assert isinstance(dut.font_description, Pango.FontDescription)
        assert (
            dut.font_description.get_family()
            == "Helvetica Not Rotated  Roman All-Caps Demi"
        )
        assert dut.font_description.get_features() is None
        assert dut.font_description.get_gravity() == Pango.Gravity.SOUTH
        assert dut.font_description.get_size() == 16384
        assert dut.font_description.get_stretch() == Pango.Stretch.NORMAL
        assert dut.font_description.get_style() == Pango.Style.NORMAL
        assert dut.font_description.get_variant() == Pango.Variant.NORMAL
        assert dut.font_description.get_weight() == Pango.Weight.BOLD
