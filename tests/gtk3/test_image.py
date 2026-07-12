"""Test module for the GTK3Image class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
import os

# Third Party Imports
import pytest

# pytkwrap Package Imports
# noinspection PyProtectedMember
from pytkwrap.gtk3._libs import Gdk, GdkPixbuf, Gio, Gtk, cairo
from pytkwrap.gtk3.image import GTK3Image
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from tests.gtk3.conftest import BaseGTK3GObjectTests
from tests.gtk3.constants import (
    EXPECTED_GOBJECT_ATTRIBUTES,
    EXPECTED_GOBJECT_HANDLER_IDS,
    EXPECTED_GOBJECT_METHODS,
    EXPECTED_IMAGE_METHODS,
    EXPECTED_IMAGE_PROPERTIES,
    EXPECTED_WIDGET_ATTRIBUTES,
    EXPECTED_WIDGET_HANDLER_IDS,
    EXPECTED_WIDGET_METHODS,
    EXPECTED_WIDGET_PROPERTIES,
)


@pytest.mark.usefixtures("suppress_stderr")
class TestGTK3Image(BaseGTK3GObjectTests):
    """Test class for the GTK3Image class."""

    widget_class = GTK3Image
    expected_attributes = EXPECTED_GOBJECT_ATTRIBUTES | EXPECTED_WIDGET_ATTRIBUTES
    expected_handler_id = EXPECTED_GOBJECT_HANDLER_IDS | EXPECTED_WIDGET_HANDLER_IDS
    expected_methods = (
        EXPECTED_GOBJECT_METHODS + EXPECTED_WIDGET_METHODS + EXPECTED_IMAGE_METHODS
    )
    expected_properties = EXPECTED_WIDGET_PROPERTIES | EXPECTED_IMAGE_PROPERTIES

    def make_dut(
        self,
        size: int = 4,
    ):
        return GTK3Image(size)

    @pytest.mark.unit
    def test_do_set_properties_default(self):
        """Should set properties to default values when passed an empty
        GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == self.expected_properties
        assert dut.do_get_property("file") is None
        assert dut.do_get_property("gicon") is None
        assert dut.do_get_property("icon_name") is None
        assert dut.do_get_property("icon_size") == 4
        assert dut.do_get_property("pixbuf") is None
        assert dut.do_get_property("pixbuf_animation") is None
        assert dut.do_get_property("pixel_size") == -1
        assert dut.do_get_property("resource") is None
        assert dut.do_get_property("surface") is None
        assert not dut.do_get_property("use_fallback")

    @pytest.mark.unit
    def test_do_set_properties_gicon(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        _gicon = Gio.ThemedIcon.new("folder")

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                file=None,
                gicon=_gicon,
                icon_name=None,
                icon_size=14,
                pixbuf=None,
                pixbuf_animation=None,
                pixel_size=2,
                resource=None,
                surface=None,
                use_fallback=True,
            )
        )

        assert dut.get_property("file") is None
        assert dut.get_property("gicon") == _gicon
        assert dut.get_gicon() == (_gicon, 14)
        assert dut.get_property("icon_name") is None
        assert dut.get_icon_name() == (None, 14)
        assert dut.get_property("icon_size") == 14
        assert dut.get_property("pixbuf") is None
        assert dut.get_pixbuf() is None
        assert dut.get_property("pixbuf_animation") is None
        assert dut.get_animation() is None
        assert dut.get_property("pixel_size") == 2
        assert dut.get_pixel_size() == 2
        assert dut.get_property("resource") is None
        assert dut.get_property("surface") is None
        assert dut.get_property("use_fallback")

    @pytest.mark.unit
    def test_do_set_properties_icon_name(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                file=None,
                gicon=None,
                icon_name="folder",
                icon_size=14,
                pixbuf=None,
                pixbuf_animation=None,
                pixel_size=2,
                resource=None,
                surface=None,
                use_fallback=True,
            )
        )

        assert dut.get_property("file") is None
        assert dut.get_property("gicon") is None
        assert dut.get_gicon() == (None, 14)
        assert dut.get_property("icon_name") == "folder"
        assert dut.get_icon_name() == ("folder", 14)
        assert dut.get_property("icon_size") == 14
        assert dut.get_property("pixbuf") is None
        assert dut.get_pixbuf() is None
        assert dut.get_property("pixbuf_animation") is None
        assert dut.get_animation() is None
        assert dut.get_property("pixel_size") == 2
        assert dut.get_pixel_size() == 2
        assert dut.get_property("resource") is None
        assert dut.get_property("surface") is None
        assert dut.get_property("use_fallback")

    @pytest.mark.unit
    def test_do_set_properties_pixbuf(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        cwd = os.getcwd()

        _pixbuf = GdkPixbuf.Pixbuf.new_from_file(f"{cwd}/tests/data/pytkwrap.png")

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                file=None,
                gicon=None,
                icon_name=None,
                icon_size=14,
                pixbuf=_pixbuf,
                pixbuf_animation=None,
                pixel_size=2,
                resource=None,
                surface=None,
                use_fallback=True,
            )
        )

        assert dut.get_property("file") is None
        assert dut.get_property("gicon") is None
        assert dut.get_gicon() == (None, 14)
        assert dut.get_property("icon_name") is None
        assert dut.get_icon_name() == (None, 14)
        assert dut.get_property("icon_size") == 14
        assert dut.get_property("pixbuf") == _pixbuf
        assert dut.get_pixbuf() == _pixbuf
        assert dut.get_property("pixbuf_animation") is None
        assert dut.get_animation() is None
        assert dut.get_property("pixel_size") == 2
        assert dut.get_pixel_size() == 2
        assert dut.get_property("resource") is None
        assert dut.get_property("surface") is None
        assert dut.get_property("use_fallback")

    @pytest.mark.unit
    def test_do_set_properties_animation(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        cwd = os.getcwd()

        _animation = GdkPixbuf.PixbufAnimation.new_from_file(
            f"{cwd}/tests/data/pytkwrap.png"
        )

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                file=None,
                gicon=None,
                icon_name=None,
                icon_size=14,
                pixbuf=None,
                pixbuf_animation=_animation,
                pixel_size=2,
                resource=None,
                surface=None,
                use_fallback=True,
            )
        )

        assert dut.get_property("file") is None
        assert dut.get_property("gicon") is None
        assert dut.get_gicon() == (None, 14)
        assert dut.get_property("icon_name") is None
        assert dut.get_icon_name() == (None, 14)
        assert dut.get_property("icon_size") == 14
        assert dut.get_property("pixbuf") is None
        assert dut.get_pixbuf() is None
        assert dut.get_property("pixbuf_animation") == _animation
        assert dut.get_animation() == _animation
        assert dut.get_property("pixel_size") == 2
        assert dut.get_pixel_size() == 2
        assert dut.get_property("resource") is None
        assert dut.get_property("surface") is None
        assert dut.get_property("use_fallback")

    @pytest.mark.unit
    def test_do_set_properties_file(self):
        """Should set properties to the values passed in the GTK3WidgetProperties."""
        cwd = os.getcwd()

        _file = f"{cwd}/tests/data/pytkwrap.png"

        dut = self.make_dut()
        dut.do_set_properties(
            GTK3WidgetProperties(
                file=_file,
                gicon=None,
                icon_name=None,
                icon_size=14,
                pixbuf=None,
                pixbuf_animation=None,
                pixel_size=2,
                resource=None,
                surface=None,
                use_fallback=True,
            )
        )

        assert dut.get_property("file") == _file
        assert dut.get_property("gicon") is None
        assert dut.get_gicon() == (None, 14)
        assert dut.get_property("icon_name") is None
        assert dut.get_icon_name() == (None, 14)
        assert dut.get_property("icon_size") == 14
        assert isinstance(dut.get_property("pixbuf"), GdkPixbuf.Pixbuf)
        assert isinstance(dut.get_pixbuf(), GdkPixbuf.Pixbuf)
        assert dut.get_property("pixbuf_animation") is None
        assert dut.get_animation() is None
        assert dut.get_property("pixel_size") == 2
        assert dut.get_pixel_size() == 2
        assert dut.get_property("resource") is None
        assert dut.get_property("surface") is None
        assert dut.get_property("use_fallback")
