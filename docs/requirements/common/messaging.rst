.. _common_messaging:

=====================================
Common Layer — Messaging Requirements
=====================================

This document defines the toolkit-independent messaging and messaging
utility requirements. The current implementation uses PyPubSub. GTK3
wrapper update/publish behavior is specified in :ref:`gtk3_messaging`;
the common ``PyTkWrapMixin`` itself does not subscribe widgets to topics.

All requirements trace to :ref:`system_requirements`.

.. contents:: Contents
   :local:
   :depth: 1

----

Widget Configuration Values
===========================

.. _PTW-COM-M-001:

PTW-COM-M-001
-------------

:Description: The common attribute mapping **SHALL** include
              ``default_value``, ``edit_signal``, ``index``,
              ``listen_topic``, and ``send_topic`` keys. The common
              defaults for these keys **SHALL** be ``None``.
:Rationale:   These keys provide configuration state shared with the
              GTK3 message implementation without imposing toolkit
              behavior on the common layer.
:Traces to:   :ref:`PTW-SR-M-001`, :ref:`PTW-SR-M-004`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-COM-M-002:

PTW-COM-M-002
-------------

:Description: ``none_to_default(value, default)`` **SHALL** return
              ``default`` when ``value`` is ``None`` and **SHALL**
              otherwise return ``value`` unchanged.
:Rationale:   The GTK3 update path uses this utility to apply the
              configured ``default_value`` when an incoming package
              contains ``None``.
:Traces to:   :ref:`PTW-SR-M-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

PyPubSub Utilities
==================

.. _PTW-COM-M-007:

PTW-COM-M-007
-------------

:Description: ``do_subscribe_to_messages()`` **SHALL** accept a mapping
              of topic names to handler callables and subscribe each
              handler to its topic using PyPubSub.
:Rationale:   Bulk subscription reduces repeated setup code for
              applications wiring wrapper messages to handlers.
:Traces to:   :ref:`PTW-SR-M-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-COM-M-008:

PTW-COM-M-008
-------------

:Description: ``do_unsubscribe_from_messages()`` **SHALL** accept a
              mapping of topic names to handler callables and
              unsubscribe each handler from its topic using PyPubSub.
:Rationale:   Bulk unsubscription provides a consistent teardown
              operation for applications and tests.
:Traces to:   :ref:`PTW-SR-M-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-COM-M-009:

PTW-COM-M-009
-------------

:Description: ``do_unsubscribe_from_messages()`` **SHALL** tolerate
              attempts to unsubscribe a handler that is not subscribed
              to the specified topic, as defined by its PyPubSub
              implementation behavior.
:Rationale:   Tolerant cleanup supports idempotent application teardown.
:Traces to:   :ref:`PTW-COM-M-008`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.
