"""The pytkwrap GTK3 package.

NOTE: Sub-modules in this package must import siblings directly
(e.g. from pytkwrap.gtk3.combo import GTK3ComboBox)
and never through this __init__.py to avoid circular imports.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Local Imports
from .adjustment import GTK3Adjustment
from .bin import GTK3Bin
from .buttons import (
    GTK3Button,
    GTK3CheckButton,
    GTK3ColorButton,
    GTK3FontButton,
    GTK3MenuButton,
    GTK3RadioButton,
    GTK3ScaleButton,
    GTK3ToggleButton,
    GTK3VolumeButton,
    do_make_buttonbox,
)
from .calendar import GTK3Calendar
from .cellrenderer import GTK3CellRenderer
from .container import GTK3Container

# from .combo import GTK3ComboBox
# from .entry import GTK3Entry
# from .frame import GTK3Frame
# from .label import (
#    GTK3Label,
#    do_make_label_group,
# )
# from .matrixview import GTK3MatrixView
from .mixins import (
    GTK3GObjectMixin,
    GTK3WidgetAttributes,
    GTK3WidgetProperties,
    set_widget_sensitivity,
)

# from .plotview import GTK3PlotView
# from .scrolledwindow import GTK3ScrolledWindow
# from .textview import GTK3TextView
from .treeviewcolumn import GTK3TreeViewColumn
from .widget import GTK3Widget

__all__ = [
    "GTK3Adjustment",
    "GTK3Bin",
    "GTK3Button",
    "GTK3Calendar",
    "GTK3CellRenderer",
    "GTK3CheckButton",
    "GTK3ColorButton",
    "GTK3Container",
    "GTK3FontButton",
    #    "GTK3ComboBox",
    #    "GTK3Entry",
    #    "GTK3FileChooserButton",
    #    "GTK3Frame",
    "GTK3GObjectMixin",
    #    "GTK3Label",
    #    "GTK3MatrixView",
    "GTK3MenuButton",
    #    "GTK3PlotView",
    "GTK3RadioButton",
    #   "GTK3ScrolledWindow",
    "GTK3ScaleButton",
    #    "GTK3SpinButton",
    #    "GTK3TextView",
    "GTK3ToggleButton",
    "GTK3TreeViewColumn",
    "GTK3VolumeButton",
    "GTK3Widget",
    "GTK3WidgetAttributes",
    "GTK3WidgetProperties",
    "do_make_buttonbox",
    #    "do_make_label_group",
    "set_widget_sensitivity",
]
