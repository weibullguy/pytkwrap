.. _gtk3_button:

================================
GTK3 Layer — Button Requirements
================================

This document defines the software requirements for the wrappers in the ``pytkwrap.gtk3.button`` package.

All requirements in this document trace to one or more system requirements defined in :ref:`system_requirements` and to GTK3 layer widget requirements defined in :ref:`gtk3_widgets`.

.. contents:: Contents
   :local:
   :depth: 1

----

Package
=======

.. _PTW-GTK3-BTN-001:

PTW-GTK3-BTN-001
----------------

:Description: The ``pytkwrap.gtk3.button`` package **SHALL** export
              ``GTK3AppChooserButton``, ``GTK3Button``,
              ``GTK3ButtonMixin``, ``GTK3CheckButton``,
              ``GTK3RadioButton``, ``GTK3ScaleButton``,
              ``GTK3SpinButton``, ``GTK3ToggleButton``,
              ``GTK3VolumeButton``, ``_AppChooserButtonHost``,
              ``_ButtonHost``, ``_RadioButtonHost``,
              ``_ScaleButtonHost``, and ``_SpinButtonHost`` through
              ``__all__``. Sub-modules of the package **SHALL** import
              sibling modules directly and **SHALL NOT** import through
              the package ``__init__.py``.
:Rationale:   A single public import location simplifies application
              code, while direct sibling imports avoid circular imports
              during package initialization.
:Traces to:   :ref:`PTW-SR-W-001`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       TBD

----

GTK3AppChooserButton
====================

.. _PTW-GTK3-BTN-002:

PTW-GTK3-BTN-002
----------------

:Description: The ``GTK3AppChooserButton`` class **SHALL** combine
              ``Gtk.AppChooserButton`` and
              ``GTK3AppChooserButtonMixin``, which derives from
              ``GTK3ComboBoxMixin``. ``GTK3AppChooserButton.__init__()``
              **SHALL** accept ``heading = 'Choose an application'`` and
              **SHALL**:

              - ``Gtk.AppChooserButton.__init__(self, heading=heading)``
              - ``GTK3AppChooserButtonMixin.__init__(self)``
              - ``dic_properties["heading"] = heading``
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_appchooserbutton.py::TestGTK3AppChooserButton::test_init``

----

.. _PTW-GTK3-BTN-003:

PTW-GTK3-BTN-003
----------------

:Description: ``GTK3AppChooserButtonMixin`` **SHALL** define
              ``_DEFAULT_HEIGHT`` as ``30``, ``_DEFAULT_WIDTH`` as
              ``200``; **SHALL** pre-register
              ``"custom-item-activated"`` in ``dic_handler_id`` with a
              value of ``-1``.
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-005`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-019`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_appchooserbutton.py::TestGTK3AppChooserButton::test_do_set_attributes``
              ``tests/gtk3/button/test_appchooserbutton.py::TestGTK3AppChooserButton::test_do_set_attributes_default``
              ``tests/gtk3/button/test_appchooserbutton.py::TestGTK3AppChooserButton::test_do_set_attributes_partial``
              ``tests/gtk3/button/test_appchooserbutton.py::TestGTK3AppChooserButton::test_init``

----

.. _PTW-GTK3-BTN-004:

PTW-GTK3-BTN-004
----------------

:Description: ``GTK3AppChooserButtonMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``heading``: ``None``
              - ``show_default_item``: ``False``
              - ``show_dialog_item``: ``False``

              ``GTK3AppChooserButtonMixin.do_set_properties()``
              **SHALL**, in order:

              - ``super().do_set_properties(properties)``
              - ``set_heading(heading)`` only if heading is not None
              - ``set_show_default_item(show_default_item)``
              - ``set_show_dialog_item(show_dialog_item)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_appchooserbutton.py::TestGTK3AppChooserButton::test_do_set_properties``
              ``tests/gtk3/button/test_appchooserbutton.py::TestGTK3AppChooserButton::test_do_set_properties_default``

----

GTK3Button
==========

.. _PTW-GTK3-BTN-005:

PTW-GTK3-BTN-005
----------------

