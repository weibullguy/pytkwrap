"""The pytkwrap GTK3TreeModelSort module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin, GTK3WidgetProperties


class GTK3TreeModelSort(Gtk.TreeModelSort, GTK3GObjectMixin):
    """Wrapper for version 3.0 Gtk.TreeModelSort."""

    _GTK3_TREEMODELSORT_PROPERTIES = GTK3WidgetProperties(
        model=None,
    )

    def __init__(
        self,
        model: Gtk.TreeModel | None,
    ) -> None:
        """Initialize an instance of the GTK3TreeModelSort."""
        Gtk.TreeModelSort.__init__(self, model=model)
        GTK3GObjectMixin.__init__(self)

        self.dic_properties.update(self._GTK3_TREEMODELSORT_PROPERTIES)
        self.dic_properties["model"] = model
