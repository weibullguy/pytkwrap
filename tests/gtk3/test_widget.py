"""Test module for the GTK3WidgetMixin class.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Third Party Imports
import pytest

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3Widget

# pytkwrap Local Imports
from .conftest import BaseGTK3WidgetTests


class TestGTK3Widget(BaseGTK3WidgetTests):
    """Test class for the GTK3Widget class."""

    widget_class = GTK3Widget
    expected_attributes = [
        "activate",
        "add_accelerator",
        "add_device_events",
        "add_events",
        "add_mnemonic_label",
        "add_tick_callback",
        "can_activate_accel",
        "child_focus",
        "child_notify",
        # "class_path", # deprecated
        "compute_expand",
        "create_pango_context",
        "create_pango_layout",
        "destroy",
        "destroyed",
        "device_is_shadowed",
        # "drag_begin", # deprecated
        "drag_begin_with_coordinates",
        "drag_check_threshold",
        "drag_dest_add_image_targets",
        "drag_dest_add_text_targets",
        "drag_dest_add_uri_targets",
        "drag_dest_find_target",
        "drag_dest_get_target_list",
        "drag_dest_get_track_motion",
        "drag_dest_set",
        # "drag_dest_set_proxy", # deprecated
        "drag_dest_set_target_list",
        "drag_dest_set_track_motion",
        "drag_dest_unset",
        "drag_get_data",
        "drag_highlight",
        "drag_source_add_image_targets",
        "drag_source_add_text_targets",
        "drag_source_add_uri_targets",
        "drag_source_get_target_list",
        "drag_source_set",
        "drag_source_set_icon_gicon",
        "drag_source_set_icon_name",
        "drag_source_set_icon_pixbuf",
        # "drag_source_set_icon_stock", # deprecated
        "drag_source_set_target_list",
        "drag_source_unset",
        "drag_unhighlight",
        "draw",
        # "ensure_style", # deprecated
        "error_bell",
        "event",
        "freeze_child_notify",
        "get_accessible",
        "get_action_group",
        "get_allocated_baseline",
        "get_allocated_height",
        "get_allocated_size",
        "get_allocated_width",
        "get_allocation",
        "get_ancestor",
        "get_app_paintable",
        "get_can_default",
        "get_can_focus",
        # "get_child_requisition", # deprecated
        "get_child_visible",
        "get_clip",
        "get_clipboard",
        # "get_composite_name", # deprecated
        "get_device_enabled",
        "get_device_events",
        "get_direction",
        "get_display",
        "get_double_buffered",
        "get_events",
        "get_focus_on_click",
        "get_font_map",
        "get_font_options",
        "get_frame_clock",
        "get_halign",
        "get_has_tooltip",
        "get_has_window",
        "get_hexpand",
        "get_hexpand_set",
        "get_mapped",
        "get_margin_bottom",
        "get_margin_end",
        # "get_margin_left", # deprecated
        # "get_margin_right", # deprecated
        "get_margin_start",
        "get_margin_top",
        "get_modifier_mask",
        # "get_modifier_style", # deprecated
        "get_name",
        "get_no_show_all",
        "get_opacity",
        "get_pango_context",
        "get_parent",
        "get_path",
        # "get_pointer", # deprecated
        "get_preferred_height",
        "get_preferred_height_and_baseline_for_width",
        "get_preferred_height_for_width",
        "get_preferred_size",
        "get_preferred_width",
        "get_preferred_width_for_height",
        "get_realized",
        "get_receives_default",
        "get_request_mode",
        # "get_requisition", # deprecated
        # "get_root_window", # deprecated
        "get_scale_factor",
        "get_screen",
        "get_sensitive",
        "get_settings",
        "get_size_request",
        # "get_state", # deprecated
        "get_state_flags",
        # "get_style", # deprecated
        "get_style_context",
        "get_support_multidevice",
        "get_template_child",
        "get_tooltip_markup",
        "get_tooltip_text",
        "get_tooltip_window",
        "get_toplevel",
        "get_valign",
        "get_valign_with_baseline",
        "get_vexpand",
        "get_vexpand_set",
        "get_visible",
        "get_visual",
        "get_window",
        "grab_add",
        "grab_default",
        "grab_focus",
        "grab_remove",
        "has_default",
        "has_focus",
        "has_grab",
        # "has_rc_style", # deprecated
        "has_screen",
        "has_visible_focus",
        "hide",
        "hide_on_delete",
        "in_destruction",
        "init_template",
        "input_shape_combine_region",
        "insert_action_group",
        "intersect",
        "is_ancestor",
        # "is_composited", # deprecated
        "is_drawable",
        "is_focus",
        "is_sensitive",
        "is_toplevel",
        "is_visible",
        "keynav_failed",
        "list_accel_closures",
        "list_action_prefixes",
        "list_mnemonic_labels",
        "map",
        # "mnemonic_activate", # deprecated
        # "modify_base", # deprecated
        # "modify_bg", # deprecated
        # "modify_cursor", # deprecated
        # "modify_fg", # deprecated
        # "modify_font", # deprecated
        # "modify_style", # deprecated
        # "modify_text", # deprecated
        # "override_background_color", # deprecated
        # "override_color", # deprecated
        # "override_cursor", # deprecated
        # "override_font", # deprecated
        # "override_symbolic_color", #deprecated
        # "path", # deprecated
        "queue_allocate",
        "queue_compute_expand",
        "queue_draw",
        "queue_draw_area",
        "queue_draw_region",
        "queue_resize",
        "queue_resize_no_redraw",
        "realize",
        # "region_intersect", # deprecated
        "register_window",
        "remove_accelerator",
        "remove_mnemonic_label",
        "remove_tick_callback",
        # "render_icon", # deprecated
        # "render_icon_pixbuf", # deprecated
        # "reparent", # deprecated
        # "reset_rc_styles", # deprecated
        "reset_style",
        # "send_expose", # deprecated
        "send_focus_change",
        "set_accel_path",
        "set_allocation",
        "set_app_paintable",
        "set_can_default",
        "set_can_focus",
        "set_child_visible",
        "set_clip",
        # "set_composite_name", # deprecated
        "set_device_enabled",
        "set_device_events",
        "set_direction",
        # "set_double_buffered", # deprecated
        "set_events",
        "set_focus_on_click",
        "set_font_map",
        "set_font_options",
        "set_halign",
        "set_has_tooltip",
        "set_has_window",
        "set_hexpand",
        "set_hexpand_set",
        "set_mapped",
        "set_margin_bottom",
        "set_margin_end",
        # "set_margin_left", # deprecated
        # "set_margin_right", # deprecated
        "set_margin_start",
        "set_margin_top",
        "set_name",
        "set_no_show_all",
        "set_opacity",
        "set_parent",
        "set_parent_window",
        "set_realized",
        "set_receives_default",
        "set_redraw_on_allocate",
        "set_sensitive",
        "set_size_request",
        # "set_state", # deprecated
        "set_state_flags",
        # "set_style", # deprecated
        "set_support_multidevice",
        "set_tooltip_markup",
        "set_tooltip_text",
        "set_tooltip_window",
        "set_valign",
        "set_vexpand",
        "set_vexpand_set",
        "set_visible",
        "set_visual",
        "set_window",
        "shape_combine_region",
        "show",
        "show_all",
        "show_now",
        "size_allocate",
        "size_allocate_with_baseline",
        # "size_request", # deprecated
        # "style_attach", # deprecated
        "style_get_property",
        "thaw_child_notify",
        "translate_coordinates",
        "trigger_tooltip_query",
        "unmap",
        "unparent",
        "unrealize",
        "unregister_window",
        "unset_state_flags",
    ]
    expected_default_height = -1
    expected_default_tooltip = ""
    expected_default_width = -1

    @pytest.mark.unit
    def test_do_set_properties(self):
        dut = self.make_dut()
        dut.do_set_properties(GTK3WidgetProperties())

        assert dut.dic_properties == {
            "can_default": False,
            "can_focus": False,
            "focus_on_click": True,
            "halign": Gtk.Align.FILL,
            "has_default": False,
            "has_focus": False,
            "has_tooltip": False,
            "height_request": -1,
            "hexpand": False,
            "hexpand_set": False,
            "is_focus": False,
            "margin": 0,
            "margin_bottom": 0,
            "margin_end": 0,
            "margin_start": 0,
            "margin_top": 0,
            "name": "pytkwrap GTK3 widget",
            "opacity": 1.0,
            "parent": None,
            "receives_default": False,
            "scale_factor": 1,
            "sensitive": True,
            "tooltip_markup": "Missing tooltip, please file an issue to have one added.",
            "tooltip_text": "Missing tooltip, please file an issue to have one added.",
            "valign": Gtk.Align.FILL,
            "vexpand": False,
            "vexpand_set": False,
            "visible": False,
            "width_request": -1,
            "window": None,
        }