:Description: The ``GTK3Button`` class **SHALL** combine ``Gtk.Button``
              and ``GTK3ButtonMixin``, which derives from
              ``GTK3ContainerMixin``. ``GTK3Button.__init__()``
              **SHALL** accept ``label: str = '...'`` and **SHALL**:

              - ``Gtk.Button.__init__(self, label=label)``
              - ``GTK3ButtonMixin.__init__(self)``
              - ``dic_properties["label"] = label``
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_button.py::TestButton::test_init``
              ``tests/gtk3/button/test_button.py::TestButton::test_init_with_label``
              ``tests/gtk3/button/test_button.py::TestButton::test_init_with_mnemonic``

----

.. _PTW-GTK3-BTN-006:

PTW-GTK3-BTN-006
----------------

:Description: ``GTK3ButtonMixin`` **SHALL** define ``_DEFAULT_HEIGHT``
              as ``30``, ``_DEFAULT_WIDTH`` as ``200``; **SHALL**
              pre-register ``"activate"``, ``"check-resize"``, and
              ``"clicked"`` in ``dic_handler_id`` with a value of
              ``-1``.
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-005`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-019`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_button.py::TestButton::test_do_set_attributes``
              ``tests/gtk3/button/test_button.py::TestButton::test_do_set_attributes_default``
              ``tests/gtk3/button/test_button.py::TestButton::test_do_set_attributes_partial``
              ``tests/gtk3/button/test_button.py::TestButton::test_init``

----

.. _PTW-GTK3-BTN-007:

PTW-GTK3-BTN-007
----------------

:Description: ``GTK3ButtonMixin.__init__()`` **SHALL** add the following
              properties to ``dic_properties``:

              - ``always_show_image``: ``False``
              - ``file``: ``None``
              - ``image``: ``None``
              - ``image_position``: ``Gtk.PositionType.LEFT``
              - ``label``: ``"..."``
              - ``relief``: ``Gtk.ReliefStyle.NORMAL``
              - ``use_underline``: ``False``

              ``GTK3ButtonMixin.do_set_properties()`` **SHALL**, in
              order:

              - ``super().do_set_properties(properties)``
              - ``set_always_show_image(always_show_image)``
              - ``set_relief(relief)``
              - ``set_use_underline(use_underline)``
              - ``dic_properties["label"] = ""`` only if label is None
              - ``set_label(label)``
              - ``_icon = GdkPixbuf.Pixbuf.new_from_file_at_size(file,
                height_request, width_request)`` only if file is not
                None
              - ``_image = Gtk.Image()`` only if file is not None
              - ``_image.set_from_pixbuf(_icon)`` only if file is not
                None
              - ``set_image(_image)`` only if file is not None
              - ``set_image_position(image_position)`` only if file is
                not None
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_button.py::TestButton::test_do_set_properties``
              ``tests/gtk3/button/test_button.py::TestButton::test_do_set_properties_default``

----

GTK3CheckButton
===============

.. _PTW-GTK3-BTN-008:

PTW-GTK3-BTN-008
----------------

:Description: The ``GTK3CheckButton`` class **SHALL** combine
              ``Gtk.CheckButton`` and ``GTK3CheckButtonMixin``, which
              derives from ``GTK3ToggleButtonMixin``.
              ``GTK3CheckButton.__init__()`` **SHALL** accept ``label =
              '...'`` and **SHALL**:

              - ``Gtk.CheckButton.__init__(self, label=label)``
              - ``GTK3CheckButtonMixin.__init__(self)``
              - ``dic_properties["label"] = label``
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_checkbutton.py::TestGTK3CheckButton::test_init``
              ``tests/gtk3/button/test_checkbutton.py::TestGTK3CheckButton::test_init_with_label``
              ``tests/gtk3/button/test_checkbutton.py::TestGTK3CheckButton::test_init_with_mnemonic``

----

.. _PTW-GTK3-BTN-009:

PTW-GTK3-BTN-009
----------------

