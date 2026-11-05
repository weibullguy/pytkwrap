.. _gtk3_file:

===============================
GTK3 Layer — File Requirements
===============================

This document defines the software requirements for the file
management wrappers in the ``pytkwrap.gtk3.file`` package:
``GTK3FileChooserButton``, ``GTK3FileChooserDialog``,
``GTK3FileChooserNative``, ``GTK3FileChooserWidget``,
``GTK3FileFilter``, ``GTK3RecentChooserDialog``, ``GTK3RecentFilter``,
and ``GTK3RecentManager``. Each concrete wrapper composes its native
``Gtk`` class with a GTK3 mixin.

The file mixin relationships are:

.. code-block:: text

    GTK3BoxMixin
        ├── GTK3FileChooserButtonMixin
        └── GTK3FileChooserWidgetMixin
    GTK3DialogMixin            (used directly by GTK3FileChooserDialog
                                and GTK3RecentChooserDialog)
    GTK3NativeDialogMixin
        └── GTK3FileChooserNativeMixin
    GTK3GObjectMixin           (used directly by GTK3FileFilter and
        │                       GTK3RecentFilter)
        └── GTK3RecentManagerMixin

All requirements in this document trace to one or more system
requirements defined in :ref:`system_requirements` and to GTK3 layer
widget requirements defined in :ref:`gtk3_widgets`.

.. contents:: Contents
   :local:
   :depth: 1

----

Package
=======

.. _PTW-GTK3-FIL-001:

PTW-GTK3-FIL-001
----------------

:Description: The ``pytkwrap.gtk3.file`` package **SHALL** export
              ``GTK3FileChooserButton``, ``GTK3FileChooserDialog``,
              ``GTK3FileChooserNative``, ``GTK3FileChooserWidget``,
              ``GTK3FileFilter``, ``GTK3RecentChooserDialog``,
              ``GTK3RecentFilter``, and ``GTK3RecentManager`` through
              ``__all__``. Sub-modules of the package **SHALL** import
              sibling modules directly and **SHALL NOT** import through
              the package ``__init__.py``.
:Rationale:   A single public import location simplifies application
              code, while direct sibling imports avoid circular
              imports during package initialization.
:Traces to:   :ref:`PTW-SR-W-001`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       TBD

----

GTK3FileChooserButton
=====================

.. note::

   The ``GTK3FileChooserButton`` tests crash at the C level when run
   as part of the full test suite, because of GIO volume monitor
   initialization conflicts. They pass in isolation and are skipped
   unless pytest is run with ``--isolated``.

.. _PTW-GTK3-FIL-002:

PTW-GTK3-FIL-002
----------------

:Description: The ``GTK3FileChooserButton`` class **SHALL** combine
              ``Gtk.FileChooserButton`` and
              ``GTK3FileChooserButtonMixin``, which derives from
              ``GTK3BoxMixin``. ``GTK3FileChooserButtonMixin`` **SHALL**
              pre-register the ``"file-set"`` signal in
              ``dic_handler_id`` with a value of ``-1``.
