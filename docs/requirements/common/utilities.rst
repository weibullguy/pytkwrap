.. _common_utilities:

=====================================
Common Layer — Utilities Requirements
=====================================

This document defines the software requirements for the utility
functions and classes defined in ``pytkwrap.utilities``. These
utilities are toolkit-agnostic and are available to all toolkit
implementations as well as application code that uses pytkwrap.

All requirements in this document trace to one or more system
requirements defined in :ref:`system_requirements`.

.. contents:: Contents
   :local:
   :depth: 1

----

Type Conversion
===============

.. _PTW-COM-U-001:

PTW-COM-U-001
-------------

:Description: The ``boolean_to_integer()`` function **SHALL** accept
              a boolean value and **SHALL** return ``1`` if the value
              is ``True`` and ``0`` if the value is ``False``.
:Rationale:   Boolean-to-integer conversion is a common operation
              when storing widget state in databases or passing values
              through messaging systems that expect integer values.
:Traces to:   :ref:`PTW-SR-W-006`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/test_utilities.py::test_boolean_to_integer_true``
              ``tests/test_utilities.py::test_boolean_to_integer_false``

----

.. _PTW-COM-U-002:

PTW-COM-U-002
-------------

:Description: The ``integer_to_boolean()`` function **SHALL** accept
              an integer value and **SHALL** return ``True`` if the
              value is greater than zero and ``False`` otherwise.
:Rationale:   Integer-to-boolean conversion is a common operation
              when reading widget state from databases or receiving
              values through messaging systems that use integer
              representations of boolean values.
:Traces to:   :ref:`PTW-SR-W-006`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/test_utilities.py::test_integer_to_boolean_positive``
              ``tests/test_utilities.py::test_integer_to_boolean_zero``
              ``tests/test_utilities.py::test_integer_to_boolean_negative``

----

.. _PTW-COM-U-003:

PTW-COM-U-003
-------------

:Description: The ``string_to_boolean()`` function **SHALL** accept
              a string or boolean value and **SHALL** return ``True``
              if the string value (case-insensitive) is one of
              ``"true"``, ``"yes"``, ``"t"``, or ``"y"``, and
              **SHALL** return ``False`` otherwise. If the input is
              already a boolean, it **SHALL** be returned unchanged.
:Rationale:   String-to-boolean conversion is a common operation
              when reading widget state from configuration files,
              databases, or messaging systems that represent boolean
              values as strings.
:Traces to:   :ref:`PTW-SR-W-006`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/test_utilities.py::test_string_to_boolean_true_strings``
              ``tests/test_utilities.py::test_string_to_boolean_false_strings``
              ``tests/test_utilities.py::test_string_to_boolean_boolean_input``
              ``tests/test_utilities.py::test_string_to_boolean_case_insensitive``

----

.. _PTW-COM-U-004:

PTW-COM-U-004
-------------

:Description: The ``none_to_default()`` function **SHALL** accept a
              value and a default and **SHALL** return the default if
              the value is ``None``, or the original value otherwise.
:Rationale:   Centralizing the ``None``-to-default substitution logic
              ensures consistent behavior across all widgets and
              avoids duplicating the ``None`` check in every widget's
              ``do_update()`` method.
