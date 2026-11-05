.. _gtk3_font:

===============================
GTK3 Layer — Font Requirements
===============================

This document defines the software requirements for the font
wrappers in the ``pytkwrap.gtk3.font`` package: ``GTK3FontButton``,
``GTK3FontChooserDialog``, and ``GTK3FontChooserWidget``. Each concrete
wrapper composes its native ``Gtk`` class with a GTK3 mixin.

The font mixin relationships are:

.. code-block:: text

    GTK3ButtonMixin
        └── GTK3FontButtonMixin
    GTK3DialogMixin            (used directly by GTK3FontChooserDialog)
    GTK3BoxMixin               (used directly by GTK3FontChooserWidget)

All requirements in this document trace to one or more system
requirements defined in :ref:`system_requirements` and to GTK3 layer
widget requirements defined in :ref:`gtk3_widgets`.

.. contents:: Contents
   :local:
   :depth: 1

----

Package
=======

.. _PTW-GTK3-FNT-001:

PTW-GTK3-FNT-001
----------------

:Description: The ``pytkwrap.gtk3.font`` package **SHALL** export
              ``GTK3FontButton``, ``GTK3FontChooserDialog``, and
              ``GTK3FontChooserWidget`` through ``__all__``.
              Sub-modules of the package **SHALL** import sibling
              modules directly and **SHALL NOT** import through the
              package ``__init__.py``.
:Rationale:   A single public import location simplifies application
              code, while direct sibling imports avoid circular
              imports during package initialization.
:Traces to:   :ref:`PTW-SR-W-001`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       TBD

----

GTK3FontButton
==============

.. _PTW-GTK3-FNT-002:

PTW-GTK3-FNT-002
----------------

:Description: The ``GTK3FontButton`` class **SHALL** combine
              ``Gtk.FontButton`` and ``GTK3FontButtonMixin``, which
              derives from ``GTK3ButtonMixin``. ``GTK3FontButtonMixin``
              **SHALL** define ``_DEFAULT_HEIGHT`` as ``30`` and
              ``_DEFAULT_WIDTH`` as ``60``; **SHALL** set
              ``dic_attributes["default_value"]`` to ``"Sans 12"`` and
              ``dic_attributes["edit_signal"]`` to ``"font-set"``; and
              **SHALL** pre-register the ``"font-set"`` signal in
              ``dic_handler_id`` with a value of ``-1``.
:Rationale:   ``Gtk.FontButton`` is a ``Gtk.Button`` subclass and emits
              ``"font-set"`` when the user selects a font, making it
              the edit signal for publish-subscribe messaging.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-011`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-019`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/font/test_fontbutton.py::TestGTK3FontButton::test_init``
              ``tests/gtk3/font/test_fontbutton.py::TestGTK3FontButton::test_do_set_attributes_default``
              ``tests/gtk3/font/test_fontbutton.py::TestGTK3FontButton::test_do_set_attributes``

----

.. _PTW-GTK3-FNT-003:

PTW-GTK3-FNT-003
----------------

:Description: ``GTK3FontButton.__init__()`` **SHALL** accept a
              ``font_name`` parameter (default ``"Sans 12"``), pass it
              to ``Gtk.FontButton.__init__()``, call
              ``GTK3FontButtonMixin.__init__()``, and then call
              ``do_set_value(font_name)``.
:Rationale:   Applying the initial font through ``do_set_value()``
              keeps ``dic_properties["font_name"]`` consistent with the
              font shown by the button.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/font/test_fontbutton.py::TestGTK3FontButton::test_init``
              ``tests/gtk3/font/test_fontbutton.py::TestGTK3FontButton::test_init_with_font``

----

.. _PTW-GTK3-FNT-004:

PTW-GTK3-FNT-004
----------------

:Description: ``GTK3FontButtonMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``font_name``: ``"Sans 12"``
              - ``show_size``: ``True``
              - ``show_style``: ``True``
              - ``title``: ``"Pick a Font"``
              - ``use_font``: ``False``
              - ``use_size``: ``False``

              ``GTK3FontButtonMixin.do_set_properties()`` **SHALL**
              call ``super().do_set_properties()`` first and then apply
              ``font_name`` with ``set_font()`` (inherited from
              ``Gtk.FontChooser``) and ``show_size``, ``show_style``,
              ``title``, ``use_font``, and ``use_size`` with their
              corresponding ``Gtk.FontButton`` setters.
:Rationale:   These properties control how the button displays the
              selected font and the title of the chooser dialog it
              opens.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/font/test_fontbutton.py::TestGTK3FontButton::test_do_set_properties_default``
              ``tests/gtk3/font/test_fontbutton.py::TestGTK3FontButton::test_do_set_properties``

