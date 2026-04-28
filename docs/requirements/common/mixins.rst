.. _common_mixins:

=================================
Common Layer — Mixin Requirements
=================================

This document defines the software requirements for the common layer
mixin classes defined in ``pytkwrap.common.mixins``. These mixins
provide toolkit-agnostic state and behavior that is shared across all
toolkit implementations.

The mixin hierarchy is:

.. code-block:: text

    BaseMixin
        ├── WidgetMixin
        │       └── DataWidgetMixin
        │               └── PlotWidgetMixin
        └── (toolkit-specific mixins extend BaseMixin directly
            for non-widget GObjects — defined in toolkit layers)

All requirements in this document trace to one or more system
requirements defined in :ref:`system_requirements`.

.. contents:: Contents
   :local:
   :depth: 1

----

BaseMixin
=========

.. _PTW-COM-X-001:

PTW-COM-X-001
-------------

:Description: The ``BaseMixin`` class **SHALL** be defined in
              ``pytkwrap.common.mixins`` and **SHALL** serve as the
              root mixin for all pytkwrap mixin classes, both in the
              common layer and in toolkit-specific layers.
:Rationale:   A single root mixin ensures that the infrastructure
              common to all pytkwrap objects — including both widget
              and non-widget objects — is defined once and inherited
              consistently across all toolkit implementations.
:Traces to:   :ref:`PTW-SR-A-001`, :ref:`PTW-SR-A-002`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_base_mixin.py::TestBaseMixin::test_init``

----

.. _PTW-COM-X-002:

PTW-COM-X-002
-------------

:Description: The ``BaseMixin`` class **SHALL** initialize a
              ``dic_attributes`` instance dictionary on instantiation.
              The dictionary **SHALL** be empty by default and
              **SHALL NOT** be shared as a class-level attribute.
:Rationale:   ``dic_attributes`` is the single source of truth for
              all pytkwrap object attribute values. Initializing it
              as an instance dictionary ensures that attribute changes
              on one instance never affect other instances of the same
              class.
:Traces to:   :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_base_mixin.py::TestBaseMixin::test_init``
              ``tests/common/test_base_mixin.py::TestBaseMixin::test_dic_attributes_not_shared``

----

.. _PTW-COM-X-003:

PTW-COM-X-003
-------------

:Description: The ``BaseMixin`` class **SHALL** initialize a
              ``dic_error_message`` instance dictionary on
              instantiation containing the following standard error
              message templates:

              - ``"unk_function"``:
                ``"{}: No such function {} exists."``
              - ``"unk_signal"``:
                ``"{}: Unknown signal name '{}'."``

:Rationale:   Centralizing error message templates in ``BaseMixin``
              ensures consistent error reporting across all pytkwrap
              objects regardless of toolkit, and eliminates duplication
              of these strings across every class that needs to report
              errors.
:Traces to:   :ref:`PTW-SR-A-002`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_base_mixin.py::TestBaseMixin::test_init``

----

.. _PTW-COM-X-004:

PTW-COM-X-004
-------------

:Description: The ``BaseMixin`` class **SHALL** contain no
              toolkit-specific imports or dependencies.
:Rationale:   As the root of the common layer mixin hierarchy,
              ``BaseMixin`` **SHALL** be usable by any toolkit
              implementation without importing any toolkit-specific
              modules.
:Traces to:   :ref:`PTW-SR-A-002`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_base_mixin.py::TestBaseMixin::test_no_toolkit_imports``

----

WidgetMixin
===========

.. _PTW-COM-X-005:

PTW-COM-X-005
-------------

:Description: The ``WidgetMixin`` class **SHALL** extend ``BaseMixin``
              and **SHALL** provide toolkit-agnostic state for all
              widgets in the ``Gtk.Widget`` tree (or equivalent in
              other toolkits). It **SHALL** contain no
              toolkit-specific imports or dependencies.
:Rationale:   Separating widget-specific state from the root
              ``BaseMixin`` allows non-widget objects (such as
              ``Gtk.Adjustment`` and ``Gtk.TextBuffer``) to use
              ``BaseMixin`` directly without carrying widget-specific
              attributes they do not need.
