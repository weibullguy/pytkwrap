.. _gtk3_entry:

===================================
GTK3 Layer — Entry Requirements
===================================

This document defines the software requirements for the
``GTK3Entry`` class defined in ``pytkwrap.gtk3.io.entry``. These
requirements cover both the standard pytkwrap widget interface and
the Entry-specific methods for font configuration and typed value
retrieval.

All requirements in this document trace to one or more system
requirements defined in :ref:`system_requirements` and to GTK3 layer
widget requirements defined in :ref:`gtk3_widgets`.

.. contents:: Contents
   :local:
   :depth: 1

----

Initialization
==============

.. _PTW-GTK3-E-001:

PTW-GTK3-E-001
--------------

:Description: The ``GTK3Entry`` class **SHALL** combine ``Gtk.Entry``
              and ``GTK3EntryMixin``. The mixin **SHALL** define
              ``edit_signal`` as ``"changed"``,
              ``_DEFAULT_HEIGHT`` as ``25``, and ``_DEFAULT_WIDTH``
              as ``200``.
:Rationale:   ``Gtk.Entry`` emits ``"changed"`` when the text
              content changes. This is the correct signal to use as
              the edit signal for publish-subscribe messaging.
:Traces to:   :ref:`PTW-GTK3-M-005`, :ref:`PTW-GTK3-W-019`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_entry.py::TestGTK3Entry::test_init``

----

.. _PTW-GTK3-E-002:

PTW-GTK3-E-002
--------------

:Description: The ``GTK3Entry.__init__()`` method **SHALL** accept
              an optional ``font`` parameter of type
              ``FontDescription | None`` defaulting to ``None`` and
              **SHALL** call ``do_set_font_description()`` with the
              provided value during initialization.
:Rationale:   Accepting a ``FontDescription`` at construction time
              allows the entry font to be configured in a single
              step without requiring a separate
              ``do_set_font_description()`` call after construction.
:Traces to:   :ref:`PTW-SR-W-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_entry.py::TestGTK3Entry::test_init``
              ``tests/gtk3/test_entry.py::TestGTK3Entry::test_init_with_font``

----

.. _PTW-GTK3-E-003:

PTW-GTK3-E-003
--------------

:Description: The ``GTK3Entry.__init__()`` method **SHALL** set
              ``default_value`` to an empty string ``""``.
:Rationale:   An empty string is the most appropriate default value
              for a text entry widget — it represents the absence of
              input without displaying ``None`` or any other
              placeholder that might be misinterpreted as user input.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-COM-M-010`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_entry.py::TestGTK3Entry::test_init``

----

do_get_value
============

.. _PTW-GTK3-E-004:

PTW-GTK3-E-004
--------------

:Description: The ``GTK3Entry.do_get_value()`` method **SHALL**
              return the text content of the entry coerced to the
              type specified by ``dic_attributes["value_type"]`` as
              follows:

              - ``"float"``: coerce to ``float``.
              - ``"int"``: coerce to ``int``.
              - ``"str"``: coerce to ``str``.
              - Any other value including ``None``: return the raw
                text string as returned by ``Gtk.Entry.get_text()``.

:Rationale:   The datatype attribute allows the Entry to return the
              correct Python type for the underlying data field
              without the caller needing to perform type coercion.
              This is particularly useful when the entry value is
              passed through the messaging system to application
              code that expects a specific type.
:Traces to:   :ref:`PTW-SR-W-006`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_entry.py::TestGTK3Entry::test_do_get_value_gfloat``
              ``tests/gtk3/test_entry.py::TestGTK3Entry::test_do_get_value_gint``
              ``tests/gtk3/test_entry.py::TestGTK3Entry::test_do_get_value_gchararray``
              ``tests/gtk3/test_entry.py::TestGTK3Entry::test_do_get_value_no_datatype``

----

do_set_value
============

.. _PTW-GTK3-E-005:

PTW-GTK3-E-005
--------------

:Description: The ``GTK3Entry.do_set_value()`` method **SHALL**
              accept a ``bool | date | float | int | str | None``
              value and **SHALL** call ``Gtk.Entry.set_text()`` with
              the string representation of the value. A ``None``
              value **SHALL** be converted to an empty string
              ``""``. A ``date`` value **SHALL** be formatted as an
              ISO-8601 string in the format ``"YYYY-MM-DD"`` before
              being passed to ``set_text()``.