:Rationale:   ``Gtk.FileChooserButton`` is a ``Gtk.Box`` subclass, so
              the box mixin supplies its inherited configuration.
              ``Gtk.FileChooserButton`` emits ``"file-set"`` when the
              user selects a file.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-017`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-05) - Moved from ``button.rst`` (formerly
              PTW-GTK3-B-015). Revised to match the implementation:
              added the base mixin; ``"file-set"`` is registered as a
              signal but is not configured as an ``edit_signal``.
              Corrected the test note and traces.
:Tests:       ``tests/gtk3/file/test_filechooserbutton.py::TestGTK3FileChooserButton::test_init``

----

.. _PTW-GTK3-FIL-003:

PTW-GTK3-FIL-003
----------------

:Description: ``GTK3FileChooserButton.__init__()`` **SHALL** accept a
              ``title`` parameter (default ``"Select a File"``), an
              ``action`` parameter (default
              ``Gtk.FileChooserAction.OPEN``), and a ``dialog``
              parameter (``Gtk.Dialog | None``, default ``None``). It
              **SHALL** pass all three as keyword arguments to
              ``Gtk.FileChooserButton.__init__()``, call
              ``GTK3FileChooserButtonMixin.__init__()``, store
              ``dialog`` and ``title`` in ``dic_properties``, and then
              call ``set_action(action)``.
:Rationale:   The chooser dialog is a construct-only property and the
              action and title are normally known when the button is
              created.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/file/test_filechooserbutton.py::TestGTK3FileChooserButton::test_init``
              ``tests/gtk3/file/test_filechooserbutton.py::TestGTK3FileChooserButton::test_init_with_action``
              ``tests/gtk3/file/test_filechooserbutton.py::TestGTK3FileChooserButton::test_init_with_dialog``
              ``tests/gtk3/file/test_filechooserbutton.py::TestGTK3FileChooserButton::test_init_with_title``

----

.. _PTW-GTK3-FIL-004:

PTW-GTK3-FIL-004
----------------

:Description: ``GTK3FileChooserButtonMixin.__init__()`` **SHALL** add
              the following properties to ``dic_properties``:

              - ``dialog``: ``None``
              - ``title``: ``"Select a File"``
              - ``width_chars``: ``-1``

              ``GTK3FileChooserButtonMixin.do_set_properties()``
              **SHALL** call ``super().do_set_properties()`` first and
              then apply ``title`` with ``set_title()`` and
              ``width_chars`` with ``set_width_chars()``. It **SHALL
              NOT** apply ``dialog``.
:Rationale:   ``dialog`` is construct-only, so it is recorded for
              inspection but cannot be changed after construction.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/file/test_filechooserbutton.py::TestGTK3FileChooserButton::test_do_set_properties_default``
              ``tests/gtk3/file/test_filechooserbutton.py::TestGTK3FileChooserButton::test_do_set_properties``

----

.. _PTW-GTK3-FIL-005:

PTW-GTK3-FIL-005
----------------

:Description: The ``GTK3FileChooserButton.do_get_value()`` method
              **SHALL** return the selected file or folder based on
              the widget's ``action`` property and ``default``
              attribute as follows:

              - If ``default`` is ``"gio"``: return a ``Gio.File``
                object or a list of ``Gio.File`` objects if
                ``select_multiple`` is ``True``.
              - If ``default`` is ``"uri"``: return a URI string or
                a list of URI strings if ``select_multiple`` is
                ``True``.
              - Otherwise (default ``"path"``): return an absolute
                path string, a list of absolute path strings if
                ``select_multiple`` is ``True``, or the current
                folder path if the action is ``SELECT_FOLDER`` or
                ``CREATE_FOLDER``.

:Rationale:   Different use cases require different representations
              of the selected file. The ``default`` attribute
              provides a consistent mechanism for configuring the
              return type without requiring subclassing.
:Traces to:   :ref:`PTW-SR-W-006`
:Status:      Planned
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-05) - Moved from ``button.rst`` (formerly
              PTW-GTK3-B-016). Status changed to Planned because the
              method is not implemented.
:Tests:       TBD

----

.. _PTW-GTK3-FIL-006:

PTW-GTK3-FIL-006
----------------

:Description: The ``GTK3FileChooserButton.do_set_value()`` method
              **SHALL** set the selected file or folder based on the
              widget's ``action`` property and ``default`` attribute.
              For path-based values, ``file_exists()`` and
              ``dir_exists()`` **SHALL** be used to determine the
              appropriate GTK3 setter method. If no valid path is
              provided for folder actions, the home directory
              **SHALL** be used as the fallback.
:Rationale:   The appropriate GTK3 setter method depends on whether
              the file or folder exists and what action the chooser
              is configured for. Using the utility functions
              ``file_exists()`` and ``dir_exists()`` ensures
              consistent path validation behavior.
:Traces to:   :ref:`PTW-SR-W-007`, :ref:`PTW-COM-U-012`,
              :ref:`PTW-COM-U-013`, :ref:`PTW-COM-U-014`
:Status:      Planned
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-05) - Moved from ``button.rst`` (formerly
              PTW-GTK3-B-017). Status changed to Planned because the
              method is not implemented.
:Tests:       TBD

----

GTK3FileChooserDialog
=====================

.. _PTW-GTK3-FIL-007:

PTW-GTK3-FIL-007
----------------

:Description: The ``GTK3FileChooserDialog`` class **SHALL** combine
              ``Gtk.FileChooserDialog`` directly with
              ``GTK3DialogMixin``. ``GTK3FileChooserDialog.__init__()``
              **SHALL** take no parameters and **SHALL** call
              ``Gtk.FileChooserDialog.__init__()`` followed by
              ``GTK3DialogMixin.__init__()``.
:Rationale:   The file chooser dialog adds no pytkwrap configuration
              beyond the dialog mixin; its file chooser API is
              available directly from ``Gtk.FileChooserDialog``.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-DLG-003`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/file/test_filechooserdialog.py::TestGTK3FileChooserDialog::test_init``
              ``tests/gtk3/file/test_filechooserdialog.py::TestGTK3FileChooserDialog::test_do_set_properties_default``