:Traces to:   :ref:`PTW-SR-A-001`, :ref:`PTW-SR-A-002`,
              :ref:`PTW-SR-A-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::TestWidgetMixin::test_init``
              ``tests/common/test_widget_mixin.py::TestWidgetMixin::test_no_toolkit_imports``

----

.. _PTW-COM-X-006:

PTW-COM-X-006
-------------

:Description: The ``WidgetMixin`` class **SHALL** define a
              class-level ``_WIDGET_ATTRIBUTES`` typed dictionary
              of type ``WidgetAttributes`` containing the following
              attributes with their default values:

              - ``n_columns``: ``0``
              - ``n_rows``: ``0``
              - ``x_pos``: ``0``
              - ``y_pos``: ``0``

:Rationale:   These attributes apply to all widgets regardless of
              toolkit. Every widget has a position and optional grid
              dimensions. Defining them at the ``WidgetMixin`` level
              ensures they are available to all toolkit widget
              implementations.
:Traces to:   :ref:`PTW-SR-W-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::TestWidgetMixin::test_init``

----

.. _PTW-COM-X-006.001:

PTW-COM-X-006.001
-----------------

:Description: The ``WidgetMixin`` class **SHALL** define class-level
              default values for various attributes.  Currently, these
              include:

              - ``_DEFAULT_HEIGHT``: ``-1``
              - ``_DEFAULT_TOOLTIP``: ``"Missing tooltip, please file an issue to have one added."``
              - ``_DEFAULT_WIDTH``: ``-1``

:Rationale:   These attributes apply to all widgets regardless of
              toolkit. Defining them at the ``WidgetMixin`` level
              ensures they are available to all toolkit widget
              implementations.
:Traces to:   :ref:`PTW-SR-W-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::TestWidgetMixin::test_init``

----

.. _PTW-COM-X-007:

PTW-COM-X-007
-------------

:Description: The ``WidgetMixin.__init__()`` method **SHALL** call
              ``super().__init__()`` and **SHALL** update
              ``dic_attributes`` with the values from
              ``_WIDGET_ATTRIBUTES``.
:Rationale:   Calling ``super().__init__()`` first ensures
              ``BaseMixin`` initializes ``dic_attributes`` before
              ``WidgetMixin`` populates it. Updating rather than
              replacing ``dic_attributes`` preserves any entries
              added by ``BaseMixin`` or other mixins earlier in
              the MRO.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-COM-X-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::TestWidgetMixin::test_init``

----

.. _PTW-COM-X-008:

PTW-COM-X-008
-------------

:Description: The ``WidgetMixin`` class **SHALL** provide a
              ``do_get_attribute()`` method that returns the value
              from ``dic_attributes`` for attributes defined in
              ``_WIDGET_ATTRIBUTES`` and **SHALL** raise a
              ``KeyError`` for attributes not defined in
              ``_WIDGET_ATTRIBUTES``.
:Rationale:   A consistent attribute retrieval interface allows
              application code to read widget attributes without
              direct dictionary access. Raising ``KeyError`` for
              unknown attributes provides a clear error signal that
              helps developers identify misconfiguration early.
:Traces to:   :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::TestWidgetMixin::test_do_get_attribute``
              ``tests/common/test_widget_mixin.py::TestWidgetMixin::test_do_get_attribute_unknown``

----

.. _PTW-COM-X-009:

PTW-COM-X-009
-------------

:Description: The ``WidgetMixin`` class **SHALL** provide a
              ``do_set_attributes()`` method that accepts a
              ``WidgetAttributes`` typed dictionary and updates
              ``dic_attributes`` with the provided values, coercing
              each value to the correct Python type. Attributes not
              present in the passed dictionary **SHALL** retain their
              existing values in ``dic_attributes``.
:Rationale:   A single method call to configure widget attributes
              reduces boilerplate, provides a consistent interface
              across all widgets, and ensures type safety through
              coercion. Preserving unspecified attributes allows
              incremental configuration without losing previously
              set values.
:Traces to:   :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::TestWidgetMixin::test_do_set_attributes``
              ``tests/common/test_widget_mixin.py::TestWidgetMixin::test_do_set_attributes_partial``
              ``tests/common/test_widget_mixin.py::TestWidgetMixin::test_do_set_attributes_defaults``

----

DataWidgetMixin
===============

.. _PTW-COM-X-010:

PTW-COM-X-010
-------------

:Description: The ``DataWidgetMixin`` class **SHALL** extend
              ``WidgetMixin`` and **SHALL** provide additional
              toolkit-agnostic state for widgets that display and
              manipulate data. It **SHALL** contain no
              toolkit-specific imports or dependencies.
:Rationale:   Not all widgets display data — structural widgets such
              as frames and scrolled windows do not need data widget
              attributes. Separating data widget state into a subclass
              of ``WidgetMixin`` keeps the base mixin lean and makes
              the data widget dependency explicit.
:Traces to:   :ref:`PTW-SR-A-001`, :ref:`PTW-SR-A-002`,
              :ref:`PTW-SR-A-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_data_widget_mixin.py::TestDataWidgetMixin::test_init``

