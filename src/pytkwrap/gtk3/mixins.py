#       pytkwrap.gtk3.mixins.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""The pytkwrap GTK3 mixins module."""

# Standard Library Imports
from types import EllipsisType

# pytkwrap Package Imports
from pytkwrap.common import DataWidgetAttributes, DataWidgetMixin, WidgetAttributes
from pytkwrap.gtk3._libs import GObject


class GTK3DataWidgetAttributes(DataWidgetAttributes, total=False):
    """GTK3-specific data widget attributes."""

    column_types: list[EllipsisType] | list[GObject.GType] | None


class GTK3DataWidgetMixin(DataWidgetMixin):
    """Adds GTK3-specific data widget attributes."""

    _GTK3_DATA_WIDGET_ATTRIBUTES = GTK3DataWidgetAttributes(
        column_types=None,
    )

    def __init__(self) -> None:
        """Initialize a new GTK3DataWidgetMixin."""
        super().__init__()

        # Initialize public instance attributes.
        self.dic_attributes.update(self._GTK3_DATA_WIDGET_ATTRIBUTES)

    def do_set_attributes(self, attributes: WidgetAttributes) -> None:
        """Set GTK3-specific data widget attributes.

        Parameters
        ----------
        attributes : GTK3DataWidgetAttributes
            The attributes to set.
        """
        super().do_set_attributes(attributes)

        self.dic_attributes["column_types"] = attributes.get(
            "column_types",
            self.dic_attributes["column_types"],
        )
