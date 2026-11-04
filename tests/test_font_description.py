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

        assert dut.family == "Sans,Serif,Monospace"
        assert dut.features == ""
        assert dut.size == 10
        assert dut.stretch == ""
        assert dut.style == "normal"
        assert dut.variant == "normal"
        assert dut.weight == "normal"

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
    @pytest.mark.requirement("PTW-COM-X-027")
    def test_to_string(self):
        """Should return a string representation of the font description."""
        dut = FontDescription()
        _font_description = dut.to_string()

        assert _font_description == "Sans,Serif,Monospace normal normal normal  10"

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
            == "<span face='Sans,Serif,Monospace' font_features='' size='10pt' "
            "stretch='Condensed' style='normal' variant='Small-Caps' weight='normal'>"
        )

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-027")
    def test_to_markup_omits_optional_attrs(self):
        """Should return a markup representation of the font description."""
        dut = FontDescription()
        _font_description = dut.to_markup()

        assert (
            _font_description
            == "<span face='Sans,Serif,Monospace' font_features='' size='10pt' "
            "style='normal' variant='normal' weight='normal'>"
        )

    @pytest.mark.unit
    @pytest.mark.requirement("PTW-COM-X-027")
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
