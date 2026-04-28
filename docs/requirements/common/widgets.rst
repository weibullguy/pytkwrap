.. _common_widgets:

==================================
Common Layer — Widget Requirements
==================================

This document defines the software requirements for the common layer
widget mixins of the pytkwrap project. These requirements apply to the
``WidgetMixin`` and ``DataWidgetMixin`` classes defined in
``pytkwrap.common.mixins`` and are toolkit-agnostic.

All requirements in this document trace to one or more system
requirements defined in :ref:`system_requirements`.

.. contents:: Contents
   :local:
   :depth: 1

----

WidgetMixin
===========

.. _PTW-COM-W-001:

PTW-COM-W-001
-------------

:Description: The ``WidgetMixin`` class **SHALL** provide toolkit-agnostic
              widget state that is shared across all toolkit
              implementations.
:Rationale:   A common base of widget state ensures that all toolkit
              implementations share the same attribute infrastructure
              without duplicating code.
:Traces to:   :ref:`PTW-SR-A-001`, :ref:`PTW-SR-A-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::WidgetMixinTests::test_init``

----

.. _PTW-COM-W-002:

PTW-COM-W-002
-------------

:Description: The ``WidgetMixin`` class **SHALL** contain no
              toolkit-specific imports or dependencies.
:Rationale:   Toolkit-specific imports in the common layer would
              prevent the common layer from being used independently
              of any specific toolkit and would violate the
              architecture defined in :ref:`PTW-SR-A-002`.
:Traces to:   :ref:`PTW-SR-A-002`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::WidgetMixinTests::test_no_toolkit_imports``

----

.. _PTW-COM-W-003:

PTW-COM-W-003
-------------

:Description: The ``WidgetMixin`` class **SHALL** initialize a
              ``dic_attributes`` dictionary from the class-level
              ``_WIDGET_ATTRIBUTES`` typed dictionary on instantiation.
:Rationale:   Initializing ``dic_attributes`` from the class-level
              default ensures every instance starts with a consistent,
              complete set of attributes without requiring explicit
              configuration.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::WidgetMixinTests::test_init``

----

.. _PTW-COM-W-004:

PTW-COM-W-004
-------------

:Description: The ``WidgetMixin`` class **SHALL** initialize a
              ``dic_error_message`` dictionary containing standard
              error message templates on instantiation.
:Rationale:   Centralizing error message templates in the common layer
              ensures consistent error reporting across all toolkit
              implementations.
:Traces to:   :ref:`PTW-SR-A-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::WidgetMixinTests::test_init``

----

.. _PTW-COM-W-005:

PTW-COM-W-005
-------------

:Description: The ``WidgetMixin`` class **SHALL** provide a
              ``do_get_attribute()`` method that returns the value of
              a named attribute from ``dic_attributes``.
:Rationale:   A consistent attribute retrieval interface allows
              application code to read widget attributes without
              direct dictionary access.
:Traces to:   :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::WidgetMixinTests::test_do_get_attribute``

----

.. _PTW-COM-W-006:

PTW-COM-W-006
-------------

:Description: The ``WidgetMixin.do_get_attribute()`` method **SHALL**
              raise a ``KeyError`` if the requested attribute is not
              defined in ``_WIDGET_ATTRIBUTES``.
:Rationale:   Raising a ``KeyError`` for unknown attributes provides
              a clear, consistent error signal that helps developers
              identify misconfiguration early.
:Traces to:   :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::WidgetMixinTests::test_do_get_attribute_unknown``

----

.. _PTW-COM-W-007:

PTW-COM-W-007
-------------

:Description: The ``WidgetMixin`` class **SHALL** provide a
              ``do_set_attributes()`` method that updates
              ``dic_attributes`` from a ``WidgetAttributes`` typed
              dictionary.
:Rationale:   A single method call to configure widget attributes
              reduces the amount of code a developer must write and
              provides a consistent configuration interface across
              all widgets.
:Traces to:   :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::WidgetMixinTests::test_do_set_attributes``

----

.. _PTW-COM-W-008:

PTW-COM-W-008
-------------

