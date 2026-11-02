"""Test module for the GTK3Assistant class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, GdkPixbuf, Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.window import GTK3Assistant, do_construct_assistant
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
from tests.gtk3.window.constants import (
    EXPECTED_ASSISTANT_HANDLER_IDS,
    EXPECTED_ASSISTANT_METHODS,
    EXPECTED_ASSISTANT_PROPERTIES,
    EXPECTED_WINDOW_HANDLER_IDS,
    EXPECTED_WINDOW_METHODS,
    EXPECTED_WINDOW_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3Assistant(BaseGTK3GObjectTests):
    """Test class for the GTK3Assistant class."""

    widget_class = GTK3Assistant
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS
        | EXPECTED_WIDGET_HANDLER_IDS
        | EXPECTED_CONTAINER_HANDLER_IDS
        | EXPECTED_WINDOW_HANDLER_IDS
        | EXPECTED_ASSISTANT_HANDLER_IDS
    )
    expected_methods = (
        EXPECTED_GOBJECT_METHODS
        + EXPECTED_WIDGET_METHODS
        + EXPECTED_CONTAINER_METHODS
        + EXPECTED_BIN_METHODS
        + EXPECTED_WINDOW_METHODS
        + EXPECTED_ASSISTANT_METHODS
    )
    expected_properties = (
        EXPECTED_WIDGET_PROPERTIES
        | EXPECTED_CONTAINER_PROPERTIES
        | EXPECTED_WINDOW_PROPERTIES
        | EXPECTED_ASSISTANT_PROPERTIES
    )

    def make_dut(self, use_header_bar: bool = False) -> GTK3Assistant:
        return self.widget_class(use_header_bar=use_header_bar)

    @pytest.mark.unit
    def test_init_with_header_bar(self):
        dut = self.make_dut(use_header_bar=True)

        assert dut.get_property("use_header_bar")

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("use_header_bar") == -1

    @pytest.mark.unit
    def test_do_add_page_append(self):
        """Should add a page to the assistant and return the index of the added page."""
        dut = self.make_dut()
        _page = Gtk.Label(label="Test Page")
        _index = dut.do_add_page(_page)

        assert _index == 0
        assert dut.n_pages == 1

    @pytest.mark.unit
    def test_do_add_page_prepend(self):
        """Should prepend a page to the assistant and return the index of the added
        page."""
        dut = self.make_dut()
        _page1 = Gtk.Label(label="Test Page 1")
        _page2 = Gtk.Label(label="Test Page 2")
        dut.do_add_page(_page1)
        _index = dut.do_add_page(_page2, position=0)

        assert _index == 0
        assert dut.n_pages == 2
        assert dut.get_nth_page(0) == _page2
        assert dut.get_nth_page(1) == _page1

    @pytest.mark.unit
    def test_do_add_page_insert(self):
        """Should insert a page at the specified position and return the index of the
        added page."""
        dut = self.make_dut()
        _page1 = Gtk.Label(label="Test Page 1")
        _page2 = Gtk.Label(label="Test Page 2")
        _page3 = Gtk.Label(label="Test Page 3")
        dut.do_add_page(_page1)
        dut.do_add_page(_page3)
        _index = dut.do_add_page(_page2, position=1)

        assert _index == 1
        assert dut.n_pages == 3
        assert dut.get_nth_page(0) == _page1
        assert dut.get_nth_page(1) == _page2
        assert dut.get_nth_page(2) == _page3

    @pytest.mark.unit
    def test_do_construct_assistant(self):
        """Should construct a GTK3Assistant with the specified pages, titles, and
        types."""
        _pages = [Gtk.Fixed(), Gtk.Fixed()]
        _titles = ["Title 1", "Title 2"]
        _types = [Gtk.AssistantPageType.INTRO, Gtk.AssistantPageType.CONTENT]
        dut = do_construct_assistant(
            pages=_pages, titles=_titles, types=_types, use_header_bar=True
        )

        assert dut.n_pages == 2
        for _idx, _page in enumerate(_pages):
            assert dut.get_nth_page(_idx) == _page
            assert dut.get_page_title(_page) == _titles[_idx]
            assert dut.get_page_type(_page) == _types[_idx]
