"""Test module for the GTK3RecentManager class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, GLib, Gtk
from pytkwrap.gtk3.file import GTK3RecentManager
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
)
from tests.gtk3.file.constants import (
    EXPECTED_RECENTMANAGER_HANDLER_IDS,
    EXPECTED_RECENTMANAGER_METHODS,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3RecentManager(BaseGTK3GObjectTests):
    """Test class for the GTK3RecentManager class."""

    widget_class = GTK3RecentManager
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES
    expected_handler_id = (
        EXPECTED_GOBJECT_HANDLER_IDS | EXPECTED_RECENTMANAGER_HANDLER_IDS
    )
    expected_methods = EXPECTED_GOBJECT_METHODS + EXPECTED_RECENTMANAGER_METHODS

    @pytest.mark.unit
    @pytest.mark.usefixtures("text_file")
    def test_do_add_item(self, text_file):
        """Should add an item to the recent manager."""
        _short_name = text_file.split("/")[-1]

        dut = self.make_dut()
        dut.purge_items()

        assert dut.do_add_recent(text_file)

        context = GLib.MainContext.default()
        found = False
        iterations = 0
        max_iterations = 50

        while not found and iterations < max_iterations:
            while context.pending():
                context.iteration(False)

            try:
                info = dut.lookup_item(text_file)
                if info:
                    found = True
                    break
            except GLib.GError:
                pass

            iterations += 1
            GLib.usleep(100000)

        assert found
        assert dut.get_items()[0].get_display_name() == f"file: {_short_name}"
        assert dut.get_items()[0].get_short_name() == f"file: {_short_name}"

    @pytest.mark.unit
    @pytest.mark.usefixtures("text_file")
    def test_do_add_item_full(self, text_file):
        """Should add an item to the recent manager."""
        _short_name = text_file.split("/")[-1]
        _recent_data = Gtk.RecentData()
        _recent_data.app_exec = "gedit %f"
        _recent_data.app_name = "gedit"
        _recent_data.description = "Test File"
        _recent_data.mime_type = "text/plain"

        dut = self.make_dut()
        dut.purge_items()

        assert dut.do_add_recent(text_file, recent_data=_recent_data)

        context = GLib.MainContext.default()
        found = False
        iterations = 0
        max_iterations = 50

        while not found and iterations < max_iterations:
            while context.pending():
                context.iteration(False)

            try:
                info = dut.lookup_item(text_file)
                if info:
                    found = True
                    break
            except GLib.GError:
                pass

            iterations += 1
            GLib.usleep(100000)

        assert found
        assert dut.get_items()[0].get_display_name() == f"file: {_short_name}"
        assert dut.get_items()[0].get_mime_type() == "text/plain"
        assert dut.get_items()[0].get_short_name() == f"file: {_short_name}"

    @pytest.mark.unit
    @pytest.mark.usefixtures("image_file")
    @pytest.mark.usefixtures("text_file")
    def test_do_remove_item(self, image_file, text_file):
        """Should remove an item from the recent manager."""
        dut = self.make_dut()

        assert dut.do_add_recent(image_file)
        assert dut.do_add_recent(text_file)

        context = GLib.MainContext.default()
        found = False
        iterations = 0
        max_iterations = 50

        while not found and iterations < max_iterations:
            while context.pending():
                context.iteration(False)

            try:
                info1 = dut.lookup_item(image_file)
                info2 = dut.lookup_item(text_file)
                if info1 and info2:
                    found = True
                    break
            except GLib.GError:
                pass

            iterations += 1
            GLib.usleep(100000)

        if found:
            assert len(dut.get_items()) == 2
            assert dut.do_remove_recent(text_file)
            assert len(dut.get_items()) == 1

    @pytest.mark.unit
    @pytest.mark.usefixtures("image_file")
    @pytest.mark.usefixtures("text_file")
    def test_do_remove_all_items(self, image_file, text_file):
        """Should remove an item from the recent manager."""
        dut = self.make_dut()

        assert dut.do_add_recent(image_file)
        assert dut.do_add_recent(text_file)

        context = GLib.MainContext.default()
        found = False
        iterations = 0
        max_iterations = 50

        while not found and iterations < max_iterations:
            while context.pending():
                context.iteration(False)

            try:
                info1 = dut.lookup_item(image_file)
                info2 = dut.lookup_item(text_file)
                if info1 and info2:
                    found = True
                    break
            except GLib.GError:
                pass

            iterations += 1
            GLib.usleep(100000)

        if found:
            assert len(dut.recent_items) == 2
            assert len(dut.get_items()) == 2
            assert dut.do_remove_recent(text_file, remove_all=True)
            assert len(dut.recent_items) == 0
            assert len(dut.get_items()) == 0
