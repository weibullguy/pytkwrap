# Third Party Imports
from _typeshed import Incomplete

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk as Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin as GTK3GObjectMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties as GTK3WidgetProperties

class GTK3TreeModelSortMixin(GTK3GObjectMixin):
    _GTK3_TREEMODELSORT_PROPERTIES: Incomplete
    def __init__(self, **kwargs) -> None: ...

class GTK3TreeModelSort(Gtk.TreeModelSort, GTK3TreeModelSortMixin):
    def __init__(self, model: Gtk.TreeModel | None) -> None: ...