:Description: The ``WidgetMixin.do_set_attributes()`` method **SHALL**
              preserve existing ``dic_attributes`` values for any
              attribute not present in the passed ``WidgetAttributes``
              dictionary.
:Rationale:   Partial attribute updates **SHALL** not reset unspecified
              attributes to their defaults, allowing incremental
              configuration without losing previously set values.
:Traces to:   :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::WidgetMixinTests::test_do_set_attributes_partial``

----

.. _PTW-COM-W-009:

PTW-COM-W-009
-------------

:Description: The ``WidgetMixin`` class **SHALL** define
              ``_WIDGET_ATTRIBUTES`` as a class-level ``WidgetAttributes``
              typed dictionary containing the following attributes with
              their default values:

              - ``n_columns``: ``0``
              - ``n_rows``: ``0``
              - ``x_pos``: ``0``
              - ``y_pos``: ``0``

:Rationale:   These attributes apply to all widgets regardless of
              toolkit — every widget has a position and optional
              grid dimensions.
:Traces to:   :ref:`PTW-SR-W-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::WidgetMixinTests::test_init``

----

DataWidgetMixin
===============

.. _PTW-COM-W-010:

PTW-COM-W-010
-------------

:Description: The ``DataWidgetMixin`` class **SHALL** extend
              ``WidgetMixin`` and provide additional toolkit-agnostic
              state for widgets that display and manipulate data.
:Rationale:   Not all widgets display data — structural widgets such
              as frames and scrolled windows do not need data widget
              attributes. Separating data widget state into a subclass
              keeps the base class lean.
:Traces to:   :ref:`PTW-SR-A-001`, :ref:`PTW-SR-A-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::DataWidgetMixinTests::test_init``

----

.. _PTW-COM-W-011:

PTW-COM-W-011
-------------

:Description: The ``DataWidgetMixin`` class **SHALL** define
              ``_DATA_WIDGET_ATTRIBUTES`` as a class-level
              ``DataWidgetAttributes`` typed dictionary containing
              the following attributes with their default values:

              - ``data_type``: ``None``
              - ``default_value``: ``None``
              - ``edit_signal``: ``""``
              - ``font_description``: ``None``
              - ``format``: ``"{}"``
              - ``index``: ``-1``
              - ``listen_topic``: ``"listen_topic"``
              - ``send_topic``: ``"send_topic"``

:Rationale:   These attributes are common to all data-displaying
              widgets regardless of toolkit and provide the foundation
              for the publish-subscribe messaging system.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-M-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::DataWidgetMixinTests::test_init``

----

.. _PTW-COM-W-012:

PTW-COM-W-012
-------------

:Description: The ``DataWidgetMixin.__init__()`` method **SHALL**
              update ``dic_attributes`` with the values from
              ``_DATA_WIDGET_ATTRIBUTES`` after calling
              ``super().__init__()``.
:Rationale:   Updating ``dic_attributes`` after calling
              ``super().__init__()`` ensures that the base class
              attributes are initialized first and then extended with
              data widget attributes, maintaining a consistent
              initialization order.
