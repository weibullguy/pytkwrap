# Third Party Imports
from gi.overrides.Gdk import Gdk
from gi.overrides.Gtk import Gtk

EXPECTED_WIDGET_HANDLER_IDS = {
    "destroy": -1,
    "direction-changed": -1,
    "hide": -1,
    "keynav-failed": -1,
    "map": -1,
    "mnemonic-activate": -1,
    "move-focus": -1,
    "notify": -1,
    "query-tooltip": -1,
    "realize": -1,
    "show": -1,
    "state-flags-changed": -1,
    "unmap": -1,
    "unrealize": -1,
}
EXPECTED_WIDGET_PROPERTIES = {
    "app_paintable": False,
    "can_default": False,
    "can_focus": False,
    "composite_child": False,
    "events": Gdk.EventMask.ALL_EVENTS_MASK,
    "expand": False,
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
    "no_show_all": False,
    "opacity": 1.0,
    "parent": None,
    "receives_default": False,
    "scale_factor": 1,
    "sensitive": True,
    "style": None,
    "tooltip_markup": "Missing tooltip, please file an issue to have one added.",
    "tooltip_text": "Missing tooltip, please file an issue to have one added.",
    "valign": Gtk.Align.FILL,
    "vexpand": False,
    "vexpand_set": False,
    "visible": False,
    "width_request": -1,
    "window": None,
}

EXPECTED_CALENDAR_HANDLER_IDS = {
    "day-selected": -1,
    "day-selected-double-click": -1,
    "month-changed": -1,
    "next-month": -1,
    "next-year": -1,
    "prev-month": -1,
    "prev-year": -1,
}
EXPECTED_CALENDAR_PROPERTIES = {
    "day": 0,
    "detail_height_rows": 0,
    "detail_width_chars": 0,
    "month": 0,
    "no_month_change": False,
    "show_day_names": True,
    "show_details": True,
    "show_heading": True,
    "show_week_numbers": False,
    "year": 0,
}

EXPECTED_CONTAINER_HANDLER_IDS = {
    "add": -1,
    "check-resize": -1,
    "remove": -1,
    "set-focus-child": -1,
}
EXPECTED_CONTAINER_PROPERTIES = {"border_width": 0}

EXPECTED_BUTTON_HANDLER_IDS = {"activate": -1, "clicked": -1}
EXPECTED_BUTTON_PROPERTIES = {
    "always_show_image": False,
    "image": None,
    "image_position": Gtk.PositionType.LEFT,
    "label": "...",
    "relief": Gtk.ReliefStyle.NORMAL,
    "use_underline": False,
}

EXPECTED_COLOR_BUTTON_HANDLER_IDS = {"color-set": -1}
EXPECTED_COLOR_BUTTON_PROPERTIES = {
    "alpha": 65535,
    "rgba": None,
    "show_editor": False,
    "title": "Pick a Color",
    "use_alpha": True,
}

EXPECTED_FONT_BUTTON_HANDLER_IDS = {"font-set": -1}
EXPECTED_FONT_BUTTON_PROPERTIES = {
    "font_name": "Sans 12",
    "show_size": True,
    "show_style": True,
    "title": "Pick a Font",
    "use_font": False,
    "use_size": False,
}

EXPECTED_SCALE_BUTTON_HANDLER_IDS = {"popdown": -1, "popup": -1, "value-changed": -1}
EXPECTED_SCALE_BUTTON_PROPERTIES = {
    "adjustment": None,
    "icons": None,
    "size": 16,
    "value": 0.0,
}

EXPECTED_VOLUME_BUTTON_PROPERTIES = {"use_stock": False}

EXPECTED_TOGGLE_BUTTON_HANDLER_IDS = {"toggled": -1}
EXPECTED_TOGGLE_BUTTON_PROPERTIES = {
    "active": False,
    "draw_indicator": False,
    "inconsistent": False,
    "use_underline": False,
}

EXPECTED_RADIO_BUTTON_HANDLER_IDS = {"group-changed": -1}
EXPECTED_RADIO_BUTTON_PROPERTIES = {"group": None}

EXPECTED_MENU_BUTTON_PROPERTIES = {
    "align_widget": None,
    "direction": Gtk.ArrowType.DOWN,
    "menu_model": None,
    "popover": None,
    "popup": None,
    "use_popover": True,
}

