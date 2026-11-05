.. _gtk3_buttons:

=================================
GTK3 Layer — Button Requirements
=================================

This document defines the software requirements for GTK3 button
wrappers defined in ``pytkwrap.gtk3.button``. These wrappers combine
native GTK classes with their corresponding pytkwrap mixins.

The button mixin hierarchy is:

.. code-block:: text

    GTK3ContainerMixin
        └── GTK3ButtonMixin
                ├── GTK3ToggleButtonMixin
                │       └── GTK3CheckButtonMixin
                │               └── GTK3RadioButtonMixin
                └── GTK3ScaleButtonMixin
                        └── GTK3VolumeButtonMixin
    GTK3EntryMixin
        └── GTK3SpinButtonMixin
    GTK3ComboBoxMixin
        └── GTK3AppChooserButtonMixin

All requirements in this document trace to one or more system
requirements defined in :ref:`system_requirements` and to GTK3 layer
widget requirements defined in :ref:`gtk3_widgets`.

.. contents:: Contents
   :local:
   :depth: 1

----

Package
=======

.. _PTW-GTK3-B-024:

PTW-GTK3-B-024
--------------

:Description: The ``pytkwrap.gtk3.button`` package **SHALL** export
              ``GTK3AppChooserButton``, ``GTK3Button``,
              ``GTK3ButtonMixin``, ``GTK3CheckButton``,
              ``GTK3RadioButton``, ``GTK3ScaleButton``,
              ``GTK3SpinButton``, ``GTK3ToggleButton``, and
              ``GTK3VolumeButton`` through ``__all__``. Sub-modules of
              the package **SHALL** import sibling modules directly and
              **SHALL NOT** import through the package ``__init__.py``.
:Rationale:   A single public import location simplifies application
              code, and ``GTK3ButtonMixin`` is exported so other
              packages can build button-derived wrappers. Direct
              sibling imports avoid circular imports during package
              initialization.
:Traces to:   :ref:`PTW-SR-W-001`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       TBD

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
              the mixin provides pytkwrap configuration behavior and
              inherited container signal bookkeeping.
:Traces to:   :ref:`PTW-SR-W-001`, :ref:`PTW-GTK3-W-001`,
              :ref:`PTW-GTK3-W-017`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Corrected traces to the wrapper
              composition requirements.
:Tests:       ``tests/gtk3/button/test_button.py::TestButton::test_init``

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
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_button.py::TestButton::test_init``

----

.. _PTW-GTK3-B-003:

PTW-GTK3-B-003
--------------

:Description: ``GTK3Button.__init__()`` **SHALL** accept a ``label``
              parameter of type ``str | None`` defaulting to ``"..."``.
              It **SHALL** call ``Gtk.Button.__init__()`` with that
              label, then ``GTK3ButtonMixin.__init__()``, and **SHALL**
              store the label, unchanged, in
              ``dic_properties["label"]``.
:Rationale:   Calling the GTK3 parent ``__init__()`` before the
              pytkwrap parent ``__init__()`` ensures the underlying
              GTK3 widget is fully constructed before pytkwrap
              attempts to configure it. Storing the constructor label
              keeps ``dic_properties`` consistent with the widget.
:Traces to:   :ref:`PTW-GTK3-W-018`, :ref:`PTW-SR-W-003`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Specified the ``str | None`` label
              type and that the label is passed to ``Gtk.Button``.
:Tests:       ``tests/gtk3/button/test_button.py::TestButton::test_init``
              ``tests/gtk3/button/test_button.py::TestButton::test_init_with_label``
              ``tests/gtk3/button/test_button.py::TestButton::test_init_with_mnemonic``

----

.. _PTW-GTK3-B-004:

PTW-GTK3-B-004
--------------

:Description: ``GTK3ButtonMixin.__init__()`` **SHALL** pre-register
              the ``"activate"``, ``"check-resize"``, and ``"clicked"``
              signals in ``dic_handler_id`` with a value of ``-1``, in
              addition to the container signals inherited from
              ``GTK3ContainerMixin`` (``"add"``, ``"check-resize"``,
              ``"remove"``, and ``"set-focus-child"``).
