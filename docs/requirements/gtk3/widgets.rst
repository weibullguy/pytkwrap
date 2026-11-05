.. _gtk3_widgets:

================================
GTK3 Layer — Widget Requirements
================================

This document specifies widget behavior implemented by
``GTK3WidgetMixin`` in ``pytkwrap.gtk3.widget`` and GObject behavior
implemented by ``GTK3GObjectMixin`` in ``pytkwrap.gtk3.mixins``.
The current implementation does not define ``GTK3BaseWidget`` or
``GTK3BaseDataWidget``. Concrete wrappers combine GTK's native class
with the appropriate GTK3 mixin.

All requirements trace to :ref:`system_requirements` and, where
applicable, :ref:`gtk3_mixins` and :ref:`common_mixins`.

.. contents:: Contents
   :local:
   :depth: 1

----

GTK3WidgetMixin
===============

.. _PTW-GTK3-W-001:

PTW-GTK3-W-001
--------------

:Description: ``GTK3WidgetMixin`` **SHALL** provide GTK3 widget
              behavior for concrete wrappers that combine it with the
              appropriate native GTK widget class.
:Rationale:   Composition with native classes preserves access to the
              complete GTK API without imposing a separate base-widget
              class hierarchy.
:Traces to:   :ref:`PTW-GTK3-X-006`, :ref:`PTW-SR-W-001`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-W-002:

PTW-GTK3-W-002
--------------

:Description: ``GTK3WidgetMixin.__init__()`` **SHALL** initialize an
              instance-local ``dic_properties`` mapping using its
              ``_GTK3_WIDGET_PROPERTIES`` defaults and **SHALL** add its
              declared widget signal names to ``dic_handler_id`` with
              initial value ``-1``.
:Rationale:   Per-instance dictionaries allow wrappers to maintain
              independent effective property values and signal handler
              IDs.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-007`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-W-003:

PTW-GTK3-W-003
--------------

:Description: GTK3 signal handler IDs **SHALL** be stored in the
              wrapper instance's ``dic_handler_id`` mapping, with
              ``-1`` used for a declared signal that has not yet been
              connected.
:Rationale:   The sentinel represents an unconnected handler without
              requiring class-shared mutable state.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-GTK3-X-003`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-W-004:

PTW-GTK3-W-004
--------------

:Description: ``GTK3WidgetMixin`` **SHALL** use ``-1`` as its default
              width and height request, indicating GTK's natural size.
:Rationale:   GTK's natural sizing remains available unless a wrapper
              or caller explicitly requests a size.
:Traces to:   :ref:`PTW-SR-W-003`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-W-005:

PTW-GTK3-W-005
--------------

:Description: ``GTK3WidgetMixin.do_set_properties()`` **SHALL** accept
              a mapping or iterable of key/value pairs, merge the
              supplied values into ``dic_properties``, and apply the
              widget properties handled by this mixin using GTK3
              setter methods.
:Rationale:   The mapping is the inspectable effective configuration;
              typed dictionaries assist static checking but are not
              runtime validators.
:Traces to:   :ref:`PTW-SR-W-004`, :ref:`PTW-GTK3-X-008`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-W-006:

PTW-GTK3-W-006
--------------

:Description: ``GTK3WidgetMixin.do_set_properties()`` **SHALL** replace
              zero ``height_request`` and ``width_request`` values with
              the mixin's default dimensions. When only one of
              ``tooltip_markup`` and ``tooltip_text`` differs from the
              default tooltip, the other **SHALL** be set to the same
              value.