EXPECTED_COMBOBOX_HANDLER_IDS = {
    "changed": -1,
    "editing-done": -1,
    "format-entry-text": -1,
    "move-active": -1,
    "popdown": -1,
    "popup": -1,
    "remove-widget": -1,
}
EXPECTED_COMBOBOX_PROPERTIES = {
    "active": -1,
    "active_id": None,
    "button_sensitivity": Gtk.SensitivityType.AUTO,
    "cell_area": None,
    "column_span_column": -1,
    "editing_canceled": False,
    "entry_text_column": -1,
    "has_entry": False,
    "has_frame": True,
    "id_column": -1,
    "model": None,
    "popup_fixed_width": True,
    "popup_shown": False,
    "row_span_column": -1,
    "wrap_width": 0,
}

EXPECTED_APP_CHOOSER_BUTTON_HANDLER_IDS = {"custum-item-activated": -1}
EXPECTED_APP_CHOOSER_BUTTON_PROPERTIES = {
    "heading": None,
    "show_default_item": False,
    "show_dialog_item": False,
}

EXPECTED_FRAME_PROPERTIES = {
    "label": "",
    "label_widget": None,
    "label_xalign": 0.0,
    "label_yalign": 0.0,
    "shadow_type": Gtk.ShadowType.NONE,
}

EXPECTED_MENU_ITEM_HANDLER_IDS = {
    "activate": -1,
    "activate-item": -1,
    "deselect": -1,
    "select": -1,
    "toggle-size-allocate": -1,
    "toggle-size-request": -1,
}
EXPECTED_MENU_ITEM_PROPERTIES = {
    "accel_path": None,
    "label": "",
    "submenu": None,
    "use_underline": False,
}

EXPECTED_CHECK_MENU_ITEM_HANDLER_IDS = {"toggled": -1}
EXPECTED_CHECK_MENU_ITEM_PROPERTIES = {
    "active": False,
    "draw_as_radio": False,
    "inconsistent": False,
}

EXPECTED_RADIO_MENU_ITEM_HANDLER_IDS = {"group-changed": -1}
EXPECTED_RADIO_MENU_ITEM_PROPERTIES = {"group": None}

EXPECTED_POPOVER_HANDLER_IDS = {"closed": -1}
EXPECTED_POPOVER_PROPERTIES = {
    "constrain_to": Gtk.PopoverConstraint.WINDOW,
    "modal": True,
    "pointing_to": None,
    "position": Gtk.PositionType.TOP,
    "relative_to": None,
}

EXPECTED_POPOVER_MENU_PROPERTIES = {"visible_submenu": None}

EXPECTED_SCROLLED_WINDOW_HANDLER_IDS = {
    "edge-overshot": -1,
    "edge-reached": -1,
    "move-focus-out": -1,
    "scroll-child": -1,
}
EXPECTED_SCROLLED_WINDOW_PROPERTIES = {
    "hadjustment": None,
    "hscrollbar_policy": Gtk.PolicyType.AUTOMATIC,
    "kinetic_scrolling": True,
    "max_content_height": -1,
    "max_content_width": -1,
    "min_content_height": -1,
    "min_content_width": -1,
    "overlay_scrolling": True,
    "propogate_natural_height": False,
    "propogate_natural_width": False,
    "shadow_type": Gtk.ShadowType.NONE,
    "vadjustment": None,
    "vscrollbar_policy": Gtk.PolicyType.AUTOMATIC,
    "window_placement": Gtk.CornerType.TOP_LEFT,
}

EXPECTED_PLACES_SIDEBAR_HANDLER_IDS = {
    "drag-action-ask": -1,
    "drag-action-requested": -1,
    "drag-perform-drop": -1,
    "mount": -1,
    "open-location": -1,
    "populate-popup": -1,
    "show-connect-to-server": -1,
    "show-enter-location": -1,
    "show-error-message": -1,
    "show-other-locations": -1,
    "show-other-locations-with-flags": -1,
    "show-starred-location": -1,
    "unmount": -1,
}
EXPECTED_PLACES_SIDEBAR_PROPERTIES = {
    "local_only": False,
    "location": None,
    "open_flags": Gtk.PlacesOpenFlags.NORMAL,
    "populate_all": False,
    "show_desktop": True,
    "show_enter_location": False,
    "show_other_locations": False,
    "show_recent": True,
    "show_starred_location": False,
    "show_trash": True,
}

EXPECTED_SEARCHBAR_PROPERTIES = {
    "search_mode_enabled": False,
    "show_close_button": False,
}

