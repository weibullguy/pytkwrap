"""Tests for building GTK3 menus."""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.exceptions import MenuError
from pytkwrap.gtk3.menu.menubuilder import _connect_gtk_callback
from pytkwrap.gtk3.menu.models import GTK3MenuShellAttribute, GTK3MenuShellItem


@pytest.mark.unit
@pytest.mark.usefixtures("logged_errors")
def test_callback_without_signal_logs_and_raises_menu_error(logged_errors):
    """A callback without a signal should log and raise MenuError."""
    _node = GTK3MenuShellItem(
        attributes=GTK3MenuShellAttribute(
            callback=lambda: None,
            label="Invalid",
        )
    )

    with pytest.raises(MenuError, match="has a callback but no signal"):
        _connect_gtk_callback(None, _node)

    assert logged_errors == ["Menu item 'Invalid' has a callback but no signal."]


@pytest.mark.unit
@pytest.mark.usefixtures("logged_errors")
def test_invalid_callback_signal_logs_and_chains_type_error(logged_errors):
    """GTK callback connection failures should log and retain their cause."""

    class _Item:
        def connect(self, _signal, _callback):
            raise TypeError("invalid signal")

    _node = GTK3MenuShellItem(
        attributes=GTK3MenuShellAttribute(
            callback=lambda: None,
            label="Invalid",
            signal="not-a-signal",
        )
    )

    with pytest.raises(MenuError, match="Could not connect signal") as _error:
        _connect_gtk_callback(_Item(), _node)

    assert isinstance(_error.value.__cause__, TypeError)
    assert logged_errors == [
        "Could not connect signal 'not-a-signal' for menu item 'Invalid'."
    ]