----

.. _PTW-COM-X-011:

PTW-COM-X-011
-------------

:Description: The ``DataWidgetMixin`` class **SHALL** define a
              class-level ``_DATA_WIDGET_ATTRIBUTES`` typed dictionary
              of type ``DataWidgetAttributes`` containing the following
              attributes with their default values:

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
              for the publish-subscribe messaging system. Defining
              them at the ``DataWidgetMixin`` level ensures they are
              available to all toolkit data widget implementations
              without duplication.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-M-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_data_widget_mixin.py::TestDataWidgetMixin::test_init``

----

.. _PTW-COM-X-012:

PTW-COM-X-012
-------------

:Description: The ``DataWidgetMixin.__init__()`` method **SHALL**
              call ``super().__init__()`` and **SHALL** update
              ``dic_attributes`` with the values from
              ``_DATA_WIDGET_ATTRIBUTES``.
:Rationale:   Calling ``super().__init__()`` first ensures the full
              ``WidgetMixin`` and ``BaseMixin`` initialization chain
              completes before ``DataWidgetMixin`` adds its own
              attributes, maintaining a consistent and predictable
              initialization order.
:Traces to:   :ref:`PTW-COM-X-005`, :ref:`PTW-COM-X-008`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_data_widget_mixin.py::TestDataWidgetMixin::test_init``

----

.. _PTW-COM-X-013:

PTW-COM-X-013
-------------

:Description: The ``DataWidgetMixin.do_get_attribute()`` method
              **SHALL** return the value from ``dic_attributes`` for
              attributes defined in ``_DATA_WIDGET_ATTRIBUTES`` and
              **SHALL** delegate to ``super().do_get_attribute()``
              for all other attributes.
:Rationale:   Delegating unknown attribute lookups to the superclass
              ensures that the full attribute hierarchy is searchable
              via a single ``do_get_attribute()`` call, regardless of
              which mixin in the hierarchy defines the attribute.
              Unknown attributes bubble up to ``WidgetMixin`` which
              raises ``KeyError``.
:Traces to:   :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_data_widget_mixin.py::TestDataWidgetMixin::test_do_get_attribute``
              ``tests/common/test_data_widget_mixin.py::TestDataWidgetMixin::test_do_get_attribute_delegates``
              ``tests/common/test_data_widget_mixin.py::TestDataWidgetMixin::test_do_get_attribute_unknown``

----

.. _PTW-COM-X-014:

PTW-COM-X-014
-------------

:Description: The ``DataWidgetMixin.do_set_attributes()`` method
              **SHALL** call ``super().do_set_attributes()`` before
              processing data widget attributes, and **SHALL** coerce
              attribute values to the correct Python type as follows:

              - ``index``: coerced to ``int``.
              - ``font_description``: coerced to ``FontDescription`` when
                the passed value is not ``None`` or a ``FontDescription``.
                Otherwise stored as-is without type coercion
              - ``data_type`` and ``default_value``:
                stored as-is without type coercion.
              - All remaining string attributes: coerced to ``str``.

              Attributes not present in the passed dictionary
              **SHALL** retain their existing values in
              ``dic_attributes``.

