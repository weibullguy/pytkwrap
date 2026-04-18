#       pytkwrap.gtk3.__init__.py is part of the pytkwrap project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""The pytkwrap GTK3 package.

NOTE: Sub-modules in this package must import siblings directly
(e.g. from pytkwrap.gtk3.combo import GTK3ComboBox)
and never through this __init__.py to avoid circular imports.
"""

# pytkwrap Local Imports
from .buttons import (
    GTK3BaseButton,
    GTK3CheckButton,
    GTK3ColorButton,
    GTK3FileChooserButton,
    GTK3OptionButton,
    GTK3SpinButton,
    do_make_buttonbox,
)
from .combo import GTK3ComboBox
from .entry import GTK3Entry
from .frame import GTK3Frame
from .label import (
    GTK3Label,
    do_make_label_group,
)
from .matrixview import GTK3MatrixView
from .mixins import (
    GTK3DataWidgetAttributes,
    GTK3DataWidgetMixin,
)
from .plotview import GTK3PlotView
from .scrolledwindow import GTK3ScrolledWindow
from .textview import GTK3TextView
from .widget import (
    GTK3BaseDataWidget,
    GTK3BaseWidget,
    GTK3WidgetProperties,
)


__all__ = [
    "GTK3BaseButton",
    "GTK3BaseDataWidget",
    "GTK3BaseWidget",
    "GTK3CheckButton",
    "GTK3ColorButton",
    "GTK3ComboBox",
    "GTK3DataWidgetAttributes",
    "GTK3DataWidgetMixin",
    "GTK3Entry",
    "GTK3FileChooserButton",
    "GTK3Frame",
    "GTK3Label",
    "GTK3MatrixView",
    "GTK3OptionButton",
    "GTK3PlotView",
    "GTK3ScrolledWindow",
    "GTK3SpinButton",
    "GTK3TextView",
    "GTK3WidgetProperties",
    "do_make_buttonbox",
    "do_make_label_group",
]
