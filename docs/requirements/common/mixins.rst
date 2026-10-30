.. _common_mixins:

=================================
Common Layer — Mixin Requirements
=================================

This document specifies the toolkit-independent convenience API defined
in ``pytkwrap.common.mixins``. The current common API consists of
``PyTkWrapMixin``, ``PyTkWrapAttributes``, ``PyTkWrapConfig``, and
``make_pytkwrap_config()``. There are no separate ``BaseMixin``,
``WidgetMixin``, ``DataWidgetMixin``, or ``PlotWidgetMixin`` classes in
the current implementation.

The common layer does not import a GUI toolkit. It does use shared
libraries including Matplotlib and PyPubSub; toolkit independence does
not imply absence of third-party dependencies.

All requirements trace to the system requirements in
:ref:`system_requirements`.

.. contents:: Contents
   :local:
   :depth: 1

----

PyTkWrapAttributes
==================

.. _PTW-COM-X-001:

PTW-COM-X-001
-------------

:Description: ``PyTkWrapAttributes`` **SHALL** be a ``TypedDict`` with
              ``total=False``. It **SHALL** describe the common keys
              ``axis``, ``canvas``, ``data_type``, ``default_value``,
              ``edit_signal``, ``figure``, ``font_description``,
              ``format``, ``index``, ``listen_topic``, ``n_columns``,
              ``n_rows``, ``send_topic``, ``x_pos``, and ``y_pos``.
:Rationale:   The partial typed dictionary provides a type-checking aid
              for common configuration while allowing callers to
              specify only values they wish to override.
:Traces to:   :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

PyTkWrapMixin
=============

.. _PTW-COM-X-002:

PTW-COM-X-002
-------------

:Description: ``PyTkWrapMixin`` **SHALL** initialize instance-local
              ``dic_attributes``, ``dic_error_message``,
              ``dic_handler_id``, and ``dic_properties`` dictionaries.
              The initial attribute mapping **SHALL** be copied from
              ``_PYTKWRAP_ATTRIBUTES``; the default keys in that mapping
              have value ``None``.
:Rationale:   Instance-local state prevents one wrapper's configuration
              from being shared with another instance.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-COM-X-003:

PTW-COM-X-003
-------------

:Description: ``PyTkWrapMixin.do_get_attribute()`` **SHALL** return the
              stored value when the requested key exists in
              ``dic_attributes``. For an unknown key, it **SHALL**
              publish a ``do_log_error`` message and raise
              ``UnkAttributeError``.
:Rationale:   A consistent lookup method reports invalid attribute
              names explicitly rather than silently returning a default.
:Traces to:   :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-COM-X-004:

PTW-COM-X-004
-------------

:Description: ``PyTkWrapMixin.do_get_property()`` **SHALL** return the
              stored value when the requested key exists in
              ``dic_properties``. For an unknown key, it **SHALL**
              publish a ``do_log_error`` message and raise
              ``UnkPropertyError``.
:Rationale:   Property lookup follows the same explicit error-reporting
              convention as attribute lookup.
:Traces to:   :ref:`PTW-SR-W-004`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-COM-X-005:

PTW-COM-X-005
-------------

:Description: ``PyTkWrapMixin.do_set_attributes()`` **SHALL** update
              recognized keys in ``dic_attributes`` from the supplied
              mapping and **SHALL** retain existing values for omitted
              keys. It **SHALL NOT** coerce values or reject unknown
              mapping keys at runtime.
:Rationale:   Partial updates support incremental configuration; the
              typed dictionary is a static typing aid, not runtime
              validation.
:Traces to:   :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-COM-X-006:

PTW-COM-X-006
-------------

:Description: ``PyTkWrapMixin.do_set_properties()`` **SHALL** accept a
              mapping or an iterable of key/value pairs and merge the
              supplied entries into ``dic_properties``. For invalid
              non-iterable input or invalid key/value pairs, it **SHALL**
              publish a ``do_log_error`` message and raise
              ``PytkwrapError`` chained from the conversion error.
:Rationale:   Both mappings and pair sequences provide a convenient
              configuration interface, while malformed configuration
              is surfaced explicitly.
:Traces to:   :ref:`PTW-SR-W-004`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-COM-X-007:

PTW-COM-X-007
-------------

:Description: The base ``PyTkWrapMixin.do_get_value()`` implementation
              **SHALL** publish a ``do_log_error`` message and raise
              ``NoValueError``. Concrete wrappers that expose a value
              **SHALL** implement the method for their own value type.
:Rationale:   Explicitly reporting the absence of a value implementation
              identifies unsupported use of the base convenience API.
