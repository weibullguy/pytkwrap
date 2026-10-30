.. _gtk3_textview:

======================================
GTK3 Layer — TextView Requirements
======================================

This document defines the software requirements for the
``GTK3TextView`` class defined in ``pytkwrap.gtk3.io.textview``. These
requirements cover its native GTK composition and text-buffer value
access. It currently uses the inherited widget-level callback and
signal-owner behavior; it does not connect edit callbacks to its buffer.

All requirements in this document trace to one or more system
requirements defined in :ref:`system_requirements` and to GTK3 layer
widget requirements defined in :ref:`gtk3_widgets`.

.. contents:: Contents
   :local:
   :depth: 1

----

Initialization
==============

.. _PTW-GTK3-TV-001:

PTW-GTK3-TV-001
---------------

:Description: The ``GTK3TextView`` class **SHALL** combine
              ``Gtk.TextView`` and ``GTK3TextViewMixin``. The mixin
              **SHALL** set ``default_value`` to an empty string.
:Rationale:   The wrapper retains the GTK text-view API and supplies
              pytkwrap behavior through its mixin.
:Traces to:   :ref:`PTW-GTK3-M-005`, :ref:`PTW-GTK3-W-019`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_textview.py::TestGTK3TextView::test_init``

----

.. _PTW-GTK3-TV-002:

PTW-GTK3-TV-002
---------------

:Description: The ``GTK3TextView.__init__()`` method **SHALL** accept
              a ``buffer`` parameter of type ``GTK3TextBuffer | None``
              and **SHALL** store it in
              ``dic_properties["buffer"]`` and initialize the native
              ``Gtk.TextView`` with that buffer.
:Rationale:   ``Gtk.TextView`` requires a ``Gtk.TextBuffer`` to hold
              its text content. Accepting the buffer at construction
              time allows the caller to provide a buffer or use the
              native GTK default when ``None`` is supplied.
:Traces to:   :ref:`PTW-SR-W-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_textview.py::TestGTK3TextView::test_init``

----

.. _PTW-GTK3-TV-003:

PTW-GTK3-TV-003
---------------

:Description: The ``GTK3TextView`` wrapper **SHALL NOT** create or
              manage a ``Gtk.ScrolledWindow``; applications may place
              it in a scrolled window when needed.
:Rationale:   The wrapper does not own application layout or scrolling
              policy.
:Traces to:   :ref:`PTW-SR-W-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_textview.py::TestGTK3TextView::test_init_scrollwindow``

----

.. _PTW-GTK3-TV-004:

PTW-GTK3-TV-004
---------------

:Description: The ``GTK3TextView.__init__()`` method **SHALL** set
              ``default_value`` to an empty string ``""``.
