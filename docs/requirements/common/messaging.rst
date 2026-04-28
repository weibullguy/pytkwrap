.. _common_messaging:

=====================================
Common Layer — Messaging Requirements
=====================================

This document defines the software requirements for the common layer
messaging infrastructure of the pytkwrap project. These requirements
apply to the publish-subscribe messaging support provided by
``pytkwrap.common.mixins`` and ``pytkwrap.utilities`` and are
toolkit-agnostic.

All requirements in this document trace to one or more system
requirements defined in :ref:`system_requirements`.

.. contents:: Contents
   :local:
   :depth: 1

----

Publish-Subscribe Topics
========================

.. _PTW-COM-M-001:

PTW-COM-M-001
-------------

:Description: The ``DataWidgetMixin`` class **SHALL** provide a
              ``send_topic`` attribute that specifies the message
              topic on which the widget publishes its value when the
              user changes the widget's value.
:Rationale:   A configurable publish topic allows different widgets
              in the same application to publish to different topics,
              enabling fine-grained control over the messaging
              architecture.
:Traces to:   :ref:`PTW-SR-M-002`, :ref:`PTW-SR-M-004`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::DataWidgetMixinTests::test_init``

----

.. _PTW-COM-M-002:

PTW-COM-M-002
-------------

:Description: The ``DataWidgetMixin`` class **SHALL** provide a
              ``listen_topic`` attribute that specifies the message
              topic to which the widget subscribes to receive value
              updates.
:Rationale:   A configurable subscribe topic allows different widgets
              in the same application to respond to different topics,
              enabling fine-grained control over the messaging
              architecture.
:Traces to:   :ref:`PTW-SR-M-003`, :ref:`PTW-SR-M-004`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::DataWidgetMixinTests::test_init``

----

.. _PTW-COM-M-003:

PTW-COM-M-003
-------------

:Description: The ``send_topic`` attribute **SHALL** default to the
              string ``"send_topic"`` and the ``listen_topic``
              attribute **SHALL** default to the string
              ``"listen_topic"``.
:Rationale:   Non-empty default topic names ensure that messaging
              infrastructure is functional immediately after
              instantiation without requiring explicit configuration,
              while still being clearly identifiable as placeholders
              that **SHOULD** be replaced in production use.
:Traces to:   :ref:`PTW-SR-M-004`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::DataWidgetMixinTests::test_init``

----

.. _PTW-COM-M-004:

PTW-COM-M-004
-------------

:Description: The ``send_topic`` and ``listen_topic`` attributes
              **SHALL** be independently configurable via
              ``do_set_attributes()`` using a ``DataWidgetAttributes``
              dictionary.
:Rationale:   Independent configuration of publish and subscribe
              topics allows a widget to listen on one topic and publish
              on another, which is a common pattern in complex
              publish-subscribe messaging architectures.
:Traces to:   :ref:`PTW-SR-M-004`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::DataWidgetMixinTests::test_do_set_attributes``

----

Edit Signal
===========

.. _PTW-COM-M-005:

PTW-COM-M-005
-------------

:Description: The ``DataWidgetMixin`` class **SHALL** provide an
              ``edit_signal`` attribute that specifies the toolkit
              signal name that indicates the user has changed the
              widget's value.
:Rationale:   The edit signal name is used to block and unblock the
              signal handler during programmatic value updates,
              preventing feedback loops in the messaging system.
:Traces to:   :ref:`PTW-SR-M-002`, :ref:`PTW-SR-M-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::DataWidgetMixinTests::test_init``

----

.. _PTW-COM-M-006:

PTW-COM-M-006
-------------

:Description: The ``DataWidgetMixin`` class **SHALL** define a
              class-level ``_DEFAULT_EDIT_SIGNAL`` attribute that
              specifies the default edit signal name for the widget.
              The base ``DataWidgetMixin._DEFAULT_EDIT_SIGNAL``
              **SHALL** default to an empty string ``""``.
:Rationale:   Defining the default edit signal at the class level
              allows subclasses to override it without modifying
              instance state, providing a clear, inspectable default
              for each widget type.
:Traces to:   :ref:`PTW-SR-M-002`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::DataWidgetMixinTests::test_init``

----

Message Subscription Utilities
===============================

.. _PTW-COM-M-007:

PTW-COM-M-007
-------------

:Description: The ``do_subscribe_to_messages()`` utility function
              **SHALL** accept a dictionary mapping message topic
              strings to handler callables and **SHALL** subscribe
              each handler to its corresponding topic.
:Rationale:   Bulk subscription to multiple message topics is a
              common operation in GUI applications. A utility function
              reduces boilerplate and provides a consistent interface.
:Traces to:   :ref:`PTW-SR-M-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/test_utilities.py::test_do_subscribe_to_messages``

----

.. _PTW-COM-M-008:

PTW-COM-M-008
-------------

:Description: The ``do_unsubscribe_from_messages()`` utility function
              **SHALL** accept a dictionary mapping message topic
              strings to handler callables and **SHALL** unsubscribe
              each handler from its corresponding topic.
:Rationale:   Bulk unsubscription from multiple message topics is
              a common operation in GUI application teardown and test
              cleanup. A utility function reduces boilerplate,
              provides a consistent interface, and prevents topic
              pollution between tests.
:Traces to:   :ref:`PTW-SR-M-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/test_utilities.py::test_do_unsubscribe_from_messages``

----

.. _PTW-COM-M-009:

PTW-COM-M-009
-------------

:Description: The ``do_unsubscribe_from_messages()`` function
              **SHALL** silently ignore attempts to unsubscribe a
              handler from a topic to which it is not subscribed.
:Rationale:   Raising an exception when unsubscribing a handler that
              is not subscribed is unnecessarily strict and complicates
              test teardown. Silent handling of this case is consistent
              with the principle of least surprise.
:Traces to:   :ref:`PTW-SR-M-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/test_utilities.py::test_do_unsubscribe_from_messages_not_subscribed``

----

Default Value Handling
======================

.. _PTW-COM-M-010:

PTW-COM-M-010
-------------

:Description: The ``DataWidgetMixin`` class **SHALL** provide a
              ``default`` attribute that specifies the fallback value
              to use when the widget's data value is ``None``.
:Rationale:   A fallback default value prevents ``None`` from being
              displayed in widgets or passed through pubsub messages
              when no data is available, improving the user experience
              and reducing the need for ``None`` checks in application
              code.
:Traces to:   :ref:`PTW-SR-M-002`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::DataWidgetMixinTests::test_init``

----

.. _PTW-COM-M-011:

PTW-COM-M-011
-------------

:Description: The ``none_to_default()`` utility function **SHALL**
              accept a value and a default and **SHALL** return the
              default if the value is ``None``, or the original value
              otherwise.
:Rationale:   Centralizing the ``None``-to-default substitution logic
              in a utility function ensures consistent behavior across
              all widgets and avoids duplicating the ``None`` check
              in every widget's ``do_update()`` method.
:Traces to:   :ref:`PTW-SR-M-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/test_utilities.py::test_none_to_default_none_value``
              ``tests/test_utilities.py::test_none_to_default_non_none_value``
