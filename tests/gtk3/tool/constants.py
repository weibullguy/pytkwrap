EXPECTED_MENUTOOLBUTTON_HANDLER_IDS = {"show-menu": -1}
EXPECTED_MENUTOOLBUTTON_METHODS = [
    "get_menu",
    "set_arrow_tooltip_markup",
    "set_arrow_tooltip_text",
    "set_menu",
]
EXPECTED_MENUTOOLBUTTON_PROPERTIES = {"menu": None}

EXPECTED_RADIOTOOLBUTTON_METHODS = ["get_group", "set_group"]
EXPECTED_RADIOTOOLBUTTON_PROPERTIES = {"group": None}

EXPECTED_SEPARATORTOOLITEM_METHODS = ["get_draw", "set_draw"]
EXPECTED_SEPARATORTOOLITEM_PROPERTIES = {"draw": True}

EXPECTED_TOGGLETOOLBUTTON_HANDLER_IDS = {"toggled": -1}
EXPECTED_TOGGLETOOLBUTTON_METHODS = ["get_active", "set_active"]
EXPECTED_TOGGLETOOLBUTTON_PROPERTIES = {"active": False}

EXPECTED_TOOLBUTTON_HANDLER_IDS = {"clicked": -1}
EXPECTED_TOOLBUTTON_METHODS = [
    "get_icon_name",
    "get_icon_widget",
    "get_label",
    "get_label_widget",
    "get_use_underline",
    "set_icon_name",
    "set_icon_widget",
    "set_label",
    "set_label_widget",
    "set_use_underline",
]
EXPECTED_TOOLBUTTON_PROPERTIES = {
    "icon_name": None,
    "icon_widget": None,
    "label": None,
    "label_widget": None,
    "use_underline": False,
}

EXPECTED_TOOLITEM_HANDLER_IDS = {"create-menu-proxy": -1, "toolbar-reconfigured": -1}
EXPECTED_TOOLITEM_METHODS = [
    "get_ellipsize_mode",
    "get_expand",
    "get_homogeneous",
    "get_icon_size",
    "get_is_important",
    "get_orientation",
    "get_proxy_menu_item",
    "get_relief_style",
    "get_text_alignment",
    "get_text_orientation",
    "get_text_size_group",
    "get_toolbar_style",
    "get_use_drag_window",
    "get_visible_horizontal",
    "get_visible_vertical",
    "rebuild_menu",
    "retrieve_proxy_menu_item",
    "set_expand",
    "set_homogeneous",
    "set_is_important",
    "set_proxy_menu_item",
    "set_tooltip_markup",
    "set_tooltip_text",
    "set_use_drag_window",
    "set_visible_horizontal",
    "set_visible_vertical",
    "toolbar_reconfigured",
]
EXPECTED_TOOLITEM_PROPERTIES = {
    "is_important": False,
    "visible_horizontal": True,
    "visible_vertical": True,
}