:Rationale:   Pre-registering the button signals makes them available
              for connection via ``do_set_callbacks()``. Callbacks for
              the inherited ``"add"``, ``"remove"``, and
              ``"set-focus-child"`` signals receive both the container
              and the child widget.
:Traces to:   :ref:`PTW-GTK3-W-003`, :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Revised to match the implementation:
              inherited container signals are registered and
              ``"check-resize"`` is also declared by the button mixin.
:Tests:       ``tests/gtk3/button/test_button.py::TestButton::test_init``

----

.. _PTW-GTK3-B-005:

PTW-GTK3-B-005
--------------

:Description: ``GTK3ButtonMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``always_show_image``: ``False``
              - ``image``: ``None``
              - ``image_position``: ``Gtk.PositionType.LEFT``
              - ``label``: ``"..."``
              - ``relief``: ``Gtk.ReliefStyle.NORMAL``
              - ``use_underline``: ``False``

              ``GTK3ButtonMixin.do_set_properties()`` **SHALL** call
              ``super().do_set_properties()`` first, then apply
              ``always_show_image``, ``relief``, ``use_underline``, and
              ``label`` with their corresponding ``Gtk.Button``
              setters.
:Rationale:   These properties are specific to ``Gtk.Button`` and
              are not part of the base ``Gtk.Widget`` property set.
              Supporting them allows full button configuration via the
              typed dictionary interface.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Added default values and the order
              of setter calls.
:Tests:       ``tests/gtk3/button/test_button.py::TestButton::test_do_set_properties_default``
              ``tests/gtk3/button/test_button.py::TestButton::test_do_set_properties``

----

.. _PTW-GTK3-B-025:

PTW-GTK3-B-025
--------------

:Description: When ``dic_properties["label"]`` is ``None``,
              ``GTK3ButtonMixin.do_set_properties()`` **SHALL** replace
              it with ``""`` in ``dic_properties`` before calling
              ``set_label()``.
:Rationale:   ``None`` is accepted as a convenient way to clear the
              label; normalizing it to an empty string gives GTK a
              valid label and keeps the stored value consistent.
:Traces to:   :ref:`PTW-SR-W-004`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_button.py::TestButton::test_do_set_properties_none_label``

----

.. _PTW-GTK3-B-006:

PTW-GTK3-B-006
--------------

:Description: When ``dic_properties["image"]`` is not ``None``,
              ``GTK3ButtonMixin.do_set_properties()`` **SHALL**, after
              applying the label:

              - set the button label to ``""``;
              - load a ``GdkPixbuf.Pixbuf`` from the file path in
                ``image``, scaled using the ``height_request`` and
                ``width_request`` properties;
              - set a ``Gtk.Image`` created from that pixbuf as the
                button image; and
              - apply ``image_position`` with
                ``set_image_position()``.

              ``image_position`` **SHALL** be applied only when an
              image is set.
:Rationale:   Icon buttons require the label to be cleared and an
              image to be loaded from a file. Handling this in
              ``do_set_properties()`` allows icon buttons to be
              configured via the same typed dictionary interface as
              all other widget properties.
:Traces to:   :ref:`PTW-SR-W-004`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Specified the size source and that
              ``image_position`` is applied only with an image.
:Tests:       ``tests/gtk3/button/test_button.py::TestButton::test_do_set_properties_image``

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
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_buttons/test_base_button.py::test_do_make_buttonbox_missing_callback``
              ``tests/gtk3/test_buttons/test_base_button.py::test_do_make_buttonbox_missing_tooltip``

----

GTK3ToggleButton
================

.. _PTW-GTK3-B-026:

PTW-GTK3-B-026
--------------

