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
:Issues:      None
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
:Issues:      None
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
:Issues:      None
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
:Issues:      None
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
:Issues:      None
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
:Issues:      None
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
:Issues:      None
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
:Issues:      None
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
:Issues:      None
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
:Issues:      None
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
:Issues:      None
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
:Issues:      None
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
:Issues:      None
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
:Issues:      None
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
:Issues:      None
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
:Issues:      None
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
:Issues:      None
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
:Issues:      None
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
:Issues:      None
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
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.
