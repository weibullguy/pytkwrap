.. _gtk3_dialog:

=================================
GTK3 Layer — Dialog Requirements
=================================

This document defines the software requirements for the dialog
wrappers in the ``pytkwrap.gtk3.dialog`` package: ``GTK3Dialog``,
``GTK3AboutDialog``, ``GTK3AppChooserDialog``, ``GTK3MessageDialog``,
and ``GTK3NativeDialog``. Each concrete wrapper composes its native
``Gtk`` class with a GTK3 mixin.

The dialog mixin hierarchy is:

.. code-block:: text

    GTK3WindowMixin
        └── GTK3DialogMixin
                ├── GTK3AboutDialogMixin
                ├── GTK3AppChooserDialogMixin
                └── GTK3MessageDialogMixin
    GTK3GObjectMixin
        └── GTK3NativeDialogMixin

All requirements in this document trace to one or more system
requirements defined in :ref:`system_requirements` and to GTK3 layer
widget requirements defined in :ref:`gtk3_widgets`.

.. contents:: Contents
   :local:
   :depth: 1

----

Package
=======

.. _PTW-GTK3-DLG-001:

PTW-GTK3-DLG-001
----------------

:Description: The ``pytkwrap.gtk3.dialog`` package **SHALL** export
              ``GTK3AboutDialog``, ``GTK3AppChooserDialog``,
              ``GTK3Dialog``, ``GTK3MessageDialog``, and
              ``GTK3NativeDialog`` through ``__all__``. Sub-modules of
              the package **SHALL** import sibling modules directly and
              **SHALL NOT** import through the package ``__init__.py``.
:Rationale:   A single public import location simplifies application
              code, while direct sibling imports avoid circular
              imports during package initialization.
:Traces to:   :ref:`PTW-SR-W-001`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       TBD

----

GTK3Dialog
==========

.. _PTW-GTK3-DLG-002:

PTW-GTK3-DLG-002
----------------

:Description: The ``GTK3Dialog`` class **SHALL** combine ``Gtk.Dialog``
              and ``GTK3DialogMixin``, which derives from
              ``GTK3WindowMixin``. ``GTK3Dialog.__init__()`` **SHALL**
              accept a ``use_header_bar`` parameter (``bool``, default
              ``False``), pass it to ``Gtk.Dialog.__init__()``, and then
              call ``GTK3DialogMixin.__init__()``.
:Rationale:   ``Gtk.Dialog`` is a ``Gtk.Window`` subclass, so dialogs
              reuse the window mixin's properties and signals.
              ``use-header-bar`` is a construct-only property and must
              be supplied when the dialog is created.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/dialog/test_dialog.py::TestGTK3Dialog::test_init``
              ``tests/gtk3/dialog/test_dialog.py::TestGTK3Dialog::test_init_with_header_bar``

----

.. _PTW-GTK3-DLG-003:

PTW-GTK3-DLG-003
----------------

:Description: ``GTK3DialogMixin.__init__()`` **SHALL** pre-register the
              ``"close"`` and ``"response"`` signals in
              ``dic_handler_id`` with a value of ``-1`` and **SHALL**
              add ``use_header_bar`` (default ``-1``) to
              ``dic_properties``. ``GTK3DialogMixin`` **SHALL NOT**
              override ``do_set_properties()``; dialog configuration is
              applied by ``GTK3WindowMixin``.
:Rationale:   ``"response"`` is the primary signal applications use to
              learn which dialog button was activated. Because
              ``use-header-bar`` is construct-only, it is recorded but
              not applied after construction.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/dialog/test_dialog.py::TestGTK3Dialog::test_init``
              ``tests/gtk3/dialog/test_dialog.py::TestGTK3Dialog::test_do_set_properties_default``
              ``tests/gtk3/dialog/test_dialog.py::TestGTK3Dialog::test_do_set_properties``

----

GTK3AboutDialog
===============

.. _PTW-GTK3-DLG-004:

PTW-GTK3-DLG-004
----------------

:Description: The ``GTK3AboutDialog`` class **SHALL** combine
              ``Gtk.AboutDialog`` and ``GTK3AboutDialogMixin``, which
              derives from ``GTK3DialogMixin``.
              ``GTK3AboutDialog.__init__()`` **SHALL** take no
              parameters and **SHALL** call
              ``Gtk.AboutDialog.__init__()`` followed by
              ``GTK3AboutDialogMixin.__init__()``.
              ``GTK3AboutDialogMixin`` **SHALL** pre-register the
              ``"activate-link"`` signal in ``dic_handler_id`` with a
              value of ``-1``.
