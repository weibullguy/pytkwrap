.. _gtk3_mixins:

================================
GTK3 Layer — Mixin Requirements
================================

This document specifies the GTK3 mixins currently implemented in
``pytkwrap.gtk3.mixins`` and ``pytkwrap.gtk3.widget``. The common
convenience behavior is supplied by ``PyTkWrapMixin``. The GTK3 layer
does not define ``GTK3DataWidgetMixin`` or a ``GTK3Base*`` wrapper
hierarchy.

The implemented mixin relationship is:

.. code-block:: text

    PyTkWrapMixin                         (common)
        └── GTK3GObjectMixin               (GObject.Object + common mixin)
                └── GTK3WidgetMixin        (GTK3 widget behavior)
                        └── GTK3ContainerMixin and other specialized mixins

Concrete wrappers combine the appropriate native GTK3 class with the
corresponding GTK3 mixin. Non-widget GObjects use
``GTK3GObjectMixin`` or a specialized mixin directly.

All requirements trace to :ref:`system_requirements` and, where
applicable, :ref:`common_mixins`.

.. contents:: Contents
   :local:
   :depth: 1

----

GTK3GObjectMixin
================

.. _PTW-GTK3-X-001:

PTW-GTK3-X-001
--------------

:Description: ``GTK3GObjectMixin`` **SHALL** combine GTK3 GObject
              behavior with ``PyTkWrapMixin`` state and **SHALL** be
              used as the common GTK3 mixin for wrappers of GObject
              instances.
:Rationale:   GObject signal support is shared by GTK3 widgets and
              non-widget objects, while the common mixin supplies
              toolkit-independent configuration and error handling.
:Traces to:   :ref:`PTW-SR-A-003`, :ref:`PTW-SR-A-004`,
              :ref:`PTW-COM-X-002`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-X-002:

PTW-GTK3-X-002
--------------

:Description: ``GTK3WidgetAttributes`` **SHALL** extend
              ``PyTkWrapAttributes`` and add the GTK3-specific
              ``column_types`` key. ``GTK3WidgetProperties`` **SHALL**
              be a partial ``TypedDict`` describing GTK3 property
              names and their value types.
:Rationale:   The extended attributes preserve common configuration
              keys while allowing GTK3-specific configuration; the
              property type describes the GTK3-native property surface.
:Traces to:   :ref:`PTW-SR-W-004`, :ref:`PTW-SR-W-005`,
              :ref:`PTW-COM-X-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-X-003:

PTW-GTK3-X-003
--------------

:Description: ``GTK3GObjectMixin`` **SHALL** initialize
              ``dic_handler_id`` with its declared GObject signal names
              and the sentinel value ``-1``. Widget-level mixins
              **SHALL** add their declared signal names to this
              instance mapping.
:Rationale:   Instance-level handler IDs allow signal connection state
              to be tracked independently for each wrapper.
:Traces to:   :ref:`PTW-SR-W-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-X-004:

PTW-GTK3-X-004
--------------

:Description: ``GTK3GObjectMixin.do_set_callbacks()`` **SHALL** accept
              one signal name or a list of signal names, a callback,
              and an ``after`` flag defaulting to ``False``. It **SHALL**
              connect each signal, using ``connect_after()`` when
              ``after`` is true, and store each returned handler ID in
              ``dic_handler_id`` under its signal name.
:Rationale:   A shared callback setup interface supports both ordinary
              and after-default GTK signal handlers.
:Traces to:   :ref:`PTW-SR-W-002`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-X-005:

PTW-GTK3-X-005
--------------

:Description: If connecting a signal in ``do_set_callbacks()`` raises
              ``TypeError``, the wrapper **SHALL** publish a
              ``do_log_error`` message and raise ``UnkSignalError``
              chained from the connection error.
:Rationale:   Invalid signal names or connections are surfaced through
              both the application's logging channel and a typed
              exception.
:Traces to:   :ref:`PTW-GTK3-X-004`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

GTK3WidgetMixin
===============

.. _PTW-GTK3-X-006:

