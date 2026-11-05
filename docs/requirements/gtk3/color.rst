.. _gtk3_color:

================================
GTK3 Layer — Color Requirements
================================

This document defines the software requirements for the color
wrappers in the ``pytkwrap.gtk3.color`` package: ``GTK3ColorButton``,
``GTK3ColorChooserDialog``, and ``GTK3ColorChooserWidget``. Each
concrete wrapper composes its native ``Gtk`` class with a GTK3 mixin.

The ``GTK3ColorButton`` requirements keep the ``PTW-GTK3-B`` IDs they
were assigned in :ref:`gtk3_buttons`.

All requirements in this document trace to one or more system
requirements defined in :ref:`system_requirements` and to GTK3 layer
widget requirements defined in :ref:`gtk3_widgets`.

.. contents:: Contents
   :local:
   :depth: 1

----

Package
=======

.. _PTW-GTK3-CLR-001:

PTW-GTK3-CLR-001
----------------

:Description: The ``pytkwrap.gtk3.color`` package **SHALL** export
              ``GTK3ColorButton``, ``GTK3ColorChooserDialog``, and
              ``GTK3ColorChooserWidget`` through ``__all__``.
              Sub-modules of the package **SHALL** import sibling
              modules directly and **SHALL NOT** import through the
              package ``__init__.py``.
:Rationale:   A single public import location simplifies application
              code, while direct sibling imports avoid circular
              imports during package initialization.
:Traces to:   :ref:`PTW-SR-W-001`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       TBD

----

GTK3ColorButton
===============

.. _PTW-GTK3-CLR-002:

PTW-GTK3-CLR-002
----------------

:Description: The ``GTK3ColorButton`` class **SHALL** combine
              ``Gtk.ColorButton`` and ``GTK3ColorButtonMixin``, which
              derives from ``GTK3ButtonMixin``. ``GTK3ColorButtonMixin``
              **SHALL** define ``_DEFAULT_HEIGHT`` as ``30`` and
              ``_DEFAULT_WIDTH`` as ``60``; **SHALL** set
              ``dic_attributes["default_value"]`` to ``None`` and
              ``dic_attributes["edit_signal"]`` to ``"color-set"``; and
              **SHALL** pre-register the ``"color-set"`` signal in
              ``dic_handler_id`` with a value of ``-1``.
:Rationale:   ``Gtk.ColorButton`` emits ``"color-set"`` when the
              user selects a new color. This is the correct signal
              to use as the edit signal for publish-subscribe
              messaging. A ``None`` default value is converted to a
              color by ``do_set_value()`` (:ref:`PTW-GTK3-B-014`).
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-011`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-019`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Moved from the button requirements;
              added the base mixin, default size, default value, and
              signal registration; corrected traces.
:Tests:       ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_init``
              ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_do_set_attributes_default``
              ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_do_set_attributes``

----

.. _PTW-GTK3-CLR-003:

PTW-GTK3-CLR-003
----------------

:Description: ``GTK3ColorButton.__init__()`` **SHALL** accept an
              ``rgba`` parameter of type ``Gdk.RGBA | None`` defaulting
              to ``None``. It **SHALL** pass ``rgba`` to
              ``Gtk.ColorButton.__init__()``, then call
              ``GTK3ColorButtonMixin.__init__()``, and **SHALL** store
              ``rgba`` in ``dic_properties["rgba"]``.
:Rationale:   Accepting the initial color at construction avoids a
              separate configuration call for the common case.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_init``
              ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_init_with_rgba``

----

.. _PTW-GTK3-CLR-004:

PTW-GTK3-CLR-004
----------------

:Description: ``GTK3ColorButtonMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``alpha``: ``65535``
              - ``rgba``: ``None``
              - ``show_editor``: ``False``
              - ``title``: ``"Pick a Color"``
              - ``use_alpha``: ``True``

              ``GTK3ColorButtonMixin.do_set_properties()`` **SHALL**
              call ``super().do_set_properties()`` first. It **SHALL**
              call ``set_rgba()`` only when ``rgba`` is not ``None``;
              **SHALL** apply ``title`` with ``set_title()``; and
              **SHALL** apply ``show_editor`` through
              ``set_property("show-editor", ...)``.
:Rationale:   Skipping a ``None`` color preserves the button's current
              color. ``show-editor`` has no dedicated setter in
              ``Gtk.ColorButton``.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_do_set_properties_default``
              ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_do_set_properties``

----

.. _PTW-GTK3-CLR-005:

PTW-GTK3-B-005
--------------

:Description: ``GTK3ColorButtonMixin.do_get_value()`` **SHALL** return
              the currently selected ``Gdk.RGBA`` color value as
              returned by ``get_rgba()``.
:Rationale:   The ``Gdk.RGBA`` color is the meaningful value of a
              color button from the application's perspective.
:Traces to:   :ref:`PTW-SR-W-006`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Moved from the button requirements;
              corrected test references.
:Tests:       ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_do_get_value``

----

.. _PTW-GTK3-CLR-006:

PTW-GTK3-CLR-006
----------------

:Description: ``GTK3ColorButtonMixin.do_set_value()`` **SHALL**
              substitute ``Gdk.RGBA(0.0, 0.0, 0.0, 1.0)`` for a
              ``None`` value. When the resulting value is a
              ``Gdk.RGBA``, it **SHALL** store the value in
              ``dic_properties["rgba"]`` and apply it with
              ``set_rgba()``. Any other value type **SHALL** be
              delegated to the base ``do_set_value()``, which publishes
              a ``do_log_error`` message and raises ``WrongTypeError``,
              and the button color **SHALL** remain unchanged.
:Rationale:   Substituting opaque black for ``None`` provides a
              visible, predictable default color that clearly
              indicates no color has been selected.
:Traces to:   :ref:`PTW-SR-W-007`, :ref:`PTW-COM-X-008`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Moved from the button requirements;
              added storage in ``dic_properties`` and the wrong-type
              behavior; corrected test references.
:Tests:       ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_do_set_value``
              ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_do_set_value_wrong_type``
              ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_do_update``
              ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_on_changed``

----

GTK3ColorChooserDialog
======================

.. _PTW-GTK3-CLR-007:

PTW-GTK3-CLR-007
----------------

:Description: The ``GTK3ColorChooserDialog`` class **SHALL** combine
              ``Gtk.ColorChooserDialog`` and
              ``GTK3ColorChooserDialogMixin``, which derives from
              ``GTK3DialogMixin``. ``GTK3ColorChooserDialog.__init__()``
              **SHALL** accept a ``title`` parameter
              (``str | None``, default ``None``) and a
              ``transient_for`` parameter (``Gtk.Window | None``,
              default ``None``), pass both as keyword arguments to
              ``Gtk.ColorChooserDialog.__init__()``, call
              ``GTK3ColorChooserDialogMixin.__init__()``, and store
              both values in ``dic_properties``.
:Rationale:   The title and transient parent are normally known when
              the dialog is created. Storing them keeps
              ``dic_properties`` consistent with the dialog when
              ``do_set_properties()`` is later called.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/color/test_colorchooserdialog.py::TestGTK3ColorChooserDialog::test_init``
              ``tests/gtk3/color/test_colorchooserdialog.py::TestGTK3ColorChooserDialog::test_init_with_title``
              ``tests/gtk3/color/test_colorchooserdialog.py::TestGTK3ColorChooserDialog::test_init_with_transient_for``

----

.. _PTW-GTK3-CLR-008:

PTW-GTK3-CLR-008
----------------

:Description: ``GTK3ColorChooserDialogMixin.__init__()`` **SHALL** add
              ``show_editor`` (default ``False``) to
              ``dic_properties``. ``GTK3ColorChooserDialogMixin.do_set_properties()``
              **SHALL** call ``super().do_set_properties()`` first and
              then apply ``show_editor`` through
              ``set_property("show-editor", ...)``.
:Rationale:   ``show-editor`` switches the dialog between the palette
              and the custom color editor and has no dedicated setter.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/color/test_colorchooserdialog.py::TestGTK3ColorChooserDialog::test_do_set_properties_default``
              ``tests/gtk3/color/test_colorchooserdialog.py::TestGTK3ColorChooserDialog::test_do_set_properties``

----

GTK3ColorChooserWidget
======================

.. _PTW-GTK3-CLR-009:

PTW-GTK3-CLR-009
----------------

:Description: The ``GTK3ColorChooserWidget`` class **SHALL** combine
              ``Gtk.ColorChooserWidget`` and
              ``GTK3ColorChooserWidgetMixin``, which derives from
              ``GTK3BoxMixin``. ``GTK3ColorChooserWidget.__init__()``
              **SHALL** take no parameters and **SHALL** call
              ``Gtk.ColorChooserWidget.__init__()`` followed by
              ``GTK3ColorChooserWidgetMixin.__init__()``.
:Rationale:   ``Gtk.ColorChooserWidget`` is a ``Gtk.Box`` subclass;
              the box mixin supplies the inherited box and container
              configuration.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/color/test_colorchooserwidget.py::TestGTK3ColorChooserWidget::test_init``

----

.. _PTW-GTK3-CLR-010:

PTW-GTK3-CLR-010
----------------

:Description: ``GTK3ColorChooserWidgetMixin.__init__()`` **SHALL** add
              ``show_editor`` (default ``False``) to
              ``dic_properties``. ``GTK3ColorChooserWidgetMixin.do_set_properties()``
              **SHALL** call ``super().do_set_properties()`` first and
              then apply ``show_editor`` through
              ``set_property("show-editor", ...)``.
:Rationale:   ``show-editor`` switches the widget between the palette
              and the custom color editor and has no dedicated setter.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/color/test_colorchooserwidget.py::TestGTK3ColorChooserWidget::test_do_set_properties_default``
              ``tests/gtk3/color/test_colorchooserwidget.py::TestGTK3ColorChooserWidget::test_do_set_properties``