:Rationale:   ``"activate-link"`` lets applications intercept links
              shown in the dialog, such as the website or license
              links.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-017`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/dialog/test_aboutdialog.py::TestGTK3AboutDialog::test_init``

----

.. _PTW-GTK3-DLG-005:

PTW-GTK3-DLG-005
----------------

:Description: ``GTK3AboutDialogMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``artists``: ``[]``
              - ``authors``: ``[]``
              - ``comments``: ``None``
              - ``copyright``: ``None``
              - ``documenters``: ``[]``
              - ``license``: ``None``
              - ``license_type``: ``Gtk.License.UNKNOWN``
              - ``logo``: ``None``
              - ``logo_icon_name``: ``"image-missing"``
              - ``program_name``: ``None``
              - ``translator_credits``: ``None``
              - ``version``: ``None``
              - ``website``: ``None``
              - ``website_label``: ``None``
              - ``wrap_license``: ``False``

:Rationale:   These properties describe the application shown in the
              about dialog and can all be configured through the typed
              dictionary interface.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/dialog/test_aboutdialog.py::TestGTK3AboutDialog::test_init``
              ``tests/gtk3/dialog/test_aboutdialog.py::TestGTK3AboutDialog::test_do_set_properties_default``

----

.. _PTW-GTK3-DLG-006:

PTW-GTK3-DLG-006
----------------

:Description: ``GTK3AboutDialogMixin.do_set_properties()`` **SHALL**
              call ``super().do_set_properties()`` first and then apply
              the about-dialog properties through their corresponding
              ``Gtk.AboutDialog`` setters in this order: ``artists``,
              ``authors``, ``comments``, ``copyright``,
              ``documenters``, ``license``, ``license_type``, ``logo``,
              ``logo_icon_name``, ``program_name``,
              ``translator_credits``, ``version``, ``website``,
              ``website_label``, and ``wrap_license``.
              ``set_program_name()`` **SHALL** be called only when
              ``program_name`` is not ``None``, and
              ``set_website_label()`` only when ``website_label`` is
              not ``None``.
:Rationale:   Skipping ``None`` for the program name and website label
              preserves GTK's defaults (the application name and the
              website URL).
:Traces to:   :ref:`PTW-SR-W-004`, :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/dialog/test_aboutdialog.py::TestGTK3AboutDialog::test_do_set_properties``

----

GTK3AppChooserDialog
====================

.. _PTW-GTK3-DLG-007:

PTW-GTK3-DLG-007
----------------

:Description: The ``GTK3AppChooserDialog`` class **SHALL** combine
              ``Gtk.AppChooserDialog`` and
              ``GTK3AppChooserDialogMixin``, which derives from
              ``GTK3DialogMixin``. ``GTK3AppChooserDialog.__init__()``
              **SHALL** accept a required ``transient_for`` parameter
              (``Gtk.Window | None``), a required ``flags`` parameter
              (``Gtk.DialogFlags``), and an optional ``gfile`` parameter
              (``Gio.File | None``, default ``None``). It **SHALL**
              pass all three as keyword arguments to
              ``Gtk.AppChooserDialog.__init__()``, call
              ``GTK3AppChooserDialogMixin.__init__()``, and store
              ``gfile`` in ``dic_properties["gfile"]``.
:Rationale:   The file whose applications are offered is a
              construct-only property and must be supplied when the
              dialog is created.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/dialog/test_appchooserdialog.py::TestGTK3AppChooserDialog::test_init``
              ``tests/gtk3/dialog/test_appchooserdialog.py::TestGTK3AppChooserDialog::test_init_with_gfile``

----

.. _PTW-GTK3-DLG-008:

PTW-GTK3-DLG-008
----------------

:Description: ``GTK3AppChooserDialogMixin.__init__()`` **SHALL** add
              ``gfile`` (default ``None``) and ``heading`` (default
              ``None``) to ``dic_properties``.
              ``GTK3AppChooserDialogMixin.do_set_properties()``
              **SHALL** call ``super().do_set_properties()`` first and
              then call ``set_heading()`` only when ``heading`` is not
              ``None``. It **SHALL NOT** apply ``gfile``.
:Rationale:   ``gfile`` is construct-only, so it is recorded for
              inspection but cannot be changed after construction.
              Skipping a ``None`` heading preserves GTK's default
              heading.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/dialog/test_appchooserdialog.py::TestGTK3AppChooserDialog::test_do_set_properties_default``
              ``tests/gtk3/dialog/test_appchooserdialog.py::TestGTK3AppChooserDialog::test_do_set_properties``

----

GTK3MessageDialog
=================

.. _PTW-GTK3-DLG-009:

PTW-GTK3-DLG-009
----------------

:Description: The ``GTK3MessageDialog`` class **SHALL** combine
              ``Gtk.MessageDialog`` and ``GTK3MessageDialogMixin``,
              which derives from ``GTK3DialogMixin``.
              ``GTK3MessageDialog.__init__()`` **SHALL** accept a
              ``buttons`` parameter (default ``Gtk.ButtonsType.NONE``)
              and a ``message_type`` parameter (default
              ``Gtk.MessageType.INFO``) and pass both as keyword
              arguments to ``Gtk.MessageDialog.__init__()``. It
              **SHALL** then call ``Gtk.Widget.set_has_window(self,
              False)``, call ``GTK3MessageDialogMixin.__init__()``, and
              store ``buttons`` and ``message_type`` in
              ``dic_properties``.
:Rationale:   ``buttons`` is a construct-only property, so the button
              set must be chosen when the dialog is created.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/dialog/test_messagedialog.py::TestGTK3MessageDialog::test_init``
              ``tests/gtk3/dialog/test_messagedialog.py::TestGTK3MessageDialog::test_init_with_buttons``
              ``tests/gtk3/dialog/test_messagedialog.py::TestGTK3MessageDialog::test_init_with_message_type``

----

.. _PTW-GTK3-DLG-010:

PTW-GTK3-DLG-010
----------------

:Description: ``GTK3MessageDialogMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``buttons``: ``Gtk.ButtonsType.NONE``
              - ``message_area``: ``None``
              - ``message_type``: ``Gtk.MessageType.INFO``
              - ``secondary_text``: ``None``
              - ``secondary_use_markup``: ``False``
              - ``text``: ``""``
              - ``use_markup``: ``False``

:Rationale:   These properties describe the message shown in the
              dialog and can be configured through the typed
              dictionary interface.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/dialog/test_messagedialog.py::TestGTK3MessageDialog::test_init``
              ``tests/gtk3/dialog/test_messagedialog.py::TestGTK3MessageDialog::test_do_set_properties_default``

----

.. _PTW-GTK3-DLG-011:

PTW-GTK3-DLG-011
----------------

:Description: ``GTK3MessageDialogMixin.do_set_properties()`` **SHALL**
              call ``super().do_set_properties()`` first. When
              ``use_markup`` is true, it **SHALL** call
              ``set_markup()`` with ``text``. It **SHALL** then apply
              ``message_type``, ``secondary_text``,
              ``secondary_use_markup``, and ``use_markup`` through
              ``set_property()`` using their hyphenated GObject
              property names. It **SHALL NOT** apply ``buttons`` or
              ``message_area``.
:Rationale:   ``buttons`` is construct-only and ``message_area`` is
              read-only, so neither can be applied after construction.
:Traces to:   :ref:`PTW-SR-W-004`, :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/dialog/test_messagedialog.py::TestGTK3MessageDialog::test_do_set_properties``

----

GTK3NativeDialog
================

.. _PTW-GTK3-DLG-012:

PTW-GTK3-DLG-012
----------------

:Description: The ``GTK3NativeDialog`` class **SHALL** combine
              ``Gtk.NativeDialog`` and ``GTK3NativeDialogMixin``, which
              derives from ``GTK3GObjectMixin`` rather than a widget
              mixin. ``GTK3NativeDialog.__init__()`` **SHALL** take no
              parameters and **SHALL** call
              ``Gtk.NativeDialog.__init__()`` followed by
              ``GTK3NativeDialogMixin.__init__()``.
              ``GTK3NativeDialogMixin`` **SHALL** pre-register the
              ``"response"`` signal in ``dic_handler_id`` with a value
              of ``-1``.
:Rationale:   ``Gtk.NativeDialog`` is a ``GObject.Object``, not a
              ``Gtk.Widget``; it wraps a platform-native dialog, so
              widget properties and signals do not apply.
:Traces to:   :ref:`PTW-GTK3-X-001`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-017`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/dialog/test_nativedialog.py::TestGTK3NativeDialog::test_init``

----

.. _PTW-GTK3-DLG-013:

PTW-GTK3-DLG-013
----------------

:Description: ``GTK3NativeDialogMixin.__init__()`` **SHALL** set
              ``dic_properties`` to the following native-dialog
              properties:

              - ``modal``: ``False``
              - ``title``: ``None``
              - ``transient_for``: ``None``
              - ``visible``: ``False``

              ``GTK3NativeDialogMixin.do_set_properties()`` **SHALL**
              call ``super().do_set_properties()`` first, apply
              ``modal`` with ``set_modal()`` and ``transient_for`` with
              ``set_transient_for()``, call ``set_title()`` only when
              ``title`` is not ``None``, and call ``show()`` only when
              ``visible`` is true.
:Rationale:   These are the properties ``Gtk.NativeDialog`` defines.
              Showing the dialog when ``visible`` is true lets the
              dialog be configured and presented in one call.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/dialog/test_nativedialog.py::TestGTK3NativeDialog::test_init``
              ``tests/gtk3/dialog/test_nativedialog.py::TestGTK3NativeDialog::test_do_set_properties_default``
              ``tests/gtk3/dialog/test_nativedialog.py::TestGTK3NativeDialog::test_do_set_properties``