:Traces to:   :ref:`PTW-SR-W-006`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-COM-X-008:

PTW-COM-X-008
-------------

:Description: The base ``PyTkWrapMixin.do_set_value()`` implementation
              **SHALL** publish a ``do_log_error`` message and raise
              ``WrongTypeError``. Concrete wrappers that accept values
              **SHALL** implement the method for their own value type.
:Rationale:   The base mixin does not assume a universal widget value
              type; unsupported setting is reported explicitly.
:Traces to:   :ref:`PTW-SR-W-007`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

PyTkWrapConfig
==============

.. _PTW-COM-X-009:

PTW-COM-X-009
-------------

:Description: ``PyTkWrapConfig`` **SHALL** be a ``TypedDict`` with
              required keys ``widget``, ``attributes``, and
              ``properties``. The keys **SHALL** respectively describe
              a ``PyTkWrapMixin`` instance, ``PyTkWrapAttributes``, and
              a property mapping.
:Rationale:   A shared configuration shape allows callers to pass a
              wrapper and its common attributes and toolkit properties
              together.
:Traces to:   :ref:`PTW-SR-W-004`, :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-COM-X-010:

PTW-COM-X-010
-------------

:Description: ``make_pytkwrap_config()`` **SHALL** accept a wrapper,
              a ``PyTkWrapAttributes`` mapping, and a properties
              dictionary and **SHALL** return a ``PyTkWrapConfig``
              containing those three objects under their corresponding
              keys.
:Rationale:   The factory centralizes creation of the documented
              wrapper-configuration shape.
:Traces to:   :ref:`PTW-COM-X-009`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-COM-X-011:

PTW-COM-X-011
-------------

:Description: ``PyTkWrapAttributes`` **SHALL** use the declared Python
              types for its common configuration values, including
              ``default_value``, ``data_type``, ``edit_signal``,
              ``font_description``, ``index``, message topics, grid
              dimensions, and coordinates.
:Rationale:   Static type declarations communicate intended values to
              callers and type checkers; they do not imply runtime
              coercion or validation.
:Traces to:   :ref:`PTW-COM-X-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-COM-X-012:

PTW-COM-X-012
-------------

:Description: ``PyTkWrapMixin.do_set_attributes()`` **SHALL** preserve
              existing values for omitted keys and **SHALL** copy
              provided values for keys defined by
              ``PyTkWrapAttributes`` without coercion.
:Rationale:   Partial updates allow callers to configure only the
              common attributes relevant to a wrapper.
:Traces to:   :ref:`PTW-COM-X-001`, :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-COM-X-013:

PTW-COM-X-013
-------------

:Description: The base ``PyTkWrapMixin`` value methods **SHALL** report
              unsupported operations explicitly: ``do_get_value()``
              publishes ``do_log_error`` and raises ``NoValueError``;
              ``do_set_value()`` publishes ``do_log_error`` and raises
              ``WrongTypeError``. Concrete value-bearing wrappers
              **SHALL** provide their own value behavior.
:Rationale:   The common mixin cannot assume a value type or display
              mechanism shared by every wrapper.
:Traces to:   :ref:`PTW-SR-W-006`, :ref:`PTW-SR-W-007`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

FontDescription
===============

.. _PTW-COM-X-025:

PTW-COM-X-025
-------------

:Description: ``FontDescription`` **SHALL** be a toolkit-independent
              dataclass in ``pytkwrap.utilities`` containing family,
              features, size, stretch, style, variant, and weight.
:Rationale:   A shared font value object avoids requiring callers to
              construct toolkit-specific font types for common
              configuration.
:Traces to:   :ref:`PTW-SR-A-002`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-COM-X-026:

PTW-COM-X-026
-------------

:Description: ``FontDescription.to_css()`` **SHALL** return CSS
              declarations for the font fields and **SHALL** omit
              stretch and feature declarations when their values are
              empty.
:Rationale:   The CSS representation supports toolkit style providers
              without introducing toolkit imports into the dataclass.
:Traces to:   :ref:`PTW-SR-A-002`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-COM-X-027:

PTW-COM-X-027
-------------

:Description: ``FontDescription.to_string()`` **SHALL** return a
              space-separated font description, and
              ``FontDescription.to_markup()`` **SHALL** return an
              opening Pango ``<span>`` tag whose text and closing tag
              are supplied by the caller.
:Rationale:   These representations support toolkit/font APIs and
              markup-capable widgets while leaving text insertion to
              the caller.
:Traces to:   :ref:`PTW-SR-A-002`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.
