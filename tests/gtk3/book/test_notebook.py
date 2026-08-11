"""Test module for the GTK3Notebook class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
import contextlib

# Third Party Imports
import pytest
from pubsub import pub

# pytkwrap Package Imports
from pytkwrap.exceptions import PytkwrapError, PytkwrapWarning

# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.book import GTK3Notebook
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from tests.gtk3.book.constants import (
    EXPECTED_NOTEBOOK_HANDLER_IDS,
    EXPECTED_NOTEBOOK_METHODS,
    EXPECTED_NOTEBOOK_PROPERTIES,
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
    EXPECTED_CONTAINER_HANDLER_IDS,
    EXPECTED_CONTAINER_METHODS,
    EXPECTED_CONTAINER_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3Notebook(BaseGTK3GObjectTests):
    """Test class for the GTK3Notebook class."""

    widget_class = GTK3Notebook
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_default_height = -1
    expected_default_width = -1
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_NOTEBOOK_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_NOTEBOOK_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_NOTEBOOK_PROPERTIES
    )

    def make_dut(self, child_widgets=None, tab_labels=None):
        return self.widget_class(child_widgets=child_widgets, tab_labels=tab_labels)

    @staticmethod
    def init_warning_handler(message):
        """Warning handler for __init__() warnings."""
        assert (
            message
            == "GTK3Notebook: The number of child widgets (1) does not match the "
            "number of tab labels (2).  Only 1 pages will be added."
        )

    @pytest.mark.unit
    def test_init_with_widgets_and_labels(self):
        """Should build the notebook with the same number of pages as the child_widgets
        list."""
        _child_widget_1 = Gtk.Fixed()
        _child_widget_2 = Gtk.Fixed()
        _child_widget_3 = Gtk.Fixed()
        _child_widgets = [_child_widget_1, _child_widget_2, _child_widget_3]
        _tab_labels = ["Test Label {}".format(i) for i in range(3)]

        dut = self.make_dut(child_widgets=_child_widgets, tab_labels=_tab_labels)

        assert dut.get_n_pages() == 3
        assert dut.get_tab_label_text(_child_widget_1) == _tab_labels[0]
        assert dut.get_tab_label_text(_child_widget_2) == _tab_labels[1]
        assert dut.get_tab_label_text(_child_widget_3) == _tab_labels[2]

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert not dut.do_get_property("enable_popup")
        assert dut.do_get_property("group_name") is None
        assert dut.do_get_property("page") == -1
        assert not dut.do_get_property("scrollable")
        assert dut.do_get_property("show_border")
        assert dut.do_get_property("show_tabs")
        assert dut.do_get_property("tab_pos") == Gtk.PositionType.TOP

    @pytest.mark.unit
    def test_do_set_properties(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()

        dut.append_page(Gtk.Fixed(), Gtk.Label())
        dut.append_page(Gtk.Fixed(), Gtk.Label())
        dut.set_current_page(1)

        dut.do_set_properties(
            GTK3WidgetProperties(
                enable_popup=True,
                group_name="Test Group Name",
                scrollable=True,
                show_border=False,
                show_tabs=False,
                tab_pos=Gtk.PositionType.BOTTOM,
            )
        )

        assert dut.get_property("enable_popup")
        assert dut.get_property("group_name") == "Test Group Name"
        assert dut.get_group_name() == "Test Group Name"
        assert dut.get_property("scrollable")
        assert dut.get_scrollable()
        assert not dut.get_property("show_border")
        assert not dut.get_show_border()
        assert not dut.get_property("show_tabs")
        assert not dut.get_show_tabs()
        assert dut.get_property("tab_pos") == Gtk.PositionType.BOTTOM
        assert dut.get_tab_pos() == Gtk.PositionType.BOTTOM

    @pytest.mark.unit
    def test_do_add_page(self):
        """Should add a page to the GTK3Notebook."""
        _fixed = Gtk.Fixed()

        dut = self.make_dut()
        dut.do_add_page(_fixed, "Test Label")

        assert dut.get_n_pages() == 1
        assert dut.get_tab_label_text(_fixed) == "Test Label"

    @pytest.mark.unit
    def test_do_prepend_page(self):
        """Should prepend a page to the GTK3Notebook."""
        _fixed1 = Gtk.Fixed()
        _fixed2 = Gtk.Fixed()

        dut = self.make_dut()
        dut.do_add_page(_fixed1, "Test Label")
        dut.do_add_page(_fixed2, "Prepended Page", position=0)

        assert dut.get_n_pages() == 2
        assert dut.get_tab_label_text(dut.get_nth_page(0)) == "Prepended Page"

    @pytest.mark.unit
    def test_do_insert_page(self):
        """Should insert a page into the GTK3Notebook."""
        _fixed1 = Gtk.Fixed()
        _fixed2 = Gtk.Fixed()
        _fixed3 = Gtk.Fixed()

        dut = self.make_dut()
        dut.do_add_page(_fixed1, "Test Label")
        dut.do_add_page(_fixed2, "Inserted Page 1")
        dut.do_add_page(_fixed3, "Inserted Page 2", position=1)

        assert dut.get_n_pages() == 3
        assert dut.get_tab_label_text(dut.get_nth_page(1)) == "Inserted Page 2"

    @pytest.mark.unit
    def test_do_remove_page(self):
        """Should remove a page from the GTK3Notebook."""
        _fixed1 = Gtk.Fixed()
        _fixed2 = Gtk.Fixed()
        _fixed3 = Gtk.Fixed()

        dut = self.make_dut()
        dut.do_add_page(_fixed1, "Test Label")
        dut.do_add_page(_fixed2, "Test Label 2")
        dut.do_add_page(_fixed3, "Test Label 3")

        assert dut.get_n_pages() == 3

        dut.do_remove_page(1)

        assert dut.get_n_pages() == 2
        assert dut.get_tab_label_text(dut.get_nth_page(1)) == "Test Label 3"

    @pytest.mark.unit
    def test_do_remove_page_no_page(self):
        """Should not raise an exception when trying to remove a page that does not
        exist."""
        dut = self.make_dut()
        dut.do_add_page(Gtk.Fixed(), "Test Label 1")
        dut.do_add_page(Gtk.Fixed(), "Test Label 2")
        dut.do_add_page(Gtk.Fixed(), "Test Label 3")

        with pytest.raises(PytkwrapError):
            dut.do_remove_page(10)

        assert dut.get_n_pages() == 3

    @pytest.mark.unit
    def test_do_build_notebook_no_child_widgets(self):
        """Should build the notebook with no pages when no child_widgets or tab labels
        are passed in."""
        dut = self.make_dut()
        dut.do_build_notebook([], [])

        assert dut.get_n_pages() == 0

    @pytest.mark.unit
    def test_do_build_notebook_more_widgets_than_labels(self):
        """Should raise a PytkwrapWarning when the number of child widgets is greater
        than the number of tab labels."""
        _child_widget_1 = Gtk.Fixed()
        _child_widget_2 = Gtk.Fixed()
        _child_widget_3 = Gtk.Fixed()
        _child_widgets = [_child_widget_1, _child_widget_2, _child_widget_3]
        _tab_labels = ["Test Label 1", "Test Label 2"]

        dut = self.make_dut()
        with pytest.raises(PytkwrapWarning) as exc_info:
            dut.do_build_notebook(child_widgets=_child_widgets, tab_labels=_tab_labels)

        assert (
            exc_info.value.args[0]
            == "GTK3Notebook: The number of child widgets (3) does not match the number of tab labels (2).  Only 2 pages will be added."
        )

        assert dut.get_n_pages() == 2
        assert dut.get_tab_label_text(_child_widget_1) == _tab_labels[0]
        assert dut.get_tab_label_text(_child_widget_2) == _tab_labels[1]

    @pytest.mark.unit
    def test_do_build_notebook_more_labels_than_widgets(self):
        """Should raise a PytkwrapWarning when the number of child widgets is less than
        the number of tab labels."""
        _child_widget_1 = Gtk.Fixed()
        _child_widgets = [_child_widget_1]
        _tab_labels = ["Test Label 1", "Test Label 2"]

        dut = self.make_dut()
        with pytest.raises(PytkwrapWarning) as exc_info:
            dut.do_build_notebook(child_widgets=_child_widgets, tab_labels=_tab_labels)

        assert (
            exc_info.value.args[0]
            == "GTK3Notebook: The number of child widgets (1) does not match the "
            "number of tab labels (2).  Only 1 pages will be added."
        )

        assert dut.get_n_pages() == 1
        assert dut.get_tab_label_text(_child_widget_1) == _tab_labels[0]