:Description: The ``GTK3ToggleButton`` class **SHALL** combine
              ``Gtk.ToggleButton`` and ``GTK3ToggleButtonMixin``, which
              derives from ``GTK3ButtonMixin``. ``GTK3ToggleButtonMixin``
              **SHALL** define ``_DEFAULT_HEIGHT`` as ``30`` and
              ``_DEFAULT_WIDTH`` as ``200``. ``GTK3ToggleButton.__init__()``
              **SHALL** accept a ``label`` parameter defaulting to
              ``"..."``, call ``Gtk.ToggleButton.__init__()`` with that
              label followed by ``GTK3ToggleButtonMixin.__init__()``,
              and store the label in ``dic_properties["label"]``.
:Rationale:   A toggle button is a button with an active state, so it
              reuses the button mixin's properties and signals.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-019`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_init``
              ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_init_with_label``
              ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_init_with_mnemonic``

----

.. _PTW-GTK3-B-027:

PTW-GTK3-B-027
--------------

:Description: ``GTK3ToggleButtonMixin.__init__()`` **SHALL** set
              ``dic_attributes["default_value"]`` to ``False`` and
              ``dic_attributes["edit_signal"]`` to ``"toggled"``, and
              **SHALL** pre-register the ``"toggled"`` signal in
              ``dic_handler_id`` with a value of ``-1``.
:Rationale:   ``Gtk.ToggleButton`` emits ``"toggled"`` when its active
              state changes, making it the edit signal for
              publish-subscribe messaging. The default value
              represents an inactive button.
:Traces to:   :ref:`PTW-SR-W-005`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-010`, :ref:`PTW-GTK3-W-011`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_do_set_attributes_default``
              ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_do_set_attributes``

----

.. _PTW-GTK3-B-028:

PTW-GTK3-B-028
--------------

:Description: ``GTK3ToggleButtonMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``active``: ``False``
              - ``draw_indicator``: ``False``
              - ``inconsistent``: ``False``

              ``GTK3ToggleButtonMixin.do_set_properties()`` **SHALL**
              call ``super().do_set_properties()`` first, then apply
              ``active`` with ``set_active()``, ``inconsistent`` with
              ``set_inconsistent()``, and ``draw_indicator`` with
              ``set_mode()``.
:Rationale:   ``Gtk.ToggleButton`` exposes the indicator setting
              through ``set_mode()``; the property key follows the
              GObject property name ``draw-indicator``.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_do_set_properties_default``
              ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_do_set_properties``

----

.. _PTW-GTK3-B-029:

PTW-GTK3-B-029
--------------

:Description: ``GTK3ToggleButtonMixin.do_get_value()`` **SHALL** return
              the active state of the button as returned by
              ``get_active()``.
:Rationale:   The active state is the meaningful value of a toggle
              button from the application's perspective.
:Traces to:   :ref:`PTW-SR-W-006`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_do_get_value``

----

.. _PTW-GTK3-B-030:

PTW-GTK3-B-030
--------------

:Description: ``GTK3ToggleButtonMixin.do_set_value()`` **SHALL** accept
              a ``bool``, ``float``, or ``int`` value, convert it with
              ``bool()``, store the result in
              ``dic_properties["active"]``, and apply it with
              ``set_active()``. Any other value type, including
              ``str`` and ``None``, **SHALL** be delegated to the base
              ``do_set_value()``, which publishes a ``do_log_error``
              message and raises ``WrongTypeError``.
:Rationale:   Numeric values have an unambiguous truth value. Strings
              such as ``"False"`` do not, so they are rejected rather
              than silently converted. ``do_update()`` substitutes
              ``default_value`` for an incoming ``None`` before
              calling this method.
:Traces to:   :ref:`PTW-SR-W-007`, :ref:`PTW-COM-X-008`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_do_set_value``
              ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_do_set_value_wrong_type``
              ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_do_update``
              ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_on_changed``

----

GTK3CheckButton
===============

.. _PTW-GTK3-B-009:

PTW-GTK3-B-009
--------------

:Description: The ``GTK3CheckButton`` class **SHALL** combine
              ``Gtk.CheckButton`` and ``GTK3CheckButtonMixin``, which
              derives from ``GTK3ToggleButtonMixin`` and therefore
              uses ``"toggled"`` as its edit signal.
              ``GTK3CheckButtonMixin`` **SHALL** define
              ``_DEFAULT_HEIGHT`` as ``40`` and ``_DEFAULT_WIDTH`` as
              ``200``. ``GTK3CheckButton.__init__()`` **SHALL** accept a
              ``label`` parameter defaulting to ``"..."``, call
              ``Gtk.CheckButton.__init__()`` with that label followed
              by ``GTK3CheckButtonMixin.__init__()``, and store the
              label in ``dic_properties["label"]``.
:Rationale:   ``Gtk.CheckButton`` inherits from ``Gtk.ToggleButton``,
              so the check button reuses the toggle button's
              properties, signals, and value handling.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-019`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Revised to match the implementation:
              ``edit_signal`` is inherited from
              ``GTK3ToggleButtonMixin``; added default size and
              constructor behavior.