:Rationale:   These rules preserve GTK natural sizing for zero requests
              and keep the two representations of a tooltip in sync.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-GTK3-X-009`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-W-007:

PTW-GTK3-W-007
--------------

:Description: ``GTK3GObjectMixin.do_set_callbacks()`` **SHALL** accept
              one signal name or a list of names, a callback, and an
              optional ``after`` flag, and **SHALL** record each
              connection's handler ID in ``dic_handler_id``.
:Rationale:   The common callback API supports multiple signal
              connections and preserves the GTK before/after handler
              choice.
:Traces to:   :ref:`PTW-GTK3-X-004`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-W-008:

PTW-GTK3-W-008
--------------

:Description: If GTK rejects a signal connection with ``TypeError``,
              ``do_set_callbacks()`` **SHALL** publish a
              ``do_log_error`` message and raise ``UnkSignalError``
              chained from that error.
:Rationale:   An invalid connection is reported both through the
              application logging channel and a typed exception.
:Traces to:   :ref:`PTW-GTK3-X-005`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

GTK3GObjectMixin Value Behavior
===============================

.. _PTW-GTK3-W-009:

PTW-GTK3-W-009
--------------

:Description: ``GTK3GObjectMixin.do_update()`` **SHALL** read the
              first key/value pair from the supplied package as the
              widget index and value. If that index differs from the
              wrapper's configured ``index``, it **SHALL** return
              without changing the displayed value.
:Rationale:   The index routes a package to the matching wrapper in a
              collection of widgets.
:Traces to:   :ref:`PTW-SR-M-003`, :ref:`PTW-SR-M-004`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-W-010:

PTW-GTK3-W-010
--------------

:Description: When the incoming package value is ``None``,
              ``GTK3GObjectMixin.do_update()`` **SHALL** substitute the
              wrapper's ``default_value`` before calling
              ``do_set_value()``.
:Rationale:   The attribute is named ``default_value`` in the current
              API; no ``default`` attribute is defined for this
              purpose.
:Traces to:   :ref:`PTW-SR-M-003`, :ref:`PTW-COM-M-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-W-011:

PTW-GTK3-W-011
--------------

:Description: During ``do_update()``, GTK3 **SHALL** block the
              configured edit-signal handler while ``do_set_value()``
              applies the received value, so the programmatic update
              does not invoke that handler.
:Rationale:   Blocking the edit handler prevents programmatic updates
              from being mistaken for user edits.
:Traces to:   :ref:`PTW-SR-W-007`, :ref:`PTW-SR-M-003`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-W-012:

PTW-GTK3-W-012
--------------

:Description: ``GTK3GObjectMixin.on_changed()`` **SHALL** publish a
              PyPubSub message on ``send_topic`` with the keyword
              argument ``package`` containing a one-entry mapping from
              the configured ``index`` to the current value returned by
              ``do_get_value()``.
:Rationale:   The indexed package routes a changed value to its intended
              consumer without requiring polling.
:Traces to:   :ref:`PTW-SR-M-002`, :ref:`PTW-COM-M-001`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-W-013:

PTW-GTK3-W-013
--------------

:Description: If ``do_update()`` cannot find a handler ID for a
              configured edit signal, it **SHALL** publish a
              ``do_log_error`` message and raise ``UnkSignalError``
              chained from the missing-key error.
:Rationale:   A missing handler mapping indicates an invalid signal
              configuration and must not be silently ignored.
:Traces to:   :ref:`PTW-SR-M-003`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-W-014:

PTW-GTK3-W-014
--------------

:Description: ``GTK3GObjectMixin.on_changed()`` **SHALL** publish the
              value package described by :ref:`PTW-GTK3-W-012` on the
              wrapper's configured ``send_topic``.
:Rationale:   The publish topic remains independently configurable for
              each wrapper through ``dic_attributes``.
:Traces to:   :ref:`PTW-SR-M-002`, :ref:`PTW-COM-M-001`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-W-015:

PTW-GTK3-W-015
--------------

:Description: ``on_changed()`` **SHALL** publish the current value
              without requiring a registered edit-signal handler and
              without blocking an edit handler during the publish call.
:Rationale:   In the current implementation the GTK signal invokes
              ``on_changed()``; that method reads the value and
              publishes it directly.
