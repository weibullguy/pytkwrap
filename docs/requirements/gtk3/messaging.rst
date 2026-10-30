.. _gtk3_messaging:

===================================
GTK3 Layer — Messaging Requirements
===================================

This document specifies the PyPubSub behavior implemented by
``GTK3GObjectMixin`` in ``pytkwrap.gtk3.mixins``. Wrappers are not
automatically subscribed to their ``listen_topic`` during construction;
application code wires subscriptions using the helpers in
:ref:`common_messaging`.

All requirements trace to :ref:`system_requirements` and, where
applicable, :ref:`common_messaging` and :ref:`gtk3_mixins`.

.. contents:: Contents
   :local:
   :depth: 1

----

Message Attributes and Configuration
====================================

.. _PTW-GTK3-M-001:

PTW-GTK3-M-001
--------------

:Description: ``GTK3GObjectMixin`` **SHALL** initialize ``index`` to
              ``-1``, ``listen_topic`` to ``"listen-topic"``, and
              ``send_topic`` to ``"send-topic"`` unless callers
              override these attributes.
:Rationale:   The concrete defaults are provided by the GTK3 mixin;
              the common ``PyTkWrapMixin`` defaults for these keys are
              ``None``.
:Traces to:   :ref:`PTW-COM-M-001`, :ref:`PTW-GTK3-X-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-M-002:

PTW-GTK3-M-002
--------------

:Description: A GTK3 wrapper's ``edit_signal`` attribute **SHALL**
              accept a signal name string or a list of signal name
              strings. The concrete wrapper **SHALL** configure the
              signal or signals used to identify a user edit.
:Rationale:   Some wrappers need more than one GTK signal to represent
              an edit; the configuration is wrapper-specific rather
              than a class-level default shared by all data widgets.
:Traces to:   :ref:`PTW-COM-M-001`, :ref:`PTW-GTK3-X-004`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

Callback Connection
===================

.. _PTW-GTK3-M-003:

PTW-GTK3-M-003
--------------

:Description: ``GTK3GObjectMixin.do_set_callbacks()`` **SHALL** connect
              each configured signal to the wrapper object using
              ``connect()`` by default or ``connect_after()`` when its
              ``after`` argument is true. It **SHALL** store each
              returned handler ID in ``dic_handler_id`` under the
              signal name.
:Rationale:   The connection method and returned ID provide the GTK3
              callback behavior used by update-time signal suppression.
:Traces to:   :ref:`PTW-GTK3-X-004`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-M-004:

PTW-GTK3-M-004
--------------

:Description: The default ``GTK3GObjectMixin._get_signal_owner()``
              **SHALL** return ``self``. A wrapper **MAY** override
              this hook to identify a child GObject whose handler must
              be blocked during a value update.
:Rationale:   Some GTK signals belong to child objects; blocking the
              handler must act on the object that owns its handler ID.
:Traces to:   :ref:`PTW-GTK3-W-016`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

Message-Driven Value Updates
============================

.. _PTW-GTK3-M-005:

PTW-GTK3-M-005
--------------

:Description: ``GTK3GObjectMixin.do_update()`` **SHALL** use the first
              key/value pair in the supplied ``package`` mapping as
              ``index`` and value. It **SHALL** leave the wrapper
              unchanged when the package index does not match the
              wrapper's configured ``index``.
:Rationale:   Index matching routes a package to the corresponding
              wrapper in a collection of indexed widgets.
:Traces to:   :ref:`PTW-SR-M-003`, :ref:`PTW-GTK3-W-009`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-M-006:

PTW-GTK3-M-006
--------------

:Description: When the received value is ``None``,
              ``GTK3GObjectMixin.do_update()`` **SHALL** substitute the
              configured ``default_value`` before passing it to
              ``do_set_value()``.
:Rationale:   ``default_value`` is the current attribute name for this
              fallback; there is no ``default`` attribute in the
              common wrapper attributes.
:Traces to:   :ref:`PTW-SR-M-003`, :ref:`PTW-COM-M-002`,
              :ref:`PTW-GTK3-W-010`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-M-007:

PTW-GTK3-M-007
--------------

:Description: For a matching package index,
              ``GTK3GObjectMixin.do_update()`` **SHALL** call
              ``do_set_value()`` while the configured edit-signal
              handler or handlers are blocked by GTK's handler-block
              context manager. A missing signal key in
              ``dic_handler_id`` **SHALL** result in a logged
              ``UnkSignalError``.
:Rationale:   Blocking the handler prevents a programmatic value update
              from being mistaken for a user edit; a missing handler
              key indicates invalid configuration.
:Traces to:   :ref:`PTW-SR-M-003`, :ref:`PTW-GTK3-W-011`,
              :ref:`PTW-GTK3-W-013`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

User-Edit Publishing
====================

.. _PTW-GTK3-M-008:

PTW-GTK3-M-008
--------------

:Description: ``GTK3GObjectMixin.on_changed()`` **SHALL** obtain the
              current value through ``do_get_value()`` and publish a
              PyPubSub message on ``send_topic`` with keyword argument
              ``package`` set to ``{index: value}``.
:Rationale:   This payload combines a wrapper's configured index with
              the value visible when its GTK signal callback runs.
:Traces to:   :ref:`PTW-SR-M-002`, :ref:`PTW-GTK3-W-012`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-M-009:

PTW-GTK3-M-009
--------------

:Description: ``on_changed()`` **SHALL** publish the value package
              directly and **SHALL NOT** block the edit-signal handler
              during the publish call or require its handler ID to be
              present in ``dic_handler_id``.
:Rationale:   In the current implementation, signal connection invokes
              ``on_changed()``; that callback reads and publishes the
              value without performing a second handler-blocking step.
:Traces to:   :ref:`PTW-SR-M-002`, :ref:`PTW-GTK3-W-015`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

Topic Subscription Wiring
=========================

.. _PTW-GTK3-M-010:

PTW-GTK3-M-010
--------------

:Description: ``GTK3GObjectMixin`` **SHALL NOT** automatically
              subscribe itself to ``listen_topic`` during
              initialization. Application code **SHALL** establish the
              topic-to-handler subscription using the common PyPubSub
              subscription utility.
:Rationale:   Subscription lifecycle and handler routing are controlled
              by the application rather than implicit wrapper setup.
:Traces to:   :ref:`PTW-SR-M-004`, :ref:`PTW-COM-M-007`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-M-011:

PTW-GTK3-M-011
--------------

:Description: The GTK3 callback connection utility **SHALL** connect
              signals to the wrapper object and **SHALL NOT** infer a
              signal owner from the ``buffer`` property. Wrappers that
              use a child object's signals require an explicit
              connection or a wrapper-specific implementation.
:Rationale:   ``do_set_callbacks()`` currently delegates directly to
              the GObject connection API; it does not dispatch
              connections based on GTK properties.
:Traces to:   :ref:`PTW-GTK3-M-003`, :ref:`PTW-GTK3-M-004`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.