:Rationale:   Calling ``super()`` first ensures base widget attributes
              are set before data widget attributes. Type coercion at
              the point of setting attributes prevents type errors
              downstream when attribute values are used in toolkit
              setter calls or pubsub messages.
:Traces to:   :ref:`PTW-SR-W-005`, :ref:`PTW-COM-X-010`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_data_widget_mixin.py::TestDataWidgetMixin::test_do_set_attributes``
              ``tests/common/test_data_widget_mixin.py::TestDataWidgetMixin::test_do_set_attributes_partial``
              ``tests/common/test_data_widget_mixin.py::TestDataWidgetMixin::test_do_set_attributes_type_coercion``
              ``tests/common/test_data_widget_mixin.py::TestDataWidgetMixin::test_do_set_attributes_calls_super``

----

.. _PTW-COM-X-015:

PTW-COM-X-015
-------------

:Description: The ``DataWidgetMixin`` class **SHALL** define a
              class-level ``_DEFAULT_EDIT_SIGNAL`` attribute with a
              default value of ``""`` (empty string). The instance
              attribute ``edit_signal`` **SHALL** be initialized from
              this class-level default.
:Rationale:   Defining the default edit signal at the class level
              allows subclasses to override it without modifying
              instance state, providing a clear, inspectable default
              for each widget type. The empty string default reflects
              that the base mixin has no specific signal to define.
:Traces to:   :ref:`PTW-SR-M-002`, :ref:`PTW-COM-M-006`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_data_widget_mixin.py::TestDataWidgetMixin::test_init``

----

.. _PTW-COM-X-015.001:

PTW-COM-X-015.001
-----------------

:Description: The ``DataWidgetMixin`` class **SHALL** define a
              class-level ``_DEFAULT_VALUE`` attribute with a
              default value of ``None``. The instance attribute
              ``default_value`` **SHALL** be initialized from
              this class-level default.
:Rationale:   Defining the default value at the class level allows
              subclasses to override it without modifying instance
              state, providing a clear, inspectable default for each
              widget type. The ``None`` default reflects that the
              base mixin has no specific value to define.
:Traces to:   :ref:`PTW-SR-M-002`, :ref:`PTW-COM-M-006`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_data_widget_mixin.py::TestDataWidgetMixin::test_init``

----

PlotWidgetMixin
===============

.. _PTW-COM-X-016:

PTW-COM-X-016
-------------

:Description: The ``PlotWidgetMixin`` class **SHALL** extend
              ``DataWidgetMixin`` and **SHALL** provide additional
              toolkit-agnostic state for widgets that display
              matplotlib plots. It **SHALL** contain no
              toolkit-specific imports or dependencies.
:Rationale:   Plot widget state is distinct from general data widget
              state. Separating it into a dedicated mixin makes the
              matplotlib dependency explicit and keeps ``DataWidgetMixin``
              lean for widgets that do not require plotting.