----

GTK3FileChooserNative
=====================

.. _PTW-GTK3-FIL-008:

PTW-GTK3-FIL-008
----------------

:Description: The ``GTK3FileChooserNative`` class **SHALL** combine
              ``Gtk.FileChooserNative`` and
              ``GTK3FileChooserNativeMixin``, which derives from
              ``GTK3NativeDialogMixin``.
              ``GTK3FileChooserNative.__init__()`` **SHALL** accept
              ``title`` (``str | None``, default ``None``), ``action``
              (default ``Gtk.FileChooserAction.OPEN``),
              ``accept_label`` (``str | None``, default ``None``), and
              ``cancel_label`` (``str | None``, default ``None``)
              parameters, pass all four as keyword arguments to
              ``Gtk.FileChooserNative.__init__()``, call
              ``GTK3FileChooserNativeMixin.__init__()``, and store
              ``accept_label``, ``cancel_label``, and ``title`` in
              ``dic_properties``.
:Rationale:   ``Gtk.FileChooserNative`` presents the platform's native
              file chooser and is a ``Gtk.NativeDialog``, not a
              widget.
:Traces to:   :ref:`PTW-GTK3-X-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-DLG-012`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/file/test_filechoosernative.py::TestGTK3FileChooserNative::test_init``
              ``tests/gtk3/file/test_filechoosernative.py::TestGTK3FileChooserNative::test_init_with_title``
              ``tests/gtk3/file/test_filechoosernative.py::TestGTK3FileChooserNative::test_init_with_action``
              ``tests/gtk3/file/test_filechoosernative.py::TestGTK3FileChooserNative::test_init_with_accept_label``
              ``tests/gtk3/file/test_filechoosernative.py::TestGTK3FileChooserNative::test_init_with_cancel_label``

----

.. _PTW-GTK3-FIL-009:

PTW-GTK3-FIL-009
----------------

:Description: ``GTK3FileChooserNativeMixin.__init__()`` **SHALL** add
              ``accept_label`` (default ``None``) and ``cancel_label``
              (default ``None``) to ``dic_properties``.
              ``GTK3FileChooserNativeMixin.do_set_properties()``
              **SHALL** call ``super().do_set_properties()`` first and
              then apply them with ``set_accept_label()`` and
              ``set_cancel_label()``.
:Rationale:   ``None`` restores the platform's default button labels.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/file/test_filechoosernative.py::TestGTK3FileChooserNative::test_do_set_properties_default``
              ``tests/gtk3/file/test_filechoosernative.py::TestGTK3FileChooserNative::test_do_set_properties``