:Traces to:   :ref:`PTW-SR-M-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-W-016:

PTW-GTK3-W-016
--------------

:Description: ``GTK3GObjectMixin._get_signal_owner()`` **SHALL** return
              ``self`` by default. A specialized wrapper **MAY**
              override this method when the relevant signal belongs to
              a child GObject, such as a text buffer.
:Rationale:   Blocking the handler on its owning GObject is necessary
              for programmatic value updates to suppress the correct
              signal.
:Traces to:   :ref:`PTW-SR-M-003`, :ref:`PTW-GTK3-M-004`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

GTK3 Wrapper Composition
========================

.. _PTW-GTK3-W-017:

PTW-GTK3-W-017
--------------

:Description: GTK3 wrappers **SHALL** use the native GTK class together
              with GTK3 mixins that provide the required common and
              widget-specific behavior. The package **SHALL NOT**
              require a universal ``GTK3BaseWidget`` or
              ``GTK3BaseDataWidget`` class.
:Rationale:   This contract reflects the implemented composition model
              and preserves native GTK inheritance and APIs.
:Traces to:   :ref:`PTW-SR-A-004`, :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-W-018:

PTW-GTK3-W-018
--------------

:Description: A concrete GTK3 mixin **SHALL** extend its inherited
              ``dic_properties``, ``dic_handler_id``, and
              ``dic_attributes`` mappings as applicable, rather than
              replacing inherited mapping contents.
:Rationale:   Extending instance configuration preserves defaults and
              signal bookkeeping established by parent mixins.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-GTK3-X-010`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-W-019:

PTW-GTK3-W-019
--------------

:Description: Concrete GTK3 wrappers are not required to override
              ``_DEFAULT_HEIGHT`` or ``_DEFAULT_WIDTH``. Unless
              overridden for a specific class, the GTK3 widget mixin
              defaults **SHALL** remain ``-1``.
:Rationale:   The common mixin defaults request GTK natural sizing;
              there is no universal requirement for widget-specific
              dimensions.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-GTK3-W-004`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

set_widget_sensitivity
======================

.. _PTW-GTK3-W-020:

PTW-GTK3-W-020
--------------

:Description: ``set_widget_sensitivity()`` **SHALL** accept a list of
              GTK widgets and a boolean sensitivity value and call
              ``set_sensitive()`` with that value on each list member.
:Rationale:   The helper applies one sensitivity setting to multiple
              GTK widgets without repeated caller code.
:Traces to:   :ref:`PTW-SR-W-001`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

GTK3WidgetMixin Defaults
========================

.. _PTW-GTK3-W-021:

PTW-GTK3-W-021
--------------

:Description: ``GTK3WidgetMixin.__init__()`` **SHALL** add the
              attributes ``x_pos`` and ``y_pos``, each with a default
              value of ``0``, to ``dic_attributes``.
:Rationale:   The position attributes record where a wrapper is placed
              in a positional layout container such as ``Gtk.Fixed``.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-005`,
              :ref:`PTW-COM-X-001`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/test_widget.py::TestGTK3Widget::test_do_set_attributes_default``
              ``tests/gtk3/test_widget.py::TestGTK3Widget::test_do_set_attributes``

----

.. _PTW-GTK3-W-022:

PTW-GTK3-W-022
--------------

:Description: ``GTK3WidgetMixin.__init__()`` **SHALL** pre-register the
              following ``Gtk.Widget`` signals in ``dic_handler_id``
              with a value of ``-1``:

              - ``"destroy"``
              - ``"direction-changed"``
              - ``"hide"``
              - ``"keynav-failed"``
              - ``"map"``
              - ``"mnemonic-activate"``
              - ``"move-focus"``
              - ``"query-tooltip"``
              - ``"realize"``
              - ``"show"``
              - ``"state-flags-changed"``
              - ``"unmap"``
              - ``"unrealize"``

:Rationale:   Pre-registering the common widget signals makes them
              available for connection via ``do_set_callbacks()`` on
              every GTK3 widget wrapper.
:Traces to:   :ref:`PTW-GTK3-W-002`, :ref:`PTW-GTK3-W-003`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/test_widget.py::TestGTK3Widget``

----

.. _PTW-GTK3-W-023:

PTW-GTK3-W-023
--------------