:Traces to:   :ref:`PTW-SR-C-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_plot_widget_mixin.py::TestPlotWidgetMixin::test_init``

----

.. _PTW-COM-X-017:

PTW-COM-X-017
-------------

:Description: The ``PlotWidgetMixin`` class **SHALL** define a
              class-level ``_PLOT_WIDGET_ATTRIBUTES`` typed dictionary
              of type ``PlotWidgetAttributes`` containing the following
              attributes with their default values:

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
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_plot_widget_mixin.py::TestPlotWidgetMixin::test_init``

----

.. _PTW-COM-X-018:

PTW-COM-X-018
-------------

:Description: The ``PlotWidgetMixin.do_get_attribute()`` method
              **SHALL** return the value from ``dic_attributes`` for
              attributes defined in ``_PLOT_WIDGET_ATTRIBUTES`` and
              **SHALL** delegate to ``super().do_get_attribute()``
              for all other attributes.
:Rationale:   Consistent delegation through the mixin hierarchy
              ensures the full attribute chain is searchable via
              a single ``do_get_attribute()`` call as required by
              :ref:`PTW-COM-X-014`.
:Traces to:   :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_plot_widget_mixin.py::TestPlotWidgetMixin::test_do_get_attribute``
              ``tests/common/test_plot_widget_mixin.py::TestPlotWidgetMixin::test_do_get_attribute_delegates``
              ``tests/common/test_plot_widget_mixin.py::TestPlotWidgetMixin::test_do_get_attribute_unknown``

----

.. _PTW-COM-X-019:

PTW-COM-X-019
-------------

:Description: The ``PlotWidgetMixin.do_set_attributes()`` method
              **SHALL** call ``super().do_set_attributes()`` before
              processing plot widget attributes. Plot widget attributes
              **SHALL** be stored as-is without type coercion since
              they are matplotlib objects.
:Rationale:   matplotlib objects such as ``Figure``, ``Axes``, and
              ``FigureCanvasBase`` cannot be coerced to simpler Python
              types. Storing them as-is preserves their type and
              allows them to be used directly in matplotlib API calls.
:Traces to:   :ref:`PTW-SR-W-005`, :ref:`PTW-COM-X-015`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_plot_widget_mixin.py::TestPlotWidgetMixin::test_do_set_attributes``
              ``tests/common/test_plot_widget_mixin.py::TestPlotWidgetMixin::test_do_set_attributes_calls_super``

----

General Mixin Constraints
=========================

.. _PTW-COM-X-020:

PTW-COM-X-020
-------------

:Description: All mixin ``__init__()`` methods **SHALL** call
              ``super().__init__()`` to ensure the full inheritance
              chain is initialized correctly via Python cooperative
              multiple inheritance.
:Rationale:   Python cooperative multiple inheritance requires that
              every ``__init__()`` in the MRO calls
              ``super().__init__()``. Failure to do so can silently
              skip initialization of classes higher in the MRO,
              causing subtle bugs that are difficult to diagnose.
:Traces to:   :ref:`PTW-SR-A-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::TestWidgetMixin::test_init``
              ``tests/common/test_data_widget_mixin.py::TestDataWidgetMixin::test_init``
              ``tests/common/test_plot_widget_mixin.py::TestPlotWidgetMixin::test_init``

----

.. _PTW-COM-X-021:

PTW-COM-X-021
-------------

:Description: All mixin ``do_set_attributes()`` methods **SHALL**
              call ``super().do_set_attributes()`` before processing
              their own attributes.
:Rationale:   Calling the superclass method first ensures that base
              attributes are always initialized before derived
              attributes, maintaining a consistent and predictable
              attribute setting order across the full inheritance
              hierarchy.
:Traces to:   :ref:`PTW-SR-A-003`, :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_data_widget_mixin.py::TestDataWidgetMixin::test_do_set_attributes_calls_super``
              ``tests/common/test_plot_widget_mixin.py::TestPlotWidgetMixin::test_do_set_attributes_calls_super``

----

.. _PTW-COM-X-022:

PTW-COM-X-022
-------------

:Description: All mixin ``do_get_attribute()`` methods **SHALL**
              delegate to ``super().do_get_attribute()`` for
              attributes not defined in their own ``_*_ATTRIBUTES``
              class-level dictionary.
:Rationale:   Delegating unknown attribute lookups to the superclass
              ensures that the full attribute hierarchy is searchable
              via a single ``do_get_attribute()`` call, regardless of
              which mixin in the hierarchy defines the attribute.
:Traces to:   :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_data_widget_mixin.py::TestDataWidgetMixin::test_do_get_attribute_delegates``
              ``tests/common/test_plot_widget_mixin.py::TestPlotWidgetMixin::test_do_get_attribute_delegates``

----

.. _PTW-COM-X-023:

PTW-COM-X-023
-------------

:Description: The class-level ``_WIDGET_ATTRIBUTES``,
              ``_DATA_WIDGET_ATTRIBUTES``, and
              ``_PLOT_WIDGET_ATTRIBUTES`` dictionaries **SHALL** be
              treated as read-only. They **SHALL NOT** be mutated
              after class definition.
