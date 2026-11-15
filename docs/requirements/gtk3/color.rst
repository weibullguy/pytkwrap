.. _gtk3_color:

===============================
GTK3 Layer — Color Requirements
===============================

This document defines the software requirements for the wrappers in the ``pytkwrap.gtk3.color`` package.

All requirements in this document trace to one or more system requirements defined in :ref:`system_requirements` and to GTK3 layer widget requirements defined in :ref:`gtk3_widgets`.

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
              ``GTK3ColorButton``, ``GTK3ColorChooserDialog``,
              ``GTK3ColorChooserWidget``, ``_ColorButtonHost``,
              ``_ColorChooserDialogHost``, and
              ``_ColorChooserWidgetHost`` through ``__all__``.
              Sub-modules of the package **SHALL** import sibling
              modules directly and **SHALL NOT** import through the
              package ``__init__.py``.
:Rationale:   A single public import location simplifies application
              code, while direct sibling imports avoid circular imports
              during package initialization.
:Traces to:   :ref:`PTW-SR-W-001`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       TBD

----

GTK3ColorButton
===============

.. _PTW-GTK3-CLR-002:

PTW-GTK3-CLR-002
----------------

:Description: The ``GTK3ColorButton`` class **SHALL** combine
              ``Gtk.ColorButton`` and ``GTK3ColorButtonMixin``, which
              derives from ``GTK3ButtonMixin``.
              ``GTK3ColorButton.__init__()`` **SHALL** accept ``rgba:
              Gdk.RGBA | None = None`` and **SHALL**:

              - ``rgba = Gdk.RGBA()`` only if rgba is None
              - ``Gtk.ColorButton.__init__(self, rgba=rgba)``
              - ``GTK3ColorButtonMixin.__init__(self)``
              - ``dic_properties["rgba"] = rgba``
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_init``
              ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_init_with_rgba``

----

.. _PTW-GTK3-CLR-003:

PTW-GTK3-CLR-003
----------------

:Description: ``GTK3ColorButtonMixin`` **SHALL** define
              ``_DEFAULT_HEIGHT`` as ``30``, ``_DEFAULT_WIDTH`` as
              ``60``; **SHALL** set ``dic_attributes["default_value"]``
              to ``None``, ``dic_attributes["edit_signal"]`` to
              ``"color-set"``; **SHALL** pre-register ``"color-set"`` in
              ``dic_handler_id`` with a value of ``-1``.
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-005`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-019`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_do_set_attributes``
              ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_do_set_attributes_default``
              ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_do_set_attributes_partial``
              ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_init``

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

              ``GTK3ColorButtonMixin.do_set_properties()`` **SHALL**, in
              order:

              - ``super().do_set_properties(properties)``
              - ``set_rgba(rgba)`` only if rgba is not None
              - ``set_title(title)``
              - ``set_property("show-editor", show_editor)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_do_set_properties``
              ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_do_set_properties_default``

----

.. _PTW-GTK3-CLR-005:

PTW-GTK3-CLR-005
----------------

:Description: The ``GTK3ColorButtonMixin.do_get_value()`` method
              **SHALL** TBD. (Return the current value of the
              GTK3ColorButton.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-006`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_do_get_value``
              ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_do_get_value_missing``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def do_get_value(self: _ColorButtonHost) -> bool | date | float | int | object | str | None:
       return self.get_rgba()

----

.. _PTW-GTK3-CLR-006:

PTW-GTK3-CLR-006
----------------

:Description: The ``GTK3ColorButtonMixin.do_set_value()`` method
              **SHALL** TBD. (Set the current value of the
              GTK3ColorButton.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-007`, :ref:`PTW-COM-X-008`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_do_set_value``
              ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_do_set_value_wrong_type``
              ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_do_update``
              ``tests/gtk3/color/test_colorbutton.py::TestGTK3ColorButton::test_on_changed``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def do_set_value(self: _ColorButtonHost, value: bool | date | float | int | object | str | tuple | None) -> None:
       if value is None:
           value = Gdk.RGBA(0.0, 0.0, 0.0, 1.0)
       if not isinstance(value, Gdk.RGBA):
           super().do_set_value(value)
           return
       self.dic_properties['rgba'] = value
       self.set_rgba(value)

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
              **SHALL** accept ``title: str = ''``, ``transient_for:
              Gtk.Window | None = None`` and **SHALL**:

              - ``Gtk.ColorChooserDialog.__init__(self, title=title,
                transient_for=transient_for)``
              - ``GTK3ColorChooserDialogMixin.__init__(self)``
              - ``dic_properties["title"] = title``
              - ``dic_properties["transient_for"] = transient_for``
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/color/test_colorchooserdialog.py::TestGTK3ColorChooserDialog::test_init``
              ``tests/gtk3/color/test_colorchooserdialog.py::TestGTK3ColorChooserDialog::test_init_with_title``
              ``tests/gtk3/color/test_colorchooserdialog.py::TestGTK3ColorChooserDialog::test_init_with_transient_for``

----

.. _PTW-GTK3-CLR-008:

PTW-GTK3-CLR-008
----------------

:Description: ``GTK3ColorChooserDialogMixin.__init__()`` **SHALL** add
              the following properties to ``dic_properties``:

              - ``show_editor``: ``False``

              ``GTK3ColorChooserDialogMixin.do_set_properties()``
              **SHALL**, in order:

              - ``super().do_set_properties(properties)``
              - ``set_property("show-editor", show_editor)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/color/test_colorchooserdialog.py::TestGTK3ColorChooserDialog::test_do_set_properties``
              ``tests/gtk3/color/test_colorchooserdialog.py::TestGTK3ColorChooserDialog::test_do_set_properties_default``

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
              **SHALL** accept no parameters and **SHALL**:

              - ``Gtk.ColorChooserWidget.__init__(self)``
              - ``GTK3ColorChooserWidgetMixin.__init__(self)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/color/test_colorchooserwidget.py::TestGTK3ColorChooserWidget::test_init``

----

.. _PTW-GTK3-CLR-010:

PTW-GTK3-CLR-010
----------------

:Description: ``GTK3ColorChooserWidgetMixin.__init__()`` **SHALL** add
              the following properties to ``dic_properties``:

              - ``show_editor``: ``False``

              ``GTK3ColorChooserWidgetMixin.do_set_properties()``
              **SHALL**, in order:

              - ``super().do_set_properties(properties)``
              - ``set_property("show-editor", show_editor)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/color/test_colorchooserwidget.py::TestGTK3ColorChooserWidget::test_do_set_properties``
              ``tests/gtk3/color/test_colorchooserwidget.py::TestGTK3ColorChooserWidget::test_do_set_properties_default``
