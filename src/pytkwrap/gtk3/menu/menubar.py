"""The pytkwrap GTK3MenuBar module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gio, Gtk
from pytkwrap.gtk3.menu.menushell import GTK3MenuShellMixin
from pytkwrap.gtk3.mixins import GTK3WidgetProperties


class GTK3MenuBarMixin(GTK3MenuShellMixin):
    """Mixin class for GTK3MenuBar.

    Notes
    -----
    GTK3MenuBar passes no widgets to its callback functions.
    """

    _GTK3_MENUBAR_PROPERTIES = GTK3WidgetProperties(
        child_pack_direction=Gtk.PackDirection.LTR,
        pack_direction=Gtk.PackDirection.LTR,
    )

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3MenuBar mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_MENUBAR_PROPERTIES)

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3MenuBar-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of
            tuples with the property values to set for the GTK3MenuBar.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        self.set_child_pack_direction(self.dic_properties["child_pack_direction"])
        self.set_pack_direction(self.dic_properties["pack_direction"])


class GTK3MenuBar(Gtk.MenuBar, GTK3MenuBarMixin):
    """Wrapper for version 3.0 Gtk.MenuBar."""

    def __init__(self, model: Gio.MenuModel | None = None) -> None:
        """Initialize an instance of the GTK3MenuBar.

        Parameters
        ----------
        model : Gio.MenuModel | None
            The Gio.MenuModel to associate the GTK3MenuBar with.

        Notes
        -----
        The Gtk.MenuBar has a new_with_model(model) method, but passing model=model
        to the Gtk.MenuBar __init__ method raises the following error:

        TypeError: gobject `pytkwrap+gtk3+menu+menubar+GTK3MenuBar' doesn't support
        property `model'
        """
        Gtk.MenuBar.__init__(self)
        GTK3MenuBarMixin.__init__(self)

        if model is not None:
            self.bind_model(model)
