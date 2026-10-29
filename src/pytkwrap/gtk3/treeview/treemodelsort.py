"""The pytkwrap GTK3TreeModelSort module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3GObjectMixin, GTK3WidgetProperties


class GTK3TreeModelSortMixin(GTK3GObjectMixin):
    """Mixin class for GTK3TreeModelSort.

    Attributes
    ----------
    _GTK3_TREEMODELSORT_PROPERTIES : GTK3WidgetProperties
        Properties unique to the GTK3TreeModelSort.
    """

    _GTK3_TREEMODELSORT_PROPERTIES = GTK3WidgetProperties(
        model=None,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3TreeModelSort mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_TREEMODELSORT_PROPERTIES)

    def do_convert_iter(
        self,
        child_iter: Gtk.TreeIter | None = None,
        sorted_iter: Gtk.TreeIter | None = None,
        child_to_sorted: bool = True,
    ) -> tuple[bool, Gtk.TreeIter] | Gtk.TreeIter:
        """Convert an iter from the child model to an iter in the sorted model.

        Parameters
        ----------
        child_iter : Gtk.TreeIter
            The Gtk.TreeIter in the child model.
        sorted_iter : Gtk.TreeIter | None, optional
            The Gtk.TreeIter in the sorted model.
        child_to_sorted: bool
            Indicates whether to convert a child iter to a sorted iter (default) or
            vice versa.

        Returns
        -------
        tuple[int, Gtk.TreeIter] | Gtk.TreeIter
            When converting from child to sorted, this method returns a tuple where
            the boolean value indicates whether the sorted iter was set and the
            Gtk.TreeIter is the sorted iter.  When converting from sorted to child,
            just the child iter is returned.
        """
        if child_to_sorted:
            return self.convert_child_iter_to_iter(child_iter)
        return self.convert_iter_to_child_iter(sorted_iter)

    def do_convert_path(
        self,
        child_path: Gtk.TreePath | None = None,
        sorted_path: Gtk.TreePath | None = None,
        child_to_sorted: bool = True,
    ) -> Gtk.TreePath | None:
        """Convert an iter from the child model to an iter in the sorted model.

        Parameters
        ----------
        child_path : Gtk.TreePath, optional
            The Gtk.TreePath in the child model.
        sorted_path : Gtk.TreePath | None, optional
            The Gtk.TreePath in the sorted model.
        child_to_sorted: bool
            Indicates whether to convert a child path to a sorted path (default) or
            vice versa.

        Returns
        -------
        Gtk.TreePath | None
            The newly allocated Gtk.TreePath .
        """
        if child_to_sorted:
            return self.convert_child_path_to_path(child_path)
        return self.convert_path_to_child_path(sorted_path)


class GTK3TreeModelSort(Gtk.TreeModelSort, GTK3TreeModelSortMixin):
    """Wrapper for version 3.0 Gtk.TreeModelSort."""

    def __init__(
        self,
        model: Gtk.TreeModel | None,
    ) -> None:
        """Initialize an instance of the GTK3TreeModelSort.

        Parameters
        ----------
        model : Gtk.TreeModel | None
            The child Gtk.TreeModel to sort.
        """
        Gtk.TreeModelSort.__init__(self, model=model)
        GTK3TreeModelSortMixin.__init__(self)

        self.dic_properties["model"] = model
