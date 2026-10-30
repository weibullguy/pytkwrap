.. _gtk3_buttons:

=================================
GTK3 Layer — Button Requirements
=================================

This document defines the software requirements for GTK3 button
wrappers defined in ``pytkwrap.gtk3.button``. These wrappers combine
native GTK classes with their corresponding pytkwrap mixins.

All requirements in this document trace to one or more system
requirements defined in :ref:`system_requirements` and to GTK3 layer
widget requirements defined in :ref:`gtk3_widgets`.

.. contents:: Contents
   :local:
   :depth: 1

----

GTK3Button
==========

.. _PTW-GTK3-B-001:

PTW-GTK3-B-001
--------------

:Description: The ``GTK3Button`` class **SHALL** combine ``Gtk.Button``
              and ``GTK3ButtonMixin``. The mixin **SHALL** derive from
              ``GTK3ContainerMixin``.
:Rationale:   The native GTK class provides the GTK button API, and
              the mixin provides pytkwrap configuration behavior.
:Traces to:   :ref:`PTW-SR-W-001`, :ref:`PTW-GTK3-W-010`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD

----

.. _PTW-GTK3-B-002:

PTW-GTK3-B-002
--------------

:Description: ``GTK3ButtonMixin`` **SHALL** define
              ``_DEFAULT_HEIGHT`` as ``30`` and ``_DEFAULT_WIDTH``
              as ``200``.
:Rationale:   These dimensions provide a usable default size for
              button widgets that is appropriate for most desktop
              GUI applications without requiring explicit size
              configuration.
:Traces to:   :ref:`PTW-GTK3-W-019`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD

----

.. _PTW-GTK3-B-003:

PTW-GTK3-B-003
--------------

:Description: ``GTK3Button.__init__()`` **SHALL** accept a ``label``
              parameter defaulting to ``"..."``, initialize
              ``Gtk.Button`` followed by ``GTK3ButtonMixin``, and store
              the label in ``dic_properties["label"]``.
:Rationale:   Calling the GTK3 parent ``__init__()`` before the
              pytkwrap parent ``__init__()`` ensures the underlying
              GTK3 widget is fully constructed before pytkwrap
              attempts to configure it.
:Traces to:   :ref:`PTW-GTK3-W-018`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD

----

.. _PTW-GTK3-B-004:

PTW-GTK3-B-004
--------------

:Description: ``GTK3ButtonMixin`` **SHALL** pre-register
              the following signals in ``dic_handler_id`` with a
              default value of ``-1``:

              - ``"activate"``
              - ``"clicked"``

              The following container signals inherited from
              ``Gtk.Bin`` **SHALL NOT** be pre-registered as they
              require callbacks with a non-standard two-argument
              signature:

              - ``"add"``
              - ``"remove"``
              - ``"set-focus-child"``

:Rationale:   Pre-registering ``"activate"`` and ``"clicked"`` makes
              these signals immediately available for connection via
              ``do_set_callbacks()``. The container signals are
              excluded because their callback signature differs from
              the standard pytkwrap callback pattern and must be
              connected manually via ``self.connect()`` if needed.
:Traces to:   :ref:`PTW-GTK3-W-003`, :ref:`PTW-GTK3-W-018`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD

----

.. _PTW-GTK3-B-005:

PTW-GTK3-B-005
--------------

:Description: ``GTK3ButtonMixin.do_set_properties()`` **SHALL**
              support configuration of the following button-specific
              properties via ``dic_properties``:

              - ``always_show_image``
              - ``image``
              - ``image_position``
              - ``label``
              - ``relief``
              - ``use_underline``

:Rationale:   These properties are specific to ``Gtk.Button`` and
              are not part of the base ``Gtk.Widget`` property set.
              They **SHALL** be supported by the pytkwrap button
              wrapper to allow full button configuration via the
              typed dictionary interface.
:Traces to:   :ref:`PTW-SR-W-004`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD

----

.. _PTW-GTK3-B-006:

PTW-GTK3-B-006
--------------

:Description: When the ``image`` property is set in
              ``dic_properties``, ``GTK3ButtonMixin.do_set_properties()``
              method **SHALL** clear the button label, load the image
              from the specified file path at the requested size, and
              set it as the button's image.
:Rationale:   Icon buttons require the label to be cleared and an
              image to be loaded from a file. Handling this in
              ``do_set_properties()`` allows icon buttons to be
              configured via the same typed dictionary interface as
              all other widget properties.
:Traces to:   :ref:`PTW-SR-W-004`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD

----

do_make_buttonbox
=================

.. _PTW-GTK3-B-007:

PTW-GTK3-B-007
--------------