:Tests:       ``tests/gtk3/button/test_checkbutton.py::TestGTK3CheckButton::test_init``
              ``tests/gtk3/button/test_checkbutton.py::TestGTK3CheckButton::test_init_with_label``
              ``tests/gtk3/button/test_checkbutton.py::TestGTK3CheckButton::test_init_with_mnemonic``

----

.. _PTW-GTK3-B-010:

PTW-GTK3-B-010
--------------

:Description: ``GTK3CheckButton.do_get_value()`` **SHALL** be the
              ``GTK3ToggleButtonMixin`` implementation described in
              :ref:`PTW-GTK3-B-029`.
:Rationale:   The active state is the meaningful value of a check
              button from the application's perspective — whether
              the box is checked or unchecked.
:Traces to:   :ref:`PTW-SR-W-006`, :ref:`PTW-GTK3-B-029`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Revised to reference the inherited
              toggle button implementation.
:Tests:       ``tests/gtk3/button/test_checkbutton.py::TestGTK3CheckButton::test_do_get_value``

----

.. _PTW-GTK3-B-011:

PTW-GTK3-B-011
--------------

:Description: ``GTK3CheckButton.do_set_value()`` **SHALL** be the
              ``GTK3ToggleButtonMixin`` implementation described in
              :ref:`PTW-GTK3-B-030`.
:Rationale:   A check button has the same boolean value semantics as a
              toggle button.
:Traces to:   :ref:`PTW-SR-W-007`, :ref:`PTW-GTK3-B-030`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Revised to match the implementation:
              ``str`` and ``None`` raise ``WrongTypeError`` rather than
              being converted.
:Tests:       ``tests/gtk3/button/test_checkbutton.py::TestGTK3CheckButton::test_do_set_value``
              ``tests/gtk3/button/test_checkbutton.py::TestGTK3CheckButton::test_do_set_value_wrong_type``
              ``tests/gtk3/button/test_checkbutton.py::TestGTK3CheckButton::test_do_update``
              ``tests/gtk3/button/test_checkbutton.py::TestGTK3CheckButton::test_on_changed``

----

GTK3RadioButton
===============

.. _PTW-GTK3-B-031:

PTW-GTK3-B-031
--------------

:Description: The ``GTK3RadioButton`` class **SHALL** combine
              ``Gtk.RadioButton`` and ``GTK3RadioButtonMixin``, which
              derives from ``GTK3CheckButtonMixin``.
              ``GTK3RadioButtonMixin`` **SHALL** define
              ``_DEFAULT_HEIGHT`` as ``40`` and ``_DEFAULT_WIDTH`` as
              ``200``. ``GTK3RadioButton.__init__()`` **SHALL** accept
              a ``label`` parameter defaulting to ``"..."`` and a
              ``group`` parameter of type ``Gtk.RadioButton | None``
              defaulting to ``None``. It **SHALL** call
              ``Gtk.RadioButton.__init__()`` with the label, then
              ``GTK3RadioButtonMixin.__init__()``, store the label in
              ``dic_properties["label"]``, and call
              ``join_group(group)``.