:Description: ``GTK3CheckButtonMixin`` **SHALL** define
              ``_DEFAULT_HEIGHT`` as ``40``, ``_DEFAULT_WIDTH`` as
              ``200``.
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-005`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-019`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_checkbutton.py::TestGTK3CheckButton::test_do_set_attributes``
              ``tests/gtk3/button/test_checkbutton.py::TestGTK3CheckButton::test_do_set_attributes_default``
              ``tests/gtk3/button/test_checkbutton.py::TestGTK3CheckButton::test_do_set_attributes_partial``
              ``tests/gtk3/button/test_checkbutton.py::TestGTK3CheckButton::test_init``

----

GTK3RadioButton
===============

.. _PTW-GTK3-BTN-010:

PTW-GTK3-BTN-010
----------------

:Description: The ``GTK3RadioButton`` class **SHALL** combine
              ``Gtk.RadioButton`` and ``GTK3RadioButtonMixin``, which
              derives from ``GTK3CheckButtonMixin``.
              ``GTK3RadioButton.__init__()`` **SHALL** accept ``label:
              str = '...'``, ``group: Gtk.RadioButton | None = None``
              and **SHALL**:

              - ``Gtk.RadioButton.__init__(self, label=label)``
              - ``GTK3RadioButtonMixin.__init__(self)``
              - ``dic_properties["label"] = label``
              - ``join_group(group)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_radiobutton.py::TestRadioButton::test_init``
              ``tests/gtk3/button/test_radiobutton.py::TestRadioButton::test_init_with_group``
              ``tests/gtk3/button/test_radiobutton.py::TestRadioButton::test_init_with_label``
              ``tests/gtk3/button/test_radiobutton.py::TestRadioButton::test_init_with_mnemonic``

----

.. _PTW-GTK3-BTN-011:

PTW-GTK3-BTN-011
----------------

:Description: ``GTK3RadioButtonMixin`` **SHALL** define
              ``_DEFAULT_HEIGHT`` as ``40``, ``_DEFAULT_WIDTH`` as
              ``200``; **SHALL** pre-register ``"group-changed"`` in
              ``dic_handler_id`` with a value of ``-1``.
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-005`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-019`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_radiobutton.py::TestRadioButton::test_do_set_attributes``
              ``tests/gtk3/button/test_radiobutton.py::TestRadioButton::test_do_set_attributes_default``
              ``tests/gtk3/button/test_radiobutton.py::TestRadioButton::test_do_set_attributes_partial``
              ``tests/gtk3/button/test_radiobutton.py::TestRadioButton::test_init``

----

.. _PTW-GTK3-BTN-012:

PTW-GTK3-BTN-012
----------------

:Description: ``GTK3RadioButtonMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``group``: ``None``

              ``GTK3RadioButtonMixin.do_set_properties()`` **SHALL**, in
              order:

              - ``super().do_set_properties(properties)``
              - ``join_group(group)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_radiobutton.py::TestRadioButton::test_do_set_properties``
              ``tests/gtk3/button/test_radiobutton.py::TestRadioButton::test_do_set_properties_default``

----

.. _PTW-GTK3-BTN-013:

PTW-GTK3-BTN-013
----------------