----

GTK3FileChooserWidget
=====================

.. _PTW-GTK3-FIL-010:

PTW-GTK3-FIL-010
----------------

:Description: The ``GTK3FileChooserWidget`` class **SHALL** combine
              ``Gtk.FileChooserWidget`` and
              ``GTK3FileChooserWidgetMixin``, which derives from
              ``GTK3BoxMixin``. ``GTK3FileChooserWidget.__init__()``
              **SHALL** accept an ``action`` parameter (default
              ``Gtk.FileChooserAction.OPEN``), pass it to
              ``Gtk.FileChooserWidget.__init__()``, and then call
              ``GTK3FileChooserWidgetMixin.__init__()``.
              ``GTK3FileChooserWidgetMixin`` **SHALL** pre-register the
              following signals in ``dic_handler_id`` with a value of
              ``-1``:

              - ``"desktop-folder"``
              - ``"down-folder"``
              - ``"home-folder"``
              - ``"location-popup"``
              - ``"location-popup-on-paste"``
              - ``"location-toggle-popup"``
              - ``"places-shortcut"``
              - ``"quick-bookmark"``
              - ``"recent-shortcut"``
              - ``"search-shortcut"``
              - ``"show-hidden"``
              - ``"up-folder"``

:Rationale:   ``Gtk.FileChooserWidget`` is a ``Gtk.Box`` subclass that
              can be embedded in other containers; its keybinding
              signals are made available to ``do_set_callbacks()``.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-017`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/file/test_filechooserwidget.py::TestGTK3FileChooserWidget::test_init``
              ``tests/gtk3/file/test_filechooserwidget.py::TestGTK3FileChooserWidget::test_init_with_action``

----

.. _PTW-GTK3-FIL-011:

PTW-GTK3-FIL-011
----------------

:Description: ``GTK3FileChooserWidgetMixin.__init__()`` **SHALL** add
              ``search_mode`` (default ``False``) to
              ``dic_properties``. ``GTK3FileChooserWidgetMixin.do_set_properties()``
              **SHALL** call ``super().do_set_properties()`` first and
              then apply ``search_mode`` through
              ``set_property("search-mode", ...)``.
:Rationale:   ``search-mode`` has no dedicated setter in
              ``Gtk.FileChooserWidget``.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/file/test_filechooserwidget.py::TestGTK3FileChooserWidget::test_do_set_properties_default``
              ``tests/gtk3/file/test_filechooserwidget.py::TestGTK3FileChooserWidget::test_do_set_properties``

----

GTK3FileFilter
==============

.. _PTW-GTK3-FIL-012:

PTW-GTK3-FIL-012
----------------

:Description: The ``GTK3FileFilter`` class **SHALL** combine
              ``Gtk.FileFilter`` directly with ``GTK3GObjectMixin``.
              ``GTK3FileFilter.__init__()`` **SHALL** take no
              parameters and **SHALL** call
              ``Gtk.FileFilter.__init__()`` followed by
              ``GTK3GObjectMixin.__init__()``.
:Rationale:   ``Gtk.FileFilter`` is a ``GObject``-derived object rather
              than a widget, so widget properties and signals do not
              apply.
:Traces to:   :ref:`PTW-GTK3-X-001`, :ref:`PTW-GTK3-W-017`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/file/test_filefilter.py::TestGTK3FileFilter::test_init``

----

.. _PTW-GTK3-FIL-013:

PTW-GTK3-FIL-013
----------------

:Description: ``GTK3FileFilter.do_set_filter()`` **SHALL** accept
              optional keyword arguments ``mime_types``
              (``list[str] | None``), ``patterns``
              (``list[str] | None``), ``needed``
              (``Gtk.FileFilterFlags | None``), and ``func``
              (``Callable | None``), plus positional ``*data`` for the
              custom filter function. It **SHALL** add exactly one kind
              of rule, chosen in this order of preference:

              - when ``mime_types`` is not ``None``, add each MIME type
                with ``add_mime_type()``;
              - otherwise, when ``patterns`` is not ``None``, add each
                pattern with ``add_pattern()``;
              - otherwise, when ``func`` is not ``None``, call
                ``add_custom(needed, func, *data)``.

:Rationale:   A single method configures the most common filter
              rules. The documented order of preference makes the
              result predictable when more than one rule type is
              supplied.
:Traces to:   :ref:`PTW-SR-W-001`, :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/file/test_filefilter.py::TestGTK3FileFilter::test_do_set_mime_type_filter``
              ``tests/gtk3/file/test_filefilter.py::TestGTK3FileFilter::test_do_set_pattern_filter``
              ``tests/gtk3/file/test_filefilter.py::TestGTK3FileFilter::test_do_set_custom_filter``
              ``tests/gtk3/file/test_filefilter.py::TestGTK3FileFilter::test_do_set_filter_prefer_mime_type``

----

GTK3RecentChooserDialog
=======================

.. _PTW-GTK3-FIL-014:

PTW-GTK3-FIL-014
----------------

:Description: The ``GTK3RecentChooserDialog`` class **SHALL** combine
              ``Gtk.RecentChooserDialog`` directly with
              ``GTK3DialogMixin``. ``GTK3RecentChooserDialog.__init__()``
              **SHALL** take no parameters and **SHALL** call
              ``Gtk.RecentChooserDialog.__init__()`` followed by
              ``GTK3DialogMixin.__init__()``.
:Rationale:   The recent chooser dialog adds no pytkwrap configuration
              beyond the dialog mixin; its recent chooser API is
              available directly from ``Gtk.RecentChooserDialog``.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-DLG-003`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/file/test_recentchooserdialog.py::TestGTK3RecentChooserDialog::test_init``
              ``tests/gtk3/file/test_recentchooserdialog.py::TestGTK3RecentChooserDialog::test_do_set_properties_default``

