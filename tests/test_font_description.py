"""Test class for the FontDescription class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.utilities import FontDescription


@pytest.mark.order(3)
class TestFontDescription:
    """Test class for the FontDescription data class."""

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-025")
    def test_init(self):
        """Should create an instance of the FontDescription data class."""
        dut = FontDescription()

        assert dut.allow_breaks == "false"
        assert dut.bgalpha == "100%"
        assert dut.bgcolor == "white"
        assert dut.family == "Sans,Serif,Monospace"
        assert dut.features == ""
        assert dut.fgalpha == "100%"
        assert dut.fgcolor == "black"
        assert dut.gravity == "south"
        assert dut.gravity_hint == "natural"
        assert dut.insert_hyphens == "true"
        assert dut.lang == "en_US"
        assert dut.letter_spacing == 0.0
        assert dut.overline == "none"
        assert dut.overline_color == "black"
        assert dut.rise == "0pt"
        assert dut.scale == ""
        assert dut.size == 10
        assert dut.stretch == ""
        assert dut.strikethrough == "false"
        assert dut.strikethrough_color == "black"
        assert dut.style == "Normal"
        assert dut.underline == "none"
        assert dut.underline_color == "black"
        assert dut.variant == ""
        assert dut.weight == "Regular"

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-025")
    def test_no_toolkit_imports(self):
        """Should not import any toolkit-specific modules."""
        # Standard Library Imports
        import ast
        import inspect

        # pytkwrap Package Imports
        import pytkwrap.utilities as utilities_module

        _source = inspect.getsource(utilities_module)
        _tree = ast.parse(_source)

        _toolkit_names = {"Gdk", "GdkPixbuf", "Gio", "GLib", "GObject", "Gtk", "Pango"}
        _imports = set()

        for _node in ast.walk(_tree):
            if isinstance(_node, ast.Import):
                for _alias in _node.names:
                    _imports.add(_alias.name.split(".")[0])
            elif isinstance(_node, ast.ImportFrom):
                if _node.module:
                    _imports.add(_node.module.split(".")[0])

        assert not _toolkit_names & _imports, (
            f"Toolkit-specific imports found in common layer: "
            f"{_toolkit_names & _imports}"
        )

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-026")
    def test_to_string(self):
        """Should return a string representation of the font description."""
        dut = FontDescription()
        _font_description = dut.to_string()

        assert _font_description == "Sans,Serif,Monospace Normal  Regular  south 10"

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-027")
    def test_to_markup(self):
        """Should return a markup representation of the font description."""
        dut = FontDescription()
        dut.letter_spacing = 1024.0
        dut.scale = "small-caps"
        dut.stretch = "Condensed"
        dut.variant = "Small-Caps"
        _font_description = dut.to_markup()

        assert (
            _font_description
            == "<span allow_breaks='false' bgalpha='100%' bgcolor='white' "
            "face='Sans,Serif,Monospace' font_features='' fgalpha='100%' "
            "fgcolor='black' gravity='south' gravity_hint='natural' "
            "insert_hyphens='true' lang='en_US' letter_spacing='1024.0' "
            "overline='none' overline_color='black' rise='0pt' "
            "font_scale='small-caps' size='10pt' stretch='Condensed' "
            "strikethrough='false' strikethrough_color='black' style='Normal' "
            "underline='none' underline_color='black' variant='Small-Caps' "
            "weight='Regular'>"
        )

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-027")
    def test_to_markup_omits_optional_attrs(self):
        """Should return a markup representation of the font description."""
        dut = FontDescription()
        _font_description = dut.to_markup()

        assert (
            _font_description
            == "<span allow_breaks='false' bgalpha='100%' bgcolor='white' "
            "face='Sans,Serif,Monospace' font_features='' fgalpha='100%' "
            "fgcolor='black' gravity='south' gravity_hint='natural' "
            "insert_hyphens='true' lang='en_US' overline='none' "
            "overline_color='black' rise='0pt' size='10pt' strikethrough='false' "
            "strikethrough_color='black' style='Normal' underline='none' "
            "underline_color='black' weight='Regular'>"
        )

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-026")
    def test_to_string_custom_values(self):
        """to_string() should reflect custom font attributes."""
        dut = FontDescription(
            family="Monospace",
            style="Italic",
            weight="Bold",
            size=12,
        )
        _result = dut.to_string()

        assert "Monospace" in _result
        assert "Italic" in _result
        assert "Bold" in _result
        assert "12" in _result