:Rationale:   Accepting the group at construction lets applications
              build a set of mutually exclusive buttons without a
              separate call for each button.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-019`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_radiobutton.py::TestRadioButton::test_init``
              ``tests/gtk3/button/test_radiobutton.py::TestRadioButton::test_init_with_group``
              ``tests/gtk3/button/test_radiobutton.py::TestRadioButton::test_init_with_label``
              ``tests/gtk3/button/test_radiobutton.py::TestRadioButton::test_init_with_mnemonic``

----

.. _PTW-GTK3-B-032:

PTW-GTK3-B-032
--------------

:Description: ``GTK3RadioButtonMixin.__init__()`` **SHALL** add the
              ``group`` property (default ``None``) to
              ``dic_properties`` and **SHALL** pre-register the
              ``"group-changed"`` signal in ``dic_handler_id`` with a
              value of ``-1``. ``GTK3RadioButtonMixin.do_set_properties()``
              **SHALL** call ``super().do_set_properties()`` first and
              then call ``join_group()`` with ``dic_properties["group"]``.
:Rationale:   The group property allows radio button membership to be
              configured through the typed dictionary interface.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-W-003`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_radiobutton.py::TestRadioButton::test_do_set_properties_default``
              ``tests/gtk3/button/test_radiobutton.py::TestRadioButton::test_do_set_properties``

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

:Description: The ``GTK3SpinButton`` class **SHALL** combine
              ``Gtk.SpinButton`` and ``GTK3SpinButtonMixin``. The
              mixin **SHALL** derive from ``GTK3EntryMixin`` and
              **SHALL** set the following attributes in
              ``dic_attributes``:

              - ``data_type``: ``float``
              - ``default_value``: ``0.0``
              - ``edit_signal``: ``"value-changed"``
              - ``format``: ``"{:3.1f}"``