----

GTK3RecentFilter
================

.. _PTW-GTK3-FIL-015:

PTW-GTK3-FIL-015
----------------

:Description: The ``GTK3RecentFilter`` class **SHALL** combine
              ``Gtk.RecentFilter`` directly with ``GTK3GObjectMixin``.
              ``GTK3RecentFilter.__init__()`` **SHALL** take no
              parameters and **SHALL** call
              ``Gtk.RecentFilter.__init__()`` followed by
              ``GTK3GObjectMixin.__init__()``.
:Rationale:   ``Gtk.RecentFilter`` is a ``GObject``-derived object
              rather than a widget, so widget properties and signals do
              not apply.
:Traces to:   :ref:`PTW-GTK3-X-001`, :ref:`PTW-GTK3-W-017`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/file/test_recentfilter.py::TestGTK3RecentFilter::test_init``

----

.. _PTW-GTK3-FIL-016:

PTW-GTK3-FIL-016
----------------

:Description: ``GTK3RecentFilter.do_set_filter()`` **SHALL** accept the
              same ``mime_types``, ``patterns``, ``needed``, ``func``,
              and ``*data`` arguments as
              ``GTK3FileFilter.do_set_filter()`` and **SHALL** add one
              of those rule types using the order of preference in
              :ref:`PTW-GTK3-FIL-013`. It **SHALL** also accept
              optional ``age`` and ``applications`` arguments. When
              ``age`` is not ``None`` it **SHALL** call
              ``add_age(age)``, and when ``applications`` is not
              ``None`` it **SHALL** call ``add_application()`` for each
              application. The age and application rules **SHALL** be
              added independently of, and in addition to, the
              MIME-type, pattern, or custom rule.
:Rationale:   Recent-file filtering commonly restricts results by how
              recently a file was used or which application used it,
              either alone or combined with a file-type rule.