:Rationale:   Class-level dictionaries are shared across all instances
              of the class. Mutating them at runtime would affect all
              existing and future instances, causing unpredictable
              behavior. They serve as immutable default templates from
              which instance ``dic_attributes`` dictionaries are
              initialized.
:Traces to:   :ref:`PTW-SR-W-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::TestWidgetMixin::test_class_attributes_not_mutated``
              ``tests/common/test_data_widget_mixin.py::TestDataWidgetMixin::test_class_attributes_not_mutated``
              ``tests/common/test_plot_widget_mixin.py::TestPlotWidgetMixin::test_class_attributes_not_mutated``

----

.. _PTW-COM-X-024:

PTW-COM-X-024
-------------

:Description: The ``dic_attributes`` dictionary **SHALL** be the
              single source of truth for all pytkwrap object attribute
              values. Attribute values **SHALL NOT** be stored as
              separate instance attributes in addition to
              ``dic_attributes``.
:Rationale:   Storing attribute values in both ``dic_attributes`` and
              separate instance attributes creates a synchronization
              problem — the two copies can become inconsistent.
              Using ``dic_attributes`` as the sole store eliminates
              this risk and simplifies the attribute access pattern.
:Traces to:   :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/common/test_widget_mixin.py::TestWidgetMixin::test_dic_attributes_is_sole_store``
              ``tests/common/test_data_widget_mixin.py::TestDataWidgetMixin::test_dic_attributes_is_sole_store``
              ``tests/common/test_plot_widget_mixin.py::TestPlotWidgetMixin::test_dic_attributes_is_sole_store``

----

FontDescription
===============

.. _PTW-COM-X-025:

PTW-COM-X-025
-------------

:Description: The ``FontDescription`` dataclass **SHALL** be defined
              in ``pytkwrap.utilities`` and **SHALL** contain no
              toolkit-specific imports or dependencies.
:Rationale:   Font description is a concept common to all GUI
              toolkits. Defining it in the utilities module without
              toolkit dependencies ensures it can be used by any
              toolkit implementation and that the common layer remains
              clean.
:Traces to:   :ref:`PTW-SR-A-002`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/test_font_description.py::TestFontDescription::test_init``
              ``tests/test_font_description.py::TestFontDescription::test_no_toolkit_imports``

----

.. _PTW-COM-X-026:

PTW-COM-X-026
-------------

:Description: The ``FontDescription`` dataclass **SHALL** provide a
              ``to_string()`` method that returns the core font
              attributes as a space-separated string suitable for
              passing to toolkit font description constructors.
:Rationale:   A toolkit-agnostic string representation of the font
              description allows toolkit-specific code to convert
              to the appropriate toolkit font object without the
              ``FontDescription`` class knowing anything about the
              toolkit.
:Traces to:   :ref:`PTW-SR-A-002`, :ref:`PTW-SR-W-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/test_font_description.py::TestFontDescription::test_to_string``

----

.. _PTW-COM-X-027:

PTW-COM-X-027
-------------

:Description: The ``FontDescription`` dataclass **SHALL** provide a
              ``to_markup()`` method that returns an opening markup
              span tag with all font attributes set. The caller
              **SHALL** be responsible for appending the text content
              and the closing ``</span>`` tag.
:Rationale:   A markup string representation of the font description
              allows markup-supporting widgets such as labels to apply
              rich text formatting without the ``FontDescription``
              class needing to know about the widget or toolkit.
:Traces to:   :ref:`PTW-SR-A-002`, :ref:`PTW-SR-W-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-27) — Initial baseline.
:Tests:       ``tests/test_font_description.py::TestFontDescription::test_to_markup``
              ``tests/test_font_description.py::TestFontDescription::test_to_markup_omits_empty_optional_attrs``

.. note::

   The ``to_markup()`` method currently produces Pango markup syntax
   (``<span>`` tags). Toolkit-specific subclasses or overrides may be
   needed for other markup formats such as Qt rich text. This is
   identified as a future consideration for non-GTK3 toolkit
   implementations.