:Rationale:   ``Gtk.SpinButton`` inherits from ``Gtk.Entry``, not
              ``Gtk.Button``. The entry mixin provides the relevant
              common behavior without imposing button-specific
              signals on the spin button. ``"value-changed"`` is
              emitted whenever the numeric value changes.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-011`,
              :ref:`PTW-GTK3-W-017`, :ref:`PTW-SR-W-005`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Added the full attribute defaults
              and corrected traces.
:Tests:       ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_init``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_set_attributes_default``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_set_attributes``

----

.. _PTW-GTK3-B-033:

PTW-GTK3-B-033
--------------

:Description: ``GTK3SpinButtonMixin.__init__()`` **SHALL** pre-register
              the ``"change-value"``, ``"input"``, ``"output"``,
              ``"value-changed"``, and ``"wrapped"`` signals in
              ``dic_handler_id`` with a value of ``-1``, and **SHALL**
              add the following properties to ``dic_properties``:

              - ``adjustment``: ``None``
              - ``climb_rate``: ``0.0``
              - ``digits``: ``0``
              - ``numeric``: ``False``
              - ``snap_to_ticks``: ``False``
              - ``update_policy``: ``Gtk.SpinButtonUpdatePolicy.ALWAYS``
              - ``value``: ``0.0``
              - ``wrap``: ``False``

:Rationale:   The signals and property defaults match the native
              ``Gtk.SpinButton``.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_init``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_set_properties_default``

----

.. _PTW-GTK3-B-034:

PTW-GTK3-B-034
--------------

:Description: ``GTK3SpinButtonMixin.do_set_properties()`` **SHALL**
              call ``super().do_set_properties()`` first. It **SHALL**
              call ``set_adjustment()`` only when ``adjustment`` is a
              ``Gtk.Adjustment``; **SHALL** apply ``digits``,
              ``numeric``, ``snap_to_ticks``, ``update_policy``,
              ``value``, and ``wrap`` with their corresponding
              ``Gtk.SpinButton`` setters; and **SHALL** apply
              ``climb_rate`` through ``set_property("climb-rate",
              ...)``.
:Rationale:   An absent adjustment leaves the spin button's current
              adjustment in place. ``climb-rate`` has no dedicated
              setter in ``Gtk.SpinButton``.
:Traces to:   :ref:`PTW-SR-W-004`, :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_set_properties``

----

.. _PTW-GTK3-B-035:

PTW-GTK3-B-035
--------------

:Description: ``GTK3SpinButton.__init__()`` **SHALL** accept an
              ``adjustment`` parameter (``GTK3Adjustment | None``,
              default ``None``), a ``climb_rate`` parameter (default
              ``0.0``), and a ``digits`` parameter (default ``1``),
              and **SHALL** pass all three as keyword arguments to
              ``Gtk.SpinButton.__init__()`` before calling
              ``GTK3SpinButtonMixin.__init__()``. It **SHALL** then set
              ``dic_attributes["format"]`` to ``"{:3.<digits>f}"`` and
              store ``adjustment``, ``climb_rate``, and ``digits`` in
              ``dic_properties``.
:Rationale:   Deriving the display format from ``digits`` keeps the
              formatted value consistent with the precision the spin
              button displays.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_init_with_adjustment``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_init_with_climb_rate``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_init_with_digits``

----

.. _PTW-GTK3-B-022:

PTW-GTK3-B-022
--------------

:Description: ``GTK3SpinButtonMixin.do_get_value()`` **SHALL** return
              the value from ``Gtk.SpinButton.get_value()`` converted
              with ``dic_attributes["data_type"]``.
:Rationale:   The configurable data type lets the spin button return
              ``float``, ``int``, or ``str`` to match the underlying
              data field without conversion in application code.
:Traces to:   :ref:`PTW-SR-W-006`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Revised to match the implementation:
              the value is converted with ``data_type`` rather than
              always returned as ``float``.
:Tests:       ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_get_value``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_get_value_int``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_get_value_str``

----

.. _PTW-GTK3-B-023:

PTW-GTK3-B-023
--------------

:Description: ``GTK3SpinButtonMixin.do_set_value()`` **SHALL** accept a
              ``float``, ``int``, or ``str`` value, convert it with
              ``dic_attributes["data_type"]``, and apply it with
              ``Gtk.SpinButton.set_value()``, which limits the value to
              the adjustment's range. Any other value type, including
              ``None``, **SHALL** be delegated to the base
              ``do_set_value()``, which publishes a ``do_log_error``
              message and raises ``WrongTypeError``.
:Rationale:   ``Gtk.SpinButton.set_value()`` keeps the value within the
              adjustment bounds, so no additional range check is
              required. ``do_update()`` substitutes ``default_value``
              for an incoming ``None`` before calling this method.
:Traces to:   :ref:`PTW-SR-W-007`, :ref:`PTW-COM-X-008`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Revised to match the implementation:
              ``None`` raises ``WrongTypeError``, ``str`` is accepted,
              and range limiting is performed by GTK rather than
              ``clamp()``.
:Tests:       ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_set_value``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_set_value_int``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_set_value_str``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_set_value_wrong_type``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_update``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_on_changed``

----

GTK3ScaleButton
===============

.. _PTW-GTK3-B-036:

PTW-GTK3-B-036
--------------

:Description: The ``GTK3ScaleButton`` class **SHALL** combine
              ``Gtk.ScaleButton`` and ``GTK3ScaleButtonMixin``, which
              derives from ``GTK3ButtonMixin``. ``GTK3ScaleButtonMixin``
              **SHALL** define ``_DEFAULT_HEIGHT`` as ``30`` and
              ``_DEFAULT_WIDTH`` as ``60``; **SHALL** set
              ``dic_attributes["default_value"]`` to ``0.0`` and
              ``dic_attributes["edit_signal"]`` to ``"value-changed"``;
              and **SHALL** pre-register the ``"popdown"``,
              ``"popup"``, and ``"value-changed"`` signals in
              ``dic_handler_id`` with a value of ``-1``.
:Rationale:   ``Gtk.ScaleButton`` is a ``Gtk.Button`` that pops up a
              scale; ``"value-changed"`` is emitted when the scale
              value changes.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-011`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-019`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_init``
              ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_do_set_attributes_default``
              ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_do_set_attributes``

----

.. _PTW-GTK3-B-037:

PTW-GTK3-B-037
--------------

:Description: ``GTK3ScaleButtonMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``adjustment``: ``None``
              - ``icons``: ``None``
              - ``size``: ``4`` (``Gtk.IconSize.BUTTON``)
              - ``value``: ``0.0``

              ``GTK3ScaleButtonMixin.do_set_properties()`` **SHALL**
              call ``super().do_set_properties()`` first. It **SHALL**
              call ``set_adjustment()`` only when ``adjustment`` is not
              ``None`` and ``set_icons()`` only when ``icons`` is a
              non-empty list; **SHALL** apply ``value`` with
              ``set_value()``; and **SHALL** apply ``size`` through
              ``set_property("size", ...)``.
:Rationale:   Skipping absent adjustments and icon lists preserves the
              native defaults. ``size`` has no dedicated setter in
              ``Gtk.ScaleButton``.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_do_set_properties_default``
              ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_do_set_properties``

----

.. _PTW-GTK3-B-038:

PTW-GTK3-B-038
--------------

:Description: ``GTK3ScaleButtonMixin.do_get_value()`` **SHALL** return
              the value from ``get_value()``.
              ``GTK3ScaleButtonMixin.do_set_value()`` **SHALL** accept
              a ``float``, ``int``, or ``str`` value, convert it with
              ``float()``, store it in ``dic_properties["value"]``, and
              apply it with ``set_value()``. Any other value type
              **SHALL** be delegated to the base ``do_set_value()``,
              which publishes a ``do_log_error`` message and raises
              ``WrongTypeError``.
:Rationale:   A scale button's value is always a floating-point
              position on its adjustment.
:Traces to:   :ref:`PTW-SR-W-006`, :ref:`PTW-SR-W-007`,
              :ref:`PTW-COM-X-008`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_do_get_value``
              ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_do_set_value``
              ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_do_set_value_wrong_type``
              ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_do_update``
              ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_on_changed``

----

.. _PTW-GTK3-B-039:

PTW-GTK3-B-039
--------------

:Description: ``GTK3ScaleButton.__init__()`` **SHALL** accept a
              required ``size`` parameter (a ``Gtk.IconSize`` value)
              and optional ``min_value`` (default ``0.0``),
              ``max_value`` (default ``100.0``), ``step`` (default
              ``2``), and ``icons`` (``list | None``, default ``None``)
              parameters. It **SHALL** call
              ``Gtk.ScaleButton.__init__()`` with ``size``, ``icons``,
              and a ``GTK3Adjustment`` whose value and lower bound are
              ``min_value``, upper bound is ``max_value``, and step
              increment is ``step``, followed by
              ``GTK3ScaleButtonMixin.__init__()``. It **SHALL** then
              store an adjustment with the same values, ``icons``, and
              ``size`` in ``dic_properties``.
:Rationale:   Constructing the adjustment from simple numeric
              parameters spares callers from creating one themselves.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_init``
              ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_init_with_size``
              ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_init_with_icons``

----

GTK3VolumeButton
================

.. _PTW-GTK3-B-040:

PTW-GTK3-B-040
--------------

:Description: The ``GTK3VolumeButton`` class **SHALL** combine
              ``Gtk.VolumeButton`` and ``GTK3VolumeButtonMixin``, which
              derives from ``GTK3ScaleButtonMixin`` and inherits its
              attributes, signals, and value handling.
              ``GTK3VolumeButtonMixin`` **SHALL** define
              ``_DEFAULT_HEIGHT`` as ``30`` and ``_DEFAULT_WIDTH`` as
              ``60``, **SHALL** add ``use_symbolic`` (default ``True``)
              to ``dic_properties``, and its ``do_set_properties()``
              **SHALL** call ``super().do_set_properties()`` and then
              apply ``use_symbolic`` through
              ``set_property("use-symbolic", ...)``.
              ``GTK3VolumeButton.__init__()`` **SHALL** accept a
              ``size`` parameter defaulting to ``4``, pass it to
              ``Gtk.VolumeButton.__init__()``, call
              ``GTK3VolumeButtonMixin.__init__()``, and store ``size``
              in ``dic_properties["size"]``.
:Rationale:   ``Gtk.VolumeButton`` is a preconfigured
              ``Gtk.ScaleButton`` with its own adjustment and volume
              icons; only the symbolic-icon setting is added.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-019`, :ref:`PTW-SR-W-004`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_volumebutton.py::TestGTK3VolumeButton::test_init``
              ``tests/gtk3/button/test_volumebutton.py::TestGTK3VolumeButton::test_do_set_attributes_default``
              ``tests/gtk3/button/test_volumebutton.py::TestGTK3VolumeButton::test_do_set_properties_default``
              ``tests/gtk3/button/test_volumebutton.py::TestGTK3VolumeButton::test_do_set_properties``
              ``tests/gtk3/button/test_volumebutton.py::TestGTK3VolumeButton::test_do_update``
              ``tests/gtk3/button/test_volumebutton.py::TestGTK3VolumeButton::test_on_changed``