:Traces to:   :ref:`PTW-SR-W-001`, :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/file/test_recentfilter.py::TestGTK3RecentFilter::test_do_set_mime_type_filter``
              ``tests/gtk3/file/test_recentfilter.py::TestGTK3RecentFilter::test_do_set_pattern_filter``
              ``tests/gtk3/file/test_recentfilter.py::TestGTK3RecentFilter::test_do_set_custom_filter``
              ``tests/gtk3/file/test_recentfilter.py::TestGTK3RecentFilter::test_do_set_filter_prefer_mime_type``
              ``tests/gtk3/file/test_recentfilter.py::TestGTK3RecentFilter::test_do_set_age_filter``
              ``tests/gtk3/file/test_recentfilter.py::TestGTK3RecentFilter::test_do_set_applications_filter``

----

GTK3RecentManager
=================

.. _PTW-GTK3-FIL-017:

PTW-GTK3-FIL-017
----------------

:Description: The ``GTK3RecentManager`` class **SHALL** combine
              ``Gtk.RecentManager`` and ``GTK3RecentManagerMixin``,
              which derives from ``GTK3GObjectMixin``.
              ``GTK3RecentManager.__init__()`` **SHALL** take no
              parameters and **SHALL** call
              ``Gtk.RecentManager.__init__()`` followed by
              ``GTK3RecentManagerMixin.__init__()``.
              ``GTK3RecentManagerMixin`` **SHALL** pre-register the
              ``"changed"`` signal in ``dic_handler_id`` with a value of
              ``-1``.
:Rationale:   ``Gtk.RecentManager`` is a ``GObject``-derived object;
              ``"changed"`` is emitted when the recently used resources
              list changes.
:Traces to:   :ref:`PTW-GTK3-X-001`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-017`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/file/test_recentmanager.py::TestGTK3RecentManager::test_init``

----

.. _PTW-GTK3-FIL-018:

PTW-GTK3-FIL-018
----------------

:Description: ``GTK3RecentManager.do_add_recent()`` **SHALL** accept a
              ``uri`` and an optional ``recent_data``
              (``Gtk.RecentData | None``, default ``None``). It
              **SHALL** call ``add_item(uri)`` when ``recent_data`` is
              ``None`` and ``add_full(uri, recent_data)`` otherwise, and
              **SHALL** return the boolean result of that call.
:Rationale:   One method covers both adding a file with default
              metadata and adding it with explicit metadata.
:Traces to:   :ref:`PTW-SR-W-001`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/file/test_recentmanager.py::TestGTK3RecentManager::test_do_add_item``
              ``tests/gtk3/file/test_recentmanager.py::TestGTK3RecentManager::test_do_add_item_full``

----

.. _PTW-GTK3-FIL-019:

PTW-GTK3-FIL-019
----------------

:Description: ``GTK3RecentManager.do_remove_recent()`` **SHALL** accept
              a ``uri`` and an optional ``remove_all`` flag (default
              ``False``). When ``remove_all`` is true it **SHALL** call
              ``purge_items()`` and return ``True`` if at least one item
              was purged; otherwise it **SHALL** call
              ``remove_item(uri)`` and return its result.
:Rationale:   One method covers removing a single recent file and
              clearing the whole list.
:Traces to:   :ref:`PTW-SR-W-001`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/file/test_recentmanager.py::TestGTK3RecentManager::test_do_remove_item``
              ``tests/gtk3/file/test_recentmanager.py::TestGTK3RecentManager::test_do_remove_all_items``

----

.. _PTW-GTK3-FIL-020:

PTW-GTK3-FIL-020
----------------

:Description: ``GTK3RecentManager`` **SHALL** provide a read-only
              ``recent_items`` property that returns the list of
              ``Gtk.RecentInfo`` objects from ``get_items()``.
:Rationale:   Pythonic attribute access to the recent items avoids a
              getter call in application code.
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-05) - Initial baseline.
:Tests:       ``tests/gtk3/file/test_recentmanager.py::TestGTK3RecentManager::test_do_remove_all_items``