:Description: ``GTK3WidgetMixin.__init__()`` **SHALL** initialize
              ``dic_properties`` with the following defaults:

              - ``app_paintable``: ``False``
              - ``can_default``: ``False``
              - ``can_focus``: ``False``
              - ``composite_child``: ``False``
              - ``events``: ``Gdk.EventMask.ALL_EVENTS_MASK``
              - ``expand``: ``False``
              - ``focus_on_click``: ``True``
              - ``halign``: ``Gtk.Align.FILL``
              - ``has_default``: ``False``
              - ``has_focus``: ``False``
              - ``has_tooltip``: ``False``
              - ``height_request``: ``-1``
              - ``hexpand``: ``False``
              - ``hexpand_set``: ``False``
              - ``is_focus``: ``False``
              - ``margin``, ``margin_bottom``, ``margin_end``,
                ``margin_start``, ``margin_top``: ``0``
              - ``name``: ``"pytkwrap GTK3 widget"``
              - ``no_show_all``: ``False``
              - ``opacity``: ``1.0``
              - ``parent``: ``None``
              - ``receives_default``: ``False``
              - ``scale_factor``: ``1``
              - ``sensitive``: ``True``
              - ``style``: ``None``
              - ``tooltip_markup``: ``_DEFAULT_TOOLTIP``
              - ``tooltip_text``: ``_DEFAULT_TOOLTIP``
              - ``valign``: ``Gtk.Align.FILL``
              - ``vexpand``: ``False``
              - ``vexpand_set``: ``False``
              - ``visible``: ``False``
              - ``width_request``: ``-1``
              - ``window``: ``None``

