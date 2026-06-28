# Standard Library Imports
import sys

try:
    # Third Party Imports
    import gi

    gi.require_version("Gdk", "3.0")
    gi.require_version("GLib", "2.0")
    gi.require_version("Gtk", "3.0")
except ImportError:
    print("Failed to import package gi; exiting.")
    sys.exit(1)
# Third Party Imports
from gi.repository import Gtk, Pango

EXPECTED_CELLRENDERER_HANDLER_IDS = {"editing-canceled": -1, "editing-started": -1}
EXPECTED_CELLRENDERER_METHODS = [
    "activate",
    "get_aligned_area",
    "get_alignment",
    "get_fixed_size",
    "get_padding",
    "get_preferred_height",
    "get_preferred_height_for_width",
    "get_preferred_size",
    "get_preferred_width",
    "get_preferred_width_for_height",
    "get_request_mode",
    "get_sensitive",
    "get_state",
    "get_visible",
    "is_activatable",
    "render",
    "set_alignment",
    "set_fixed_size",
    "set_padding",
    "set_sensitive",
    "set_visible",
    "start_editing",
    "stop_editing",
]
EXPECTED_CELLRENDERER_PROPERTIES = {
    "cell_background": None,
    "cell_background_rgba": None,
    "cell_background_set": False,
    "height": -1,
    "is_expanded": False,
    "is_expander": False,
    "mode": Gtk.CellRendererMode.INERT,
    "sensitive": True,
    "visible": True,
    "width": -1,
    "xalign": 0.5,
    "xpad": 0,
    "yalign": 0.5,
    "ypad": 0,
}

EXPECTED_CELLRENDERERPIXBUF_PROPERTIES = {
    "gicon": None,
    "icon_name": None,
    "pixbuf": None,
    "pixbuf_expander_closed": None,
    "pixbuf_expander_open": None,
    "stock_detail": None,
    "stock_size": 1,
    "surface": None,
}

EXPECTED_CELLRENDERERPROGRESS_PROPERTIES = {
    "inverted": False,
    "pulse": -1,
    "text": None,
    "text_xalign": 0.5,
    "text_yalign": 0.5,
    "value": 0,
}

EXPECTED_CELLRENDERESPINNER_PROPERTIES = {
    "active": False,
    "pulse": 0,
    "size": Gtk.IconSize.MENU,
}

EXPECTED_CELLRENDERERTEXT_HANDLER_IDS = {"edited": -1}
EXPECTED_CELLRENDERERTEXT_METHODS = ["set_fixed_height_from_font"]
EXPECTED_CELLRENDERERTEXT_PROPERTIES = {
    "align_set": False,
    "alignment": Pango.Alignment.LEFT,
    "attributes": None,
    "background": None,
    "background_rgba": None,
    "background_set": False,
    "editable": False,
    "editable_set": False,
    "ellipsize": Pango.EllipsizeMode.NONE,
    "ellipsize_set": False,
    "family": None,
    "family_set": False,
    "font": None,
    "font_desc": None,
    "foreground": None,
    "foreground_rgba": None,
    "foreground_set": False,
    "language": None,
    "language_set": False,
    "markup": None,
    "max_width_chars": -1,
    "placeholder_text": None,
    "rise": 0,
    "rise_set": False,
    "scale": 1.0,
    "scale_set": False,
    "single_paragraph_mode": False,
    "size": 0,
    "size_points": 0.0,
    "size_set": False,
    "stretch": Pango.Stretch.NORMAL,
    "stretch_set": False,
    "strikethrough": False,
    "strikethrough_set": False,
    "style": Pango.Style.NORMAL,
    "style_set": False,
    "text": None,
    "underline": Pango.Underline.NONE,
    "underline_set": False,
    "variant": Pango.Variant.NORMAL,
    "variant_set": False,
    "weight": 400,
    "weight_set": False,
    "width_chars": -1,
    "wrap_mode": Pango.WrapMode.CHAR,
    "wrap_width": -1,
}

EXPECTED_CELLRENDERERCOMBO_HANDLER_IDS = {"changed": -1}
EXPECTED_CELLRENDERERCOMBO_PROPERTIES = {
    "has_entry": True,
    "model": None,
    "text_column": -1,
}

EXPECTED_CELLRENDERERSPIN_PROPERTIES = {
    "adjustment": None,
    "climb_rate": 0.0,
    "digits": 0,
}

EXPECTED_CELLRENDERERTOGGLE_HANDLER_IDS = {"toggled": -1}
EXPECTED_CELLRENDERERTOGGLE_METHODS = [
    "get_activatable",
    "get_active",
    "get_radio",
    "set_activatable",
    "set_active",
    "set_radio",
]
EXPECTED_CELLRENDERERTOGGLE_PROPERTIES = {
    "activatable": True,
    "active": False,
    "inconsistent": False,
    "radio": False,
}

EXPECTED_CELLVIEW_METHODS = [
    "get_displayed_row",
    "get_draw_sensitive",
    "get_fit_model",
    "get_model",
    "get_size_of_row",
    "set_background_rgba",
    "set_displayed_row",
    "set_draw_sensitive",
    "set_fit_model",
    "set_model",
]
EXPECTED_CELLVIEW_PROPERTIES = {
    "background": None,
    "background_rgba": None,
    "background_set": False,
    "cell_area": None,
    "cell_area_context": None,
    "draw_sensitive": False,
    "fit_model": False,
    "model": None,
}

EXPECTED_TREEVIEWCOLUMN_HANDLER_IDS = {"clicked": -1}
EXPECTED_TREEVIEWCOLUMN_METHODS = [
    "add_attribute",
    "cell_get_position",
    "cell_get_size",
    "cell_is_visible",
    "cell_set_cell_data",
    "clear",
    "clear_attributes",
    "clicked",
    "focus_cell",
    "get_alignment",
    "get_button",
    "get_clickable",
    "get_expand",
    "get_fixed_width",
    "get_max_width",
    "get_min_width",
    "get_reorderable",
    "get_resizable",
    "get_sizing",
    "get_sort_column_id",
    "get_sort_indicator",
    "get_sort_order",
    "get_spacing",
    "get_title",
    "get_tree_view",
    "get_visible",
    "get_widget",
    "get_width",
    "get_x_offset",
    "pack_end",
    "pack_start",
    "queue_resize",
    "set_alignment",
    "set_attributes",
    "set_cell_data_func",
    "set_clickable",
    "set_expand",
    "set_fixed_width",
    "set_max_width",
    "set_min_width",
    "set_reorderable",
    "set_resizable",
    "set_sizing",
    "set_sort_column_id",
    "set_sort_indicator",
    "set_sort_order",
    "set_spacing",
    "set_title",
    "set_visible",
    "set_widget",
]
EXPECTED_TREEVIEWCOLUMN_PROPERTIES = {
    "alignment": 0.0,
    "cell_area": None,
    "clickable": False,
    "expand": False,
    "fixed_width": -1,
    "max_width": -1,
    "min_width": -1,
    "reorderable": False,
    "resizable": False,
    "sizing": Gtk.TreeViewColumnSizing.GROW_ONLY,
    "sort_column_id": -1,
    "sort_indicator": False,
    "sort_order": Gtk.SortType.ASCENDING,
    "spacing": 0,
    "title": "",
    "visible": True,
    "widget": None,
    "width": 0,
    "x_offset": 0,
}