EXPECTED_TOOL_ITEM_HANDLER_IDS = {"create-menu-proxy": -1, "toolbar-reconfigured": -1}
EXPECTED_TOOL_ITEM_PROPERTIES = {
    "is_important": False,
    "visible_horizontal": True,
    "visible_vertical": True,
}

EXPECTED_SEPARATOR_TOOL_ITEM_PROPERTIES = {"draw": True}

EXPECTED_TOOL_BUTTON_HANDLER_IDS = {"clicked": -1}
EXPECTED_TOOL_BUTTON_PROPERTIES = {
    "icon_name": None,
    "icon_widget": None,
    "label": None,
    "label_widget": None,
    "use_underline": False,
}

EXPECTED_MENU_TOOL_BUTTON_HANDLER_IDS = {"show-menu": -1}
EXPECTED_MENU_TOOL_BUTTON_PROPERTIES = {"menu": None}

EXPECTED_TOGGLE_TOOL_BUTTON_HANDLER_IDS = {"toggled": -1}
EXPECTED_TOGGLE_TOOL_BUTTON_PROPERTIES = {"active": False}

EXPECTED_RADIO_TOOL_BUTTON_PROPERTIES = {"group": None}

EXPECTED_VIEWPORT_PROPERTIES = {"shadow_type": Gtk.ShadowType.IN}

EXPECTED_WINDOW_HANDLER_IDS = {
    "activate-default": -1,
    "activate-focus": -1,
    "enable-debugging": -1,
    "keys-changed": -1,
    "set-focus": -1,
}
EXPECTED_WINDOW_PROPERTIES = {
    "accept_focus": True,
    "application": None,
    "attached_to": None,
    "decorated": True,
    "default_height": -1,
    "default_width": -1,
    "deletable": True,
    "destroy_with_parent": False,
    "focus_on_map": True,
    "focus_visible": True,
    "gravity": Gdk.Gravity.NORTH_WEST,
    "has_toplevel_focus": False,
    "hide_titlebar_when_maximized": False,
    "icon": None,
    "icon_name": None,
    "mnemonics_visible": True,
    "modal": False,
    "resizable": True,
    "role": None,
    "screen": None,
    "skip_taskbar_hint": False,
    "startup_id": None,
    "title": "pytkwrap GTK3 window",
    "transient_for": None,
    "type": Gdk.WindowType.TOPLEVEL,
    "type_hint": Gdk.WindowTypeHint.NORMAL,
    "urgency_hint": False,
    "window_position": Gtk.WindowPosition.NONE,
}

EXPECTED_ASSISTANT_HANDLER_IDS = {
    "apply": -1,
    "cancel": -1,
    "close": -1,
    "escape": -1,
    "prepare": -1,
}
EXPECTED_ASSISTANT_PROPERTIES = {"use_header_bar": -1}

EXPECTED_DIALOG_HANDLER_IDS = {"close": -1, "response": -1}
EXPECTED_DIALOG_PROPERTIES = {"use_header_bar": -1}

EXPECTED_ABOUT_DIALOG_HANDLER_IDS = {"activate-link": -1}
EXPECTED_ABOUT_DIALOG_PROPERTIES = {
    "artists": [],
    "authors": [],
    "comments": None,
    "copyright": None,
    "documenters": [],
    "license": None,
    "license_type": Gtk.License.UNKNOWN,
    "logo": None,
    "logo_icon_name": "image-missing",
    "program_name": None,
    "translator_credits": None,
    "version": None,
    "website": None,
    "website_label": None,
    "wrap_license": False,
}

EXPECTED_APP_CHOOSER_DIALOG_PROPERTIES = {"gfile": None, "heading": None}

EXPECTED_COLOR_CHOOSER_DIALOG_PROPERTIES = {"show_editor": False}

EXPECTED_MESSAGE_DIALOG_PROPERTIES = {
    "buttons": Gtk.ButtonsType.NONE,
    "message_area": None,
    "message_type": Gtk.MessageType.INFO,
    "secondary_text": None,
    "secondary_use_markup": False,
    "text": "",
    "use_markup": False,
}

EXPECTED_SHORTCUTS_WINDOW_HANDLER_IDS = {"close": -1, "search": -1}
EXPECTED_SHORTCUTS_WINDOW_PROPERTIES = {
    "section_name": "internal-search",
    "view_name": None,
}