:Rationale:   Every GTK3 widget wrapper starts from a known, complete
              property configuration. The tooltip defaults use the
              translatable ``_DEFAULT_TOOLTIP`` so that a widget
              missing a tooltip is visible to the user and reportable.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-GTK3-W-002`,
              :ref:`PTW-COM-X-028`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/test_widget.py::TestGTK3Widget::test_do_set_properties_default``

----

GTK3WidgetMixin do_set_properties
=================================

.. _PTW-GTK3-W-024:

PTW-GTK3-W-024
--------------

:Description: ``GTK3WidgetMixin.do_set_properties()`` **SHALL** apply
              the following properties through the corresponding
              ``Gtk.Widget`` ``set_<name>()`` method:

              ``can_default``, ``can_focus``, ``halign``,
              ``has_tooltip``, ``hexpand``, ``hexpand_set``,
              ``margin_bottom``, ``margin_end``, ``margin_start``,
              ``margin_top``, ``name``, ``opacity``,
              ``receives_default``, ``sensitive``, ``tooltip_markup``,
              ``tooltip_text``, ``valign``, ``vexpand``,
              ``vexpand_set``, and ``visible``.

              These setters **SHALL** be called after the size and
              tooltip normalization described by
              :ref:`PTW-GTK3-W-006`.
:Rationale:   Normalizing first ensures GTK receives the final,
              consistent size and tooltip values.
:Traces to:   :ref:`PTW-SR-W-004`, :ref:`PTW-GTK3-W-005`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/test_widget.py::TestGTK3Widget::test_do_set_properties``

----

.. _PTW-GTK3-W-025:

PTW-GTK3-W-025
--------------

:Description: ``GTK3WidgetMixin.do_set_properties()`` **SHALL**:

              - call ``set_size_request()`` with ``width_request`` and
                ``height_request`` only when the wrapper is an instance
                of ``Gtk.Widget``;
              - apply ``focus_on_click`` through
                ``set_property("focus-on-click", ...)``;
              - apply ``parent`` through ``set_property("parent",
                ...)`` only when ``parent`` is not ``None``.

:Rationale:   The ``isinstance`` guard prevents a size request on a
              composition that does not include ``Gtk.Widget``. A
              ``None`` parent is not passed to GTK, so an unparented
              widget is not reparented.
:Traces to:   :ref:`PTW-SR-W-004`, :ref:`PTW-GTK3-W-005`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/test_widget.py::TestGTK3Widget::test_do_set_properties``
              ``tests/gtk3/test_widget.py::TestGTK3Widget::test_do_set_properties_zero_height``
              ``tests/gtk3/test_widget.py::TestGTK3Widget::test_do_set_properties_zero_width``
              ``tests/gtk3/test_widget.py::TestGTK3Widget::test_do_set_properties_default_tooltip_markup``
              ``tests/gtk3/test_widget.py::TestGTK3Widget::test_do_set_properties_default_tooltip_text``

----

Managed Attributes
==================

.. _PTW-GTK3-W-026:

PTW-GTK3-W-026
--------------

:Description: ``GTK3WidgetMixin`` **SHALL** provide the following
              read-only Python properties, each returning the result
              of the corresponding ``Gtk.Widget`` getter:

              ============================  =================================
              Property                      Getter
              ============================  =================================
              ``accessible``                ``get_accessible()``
              ``allocated_baseline``        ``get_allocated_baseline()``
              ``allocated_height``          ``get_allocated_height()``
              ``allocated_width``           ``get_allocated_width()``
              ``display``                   ``get_display()``
              ``frame_clock``               ``get_frame_clock()``
              ``pango_context``             ``get_pango_context()``
              ``parent_window``             ``get_parent_window()``
              ``preferred_height``          ``get_preferred_height()``
              ``preferred_size``            ``get_preferred_size()``
              ``preferred_width``           ``get_preferred_width()``
              ``request_mode``              ``get_request_mode()``
              ``scale_factor``              ``get_scale_factor()``
              ``screen``                    ``get_screen()``
              ``settings``                  ``get_settings()``
              ``style_context``             ``get_style_context()``
              ``toplevel``                  ``get_toplevel()``
              ``valign_with_baseline``      ``get_valign_with_baseline()``
              ============================  =================================

              None of these properties **SHALL** define a setter.
:Rationale:   These values are computed or owned by GTK at runtime
              and cannot be set directly. Exposing them as properties
              gives Pythonic attribute access without duplicating state
              in ``dic_properties``.
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/test_widget.py::TestGTK3Widget::test_accessible``
              ``tests/gtk3/test_widget.py::TestGTK3Widget::test_allocated_baseline``
              ``tests/gtk3/test_widget.py::TestGTK3Widget::test_allocated_height``
              ``tests/gtk3/test_widget.py::TestGTK3Widget::test_allocated_width``
              ``tests/gtk3/test_widget.py::TestGTK3Widget::test_display``
              ``tests/gtk3/test_widget.py::TestGTK3Widget::test_frame_clock``
              ``tests/gtk3/test_widget.py::TestGTK3Widget::test_pango_context``
              ``tests/gtk3/test_widget.py::TestGTK3Widget::test_parent_window``
              ``tests/gtk3/test_widget.py::TestGTK3Widget::test_preferred_height``
              ``tests/gtk3/test_widget.py::TestGTK3Widget::test_preferred_size``
              ``tests/gtk3/test_widget.py::TestGTK3Widget::test_preferred_width``
              ``tests/gtk3/test_widget.py::TestGTK3Widget::test_request_mode``
              ``tests/gtk3/test_widget.py::TestGTK3Widget::test_scale_factor``
              ``tests/gtk3/test_widget.py::TestGTK3Widget::test_screen``
              ``tests/gtk3/test_widget.py::TestGTK3Widget::test_settings``
              ``tests/gtk3/test_widget.py::TestGTK3Widget::test_style_context``
              ``tests/gtk3/test_widget.py::TestGTK3Widget::test_toplevel``
              ``tests/gtk3/test_widget.py::TestGTK3Widget::test_valign_with_baseline``

----

GTK3Widget
==========

.. _PTW-GTK3-W-027:

PTW-GTK3-W-027
--------------

:Description: The ``GTK3Widget`` class **SHALL** combine ``Gtk.Widget``
              with ``GTK3WidgetMixin``. Its ``__init__()`` method
              **SHALL** call ``Gtk.Widget.__init__()``, then
              ``GTK3WidgetMixin.__init__()``, and then ``show_all()``.
:Rationale:   ``GTK3Widget`` is the concrete wrapper for the base GTK3
              widget and is shown immediately after construction.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/test_widget.py::TestGTK3Widget``