:Rationale:   ``Gtk.Entry.set_text()`` requires a string argument.
              Handling ``None`` and ``date`` conversions in
              ``do_set_value()`` ensures the entry always displays
              a meaningful value and eliminates the need for type
              conversion in application code.
:Traces to:   :ref:`PTW-SR-W-007`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_entry.py::TestGTK3Entry::test_do_set_value_string``
              ``tests/gtk3/test_entry.py::TestGTK3Entry::test_do_set_value_integer``
              ``tests/gtk3/test_entry.py::TestGTK3Entry::test_do_set_value_float``
              ``tests/gtk3/test_entry.py::TestGTK3Entry::test_do_set_value_date``
              ``tests/gtk3/test_entry.py::TestGTK3Entry::test_do_set_value_none``

----

Font Configuration
==================

.. _PTW-GTK3-E-006:

PTW-GTK3-E-006
--------------

:Description: The ``GTK3Entry`` class **SHALL** provide a
              ``do_set_font_description()`` method that accepts an
              optional ``FontDescription | None`` parameter defaulting
              to ``None`` and **SHALL** apply the font to the entry
              widget using ``Gtk.Widget.override_font()``.
:Rationale:   Font configuration is a common requirement for entry
              widgets in applications that display data with specific
              formatting requirements. Encapsulating the font
              application logic in a dedicated method provides a
              consistent interface that hides the GTK3-specific
              ``override_font()`` call.
:Traces to:   :ref:`PTW-SR-W-001`, :ref:`PTW-COM-X-012`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_entry.py::TestGTK3Entry::test_do_set_font_description``
              ``tests/gtk3/test_entry.py::TestGTK3Entry::test_do_set_font_description_none``

----

.. _PTW-GTK3-E-007:

PTW-GTK3-E-007
--------------

:Description: The ``GTK3Entry.do_set_font_description()`` method
              **SHALL** store the ``FontDescription`` instance in
              ``dic_attributes["font_description"]`` and **SHALL**
              call ``Gtk.Widget.override_font()`` with a
              ``Pango.FontDescription`` constructed from
              ``FontDescription.to_string()``.
:Rationale:   Storing the ``FontDescription`` instance in
              ``dic_attributes`` ensures it is accessible via
              ``do_get_attribute()`` and persists across calls to
              ``do_set_attributes()``. Converting to a
              ``Pango.FontDescription`` via ``to_string()`` keeps
              the ``FontDescription`` dataclass toolkit-agnostic
              as required by :ref:`PTW-COM-X-011`.
:Traces to:   :ref:`PTW-COM-X-011`, :ref:`PTW-COM-X-012`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_entry.py::TestGTK3Entry::test_do_set_font_description``
              ``tests/gtk3/test_entry.py::TestGTK3Entry::test_do_set_font_description_stored_in_dic_attributes``

----

.. _PTW-GTK3-E-008:

PTW-GTK3-E-008
--------------

:Description: When ``do_set_font_description()`` is called with
              ``None``, a default ``FontDescription()`` instance
              **SHALL** be used.
:Rationale:   Using a default ``FontDescription()`` when ``None``
              is passed ensures the entry always has a valid font
              applied and eliminates the need for ``None`` checks
              in calling code.
:Traces to:   :ref:`PTW-SR-W-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_entry.py::TestGTK3Entry::test_do_set_font_description_none``

----

.. _PTW-GTK3-E-009:

PTW-GTK3-E-009
--------------

:Description: The ``GTK3Entry.do_set_attributes()`` method **SHALL**
              call ``do_set_font_description()`` with the
              ``font_description`` value from ``dic_attributes``
              after calling ``super().do_set_attributes()``.
:Rationale:   Reapplying the font after setting attributes ensures
              that font changes made via ``do_set_attributes()``
              are immediately reflected in the widget's appearance,
              without requiring a separate call to
              ``do_set_font_description()``.
:Traces to:   :ref:`PTW-SR-W-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_entry.py::TestGTK3Entry::test_do_set_attributes_applies_font``
