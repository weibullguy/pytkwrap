"""Tests for loading GTK3 menu data."""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.exceptions import MenuError, WrongTypeError
from pytkwrap.gtk3.menu.menuloader import (
    _as_mapping,
    _required_mapping,
    do_build_menu_from_file,
)


@pytest.mark.unit
def test_invalid_menu_value_logs_and_raises_wrong_type(logged_errors):
    """Invalid menu value types should log and raise WrongTypeError."""
    with pytest.raises(WrongTypeError, match="menu must be a TOML table"):
        _as_mapping(None, "menu")

    assert logged_errors == ["menu must be a TOML table."]


@pytest.mark.unit
def test_missing_menu_table_logs_and_raises_menu_error(logged_errors):
    """Missing required menu tables should log and raise MenuError."""
    with pytest.raises(MenuError, match="missing required table"):
        _required_mapping({}, "attributes", "menu.items[0]")

    assert logged_errors == ["menu.items[0] is missing required table 'attributes'."]


@pytest.mark.unit
def test_invalid_filename_logs_and_raises_wrong_type(logged_errors):
    """Invalid filename types should log and raise WrongTypeError."""
    with pytest.raises(WrongTypeError, match="filename must be"):
        do_build_menu_from_file(None)

    assert logged_errors == ["filename must be a string or pathlib.Path."]


@pytest.mark.unit
def test_unreadable_menu_file_logs_and_chains_os_error(tmp_path, logged_errors):
    """File loading failures should log and retain the original exception."""
    _filename = tmp_path / "missing.toml"

    with pytest.raises(MenuError, match="Could not load menu TOML file") as _error:
        do_build_menu_from_file(_filename)

    assert isinstance(_error.value.__cause__, OSError)
    assert len(logged_errors) == 1
    assert logged_errors[0] == str(_error.value)


@pytest.mark.unit
def test_malformed_toml_logs_and_chains_parse_error(tmp_path, logged_errors):
    """Malformed TOML should log MenuError and retain the parse exception."""
    _filename = tmp_path / "invalid.toml"
    _filename.write_text("[menu\n", encoding="utf-8")

    with pytest.raises(MenuError, match="Could not load menu TOML file") as _error:
        do_build_menu_from_file(_filename)

    assert isinstance(_error.value.__cause__, ValueError)
    assert len(logged_errors) == 1
    assert logged_errors[0] == str(_error.value)
