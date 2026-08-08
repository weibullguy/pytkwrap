"""The pytkwrap GTK3CellRendererText module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from collections.abc import Mapping

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk, Pango
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.treeview.cellrenderer import GTK3CellRendererMixin


class GTK3CellRendererTextMixin(GTK3CellRendererMixin):
    """Mixin class for GTK3CellRendererText."""

    _GTK3_CELLRENDERERTEXT_PROPERTIES = GTK3WidgetProperties(
        align_set=False,
        alignment=Pango.Alignment.LEFT,
        attributes=None,
        background=None,
        background_rgba=None,
        background_set=False,
        editable=False,
        editable_set=False,
        ellipsize=Pango.EllipsizeMode.NONE,
        ellipsize_set=False,
        family=None,
        family_set=False,
        font=None,
        font_desc=None,
        foreground=None,
        foreground_rgba=None,
        foreground_set=False,
        language=None,
        language_set=False,
        markup=None,
        max_width_chars=-1,
        placeholder_text=None,
        rise=0,
        rise_set=False,
        scale=1.0,
        scale_set=False,
        single_paragraph_mode=False,
        size=0,
        size_points=0.0,
        size_set=False,
        stretch=Pango.Stretch.NORMAL,
        stretch_set=False,
        strikethrough=False,
        strikethrough_set=False,
        style=Pango.Style.NORMAL,
        style_set=False,
        text=None,
        underline=Pango.Underline.NONE,
        underline_set=False,
        variant=Pango.Variant.NORMAL,
        variant_set=False,
        weight=400,
        weight_set=False,
        width_chars=-1,
        wrap_mode=Pango.WrapMode.CHAR,
        wrap_width=-1,
    )
    _GTK3_CELLRENDERERTEXT_SIGNALS = [
        "edited",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3CellRendererText mixin."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_properties.update(self._GTK3_CELLRENDERERTEXT_PROPERTIES)
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_CELLRENDERERTEXT_SIGNALS}
        )

    def do_set_properties(
        self,
        properties: Mapping[str, object] | list[list | tuple],
    ) -> None:
        """Set the values of the GTK3CellRendererText-specific properties.

        Parameters
        ----------
        properties : GTK3WidgetProperties | dict | list[list | tuple]
            The typed dict (preferred), non-typed dict, list of lists, or list of tuples
            with the property values to set for the GTK3CellRendererText.
        """
        # Update the property dictionary.
        super().do_set_properties(properties)

        # TODO: Replace this with a FontDescription object after adding methods to
        #  the FontDescription class to set the Pango properties and return a
        #  Pango.FontDescription.
        if self.dic_properties.get("family"):
            _font_desc = Pango.FontDescription()
            _font_desc.set_family(self.dic_properties.get("family", "Sans"))

            if self.dic_properties.get("size"):
                _font_desc.set_size(self.dic_properties.get("size") * Pango.SCALE)
            if self.dic_properties.get("stretch"):
                _font_desc.set_stretch(self.dic_properties.get("stretch"))
            if self.dic_properties.get("style"):
                _font_desc.set_style(self.dic_properties.get("style"))
            if self.dic_properties.get("variant"):
                _font_desc.set_variant(self.dic_properties.get("variant"))
            if self.dic_properties.get("weight"):
                _font_desc.set_weight(self.dic_properties.get("weight"))

            self.dic_properties["font_desc"] = _font_desc
        elif self.dic_properties.get("font"):
            _font_desc = Pango.FontDescription.from_string(
                self.dic_properties.get("font")
            )
            self.dic_properties["font_desc"] = _font_desc

        if self.dic_properties.get("font_desc"):
            self.dic_properties["family_set"] = True
            self.dic_properties["size_set"] = True
            self.dic_properties["stretch_set"] = True
            self.dic_properties["style_set"] = True
            self.dic_properties["variant_set"] = True
            self.dic_properties["weight_set"] = True

        for _property in [
            "align_set",
            "alignment",
            "attributes",
            "background",
            "background_rgba",
            "background_set",
            "editable",
            "editable_set",
            "ellipsize",
            "ellipsize_set",
            "family_set",
            "font_desc",
            "foreground",
            "foreground_rgba",
            "foreground_set",
            "language",
            "language_set",
            "markup",
            "max_width_chars",
            "placeholder_text",
            "rise",
            "rise_set",
            "scale",
            "scale_set",
            "single_paragraph_mode",
            "size_points",
            "size_set",
            "stretch_set",
            "strikethrough",
            "strikethrough_set",
            "style_set",
            "text",
            "underline",
            "underline_set",
            "variant_set",
            "weight_set",
            "width_chars",
            "wrap_mode",
            "wrap_width",
        ]:
            self.set_property(
                _property.replace("_", "-"), self.dic_properties[_property]
            )


class GTK3CellRendererText(Gtk.CellRendererText, GTK3CellRendererTextMixin):
    """Wrapper for version 3.0 Gtk.CellRendererText."""

    def __init__(self) -> None:
        """Initialize an instance of the GTK3CellRendererText."""
        Gtk.CellRendererText.__init__(self)
        GTK3CellRendererTextMixin.__init__(self)