:Traces to:   :ref:`PTW-SR-W-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::DataWidgetMixinTests::test_init``

----

.. _PTW-COM-W-013:

PTW-COM-W-013
-------------

:Description: The ``DataWidgetMixin.do_get_attribute()`` method
              **SHALL** return the value from ``dic_attributes`` for
              attributes defined in ``_DATA_WIDGET_ATTRIBUTES`` and
              **SHALL** delegate to ``super().do_get_attribute()`` for
              all other attributes.
:Rationale:   Delegating to the superclass for unknown attributes
              maintains the correct attribute lookup chain across the
              full inheritance hierarchy without duplicating logic.
:Traces to:   :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::DataWidgetMixinTests::test_do_get_attribute``
              ``tests/common/test_widget_mixin.py::DataWidgetMixinTests::test_do_get_attribute_delegates``

----

.. _PTW-COM-W-014:

PTW-COM-W-014
-------------

:Description: The ``DataWidgetMixin.do_set_attributes()`` method
              **SHALL** call ``super().do_set_attributes()`` before
              processing data widget attributes.
:Rationale:   Calling the superclass method first ensures that base
              widget attributes are set before data widget attributes,
              maintaining a consistent initialization order across the
              inheritance hierarchy.
:Traces to:   :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::DataWidgetMixinTests::test_do_set_attributes``

----

.. _PTW-COM-W-015:

PTW-COM-W-015
-------------

:Description: The ``DataWidgetMixin.do_set_attributes()`` method
              **SHALL** coerce attribute values to the correct Python
              type as follows:

              - ``index``: coerced to ``int``.
              - ``font_description``: coreced to ``FontDescription``.
              - ``default_value`` and ``value_type``: stored as-is
                without type coercion.
              - All remaining string attributes: coerced to ``str``.

:Rationale:   Type coercion at the point of setting attributes
              prevents type errors downstream when attribute values
              are used in toolkit setter calls or pubsub messages.
:Traces to:   :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::DataWidgetMixinTests::test_do_set_attributes_type_coercion``

----

WidgetAttributes
================

.. _PTW-COM-W-016:

PTW-COM-W-016
-------------

:Description: The ``WidgetAttributes`` class **SHALL** be defined as
              a ``TypedDict`` with ``total=False`` containing the
              following keys:

              - ``n_columns``: ``int``
              - ``n_rows``: ``int``
              - ``x_pos``: ``float | int``
              - ``y_pos``: ``float | int``

:Rationale:   Defining ``WidgetAttributes`` as a ``TypedDict`` with
              ``total=False`` allows partial dictionaries to be passed
              to ``do_set_attributes()`` without requiring all keys
              to be present.
:Traces to:   :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::WidgetMixinTests::test_widget_attributes_type``

----

.. _PTW-COM-W-017:

PTW-COM-W-017
-------------

:Description: The ``DataWidgetAttributes`` class **SHALL** extend
              ``WidgetAttributes`` as a ``TypedDict`` with
              ``total=False`` and **SHALL** contain no
              toolkit-specific types.
:Rationale:   Extending ``WidgetAttributes`` ensures that all widget
              attributes are available in a single dictionary. The
              absence of toolkit-specific types ensures the common
              layer remains toolkit-agnostic.
:Traces to:   :ref:`PTW-SR-A-002`, :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::DataWidgetMixinTests::test_data_widget_attributes_type``

----

PlotWidgetMixin
===============

.. _PTW-COM-W-018:

PTW-COM-W-018
-------------

:Description: The ``PlotWidgetMixin`` class **SHALL** extend
              ``DataWidgetMixin`` and provide additional
              toolkit-agnostic state for widgets that display
              matplotlib plots.
:Rationale:   Plot widget state is distinct from general data widget
              state. Separating it into a dedicated mixin keeps the
              base ``DataWidgetMixin`` lean and makes the plot widget
              dependency on matplotlib explicit.
:Traces to:   :ref:`PTW-SR-C-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::PlotWidgetMixinTests::test_init``

----

.. _PTW-COM-W-019:

PTW-COM-W-019
-------------

:Description: The ``PlotWidgetMixin`` class **SHALL** define
              ``_PLOT_WIDGET_ATTRIBUTES`` as a class-level
              ``PlotWidgetAttributes`` typed dictionary containing
              the following attributes with their default values:

              - ``axis``: ``None``
              - ``canvas``: ``None``
              - ``figure``: ``None``

:Rationale:   These three attributes represent the core matplotlib
              objects required to embed a plot in a GUI window and
              are common to all plot widget implementations regardless
              of toolkit.
:Traces to:   :ref:`PTW-SR-C-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::PlotWidgetMixinTests::test_init``

----

Utility Functions
=================

.. _PTW-COM-W-020:

PTW-COM-W-020
-------------

:Description: The ``make_widget_config()`` function **SHALL** accept
              a widget instance, a ``WidgetAttributes`` dictionary,
              and a properties dictionary and **SHALL** return a
              ``WidgetConfig`` typed dictionary containing all three.
:Rationale:   A typed factory function for widget configuration
              dictionaries provides type safety and a consistent
              interface for passing widget configuration between
              application layers.
:Traces to:   :ref:`PTW-SR-W-004`, :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::test_make_widget_config``