:Description: The ``GTK3RadioButtonMixin.group()`` read-only property
              **SHALL** TBD. (Get the list of GTK3RadioButtons in the
              same group as self.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_radiobutton.py::TestRadioButton::test_init_with_group``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def group(self: _RadioButtonHost) -> list[Gtk.RadioButton]:
       return self.get_group()

----

GTK3ScaleButton
===============

.. _PTW-GTK3-BTN-014:

PTW-GTK3-BTN-014
----------------

:Description: The ``GTK3ScaleButton`` class **SHALL** combine
              ``Gtk.ScaleButton`` and ``GTK3ScaleButtonMixin``, which
              derives from ``GTK3ButtonMixin``.
              ``GTK3ScaleButton.__init__()`` **SHALL** accept ``icons:
              Sequence[str]``, ``size: Gtk.IconSize``, ``min_value:
              float = 0.0``, ``max_value: float = 100.0``, ``step: float
              = 2`` and **SHALL**:

              - ``_adjustment = GTK3Adjustment(min_value, min_value,
                max_value, step)``
              - ``Gtk.ScaleButton.__init__(self, adjustment=_adjustment,
                icons=icons, size=size)``
              - ``GTK3ScaleButtonMixin.__init__(self)``
              - ``dic_properties["adjustment"] = _adjustment``
              - ``dic_properties["icons"] = icons``
              - ``dic_properties["size"] = size``
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_init``
              ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_init_with_icons``
              ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_init_with_size``

----

.. _PTW-GTK3-BTN-015:

PTW-GTK3-BTN-015
----------------

:Description: ``GTK3ScaleButtonMixin`` **SHALL** define
              ``_DEFAULT_HEIGHT`` as ``30``, ``_DEFAULT_WIDTH`` as
              ``60``; **SHALL** set ``dic_attributes["default_value"]``
              to ``0.0``, ``dic_attributes["edit_signal"]`` to
              ``"value-changed"``; **SHALL** pre-register ``"popdown"``,
              ``"popup"``, and ``"value-changed"`` in ``dic_handler_id``
              with a value of ``-1``.
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-005`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-019`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_do_set_attributes``
              ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_do_set_attributes_default``
              ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_do_set_attributes_partial``
              ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_init``

----

.. _PTW-GTK3-BTN-016:

PTW-GTK3-BTN-016
----------------

:Description: ``GTK3ScaleButtonMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``adjustment``: ``GTK3Adjustment()``
              - ``icons``: ``None``
              - ``size``: ``4``
              - ``value``: ``0.0``

              ``GTK3ScaleButtonMixin.do_set_properties()`` **SHALL**, in
              order:

              - ``super().do_set_properties(properties)``
              - ``set_adjustment(adjustment)`` only if adjustment is not
                None
              - ``set_icons(icons)`` only if icons is not None and
                len(icons) > 0
              - ``set_value(value)``
              - ``set_property("size", size)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_do_set_properties``
              ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_do_set_properties_default``

----

.. _PTW-GTK3-BTN-017:

PTW-GTK3-BTN-017
----------------

:Description: The ``GTK3ScaleButtonMixin.do_get_value()`` method
              **SHALL** TBD. (Return the current value of the
              GTK3ScaleButton.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-006`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_do_get_value``
              ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_do_get_value_missing``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def do_get_value(self: _ScaleButtonHost) -> bool | date | float | int | object | str | None:
       return self.get_value()

----

.. _PTW-GTK3-BTN-018:

PTW-GTK3-BTN-018
----------------

:Description: The ``GTK3ScaleButtonMixin.do_set_value()`` method
              **SHALL** TBD. (Set the current value of the
              GTK3ScaleButton.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-007`, :ref:`PTW-COM-X-008`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_do_set_value``
              ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_do_set_value_wrong_type``
              ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_do_update``
              ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_on_changed``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def do_set_value(self: _ScaleButtonHost, value: bool | date | float | int | object | str | tuple | None) -> None:
       if not isinstance(value, (float, int, str)):
           super().do_set_value(value)
       self.dic_properties['value'] = float(value)
       self.set_value(float(value))

----

.. _PTW-GTK3-BTN-019:

PTW-GTK3-BTN-019
----------------

:Description: The ``GTK3ScaleButtonMixin.do_configure()`` method
              **SHALL** TBD. (Configure the GTK3ScaleButton's
              GTK3Adjustment.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_do_configure``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def do_configure(self: _ScaleButtonHost, value: float, lower: float, upper: float, step_increment: float, page_increment: float, page_size: float) -> None:
       self.dic_properties['value'] = value
       return self.dic_properties['adjustment'].configure(value, lower, upper, step_increment, page_increment, page_size)

----

.. _PTW-GTK3-BTN-020:

PTW-GTK3-BTN-020
----------------

:Description: The ``GTK3ScaleButtonMixin.lower()`` read-only property
              **SHALL** TBD. (Get the minimum value of the
              GTK3ScaleButton's GTK3Adjustment.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_lower``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def lower(self: _ScaleButtonHost) -> float:
       return self.dic_properties['adjustment'].get_lower()

----

.. _PTW-GTK3-BTN-021:

PTW-GTK3-BTN-021
----------------

:Description: The ``GTK3ScaleButtonMixin.minus_button()`` read-only
              property **SHALL** TBD. (Get the minus button of the
              GTK3ScaleButton.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_minus_button``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def minus_button(self: _ScaleButtonHost) -> Gtk.Button:
       return self.get_minus_button()

----

.. _PTW-GTK3-BTN-022:

PTW-GTK3-BTN-022
----------------

:Description: The ``GTK3ScaleButtonMixin.page_increment()`` read-only
              property **SHALL** TBD. (Get the page increment of the
              GTK3ScaleButton's GTK3Adjustment.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_page_increment``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def page_increment(self: _ScaleButtonHost) -> float:
       return self.dic_properties['adjustment'].get_page_increment()

----

.. _PTW-GTK3-BTN-023:

PTW-GTK3-BTN-023
----------------

:Description: The ``GTK3ScaleButtonMixin.page_size()`` read-only
              property **SHALL** TBD. (Get the page size of the
              GTK3ScaleButton's GTK3Adjustment.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_page_size``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def page_size(self: _ScaleButtonHost) -> float:
       return self.dic_properties['adjustment'].get_page_size()

----

.. _PTW-GTK3-BTN-024:

PTW-GTK3-BTN-024
----------------

:Description: The ``GTK3ScaleButtonMixin.plus_button()`` read-only
              property **SHALL** TBD. (Get the plus button of the
              GTK3ScaleButton.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_plus_button``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def plus_button(self: _ScaleButtonHost) -> Gtk.Button:
       return self.get_plus_button()

----

.. _PTW-GTK3-BTN-025:

PTW-GTK3-BTN-025
----------------

:Description: The ``GTK3ScaleButtonMixin.popup()`` read-only property
              **SHALL** TBD. (Get the popup of the GTK3ScaleButton.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_popup``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def popup(self: _ScaleButtonHost) -> Gtk.Widget:
       return self.get_popup()

----

.. _PTW-GTK3-BTN-026:

PTW-GTK3-BTN-026
----------------

:Description: The ``GTK3ScaleButtonMixin.step_increment()`` read-only
              property **SHALL** TBD. (Get the step increment of the
              GTK3ScaleButton's GTK3Adjustment.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_step_increment``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def step_increment(self: _ScaleButtonHost) -> float:
       return self.dic_properties['adjustment'].get_step_increment()

----

.. _PTW-GTK3-BTN-027:

PTW-GTK3-BTN-027
----------------

:Description: The ``GTK3ScaleButtonMixin.upper()`` read-only property
              **SHALL** TBD. (Get the maximum value of the
              GTK3ScaleButton's GTK3Adjustment.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_scalebutton.py::TestGTK3ScaleButton::test_upper``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def upper(self: _ScaleButtonHost) -> float:
       return self.dic_properties['adjustment'].get_upper()

----

GTK3SpinButton
==============

.. _PTW-GTK3-BTN-028:

PTW-GTK3-BTN-028
----------------

:Description: The ``GTK3SpinButton`` class **SHALL** combine
              ``Gtk.SpinButton`` and ``GTK3SpinButtonMixin``, which
              derives from ``GTK3EntryMixin``.
              ``GTK3SpinButton.__init__()`` **SHALL** accept
              ``adjustment: Gtk.Adjustment | None = None``,
              ``climb_rate: float = 0.0``, ``digits: int = 1`` and
              **SHALL**:

              - ``Gtk.SpinButton.__init__(self, adjustment=adjustment,
                climb_rate=climb_rate, digits=digits)``
              - ``GTK3SpinButtonMixin.__init__(self)``
              - ``dic_attributes["format"] = f"{{:3.{digits}f}}"``
              - ``dic_properties["adjustment"] = adjustment``
              - ``dic_properties["climb_rate"] = climb_rate``
              - ``dic_properties["digits"] = digits``
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_init``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_init_with_adjustment``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_init_with_climb_rate``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_init_with_digits``

----

.. _PTW-GTK3-BTN-029:

PTW-GTK3-BTN-029
----------------

:Description: ``GTK3SpinButtonMixin`` **SHALL** set
              ``dic_attributes["data_type"]`` to ``float``,
              ``dic_attributes["default_value"]`` to ``0.0``,
              ``dic_attributes["edit_signal"]`` to ``"value-changed"``,
              ``dic_attributes["format"]`` to ``"{:3.1f}"``; **SHALL**
              pre-register ``"change-value"``, ``"input"``,
              ``"output"``, ``"value-changed"``, and ``"wrapped"`` in
              ``dic_handler_id`` with a value of ``-1``.
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-005`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-019`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_set_attributes``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_set_attributes_default``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_set_attributes_partial``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_init``

----

.. _PTW-GTK3-BTN-030:

PTW-GTK3-BTN-030
----------------

:Description: ``GTK3SpinButtonMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``adjustment``: ``GTK3Adjustment()``
              - ``climb_rate``: ``0.0``
              - ``digits``: ``0``
              - ``lower``: ``0.0``
              - ``numeric``: ``False``
              - ``page_increment``: ``0.0``
              - ``page_size``: ``0.0``
              - ``snap_to_ticks``: ``False``
              - ``step_increment``: ``0.0``
              - ``update_policy``: ``Gtk.SpinButtonUpdatePolicy.ALWAYS``
              - ``upper``: ``0.0``
              - ``value``: ``0.0``
              - ``wrap``: ``False``

              ``GTK3SpinButtonMixin.do_set_properties()`` **SHALL**, in
              order:

              - ``super().do_set_properties(properties)``
              - ``dic_properties["page_increment"] =
                adjustment.get_page_increment()`` only if
                isinstance(adjustment, Gtk.Adjustment)
              - ``dic_properties["page_size"] =
                adjustment.get_page_size()`` only if
                isinstance(adjustment, Gtk.Adjustment)
              - ``dic_properties["step_increment"] =
                adjustment.get_step_increment()`` only if
                isinstance(adjustment, Gtk.Adjustment)
              - ``dic_properties["lower"] = adjustment.get_lower()``
                only if isinstance(adjustment, Gtk.Adjustment)
              - ``dic_properties["upper"] = adjustment.get_upper()``
                only if isinstance(adjustment, Gtk.Adjustment)
              - ``set_adjustment(adjustment)`` only if
                isinstance(adjustment, Gtk.Adjustment)
              - ``set_increments(step_increment, page_increment)`` only
                not (isinstance(adjustment, Gtk.Adjustment))
              - ``set_range(lower, upper)`` only not
                (isinstance(adjustment, Gtk.Adjustment))
              - ``set_digits(digits)``
              - ``set_numeric(numeric)``
              - ``set_snap_to_ticks(snap_to_ticks)``
              - ``set_update_policy(update_policy)``
              - ``set_value(value)``
              - ``set_wrap(wrap)``
              - ``set_property("climb-rate", climb_rate)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_set_properties``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_set_properties_default``

----

.. _PTW-GTK3-BTN-031:

PTW-GTK3-BTN-031
----------------

:Description: The ``GTK3SpinButtonMixin.do_get_value()`` method
              **SHALL** TBD. (Return the value of the GTK3SpinButton.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-006`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_get_value``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_get_value_int``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_get_value_missing``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_get_value_str``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def do_get_value(self: _SpinButtonHost) -> float | int:
       return self.dic_attributes['data_type'](self.get_value())

----

.. _PTW-GTK3-BTN-032:

PTW-GTK3-BTN-032
----------------

:Description: The ``GTK3SpinButtonMixin.do_set_value()`` method
              **SHALL** TBD. (Set the value of the GTK3SpinButton.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-007`, :ref:`PTW-COM-X-008`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_set_value``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_set_value_int``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_set_value_str``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_set_value_wrong_type``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_update``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_on_changed``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def do_set_value(self: _SpinButtonHost, value: bool | date | float | int | object | str | tuple | None=None) -> None:
       if not isinstance(value, (float, int, str)):
           super().do_set_value(value)
       self.set_value(self.dic_attributes['data_type'](value))

----

.. _PTW-GTK3-BTN-033:

PTW-GTK3-BTN-033
----------------

:Description: The ``GTK3SpinButtonMixin.do_configure()`` method
              **SHALL** TBD. ((Re)configure the GTK3SpinButton.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_configure``
              ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_do_configure_same_adjustment``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def do_configure(self: _SpinButtonHost, adjustment: GTK3Adjustment | None, climb_rate: float, digits: int) -> None:
       if adjustment is not None:
           self.dic_properties['adjustment'] = adjustment
       self.dic_properties['climb_rate'] = climb_rate
       self.dic_properties['digits'] = digits
       self.dic_attributes['format'] = f'{{:3.{digits}f}}'
       self.configure(adjustment, climb_rate, digits)

----

.. _PTW-GTK3-BTN-034:

PTW-GTK3-BTN-034
----------------

:Description: The ``GTK3SpinButtonMixin.increments()`` read-only
              property **SHALL** TBD. (Get the step and page increments
              for the embedded GTK3Adjustment.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_increments``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def increments(self: _SpinButtonHost) -> tuple[float | None, float | None]:
       return self.get_increments()

----

.. _PTW-GTK3-BTN-035:

PTW-GTK3-BTN-035
----------------

:Description: The ``GTK3SpinButtonMixin.lower()`` read-only property
              **SHALL** TBD. (Get the current minimum value of the
              GTK3SpinButton.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_lower``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def lower(self: _SpinButtonHost) -> float:
       return self.get_adjustment().get_lower()

----

.. _PTW-GTK3-BTN-036:

PTW-GTK3-BTN-036
----------------

:Description: The ``GTK3SpinButtonMixin.page_increment()`` read-only
              property **SHALL** TBD. (Get the current page increment
              value of the GTK3SpinButton.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_page_increment``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def page_increment(self: _SpinButtonHost) -> float:
       return self.get_adjustment().get_page_increment()

----

.. _PTW-GTK3-BTN-037:

PTW-GTK3-BTN-037
----------------

:Description: The ``GTK3SpinButtonMixin.range()`` read-only property
              **SHALL** TBD. (Get the minimum and maximum values for the
              embedded GTK3Adjustment.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_range``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def range(self: _SpinButtonHost) -> tuple[float | None, float | None]:
       return self.get_range()

----

.. _PTW-GTK3-BTN-038:

PTW-GTK3-BTN-038
----------------

:Description: The ``GTK3SpinButtonMixin.step_increment()`` read-only
              property **SHALL** TBD. (Get the current step increment
              value of the GTK3SpinButton.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_step_increment``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def step_increment(self: _SpinButtonHost) -> float:
       return self.get_adjustment().get_step_increment()

----

.. _PTW-GTK3-BTN-039:

PTW-GTK3-BTN-039
----------------

:Description: The ``GTK3SpinButtonMixin.upper()`` read-only property
              **SHALL** TBD. (Get the current maximum value of the
              GTK3SpinButton.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_spinbutton.py::TestGTK3SpinButton::test_upper``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def upper(self: _SpinButtonHost) -> float:
       return self.get_adjustment().get_upper()

----

GTK3ToggleButton
================

.. _PTW-GTK3-BTN-040:

PTW-GTK3-BTN-040
----------------

:Description: The ``GTK3ToggleButton`` class **SHALL** combine
              ``Gtk.ToggleButton`` and ``GTK3ToggleButtonMixin``, which
              derives from ``GTK3ButtonMixin``.
              ``GTK3ToggleButton.__init__()`` **SHALL** accept ``label:
              str = '...'`` and **SHALL**:

              - ``Gtk.ToggleButton.__init__(self, label=label)``
              - ``GTK3ToggleButtonMixin.__init__(self)``
              - ``dic_properties["label"] = label``
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_init``
              ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_init_with_label``
              ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_init_with_mnemonic``

----

.. _PTW-GTK3-BTN-041:

PTW-GTK3-BTN-041
----------------

:Description: ``GTK3ToggleButtonMixin`` **SHALL** define
              ``_DEFAULT_HEIGHT`` as ``30``, ``_DEFAULT_WIDTH`` as
              ``200``; **SHALL** set ``dic_attributes["default_value"]``
              to ``False``, ``dic_attributes["edit_signal"]`` to
              ``"toggled"``; **SHALL** pre-register ``"toggled"`` in
              ``dic_handler_id`` with a value of ``-1``.
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-005`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-019`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_do_set_attributes``
              ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_do_set_attributes_default``
              ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_do_set_attributes_partial``
              ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_init``

----

.. _PTW-GTK3-BTN-042:

PTW-GTK3-BTN-042
----------------

:Description: ``GTK3ToggleButtonMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``active``: ``False``
              - ``draw_indicator``: ``False``
              - ``inconsistent``: ``False``

              ``GTK3ToggleButtonMixin.do_set_properties()`` **SHALL**,
              in order:

              - ``super().do_set_properties(properties)``
              - ``set_active(active)``
              - ``set_inconsistent(inconsistent)``
              - ``set_mode(draw_indicator)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_do_set_properties``
              ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_do_set_properties_default``

----

.. _PTW-GTK3-BTN-043:

PTW-GTK3-BTN-043
----------------

:Description: The ``GTK3ToggleButtonMixin.do_get_value()`` method
              **SHALL** TBD. (Return the current value of the
              GTK3ToggleButton.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-006`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_do_get_value``
              ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_do_get_value_missing``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def do_get_value(self: _ToggleButtonHost) -> bool | date | float | int | object | str | None:
       return self.get_active()

----

.. _PTW-GTK3-BTN-044:

PTW-GTK3-BTN-044
----------------

:Description: The ``GTK3ToggleButtonMixin.do_set_value()`` method
              **SHALL** TBD. (Set the current value of the
              GTK3ToggleButton.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-007`, :ref:`PTW-COM-X-008`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_do_set_value``
              ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_do_set_value_wrong_type``
              ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_do_update``
              ``tests/gtk3/button/test_togglebutton.py::TestGTK3ToggleButton::test_on_changed``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def do_set_value(self: _ToggleButtonHost, value: bool | date | float | int | object | str | tuple | None) -> None:
       if not isinstance(value, (bool, float, int)):
           super().do_set_value(value)
       self.dic_properties['active'] = bool(value)
       self.set_active(bool(value))

----

GTK3VolumeButton
================

.. _PTW-GTK3-BTN-045:

PTW-GTK3-BTN-045
----------------

:Description: The ``GTK3VolumeButton`` class **SHALL** combine
              ``Gtk.VolumeButton`` and ``GTK3VolumeButtonMixin``, which
              derives from ``GTK3ScaleButtonMixin``.
              ``GTK3VolumeButton.__init__()`` **SHALL** accept ``size:
              Gtk.IconSize = Gtk.IconSize.BUTTON`` and **SHALL**:

              - ``Gtk.VolumeButton.__init__(self, size=size)``
              - ``GTK3VolumeButtonMixin.__init__(self)``
              - ``dic_properties["size"] = size``
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_volumebutton.py::TestGTK3VolumeButton::test_init``

----

.. _PTW-GTK3-BTN-046:

PTW-GTK3-BTN-046
----------------

:Description: ``GTK3VolumeButtonMixin`` **SHALL** define
              ``_DEFAULT_HEIGHT`` as ``30``, ``_DEFAULT_WIDTH`` as
              ``60``.
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-005`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-019`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_volumebutton.py::TestGTK3VolumeButton::test_do_set_attributes``
              ``tests/gtk3/button/test_volumebutton.py::TestGTK3VolumeButton::test_do_set_attributes_default``
              ``tests/gtk3/button/test_volumebutton.py::TestGTK3VolumeButton::test_do_set_attributes_partial``
              ``tests/gtk3/button/test_volumebutton.py::TestGTK3VolumeButton::test_init``

----

.. _PTW-GTK3-BTN-047:

PTW-GTK3-BTN-047
----------------

:Description: ``GTK3VolumeButtonMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``use_symbolic``: ``True``

              ``GTK3VolumeButtonMixin.do_set_properties()`` **SHALL**,
              in order:

              - ``super().do_set_properties(properties)``
              - ``set_property("use-symbolic", use_symbolic)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-15) - Initial baseline.
:Tests:       ``tests/gtk3/button/test_volumebutton.py::TestGTK3VolumeButton::test_do_set_properties``
              ``tests/gtk3/button/test_volumebutton.py::TestGTK3VolumeButton::test_do_set_properties_default``