:Traces to:   :ref:`PTW-SR-M-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/test_utilities.py::test_none_to_default_none_value``
              ``tests/test_utilities.py::test_none_to_default_non_none_value``

----

.. _PTW-COM-U-005:

PTW-COM-U-005
-------------

:Description: The ``none_to_string()`` function **SHALL** accept a
              string or ``None`` value and **SHALL** return an empty
              string if the value is ``None`` or the string ``"None"``,
              and **SHALL** return the original string otherwise.
:Rationale:   Converting ``None`` to an empty string is a common
              operation when populating text-based widgets that cannot
              display ``None`` values.
:Traces to:   :ref:`PTW-SR-W-006`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/test_utilities.py::test_none_to_string_none``
              ``tests/test_utilities.py::test_none_to_string_none_string``
              ``tests/test_utilities.py::test_none_to_string_valid_string``

----

Date Conversion
===============

.. _PTW-COM-U-006:

PTW-COM-U-006
-------------

:Description: The ``date_to_ordinal()`` function **SHALL** accept a
              date string and **SHALL** return its ordinal integer
              representation. If the string cannot be parsed as a
              date, it **SHALL** return the ordinal of
              ``"01/01/1970"``.
:Rationale:   Ordinal date representation is a compact, sortable
              integer format suitable for database storage and
              arithmetic operations on dates.
:Traces to:   :ref:`PTW-SR-W-006`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/test_utilities.py::test_date_to_ordinal_valid``
              ``tests/test_utilities.py::test_date_to_ordinal_invalid``

----

.. _PTW-COM-U-007:

PTW-COM-U-007
-------------

:Description: The ``ordinal_to_date()`` function **SHALL** accept an
              ordinal integer and **SHALL** return its ISO-8601 date
              string representation in the format ``"YYYY-MM-DD"``.
              If the ordinal cannot be converted, it **SHALL** return
              the current date in ISO-8601 format.
:Rationale:   Converting ordinal dates back to ISO-8601 strings is
              necessary for displaying date values in text-based
              widgets and for human-readable output.
:Traces to:   :ref:`PTW-SR-W-006`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/test_utilities.py::test_ordinal_to_date_valid``
              ``tests/test_utilities.py::test_ordinal_to_date_invalid``

----

.. _PTW-COM-U-008:

PTW-COM-U-008
-------------

:Description: The ``string_to_date()`` function **SHALL** accept an
              ISO-8601 date string in the format ``"YYYY-MM-DD"`` and
              **SHALL** return a ``datetime.date`` object. If the
              string cannot be parsed, it **SHALL** return the current
              date.
:Rationale:   Converting ISO-8601 date strings to ``datetime.date``
              objects is necessary for processing date values received
              from text-based widgets or messaging systems.
:Traces to:   :ref:`PTW-SR-W-006`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/test_utilities.py::test_string_to_date_valid``
              ``tests/test_utilities.py::test_string_to_date_invalid``

----

String Utilities
================

.. _PTW-COM-U-009:

PTW-COM-U-009
-------------

:Description: The ``split_string()`` function **SHALL** accept a
              delimited string and an optional delimiter character
              defaulting to ``":"`` and **SHALL** return a list of
              the constituent parts.
:Rationale:   Splitting delimited strings is a common operation when
              parsing configuration values or topic names in
              publish-subscribe messaging systems.
:Traces to:   :ref:`PTW-SR-W-006`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/test_utilities.py::test_split_string_default_delimiter``
              ``tests/test_utilities.py::test_split_string_custom_delimiter``

----

Dictionary Utilities
====================

.. _PTW-COM-U-010:

PTW-COM-U-010
-------------

:Description: The ``sort_dict()`` function **SHALL** accept a
              dictionary, a boolean ``by_value`` flag defaulting to
              ``True``, and a boolean ``reverse`` flag defaulting to
              ``False``, and **SHALL** return a new dictionary sorted
              by value when ``by_value`` is ``True`` or by key when
              ``by_value`` is ``False``, in ascending order when
              ``reverse`` is ``False`` or descending order when
              ``reverse`` is ``True``.
:Rationale:   Sorted dictionaries are commonly needed when populating
              ComboBox or TreeView widgets with ordered data.
:Traces to:   :ref:`PTW-SR-W-006`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/test_utilities.py::test_sort_dict_by_value``
              ``tests/test_utilities.py::test_sort_dict_by_key``
              ``tests/test_utilities.py::test_sort_dict_reverse``

----

Numeric Utilities
=================

.. _PTW-COM-U-011:

PTW-COM-U-011
-------------

:Description: The ``clamp()`` function **SHALL** accept a numeric
              value, a minimum bound, and a maximum bound, and
              **SHALL** return the value unchanged if it is within
              the bounds, the minimum if it is below the minimum,
              or the maximum if it is above the maximum.
:Rationale:   Clamping values to a valid range is a common operation
              for range-constrained widgets, preventing out-of-range
              values from being passed to setter methods.
:Traces to:   :ref:`PTW-SR-W-006`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/test_utilities.py::test_clamp_within_range``
              ``tests/test_utilities.py::test_clamp_below_minimum``
              ``tests/test_utilities.py::test_clamp_above_maximum``
              ``tests/test_utilities.py::test_clamp_at_bounds``

----

File and Directory Utilities
=============================

.. _PTW-COM-U-012:

PTW-COM-U-012
-------------

:Description: The ``file_exists()`` function **SHALL** accept a file
              path string and **SHALL** return ``True`` if the file
              exists and ``False`` otherwise.
:Rationale:   File existence checking is required by
              ``GTK3FileChooserButton.do_set_value()`` to determine
              the appropriate GTK3 setter method to call.
:Traces to:   :ref:`PTW-SR-W-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/test_utilities.py::test_file_exists_true``
              ``tests/test_utilities.py::test_file_exists_false``

----

.. _PTW-COM-U-013:

PTW-COM-U-013
-------------

:Description: The ``dir_exists()`` function **SHALL** accept a
              directory path string and **SHALL** return ``True`` if
              the directory exists and ``False`` otherwise.
:Rationale:   Directory existence checking is required by
              ``GTK3FileChooserButton.do_set_value()`` when the
              action is ``SELECT_FOLDER`` or ``CREATE_FOLDER``.
:Traces to:   :ref:`PTW-SR-W-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/test_utilities.py::test_dir_exists_true``
              ``tests/test_utilities.py::test_dir_exists_false``

----

.. _PTW-COM-U-014:

PTW-COM-U-014
-------------

:Description: The ``get_home_directory()`` function **SHALL** return
              the absolute path of the current user's home directory
              as a string.
:Rationale:   The home directory is the default fallback location
              for ``GTK3FileChooserButton`` when no valid path is
              available, providing a sensible default that always
              exists.
:Traces to:   :ref:`PTW-SR-W-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/test_utilities.py::test_get_home_directory``

----

.. _PTW-COM-U-015:

PTW-COM-U-015
-------------

:Description: The ``get_install_prefix()`` function **SHALL** return
              the prefix path into which pytkwrap was installed, using
              ``sys.prefix`` to ensure cross-platform compatibility.
:Rationale:   The install prefix is needed to locate installed
              resources such as icons and data files regardless of
              the platform or installation method.
:Traces to:   :ref:`PTW-SR-W-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/test_utilities.py::test_get_install_prefix``

----

Deprecation
===========

.. _PTW-COM-U-016:

PTW-COM-U-016
-------------

:Description: The ``deprecated()`` decorator **SHALL** wrap a
              function and **SHALL** emit a ``DeprecationWarning``
              with the function name whenever the decorated function
              is called.
:Rationale:   A standard deprecation decorator ensures that
              deprecated functions emit consistent, identifiable
              warnings that can be filtered or caught by application
              code and test suites, providing a clear migration path
              for users when APIs change.
:Traces to:   :ref:`PTW-SR-Q-004`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-04-22) — Initial baseline.
:Tests:       ``tests/test_utilities.py::test_deprecated_emits_warning``
              ``tests/test_utilities.py::test_deprecated_calls_original_function``
