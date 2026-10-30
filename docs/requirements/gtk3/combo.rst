.. _gtk3_combo:

=====================================
GTK3 Layer — ComboBox Requirements
=====================================

This document defines the software requirements for the
``GTK3ComboBox`` class defined in ``pytkwrap.gtk3.io.combobox``. These
requirements cover both the standard pytkwrap widget interface and
the ComboBox-specific methods that have no equivalent in other widget
types.

All requirements in this document trace to one or more system
requirements defined in :ref:`system_requirements` and to GTK3 layer
widget requirements defined in :ref:`gtk3_widgets`.

.. contents:: Contents
   :local:
   :depth: 1

----

Initialization
==============

.. _PTW-GTK3-CB-001:

PTW-GTK3-CB-001
---------------

:Description: The ``GTK3ComboBox`` class **SHALL** combine
              ``Gtk.ComboBox`` and ``GTK3ComboBoxMixin``. The mixin
              **SHALL** define ``edit_signal`` as ``"changed"``,
              ``_DEFAULT_HEIGHT`` as ``30``, and
              ``_DEFAULT_WIDTH`` as ``200``.
:Rationale:   ``Gtk.ComboBox`` emits ``"changed"`` when the active
              selection changes. This is the correct signal to use
              as the edit signal for publish-subscribe messaging.
:Traces to:   :ref:`PTW-GTK3-M-005`, :ref:`PTW-GTK3-W-019`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_init``

----

.. _PTW-GTK3-CB-002:

PTW-GTK3-CB-002
---------------

:Description: The ``GTK3ComboBox.__init__()`` method **SHALL** accept
              the following parameters:

              - ``index``: ``int`` defaulting to ``0`` — the column
                index to display.
              - ``simple``: ``bool`` defaulting to ``True`` — whether
                the ComboBox has a single column.
              - ``n_items``: ``int`` defaulting to ``1`` — the number
                of columns in the model.
              - ``column_types``: ``list | None`` defaulting to
                ``None`` — the GObject types of each column.
              - ``has_entry``: ``bool`` defaulting to ``False`` —
                whether the ComboBox has an embedded entry widget.

:Rationale:   These parameters cover the most common ComboBox
              configuration options and allow both simple single-column
              and complex multi-column ComboBoxes to be created
              without requiring post-construction configuration.
:Traces to:   :ref:`PTW-SR-W-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_init``
              ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_init_compound``

----

.. _PTW-GTK3-CB-003:

PTW-GTK3-CB-003
---------------

:Description: When ``column_types`` is ``None``, the
              ``GTK3ComboBox.__init__()`` method **SHALL** default
              to ``[GObject.TYPE_STRING] * n_items``.
:Rationale:   String columns are the most common column type for
              ComboBox widgets. Defaulting to string types eliminates
              the need to specify column types for the most common
              use case.
:Traces to:   :ref:`PTW-SR-W-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_init_default_column_types``

----

.. _PTW-GTK3-CB-004:

PTW-GTK3-CB-004
---------------

:Description: The ``GTK3ComboBox.__init__()`` method **SHALL**
              initialize a ``Gtk.ListStore`` model with the specified
              ``column_types`` and **SHALL** attach a
              ``Gtk.CellRendererText`` for each column, adding the
              text attribute only for the column at ``index``.
:Rationale:   Initializing the model and cell renderers in
              ``__init__()`` ensures the ComboBox is immediately
              usable without requiring the caller to configure the
              model separately. Only the display column receives a
              text attribute to avoid displaying all columns.