:Rationale:   An empty string is the most appropriate default value
              for a multi-line text entry widget, consistent with
              the default for ``GTK3Entry``.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-COM-M-010`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_textview.py::TestGTK3TextView::test_init``

----

Signal and Callback Ownership
=============================

.. _PTW-GTK3-TV-005:

PTW-GTK3-TV-005
---------------

:Description: ``GTK3TextView`` **SHALL** use the inherited
              ``_get_signal_owner()`` behavior, which returns the
              wrapper instance. It does not override this method to
              return the text buffer.
:Rationale:   TextView-specific signal ownership is not implemented
              in the current wrapper.
:Traces to:   :ref:`PTW-GTK3-M-004`, :ref:`PTW-GTK3-W-016`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_textview.py::TestGTK3TextView::test_get_signal_owner``

----

.. _PTW-GTK3-TV-006:

PTW-GTK3-TV-006
---------------

:Description: ``GTK3TextView`` **SHALL** use the inherited
              ``do_set_callbacks()`` behavior, which connects signals
              to the wrapper instance rather than to
              ``dic_properties["buffer"]``.
:Rationale:   Buffer-specific callback wiring is not implemented by
              the current TextView wrapper.
:Traces to:   :ref:`PTW-GTK3-M-010`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_textview.py::TestGTK3TextView::test_do_set_callbacks_with_buffer``

----

do_get_value and do_set_value
==============================

.. _PTW-GTK3-TV-007:

PTW-GTK3-TV-007
---------------

:Description: The ``GTK3TextView.do_get_value()`` method **SHALL**
              return the full text content of the
              ``Gtk.TextBuffer`` including hidden characters, as
              returned by
              ``Gtk.TextBuffer.get_text(*get_bounds(), True)``.
:Rationale:   ``get_text()`` with ``include_hidden_chars=True``
              returns the complete text content of the buffer,
              including any text that may be hidden by tags. This
              ensures the full content is always returned regardless
              of any formatting applied.
:Traces to:   :ref:`PTW-SR-W-006`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_textview.py::TestGTK3TextView::test_do_get_value``
              ``tests/gtk3/test_textview.py::TestGTK3TextView::test_do_get_value_empty``

----

.. _PTW-GTK3-TV-008:

PTW-GTK3-TV-008
---------------

:Description: The ``GTK3TextView.do_set_value()`` method **SHALL**
              accept a ``bool | date | float | int | str | None``
              value and **SHALL** call
              ``Gtk.TextBuffer.set_text()`` with the string
              representation of the value. A ``None`` value
              **SHALL** be converted to an empty string ``""``.
:Rationale:   ``Gtk.TextBuffer.set_text()`` requires a string
              argument. Converting all value types to strings
              ensures the buffer always receives a valid argument
              and eliminates the need for type conversion in
              application code.
:Traces to:   :ref:`PTW-SR-W-007`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_textview.py::TestGTK3TextView::test_do_set_value``
              ``tests/gtk3/test_textview.py::TestGTK3TextView::test_do_set_value_none``
              ``tests/gtk3/test_textview.py::TestGTK3TextView::test_do_set_value_integer``
              ``tests/gtk3/test_textview.py::TestGTK3TextView::test_do_set_value_date``

----

do_update Behavior
==================

.. _PTW-GTK3-TV-009:

PTW-GTK3-TV-009
---------------

:Description: ``GTK3TextView.do_update()`` **SHALL** use the inherited
              update behavior, including filtering by ``index``,
              substituting ``default_value`` for ``None``, and
              blocking configured handlers on the wrapper instance.
:Rationale:   The TextView wrapper does not override the generic
              update or signal-owner methods.
:Traces to:   :ref:`PTW-GTK3-M-001`, :ref:`PTW-GTK3-M-004`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_textview.py::TestGTK3TextView::test_do_update``
              ``tests/gtk3/test_textview.py::TestGTK3TextView::test_do_update_does_not_trigger_callback``
              ``tests/gtk3/test_textview.py::TestGTK3TextView::test_do_update_none_value``

----

.. _PTW-GTK3-TV-010:

PTW-GTK3-TV-010
---------------

:Description: If the configured ``edit_signal`` is absent from
              ``dic_handler_id``, inherited ``do_update()`` **SHALL**
              log an error and raise ``UnkSignalError``. It does not
              translate ``OverflowError`` from GTK signal blocking.
:Rationale:   The generic update method treats an unknown configured
              signal as a wrapper configuration error.
:Traces to:   :ref:`PTW-GTK3-W-013`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_textview.py::TestGTK3TextView::test_do_update_unknown_signal``
              ``tests/gtk3/test_textview.py::TestGTK3TextView::test_do_update_overflow_error``

----

on_changed Behavior
===================

.. _PTW-GTK3-TV-011:

PTW-GTK3-TV-011
---------------

:Description: ``GTK3TextView`` **SHALL** use the inherited
              ``on_changed()`` callback, which receives the wrapper
              instance and publishes its value on ``send_topic``
              without blocking the edit handler.
:Rationale:   The TextView wrapper does not override
              ``on_changed()`` with buffer-specific behavior.
:Traces to:   :ref:`PTW-GTK3-M-002`, :ref:`PTW-GTK3-M-004`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_textview.py::TestGTK3TextView::test_on_changed``
              ``tests/gtk3/test_textview.py::TestGTK3TextView::test_on_changed_does_not_trigger_callback``
              ``tests/gtk3/test_textview.py::TestGTK3TextView::test_on_changed_unknown_signal``