:Description: The ``do_make_buttonbox()`` function **SHALL** accept
              a list of icon file paths, a list of tooltip strings,
              a list of callback functions, and optional keyword
              arguments for ``height``, ``width``, ``layout``, and
              ``orientation``, and **SHALL** return a populated
              ``Gtk.HButtonBox`` or ``Gtk.VButtonBox``.
:Rationale:   A factory function for button boxes reduces the
              boilerplate required to create a row or column of
              icon buttons, which is a common UI pattern in
              application toolbars.
:Traces to:   :ref:`PTW-SR-W-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_buttons/test_base_button.py::test_do_make_buttonbox_vertical``
              ``tests/gtk3/test_buttons/test_base_button.py::test_do_make_buttonbox_horizontal``

----

.. _PTW-GTK3-B-008:

PTW-GTK3-B-008
--------------

:Description: The ``do_make_buttonbox()`` function **SHALL** set a
              button insensitive if no callback is provided for that
              button's index, and **SHALL** set an empty tooltip if
              no tooltip is provided for that button's index.
:Rationale:   Graceful handling of mismatched list lengths prevents
              ``IndexError`` exceptions when the number of callbacks
              or tooltips does not match the number of icons, allowing
              partial configuration of button boxes without raising
              exceptions.
:Traces to:   :ref:`PTW-SR-W-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_buttons/test_base_button.py::test_do_make_buttonbox_missing_callback``
              ``tests/gtk3/test_buttons/test_base_button.py::test_do_make_buttonbox_missing_tooltip``

----

GTK3CheckButton
===============

.. _PTW-GTK3-B-009:

PTW-GTK3-B-009
--------------

:Description: The ``GTK3CheckButton`` class **SHALL** inherit from
              ``Gtk.CheckButton`` and ``GTK3CheckButtonMixin``. The
              mixin **SHALL** define ``edit_signal`` as
              ``"toggled"``.
:Rationale:   ``Gtk.CheckButton`` inherits from ``Gtk.ToggleButton``
              which emits ``"toggled"`` when the button state changes.
              This is the correct signal to use as the edit signal
              for publish-subscribe messaging.
:Traces to:   :ref:`PTW-GTK3-M-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_buttons/test_check_button.py::TestGTK3CheckButton::test_init``

----

.. _PTW-GTK3-B-010:

PTW-GTK3-B-010
--------------

:Description: The ``GTK3CheckButton.do_get_value()`` method **SHALL**
              return the boolean active state of the check button as
              returned by ``Gtk.CheckButton.get_active()``.
:Rationale:   The active state is the meaningful value of a check
              button from the application's perspective — whether
              the box is checked or unchecked.
:Traces to:   :ref:`PTW-SR-W-006`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_buttons/test_check_button.py::TestGTK3CheckButton::test_do_get_value``

----

.. _PTW-GTK3-B-011:

PTW-GTK3-B-011
--------------

:Description: The ``GTK3CheckButton.do_set_value()`` method **SHALL**
              accept a ``bool | float | int | str | None`` value and
              **SHALL** call ``Gtk.CheckButton.set_active()`` with
              the boolean representation of the value. A ``None``
              value **SHALL** be treated as ``False``.
:Rationale:   Accepting the widest possible input type allows
              ``do_set_value()`` to be called from
              ``GTK3MatrixView.set_cell_value()`` with any value type
              without raising a ``TypeError``.
:Traces to:   :ref:`PTW-SR-W-007`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_buttons/test_check_button.py::TestGTK3CheckButton::test_do_set_value``
              ``tests/gtk3/test_buttons/test_check_button.py::TestGTK3CheckButton::test_do_set_value_none``

----

GTK3ColorButton
===============

.. _PTW-GTK3-B-012:

PTW-GTK3-B-012
--------------

:Description: The ``GTK3ColorButton`` class **SHALL** inherit from
              ``Gtk.ColorButton`` and ``GTK3ColorButtonMixin``. The
              mixin **SHALL** define ``edit_signal`` as
              ``"color-set"``.
:Rationale:   ``Gtk.ColorButton`` emits ``"color-set"`` when the
              user selects a new color. This is the correct signal
              to use as the edit signal for publish-subscribe
              messaging.
:Traces to:   :ref:`PTW-GTK3-M-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_buttons/test_color_button.py::TestGTK3ColorButton::test_init``

----

.. _PTW-GTK3-B-013:

PTW-GTK3-B-013
--------------

:Description: The ``GTK3ColorButton.do_get_value()`` method **SHALL**
              return the currently selected ``Gdk.RGBA`` color value
              as returned by ``Gtk.ColorButton.get_rgba()``.
:Rationale:   The ``Gdk.RGBA`` color is the meaningful value of a
              color button from the application's perspective.