----

GTK3AppChooserButton
====================

.. _PTW-GTK3-B-041:

PTW-GTK3-B-041
--------------

:Description: The ``GTK3AppChooserButton`` class **SHALL** combine
              ``Gtk.AppChooserButton`` and
              ``GTK3AppChooserButtonMixin``, which derives from
              ``GTK3ComboBoxMixin``. ``GTK3AppChooserButtonMixin``
              **SHALL** define ``_DEFAULT_HEIGHT`` as ``30`` and
              ``_DEFAULT_WIDTH`` as ``200`` and **SHALL** pre-register
              the ``"custom-item-activated"`` signal in
              ``dic_handler_id`` with a value of ``-1``.
              ``GTK3AppChooserButton.__init__()`` **SHALL** accept a
              ``heading`` parameter defaulting to ``"Choose an
              application"``, pass it to
              ``Gtk.AppChooserButton.__init__()``, call
              ``GTK3AppChooserButtonMixin.__init__()``, and store the
              heading in ``dic_properties["heading"]``.
:Rationale:   ``Gtk.AppChooserButton`` is a ``Gtk.ComboBox``
              subclass, so it reuses the combo box mixin's attributes
              and value handling.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-017`, :ref:`PTW-GTK3-W-019`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_appchooserbutton.py::TestGTK3AppChooserButton::test_init``
              ``tests/gtk3/button/test_appchooserbutton.py::TestGTK3AppChooserButton::test_do_set_attributes_default``
              ``tests/gtk3/button/test_appchooserbutton.py::TestGTK3AppChooserButton::test_do_set_attributes``
              ``tests/gtk3/button/test_appchooserbutton.py::TestGTK3AppChooserButton::test_append_custom_item``

----

.. _PTW-GTK3-B-042:

PTW-GTK3-B-042
--------------

:Description: ``GTK3AppChooserButtonMixin.__init__()`` **SHALL** add
              the following properties to ``dic_properties``:

              - ``heading``: ``None``
              - ``show_default_item``: ``False``
              - ``show_dialog_item``: ``False``

              ``GTK3AppChooserButtonMixin.do_set_properties()``
              **SHALL** call ``super().do_set_properties()`` first,
              call ``set_heading()`` only when ``heading`` is not
              ``None``, and apply ``show_default_item`` and
              ``show_dialog_item`` with their corresponding setters.
:Rationale:   Skipping a ``None`` heading preserves the heading set at
              construction.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_appchooserbutton.py::TestGTK3AppChooserButton::test_do_set_properties_default``
              ``tests/gtk3/button/test_appchooserbutton.py::TestGTK3AppChooserButton::test_do_set_properties``