----

.. _PTW-GTK3-FNT-005:

PTW-GTK3-FNT-005
----------------

:Description: ``GTK3FontButtonMixin.do_get_value()`` **SHALL** return
              the name of the currently selected font as returned by
              ``get_font()``.
:Rationale:   The font name string (for example ``"Sans 12"``) is the
              meaningful value of a font button from the application's
              perspective.
:Traces to:   :ref:`PTW-SR-W-006`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/font/test_fontbutton.py::TestGTK3FontButton::test_do_get_value``

----

.. _PTW-GTK3-FNT-006:

PTW-GTK3-FNT-006
----------------

:Description: ``GTK3FontButtonMixin.do_set_value()`` **SHALL** delegate
              a ``bool``, ``date``, ``float``, ``int``, or ``tuple``
              value to the base ``do_set_value()``, which publishes a
              ``do_log_error`` message and raises ``WrongTypeError``.
              For any other value it **SHALL** store the value in
              ``dic_properties["font_name"]`` and apply ``str(value)``
              with ``set_font()``.
:Rationale:   Font names are strings; numeric, date, and tuple values
              cannot describe a font and are rejected.
              ``do_update()`` substitutes ``default_value`` for an
              incoming ``None`` before calling this method.
:Traces to:   :ref:`PTW-SR-W-007`, :ref:`PTW-COM-X-008`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/font/test_fontbutton.py::TestGTK3FontButton::test_do_set_value``
              ``tests/gtk3/font/test_fontbutton.py::TestGTK3FontButton::test_do_set_value_wrong_type``
              ``tests/gtk3/font/test_fontbutton.py::TestGTK3FontButton::test_do_update``
              ``tests/gtk3/font/test_fontbutton.py::TestGTK3FontButton::test_do_update_none_value``
              ``tests/gtk3/font/test_fontbutton.py::TestGTK3FontButton::test_on_changed``

----

GTK3FontChooserDialog
=====================

.. _PTW-GTK3-FNT-007:

PTW-GTK3-FNT-007
----------------

:Description: The ``GTK3FontChooserDialog`` class **SHALL** combine
              ``Gtk.FontChooserDialog`` directly with
              ``GTK3DialogMixin``. ``GTK3FontChooserDialog.__init__()``
              **SHALL** accept a ``title`` parameter (``str | None``,
              default ``"Choose a Font"``) and a ``transient_for``
              parameter (``Gtk.Window | None``, default ``None``) and
              pass both as keyword arguments to
              ``Gtk.FontChooserDialog.__init__()``. It **SHALL** then
              call ``GTK3DialogMixin.__init__()``, store ``title`` and
              ``transient_for`` in ``dic_properties``, and call
              ``do_set_properties(dic_properties)``.
:Rationale:   Storing the title and parent before applying the
              properties ensures the window mixin re-applies the
              supplied values rather than its own defaults.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`, :ref:`PTW-GTK3-DLG-003`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/font/test_fontchooserdialog.py::TestGTK3FontChooserDialog::test_init``
              ``tests/gtk3/font/test_fontchooserdialog.py::TestGTK3FontChooserDialog::test_init_with_title``
              ``tests/gtk3/font/test_fontchooserdialog.py::TestGTK3FontChooserDialog::test_init_with_transient_for``
              ``tests/gtk3/font/test_fontchooserdialog.py::TestGTK3FontChooserDialog::test_do_set_properties_default``
              ``tests/gtk3/font/test_fontchooserdialog.py::TestGTK3FontChooserDialog::test_do_set_properties``

----

GTK3FontChooserWidget
=====================

.. _PTW-GTK3-FNT-008:

PTW-GTK3-FNT-008
----------------

:Description: The ``GTK3FontChooserWidget`` class **SHALL** combine
              ``Gtk.FontChooserWidget`` directly with
              ``GTK3BoxMixin``. ``GTK3FontChooserWidget.__init__()``
              **SHALL** take no parameters and **SHALL** call
              ``Gtk.FontChooserWidget.__init__()`` followed by
              ``GTK3BoxMixin.__init__()``.
:Rationale:   ``Gtk.FontChooserWidget`` is a ``Gtk.Box`` subclass that
              can be embedded in other containers; its font chooser API
              is available directly from the native class.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-BC-024`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/font/test_fontchooserwidget.py::TestGTK3FontChooserWidget::test_init``
              ``tests/gtk3/font/test_fontchooserwidget.py::TestGTK3FontChooserWidget::test_do_set_properties_default``
              ``tests/gtk3/font/test_fontchooserwidget.py::TestGTK3FontChooserWidget::test_do_set_properties``