PTW-GTK3-X-006
--------------

:Description: ``GTK3WidgetMixin`` **SHALL** extend
              ``GTK3GObjectMixin`` with GTK3 widget attributes,
              properties, signal names, and widget property-setting
              behavior. Concrete GTK3 widgets **SHALL** combine their
              native GTK class with the appropriate GTK3 mixin.
:Rationale:   GTK3 widget behavior is shared without introducing
              artificial intermediate classes into the native GTK
              inheritance tree.
:Traces to:   :ref:`PTW-SR-A-003`, :ref:`PTW-SR-A-004`,
              :ref:`PTW-SR-W-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-X-007:

PTW-GTK3-X-007
--------------

:Description: ``GTK3WidgetMixin`` **SHALL** create an instance-local
              ``dic_properties`` mapping from its GTK3 widget property
              defaults and initialize its GTK3 widget signal handler
              entries to ``-1``.
:Rationale:   Each instance begins with its own configured property and
              handler state, while specialized mixins can extend those
              mappings.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-X-008:

PTW-GTK3-X-008
--------------

:Description: ``GTK3WidgetMixin.do_set_properties()`` **SHALL** merge
              supplied properties into ``dic_properties`` and apply
              the properties handled at this mixin level using the
              corresponding GTK3 setters. A ``Mapping`` or iterable of
              key/value pairs **SHALL** be accepted.
:Rationale:   Keeping the effective values in ``dic_properties`` makes
              the GTK3 property state inspectable and permits
              specialized mixins to extend property handling.
:Traces to:   :ref:`PTW-SR-W-004`, :ref:`PTW-COM-X-006`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-X-009:

PTW-GTK3-X-009
--------------

:Description: ``GTK3WidgetMixin.do_set_properties()`` **SHALL** map
              zero ``height_request`` and ``width_request`` values to
              the mixin's default dimensions and **SHALL** keep
              ``tooltip_markup`` and ``tooltip_text`` synchronized when
              only one differs from their default.
:Rationale:   GTK3 uses ``-1`` for natural sizing, and paired tooltip
              properties should reflect a single configured tooltip.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-GTK3-X-008`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

Concrete GTK3 Mixins
====================

.. _PTW-GTK3-X-010:

PTW-GTK3-X-010
--------------

:Description: GTK3 specialized mixins **SHALL** extend the most
              specific applicable GTK3 mixin and **SHALL** extend its
              instance property and signal dictionaries rather than
              replacing the inherited state.
:Rationale:   Incremental mixin composition preserves configuration
              defaults and handler bookkeeping from parent mixins.
:Traces to:   :ref:`PTW-SR-A-003`, :ref:`PTW-SR-W-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-X-011:

PTW-GTK3-X-011
--------------

:Description: ``GTK3WidgetAttributes`` **SHALL** be the GTK3 extension
              of ``PyTkWrapAttributes`` used for GTK3-specific
              configuration such as ``column_types``.
:Rationale:   A single partial typed dictionary can carry both common
              and GTK3-specific attribute configuration.
:Traces to:   :ref:`PTW-SR-W-005`, :ref:`PTW-GTK3-X-002`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-X-012:

PTW-GTK3-X-012
--------------

:Description: ``GTK3WidgetProperties`` **SHALL** be a partial
              ``TypedDict`` containing the GTK3 property keys and
              annotated value types supported by the wrapper package.
:Rationale:   The typed dictionary provides editor and static-checker
              assistance when configuring GTK3-native properties; it
              does not perform runtime validation.
:Traces to:   :ref:`PTW-SR-W-004`, :ref:`PTW-GTK3-X-002`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-X-013:

PTW-GTK3-X-013
--------------

:Description: A concrete GTK3 wrapper **SHALL** combine the relevant
              native GTK class with its GTK3 mixin, rather than
              inheriting from a universal ``GTK3Base*`` wrapper class.
:Rationale:   The mixin composition retains the native GTK class API
              and matches the current wrapper inheritance model.
:Traces to:   :ref:`PTW-SR-A-004`, :ref:`PTW-SR-W-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.
