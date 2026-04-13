#       pytkwrap.gtk3.mixins.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""The pytkwrap GTK3 mixins module."""

# Standard Library Imports
from types import EllipsisType

# pytkwrap Package Imports
from pytkwrap.common import DataWidgetAttributes, DataWidgetMixin
from pytkwrap.gtk3._libs import GObject, Pango


class GTK3DataWidgetAttributes(DataWidgetAttributes, total=False):
    """GTK3-specific data widget attributes."""

    column_types: list[EllipsisType] | list[GObject.GType] | None
    font_description: Pango.FontDescription | str | None


class GTK3DataWidgetMixin(DataWidgetMixin):
    """Adds GTK3-specific data widget attributes."""

    _DEFAULT_EDIT_SIGNAL: str = ""
    _GTK3_DATA_WIDGET_ATTRIBUTES = GTK3DataWidgetAttributes(column_types=None,
                                                       font_description=None,)

    def __init__(self) -> None:
        """Initialize a new GTK3DataWidgetMixin."""
        super().__init__()

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_DATA_WIDGET_ATTRIBUTES)

        self.column_types: list[EllipsisType] | list[GObject.GType] | None = None
        self.edit_signal: str=self._DEFAULT_EDIT_SIGNAL
        self.font_description: Pango.FontDescription | str | None = None