:Traces to:   :ref:`PTW-SR-W-006`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_buttons/test_color_button.py::TestGTK3ColorButton::test_do_get_value``

----

.. _PTW-GTK3-B-014:

PTW-GTK3-B-014
--------------

:Description: The ``GTK3ColorButton.do_set_value()`` method **SHALL**
              accept a ``Gdk.RGBA | None`` value and **SHALL** call
              ``Gtk.ColorButton.set_rgba()`` with the value. A
              ``None`` value **SHALL** be substituted with
              ``Gdk.RGBA(0.0, 0.0, 0.0, 1.0)``.
:Rationale:   Substituting opaque black for ``None`` provides a
              visible, predictable default color that clearly
              indicates no color has been selected.
:Traces to:   :ref:`PTW-SR-W-007`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_buttons/test_color_button.py::TestGTK3ColorButton::test_do_set_value``
              ``tests/gtk3/test_buttons/test_color_button.py::TestGTK3ColorButton::test_do_set_value_none``

----

GTK3FileChooserButton
=====================

.. _PTW-GTK3-B-015:

PTW-GTK3-B-015
--------------

:Description: The ``GTK3FileChooserButton`` class **SHALL** inherit
              from both ``Gtk.FileChooserButton`` and
              ``GTK3FileChooserButtonMixin`` and **SHALL** register
              ``"file-set"`` as a signal.
:Rationale:   ``Gtk.FileChooserButton`` emits ``"file-set"`` when
              the user selects a file. This is the correct signal
              to use as the edit signal for publish-subscribe
              messaging.
:Traces to:   :ref:`PTW-GTK3-M-005`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD

.. note::

   ``GTK3FileChooserButton`` cannot be tested in a headless
   environment because ``Gtk.FileChooserButton`` requires a fully
   realized display backend and crashes at the C level without one.
   Tests for this class require a running display and are marked
   with ``@pytest.mark.skip`` in headless environments.

----

.. _PTW-GTK3-B-016:

PTW-GTK3-B-016
--------------

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
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD

----

.. _PTW-GTK3-B-017:

PTW-GTK3-B-017
--------------

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
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD

----

GTK3SpinButton
==============

.. _PTW-GTK3-B-021:

PTW-GTK3-B-021
--------------

:Description: The ``GTK3SpinButton`` class **SHALL** inherit from
              ``Gtk.SpinButton`` and ``GTK3SpinButtonMixin``. The
              mixin **SHALL** derive from ``GTK3EntryMixin`` and
              configure ``edit_signal`` as ``"value-changed"``.
:Rationale:   ``Gtk.SpinButton`` inherits from ``Gtk.Entry``, not
              ``Gtk.Button``. The entry mixin provides the relevant
              common behavior without imposing button-specific
              signals on the spin button.
:Traces to:   :ref:`PTW-GTK3-M-005`, :ref:`PTW-GTK3-W-017`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_buttons/test_spin_button.py::TestGTK3SpinButton::test_init``

----

.. _PTW-GTK3-B-022:

PTW-GTK3-B-022
--------------

:Description: The ``GTK3SpinButton.do_get_value()`` method **SHALL**
              return the current numeric value of the spin button as
              a ``float`` as returned by
              ``Gtk.SpinButton.get_value()``.
:Rationale:   The numeric value is the meaningful output of a spin
              button. Returning a ``float`` covers both integer and
              floating-point spin button configurations.
:Traces to:   :ref:`PTW-SR-W-006`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_buttons/test_spin_button.py::TestGTK3SpinButton::test_do_get_value``

----

.. _PTW-GTK3-B-023:

PTW-GTK3-B-023
--------------

:Description: The ``GTK3SpinButton.do_set_value()`` method **SHALL**
              accept a ``float | int | None`` value, clamp it to
              the widget's configured ``lower`` and ``upper`` range
              using ``clamp()``, and **SHALL** call
              ``Gtk.SpinButton.set_value()`` with the clamped float
              value. A ``None`` value **SHALL** be silently ignored.
:Rationale:   Clamping the value before passing it to
              ``Gtk.SpinButton.set_value()`` prevents out-of-range
              values from causing GTK3 warnings or unexpected
              behavior.
:Traces to:   :ref:`PTW-SR-W-007`, :ref:`PTW-COM-U-011`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_buttons/test_spin_button.py::TestGTK3SpinButton::test_do_set_value``
              ``tests/gtk3/test_buttons/test_spin_button.py::TestGTK3SpinButton::test_do_set_value_clamped``
              ``tests/gtk3/test_buttons/test_spin_button.py::TestGTK3SpinButton::test_do_set_value_none``