:Traces to:   :ref:`PTW-SR-W-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_init``
              ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_init_compound``

----

do_set_attributes
=================

.. _PTW-GTK3-CB-005:

PTW-GTK3-CB-005
---------------

:Description: The ``GTK3ComboBox.do_set_attributes()`` method
              **SHALL** preserve the existing ``column_types`` value
              in ``dic_attributes`` if ``column_types`` is not
              present in the passed attributes dictionary.
:Rationale:   ``column_types`` is set at construction time and
              defines the structure of the underlying
              ``Gtk.ListStore``. Silently resetting it to a default
              value when ``do_set_attributes()`` is called without
              explicitly passing ``column_types`` would corrupt the
              model structure.
:Traces to:   :ref:`PTW-COM-W-008`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_do_set_attributes_preserves_column_types``
              ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_do_set_attributes_overrides_column_types``

----

do_get_value and do_set_value
==============================

.. _PTW-GTK3-CB-006:

PTW-GTK3-CB-006
---------------

:Description: The ``GTK3ComboBox.do_get_value()`` method **SHALL**
              return the string value at the display column
              (``dic_attributes["index"]``) of the currently active
              row in the model. If no row is active or the model is
              ``None``, it **SHALL** return an empty string ``""``.
:Rationale:   Returning the display column value is consistent with
              what the user sees in the ComboBox. Returning an empty
              string rather than ``None`` when no row is active
              prevents ``None`` propagation through the messaging
              system.
:Traces to:   :ref:`PTW-SR-W-006`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_do_get_value``
              ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_do_get_value_no_selection``
              ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_do_get_value_no_model``

----

.. _PTW-GTK3-CB-007:

PTW-GTK3-CB-007
---------------

:Description: The ``GTK3ComboBox.do_set_value()`` method **SHALL**
              accept a ``bool | float | int | str | None`` value and
              **SHALL** call ``Gtk.ComboBox.set_active()`` with the
              integer representation of the value. Non-integer and
              non-numeric values **SHALL** be silently ignored.
:Rationale:   ``Gtk.ComboBox.set_active()`` requires an integer index.
              Accepting the widest possible input type allows
              ``do_set_value()`` to be called from
              ``GTK3MatrixView.set_cell_value()`` without raising a
              ``TypeError``.
:Traces to:   :ref:`PTW-SR-W-007`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_do_set_value``
              ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_do_set_value_non_integer``

----

ComboBox-Specific Methods
=========================

.. _PTW-GTK3-CB-008:

PTW-GTK3-CB-008
---------------

:Description: The ``GTK3ComboBox`` class **SHALL** provide a
              ``do_load_combo()`` method that accepts a list of
              entries and populates the ``Gtk.ListStore`` model with
              an empty first row followed by one row per entry. The
              signal handler **SHALL** be blocked during the load
              operation if a handler is connected.
:Rationale:   Loading a ComboBox with data is a common operation that
              requires clearing the model, adding a blank first row
              as a placeholder, and populating the remaining rows.
              Blocking the signal handler prevents spurious
              ``"changed"`` signals from firing during the load.
:Traces to:   :ref:`PTW-SR-W-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_do_load_combo_simple``
              ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_do_load_combo_compound``
              ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_do_load_combo_clears_previous``
              ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_do_load_combo_no_model``

----

.. _PTW-GTK3-CB-009:

PTW-GTK3-CB-009
---------------

:Description: The ``GTK3ComboBox.do_load_combo()`` method **SHALL**
              behave differently based on the ``simple`` attribute:

              - When ``simple`` is ``True``: each entry **SHALL** be
                wrapped in a list and appended as a single-column row.
              - When ``simple`` is ``False``: each entry **SHALL** be
                appended as-is, allowing multi-column rows.

:Rationale:   Simple ComboBoxes contain plain string entries while
              compound ComboBoxes contain structured multi-column
              data. The ``simple`` flag controls how entries are
              interpreted and stored in the model.
:Traces to:   :ref:`PTW-SR-W-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_do_load_combo_simple``
              ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_do_load_combo_compound``

----

.. _PTW-GTK3-CB-010:

PTW-GTK3-CB-010
---------------

:Description: The ``GTK3ComboBox`` class **SHALL** provide a
              ``do_get_options()`` method that returns a dictionary
              mapping integer row indices to the value at the display
              column (``dic_attributes["index"]``) for each row in
              the model. If the model is ``None``, it **SHALL** return
              an empty dictionary.
:Rationale:   Retrieving all options from a ComboBox is a common
              operation for validation and for populating other
              widgets. Returning a dictionary keyed by row index
              provides a convenient mapping for programmatic access
              to all options.
:Traces to:   :ref:`PTW-SR-W-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_do_get_options``
              ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_do_get_options_empty``
              ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_do_get_options_no_model``

----

.. _PTW-GTK3-CB-011:

PTW-GTK3-CB-011
---------------

:Description: The ``GTK3ComboBox`` class **SHALL** provide a
              ``get_value_at_index()`` method that accepts an integer
              column index and returns the string value at that column
              in the currently active row. If no row is active, the
              model is ``None``, or the model is not a
              ``Gtk.ListStore``, it **SHALL** return an empty string
              ``""``. If no index is provided or the index is ``-1``,
              it **SHALL** default to ``dic_attributes["index"]``.
:Rationale:   For compound ComboBoxes, application code may need to
              read values from columns other than the display column.
              ``get_value_at_index()`` provides this access without
              violating the LSP constraint on ``do_get_value()``,
              which must maintain a consistent no-argument signature
              across all data widgets.
:Traces to:   :ref:`PTW-SR-W-006`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_get_value_at_index``
              ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_get_value_at_index_default``
              ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_get_value_at_index_no_selection``
              ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_get_value_at_index_no_model``

----

do_update Behavior
==================

.. _PTW-GTK3-CB-012:

PTW-GTK3-CB-012
---------------

:Description: The ``GTK3ComboBox.do_update()`` method **SHALL**
              only update the active selection when the incoming
              value is an integer. Non-integer values **SHALL** be
              silently ignored.
:Rationale:   ``Gtk.ComboBox.set_active()`` requires an integer
              index. Ignoring non-integer values prevents GTK3
              errors when the messaging system delivers a value of
              an unexpected type.
:Traces to:   :ref:`PTW-SR-M-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_do_update_simple``
              ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_do_update_compound``
              ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_do_update_non_integer``
              ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_do_update_none_value``
              ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_do_update_unknown_signal``
