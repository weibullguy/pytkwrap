.. _gtk3_container:

===================================
GTK3 Layer — Container Requirements
===================================

This document defines the software requirements for the wrappers in the ``pytkwrap.gtk3.container`` package.

All requirements in this document trace to one or more system requirements defined in :ref:`system_requirements` and to GTK3 layer widget requirements defined in :ref:`gtk3_widgets`.

.. contents:: Contents
   :local:
   :depth: 1

----

Package
=======

.. _PTW-GTK3-CON-001:

PTW-GTK3-CON-001
----------------

:Description: The ``pytkwrap.gtk3.container`` package **SHALL** export
              ``GTK3Bin``, ``GTK3Box``, ``GTK3ButtonBox``,
              ``GTK3Container``, ``GTK3ContainerMixin``,
              ``GTK3Expander``, ``GTK3Frame``, ``GTK3ListBox``,
              ``GTK3Paned``, ``GTK3Revealer``, ``GTK3Socket``,
              ``GTK3Stack``, ``GTK3StackSidebar``,
              ``GTK3StackSwitcher``, ``GTK3Viewport``, ``_BoxHost``,
              ``_ButtonBoxHost``, ``_ContainerHost``, ``_ExpanderHost``,
              ``_FrameHost``, ``_ListBoxHost``, ``_PanedHost``,
              ``_RevealerHost``, ``_SocketHost``, ``_StackHost``,
              ``_StackSidebarHost``, ``_StackSwitcherHost``,
              ``_ViewportHost``, and ``do_make_buttonbox`` through
              ``__all__``. Sub-modules of the package **SHALL** import
              sibling modules directly and **SHALL NOT** import through
              the package ``__init__.py``.
:Rationale:   A single public import location simplifies application
              code, while direct sibling imports avoid circular imports
              during package initialization.
:Traces to:   :ref:`PTW-SR-W-001`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       TBD

----

do_make_buttonbox
=================

.. _PTW-GTK3-CON-002:

PTW-GTK3-CON-002
----------------

:Description: ``do_make_buttonbox(icons: list[str], tooltips: list[str],
              callbacks: list[Callable], height: int=-1, layout:
              Gtk.ButtonBoxStyle=Gtk.ButtonBoxStyle.START, orientation:
              str='horizontal', width: int=-1) -> GTK3ButtonBox``
              **SHALL** TBD. (Create a buttonbox for views.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-001`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       TBD

----

GTK3Bin
=======

.. _PTW-GTK3-CON-003:

PTW-GTK3-CON-003
----------------

:Description: The ``GTK3Bin`` class **SHALL** combine ``Gtk.Bin`` and
              ``GTK3ContainerMixin``, which derives from
              ``GTK3WidgetMixin``. ``GTK3Bin.__init__()`` **SHALL**
              accept no parameters and **SHALL**:

              - ``Gtk.Bin.__init__(self)``
              - ``GTK3ContainerMixin.__init__(self)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_bin.py::TestGTK3Bin::test_init``

----

.. _PTW-GTK3-CON-004:

PTW-GTK3-CON-004
----------------

:Description: ``GTK3ContainerMixin`` **SHALL** pre-register ``"add"``,
              ``"check-resize"``, ``"remove"``, and
              ``"set-focus-child"`` in ``dic_handler_id`` with a value
              of ``-1``.
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-005`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-019`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_bin.py::TestGTK3Bin::test_do_set_attributes``
              ``tests/gtk3/container/test_bin.py::TestGTK3Bin::test_do_set_attributes_default``
              ``tests/gtk3/container/test_bin.py::TestGTK3Bin::test_do_set_attributes_partial``
              ``tests/gtk3/container/test_bin.py::TestGTK3Bin::test_init``

----

.. _PTW-GTK3-CON-005:

PTW-GTK3-CON-005
----------------

:Description: ``GTK3ContainerMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``border_width``: ``0``

              ``GTK3ContainerMixin.do_set_properties()`` **SHALL**, in
              order:

              - ``super().do_set_properties(properties)``
              - ``set_border_width(border_width)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_bin.py::TestGTK3Bin::test_do_set_properties``
              ``tests/gtk3/container/test_bin.py::TestGTK3Bin::test_do_set_properties_default``

----

GTK3Box
=======

.. _PTW-GTK3-CON-006:

PTW-GTK3-CON-006
----------------

:Description: The ``GTK3Box`` class **SHALL** combine ``Gtk.Box`` and
              ``GTK3BoxMixin``, which derives from
              ``GTK3ContainerMixin``. ``GTK3Box.__init__()`` **SHALL**
              accept ``orientation: Gtk.Orientation =
              Gtk.Orientation.HORIZONTAL``, ``spacing: int = 0`` and
              **SHALL**:

              - ``Gtk.Box.__init__(self, orientation=orientation,
                spacing=spacing)``
              - ``GTK3BoxMixin.__init__(self)``
              - ``dic_properties["spacing"] = spacing``
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_box.py::TestGTK3Box::test_init``
              ``tests/gtk3/container/test_box.py::TestGTK3Box::test_init_with_orientation``
              ``tests/gtk3/container/test_box.py::TestGTK3Box::test_init_with_spacing``

----

.. _PTW-GTK3-CON-007:

PTW-GTK3-CON-007
----------------

:Description: ``GTK3BoxMixin.__init__()`` **SHALL** add the following
              properties to ``dic_properties``:

              - ``baseline_position``: ``Gtk.BaselinePosition.CENTER``
              - ``center_widget``: ``None``
              - ``homogeneous``: ``False``
              - ``spacing``: ``0``

              ``GTK3BoxMixin.do_set_properties()`` **SHALL**, in order:

              - ``super().do_set_properties(properties)``
              - ``set_baseline_position(baseline_position)``
              - ``set_center_widget(center_widget)``
              - ``set_homogeneous(homogeneous)``
              - ``set_spacing(spacing)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_box.py::TestGTK3Box::test_do_set_properties``
              ``tests/gtk3/container/test_box.py::TestGTK3Box::test_do_set_properties_default``

----

.. _PTW-GTK3-CON-008:

PTW-GTK3-CON-008
----------------

:Description: The ``GTK3BoxMixin.do_add_child()`` method **SHALL** TBD.
              (Add a child widget to the GTK3Box.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_box.py::TestGTK3Box::test_add_child_end``
              ``tests/gtk3/container/test_box.py::TestGTK3Box::test_add_child_start``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def do_add_child(self: _BoxHost, child: GTK3Widget, expand: bool, fill: bool, padding: int, start: bool=True) -> None:
       if start:
           return self.pack_start(child, expand, fill, padding)
       return self.pack_end(child, expand, fill, padding)

----

.. _PTW-GTK3-CON-009:

PTW-GTK3-CON-009
----------------

:Description: The ``GTK3BoxMixin.children()`` read-only property
              **SHALL** TBD. (Get the list of child widgets for the
              GTK3Box.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       TBD

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def children(self: _BoxHost) -> list[Gtk.Widget]:
       return self.get_children()

----

GTK3ButtonBox
=============

.. _PTW-GTK3-CON-010:

PTW-GTK3-CON-010
----------------

:Description: The ``GTK3ButtonBox`` class **SHALL** combine
              ``Gtk.ButtonBox`` and ``GTK3ButtonBoxMixin``, which
              derives from ``GTK3BoxMixin``.
              ``GTK3ButtonBox.__init__()`` **SHALL** accept
              ``orientation: Gtk.Orientation =
              Gtk.Orientation.HORIZONTAL`` and **SHALL**:

              - ``Gtk.ButtonBox.__init__(self,
                orientation=orientation)``
              - ``GTK3ButtonBoxMixin.__init__(self)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_buttonbox.py::TestGTK3ButtonBox::test_init``
              ``tests/gtk3/container/test_buttonbox.py::TestGTK3ButtonBox::test_init_with_orientation``

----

.. _PTW-GTK3-CON-011:

PTW-GTK3-CON-011
----------------

:Description: ``GTK3ButtonBoxMixin`` **SHALL** set
              ``dic_attributes["orientation"]`` to
              ``Gtk.Orientation.HORIZONTAL``.
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-005`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-019`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_buttonbox.py::TestGTK3ButtonBox::test_do_set_attributes``
              ``tests/gtk3/container/test_buttonbox.py::TestGTK3ButtonBox::test_do_set_attributes_default``
              ``tests/gtk3/container/test_buttonbox.py::TestGTK3ButtonBox::test_do_set_attributes_partial``
              ``tests/gtk3/container/test_buttonbox.py::TestGTK3ButtonBox::test_init``

----

.. _PTW-GTK3-CON-012:

PTW-GTK3-CON-012
----------------

:Description: ``GTK3ButtonBoxMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``layout_style``: ``Gtk.ButtonBoxStyle.END``

              ``GTK3ButtonBoxMixin.do_set_properties()`` **SHALL**, in
              order:

              - ``super().do_set_properties(properties)``
              - ``set_layout(layout_style)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_buttonbox.py::TestGTK3ButtonBox::test_do_set_properties``
              ``tests/gtk3/container/test_buttonbox.py::TestGTK3ButtonBox::test_do_set_properties_default``

----

.. _PTW-GTK3-CON-013:

PTW-GTK3-CON-013
----------------

:Description: The ``GTK3ButtonBoxMixin.do_get_attribute()`` method
              **SHALL** TBD. (Get the value of the requested
              GTK3TreeModel attribute.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_buttonbox.py::TestGTK3ButtonBox::test_do_get_attribute``
              ``tests/gtk3/container/test_buttonbox.py::TestGTK3ButtonBox::test_do_get_attribute_unknown``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def do_get_attribute(self: _ButtonBoxHost, attribute: str) -> bool | date | float | int | object | str | None:
       if attribute in self.dic_attributes:
           return self.dic_attributes.get(attribute)
       return super().do_get_attribute(attribute)

----

.. _PTW-GTK3-CON-014:

PTW-GTK3-CON-014
----------------

:Description: The ``GTK3ButtonBoxMixin.do_set_attributes()`` method
              **SHALL** TBD. (Set the GTK3ButtonBox attributes.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_buttonbox.py::TestGTK3ButtonBox::test_do_set_attributes``
              ``tests/gtk3/container/test_buttonbox.py::TestGTK3ButtonBox::test_do_set_attributes_default``
              ``tests/gtk3/container/test_buttonbox.py::TestGTK3ButtonBox::test_do_set_attributes_partial``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def do_set_attributes(self: _ButtonBoxHost, attributes: GTK3WidgetAttributes) -> None:
       super().do_set_attributes(attributes)
       self.dic_attributes['orientation'] = attributes.get('orientation', self.dic_attributes['orientation'])

----

.. _PTW-GTK3-CON-015:

PTW-GTK3-CON-015
----------------

:Description: The ``GTK3ButtonBoxMixin.children()`` read-only property
              **SHALL** TBD. (Get the list of child widgets in the
              GTK3ButtonBox.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       TBD

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def children(self: _ButtonBoxHost) -> list[Gtk.Widget]:
       return self.get_children()

----

GTK3Container
=============

.. _PTW-GTK3-CON-016:

PTW-GTK3-CON-016
----------------

:Description: The ``GTK3Container`` class **SHALL** combine
              ``Gtk.Container`` and ``GTK3ContainerMixin``, which
              derives from ``GTK3WidgetMixin``.
              ``GTK3Container.__init__()`` **SHALL** accept no
              parameters and **SHALL**:

              - ``Gtk.Container.__init__(self)``
              - ``GTK3ContainerMixin.__init__(self)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_container.py::TestGTK3Container::test_init``

----

.. _PTW-GTK3-CON-017:

PTW-GTK3-CON-017
----------------

:Description: ``GTK3ContainerMixin`` **SHALL** pre-register ``"add"``,
              ``"check-resize"``, ``"remove"``, and
              ``"set-focus-child"`` in ``dic_handler_id`` with a value
              of ``-1``.
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-005`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-019`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_container.py::TestGTK3Container::test_do_set_attributes``
              ``tests/gtk3/container/test_container.py::TestGTK3Container::test_do_set_attributes_default``
              ``tests/gtk3/container/test_container.py::TestGTK3Container::test_do_set_attributes_partial``
              ``tests/gtk3/container/test_container.py::TestGTK3Container::test_init``

----

.. _PTW-GTK3-CON-018:

PTW-GTK3-CON-018
----------------

:Description: ``GTK3ContainerMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``border_width``: ``0``

              ``GTK3ContainerMixin.do_set_properties()`` **SHALL**, in
              order:

              - ``super().do_set_properties(properties)``
              - ``set_border_width(border_width)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_container.py::TestGTK3Container::test_do_set_properties``
              ``tests/gtk3/container/test_container.py::TestGTK3Container::test_do_set_properties_default``

----

GTK3Expander
============

.. _PTW-GTK3-CON-019:

PTW-GTK3-CON-019
----------------

:Description: The ``GTK3Expander`` class **SHALL** combine
              ``Gtk.Expander`` and ``GTK3ExpanderMixin``, which derives
              from ``GTK3ContainerMixin``. ``GTK3Expander.__init__()``
              **SHALL** accept ``label: str | None = None`` and
              **SHALL**:

              - ``Gtk.Expander.__init__(self, label=label)``
              - ``GTK3ExpanderMixin.__init__(self)``
              - ``dic_properties["label"] = label``
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_expander.py::TestGTK3Expander::test_init``
              ``tests/gtk3/container/test_expander.py::TestGTK3Expander::test_init_with_label``
              ``tests/gtk3/container/test_expander.py::TestGTK3Expander::test_init_with_mnemonic``

----

.. _PTW-GTK3-CON-020:

PTW-GTK3-CON-020
----------------

:Description: ``GTK3ExpanderMixin`` **SHALL** pre-register
              ``"activate"`` in ``dic_handler_id`` with a value of
              ``-1``.
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-005`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-019`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_expander.py::TestGTK3Expander::test_do_set_attributes``
              ``tests/gtk3/container/test_expander.py::TestGTK3Expander::test_do_set_attributes_default``
              ``tests/gtk3/container/test_expander.py::TestGTK3Expander::test_do_set_attributes_partial``
              ``tests/gtk3/container/test_expander.py::TestGTK3Expander::test_init``

----

.. _PTW-GTK3-CON-021:

PTW-GTK3-CON-021
----------------

:Description: ``GTK3ExpanderMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``expanded``: ``False``
              - ``label``: ``None``
              - ``label_fill``: ``False``
              - ``label_widget``: ``None``
              - ``resize_toplevel``: ``False``
              - ``use_markup``: ``False``
              - ``use_underline``: ``False``

              ``GTK3ExpanderMixin.do_set_properties()`` **SHALL**, in
              order:

              - ``super().do_set_properties(properties)``
              - ``set_expanded(expanded)``
              - ``set_label(label)``
              - ``set_label_fill(label_fill)``
              - ``set_label_widget(label_widget)``
              - ``set_resize_toplevel(resize_toplevel)``
              - ``set_use_markup(use_markup)``
              - ``set_use_underline(use_underline)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_expander.py::TestGTK3Expander::test_do_set_properties``
              ``tests/gtk3/container/test_expander.py::TestGTK3Expander::test_do_set_properties_default``

----

GTK3Frame
=========

.. _PTW-GTK3-CON-022:

PTW-GTK3-CON-022
----------------

:Description: The ``GTK3Frame`` class **SHALL** combine ``Gtk.Frame``
              and ``GTK3FrameMixin``, which derives from
              ``GTK3ContainerMixin``. ``GTK3Frame.__init__()`` **SHALL**
              accept ``label: str | None = None`` and **SHALL**:

              - ``Gtk.Frame.__init__(self, label=label)``
              - ``GTK3FrameMixin.__init__(self)``
              - ``dic_properties["label"] = label``
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_frame.py::TestFrame::test_init``
              ``tests/gtk3/container/test_frame.py::TestFrame::test_init_with_label``

----

.. _PTW-GTK3-CON-023:

PTW-GTK3-CON-023
----------------

:Description: ``GTK3FrameMixin.__init__()`` **SHALL** add the following
              properties to ``dic_properties``:

              - ``label``: ``None``
              - ``label_widget``: ``None``
              - ``label_xalign``: ``0.0``
              - ``label_yalign``: ``0.5``
              - ``shadow_type``: ``Gtk.ShadowType.ETCHED_IN``

              ``GTK3FrameMixin.do_set_properties()`` **SHALL**, in
              order:

              - ``super().do_set_properties(properties)``
              - ``set_label_widget(label_widget)`` only if label_widget
                is not None
              - ``set_label(label)`` only if label is not None
              - ``set_label_align(label_xalign, label_yalign)``
              - ``set_shadow_type(shadow_type)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_frame.py::TestFrame::test_do_set_properties``
              ``tests/gtk3/container/test_frame.py::TestFrame::test_do_set_properties_default``

----

GTK3ListBox
===========

.. _PTW-GTK3-CON-024:

PTW-GTK3-CON-024
----------------

:Description: The ``GTK3ListBox`` class **SHALL** combine
              ``Gtk.ListBox`` and ``GTK3ListBoxMixin``, which derives
              from ``GTK3ContainerMixin``. ``GTK3ListBox.__init__()``
              **SHALL** accept ``adjustment: GTK3Adjustment | None =
              None`` and **SHALL**:

              - ``Gtk.ListBox.__init__(self)``
              - ``GTK3ListBoxMixin.__init__(self)``
              - ``dic_properties["adjustment"] = adjustment`` only if
                adjustment is not None
              - ``do_set_properties(self.dic_properties)`` only if
                adjustment is not None
              - ``dic_properties["adjustment"] = self.get_adjustment()``
                only not (adjustment is not None)
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_listbox.py::TestGTK3ListBox::test_init``
              ``tests/gtk3/container/test_listbox.py::TestGTK3ListBox::test_init_with_adjustment``

----

.. _PTW-GTK3-CON-025:

PTW-GTK3-CON-025
----------------

:Description: ``GTK3ListBoxMixin`` **SHALL** pre-register
              ``"activate-cursor-row"``, ``"move-cursor"``,
              ``"row-activated"``, ``"row-selected"``, ``"select-all"``,
              ``"selected-rows-changed"``, ``"toggle-cursor-row"``, and
              ``"unselect-all"`` in ``dic_handler_id`` with a value of
              ``-1``.
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-005`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-019`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_listbox.py::TestGTK3ListBox::test_do_set_attributes``
              ``tests/gtk3/container/test_listbox.py::TestGTK3ListBox::test_do_set_attributes_default``
              ``tests/gtk3/container/test_listbox.py::TestGTK3ListBox::test_do_set_attributes_partial``
              ``tests/gtk3/container/test_listbox.py::TestGTK3ListBox::test_init``

----

.. _PTW-GTK3-CON-026:

PTW-GTK3-CON-026
----------------

:Description: ``GTK3ListBoxMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``activate_on_single_click``: ``True``
              - ``adjustment``: ``GTK3Adjustment()``
              - ``selection_mode``: ``Gtk.SelectionMode.SINGLE``

              ``GTK3ListBoxMixin.do_set_properties()`` **SHALL**, in
              order:

              - ``super().do_set_properties(properties)``
              -
                ``set_activate_on_single_click(activate_on_single_click)``
              - ``set_adjustment(adjustment)``
              - ``set_selection_mode(selection_mode)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_listbox.py::TestGTK3ListBox::test_do_set_properties``
              ``tests/gtk3/container/test_listbox.py::TestGTK3ListBox::test_do_set_properties_default``

----

.. _PTW-GTK3-CON-027:

PTW-GTK3-CON-027
----------------

:Description: The ``GTK3ListBoxMixin.do_add_child()`` method **SHALL**
              TBD. (Add a child widget to the GTK3ListBox.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_listbox.py::TestGTK3ListBox::test_do_add_child``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def do_add_child(self: _ListBoxHost, child: Gtk.Widget, position: int | None=None) -> None:
       if position is None:
           self.prepend(child)
       else:
           self.insert(child, position)

----

.. _PTW-GTK3-CON-028:

PTW-GTK3-CON-028
----------------

:Description: The ``GTK3ListBoxMixin.do_get_row()`` method **SHALL**
              TBD. (Get the requested row from the GTK3ListBox.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_listbox.py::TestGTK3ListBox::test_do_get_row_at_index``
              ``tests/gtk3/container/test_listbox.py::TestGTK3ListBox::test_do_get_row_at_y``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def do_get_row(self: _ListBoxHost, index: int | None=None, y: int | None=None) -> Gtk.ListBoxRow | None:
       if index is not None:
           return self.get_row_at_index(index)
       if y is not None:
           return self.get_row_at_y(y)
       return None

----

.. _PTW-GTK3-CON-029:

PTW-GTK3-CON-029
----------------

:Description: The ``GTK3ListBoxMixin.do_get_selected()`` method
              **SHALL** TBD. (Get the currently selected row or group of
              rows.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       TBD

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def do_get_selected(self: _ListBoxHost) -> list[Gtk.ListBoxRow]:
       return self.get_selected_rows()

----

.. _PTW-GTK3-CON-030:

PTW-GTK3-CON-030
----------------

:Description: The ``GTK3ListBoxMixin.do_select_row()`` method **SHALL**
              TBD. (Select one or more rows in the GTK3ListBox.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_listbox.py::TestGTK3ListBox::test_do_select_row``
              ``tests/gtk3/container/test_listbox.py::TestGTK3ListBox::test_do_select_row_all``
              ``tests/gtk3/container/test_listbox.py::TestGTK3ListBox::test_do_unselect_row``
              ``tests/gtk3/container/test_listbox.py::TestGTK3ListBox::test_do_unselect_row_all``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def do_select_row(self: _ListBoxHost, row: Gtk.ListBoxRow | None) -> None:
       if row is None:
           self.select_all()
       else:
           self.select_row(row)

----

.. _PTW-GTK3-CON-031:

PTW-GTK3-CON-031
----------------

:Description: The ``GTK3ListBoxMixin.do_unselect_row()`` method
              **SHALL** TBD. (Unselect one or more rows in the
              GTK3ListBox.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_listbox.py::TestGTK3ListBox::test_do_unselect_row``
              ``tests/gtk3/container/test_listbox.py::TestGTK3ListBox::test_do_unselect_row_all``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def do_unselect_row(self: _ListBoxHost, row: Gtk.ListBoxRow | None) -> None:
       if row is None:
           self.unselect_all()
       else:
           self.unselect_row(row)

----

GTK3Paned
=========

.. _PTW-GTK3-CON-032:

PTW-GTK3-CON-032
----------------

:Description: The ``GTK3Paned`` class **SHALL** combine ``Gtk.Paned``
              and ``GTK3PanedMixin``, which derives from
              ``GTK3ContainerMixin``. ``GTK3Paned.__init__()`` **SHALL**
              accept ``orientation: Gtk.Orientation =
              Gtk.Orientation.HORIZONTAL`` and **SHALL**:

              - ``Gtk.Paned.__init__(self, orientation=orientation)``
              - ``GTK3PanedMixin.__init__(self)``
              - ``dic_attributes["orientation"] = orientation``
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_paned.py::TestGTK3Paned::test_init``
              ``tests/gtk3/container/test_paned.py::TestGTK3Paned::test_init_vertical_paned``

----

.. _PTW-GTK3-CON-033:

PTW-GTK3-CON-033
----------------

:Description: ``GTK3PanedMixin`` **SHALL** set
              ``dic_attributes["orientation"]`` to
              ``Gtk.Orientation.HORIZONTAL``; **SHALL** pre-register
              ``"accept-position"``, ``"cancel-position"``,
              ``"cycle-child-focus"``, ``"cycle-handle-focus"``,
              ``"move-handle"``, and ``"toggle-handle-focus"`` in
              ``dic_handler_id`` with a value of ``-1``.
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-005`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-019`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_paned.py::TestGTK3Paned::test_do_set_attributes``
              ``tests/gtk3/container/test_paned.py::TestGTK3Paned::test_do_set_attributes_default``
              ``tests/gtk3/container/test_paned.py::TestGTK3Paned::test_do_set_attributes_partial``
              ``tests/gtk3/container/test_paned.py::TestGTK3Paned::test_init``

----

.. _PTW-GTK3-CON-034:

PTW-GTK3-CON-034
----------------

:Description: ``GTK3PanedMixin.__init__()`` **SHALL** add the following
              properties to ``dic_properties``:

              - ``position``: ``0``
              - ``position_set``: ``False``
              - ``wide_handle``: ``False``

              ``GTK3PanedMixin.do_set_properties()`` **SHALL**, in
              order:

              - ``super().do_set_properties(properties)``
              - ``set_position(position)``
              - ``set_wide_handle(wide_handle)``
              - ``set_property("position-set", position_set)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_paned.py::TestGTK3Paned::test_do_set_properties``
              ``tests/gtk3/container/test_paned.py::TestGTK3Paned::test_do_set_properties_default``

----

.. _PTW-GTK3-CON-035:

PTW-GTK3-CON-035
----------------

:Description: The ``GTK3PanedMixin.do_add_child()`` method **SHALL**
              TBD. (Add a child widget to the GTK3Paned.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_paned.py::TestGTK3Paned::test_do_add_child``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def do_add_child(self: _PanedHost, child: Gtk.Widget, resize: bool, shrink: bool, position: int=1) -> None:
       if position == TOPLEFT:
           self.pack1(child, resize, shrink)
       elif position == BOTTOMRIGHT:
           self.pack2(child, resize, shrink)

----

.. _PTW-GTK3-CON-036:

PTW-GTK3-CON-036
----------------

:Description: The ``GTK3PanedMixin.children()`` read-only property
              **SHALL** TBD. (Get a tuple of the child widgets in the
              GTK3Paned.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       TBD

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def children(self: _PanedHost) -> tuple[Gtk.Widget, Gtk.Widget]:
       return (self.get_child1(), self.get_child2())

----

.. _PTW-GTK3-CON-037:

PTW-GTK3-CON-037
----------------

:Description: The ``GTK3PanedMixin.handle_window()`` read-only property
              **SHALL** TBD. (Get the Gdk.Window of the handle.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_paned.py::TestGTK3Paned::test_handle_window``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def handle_window(self: _PanedHost) -> Gdk.Window:
       return self.get_handle_window()

----

GTK3Revealer
============

.. _PTW-GTK3-CON-038:

PTW-GTK3-CON-038
----------------

:Description: The ``GTK3Revealer`` class **SHALL** combine
              ``Gtk.Revealer`` and ``GTK3RevealerMixin``, which derives
              from ``GTK3ContainerMixin``. ``GTK3Revealer.__init__()``
              **SHALL** accept no parameters and **SHALL**:

              - ``Gtk.Revealer.__init__(self)``
              - ``GTK3RevealerMixin.__init__(self)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_revealer.py::TestGTK3Revealer::test_init``

----

.. _PTW-GTK3-CON-039:

PTW-GTK3-CON-039
----------------

:Description: ``GTK3RevealerMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``reveal_child``: ``False``
              - ``transition_duration``: ``250``
              - ``transition_type``:
                ``Gtk.RevealerTransitionType.SLIDE_DOWN``

              ``GTK3RevealerMixin.do_set_properties()`` **SHALL**, in
              order:

              - ``super().do_set_properties(properties)``
              - ``set_reveal_child(reveal_child)``
              - ``set_transition_duration(transition_duration)``
              - ``set_transition_type(transition_type)`` only if
                isinstance(transition_type, Gtk.RevealerTransitionType)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_revealer.py::TestGTK3Revealer::test_do_set_properties``
              ``tests/gtk3/container/test_revealer.py::TestGTK3Revealer::test_do_set_properties_default``

----

.. _PTW-GTK3-CON-040:

PTW-GTK3-CON-040
----------------

:Description: The ``GTK3RevealerMixin.child_revealed()`` read-only
              property **SHALL** TBD. (Get whether the child is fully
              revealed.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_revealer.py::TestGTK3Revealer::test_child_revealed``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def child_revealed(self: _RevealerHost) -> bool:
       return self.get_child_revealed()

----

GTK3Socket
==========

.. _PTW-GTK3-CON-041:

PTW-GTK3-CON-041
----------------

:Description: The ``GTK3Socket`` class **SHALL** combine ``Gtk.Socket``
              and ``GTK3SocketMixin``, which derives from
              ``GTK3ContainerMixin``. ``GTK3Socket.__init__()``
              **SHALL** accept no parameters and **SHALL**:

              - ``Gtk.Socket.__init__(self)``
              - ``GTK3SocketMixin.__init__(self)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_socket.py::TestGTK3Socket::test_init``

----

.. _PTW-GTK3-CON-042:

PTW-GTK3-CON-042
----------------

:Description: ``GTK3SocketMixin`` **SHALL** pre-register
              ``"plug-added"``, and ``"plug-removed"`` in
              ``dic_handler_id`` with a value of ``-1``.
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-005`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-019`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_socket.py::TestGTK3Socket::test_do_set_attributes``
              ``tests/gtk3/container/test_socket.py::TestGTK3Socket::test_do_set_attributes_default``
              ``tests/gtk3/container/test_socket.py::TestGTK3Socket::test_do_set_attributes_partial``
              ``tests/gtk3/container/test_socket.py::TestGTK3Socket::test_init``

----

.. _PTW-GTK3-CON-043:

PTW-GTK3-CON-043
----------------

:Description: The ``GTK3SocketMixin.id()`` read-only property **SHALL**
              TBD. (Get the window ID of the GTK3Socket.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_socket.py::TestGTK3Socket::test_id``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def id(self: _SocketHost) -> int:
       return self.get_id()

----

.. _PTW-GTK3-CON-044:

PTW-GTK3-CON-044
----------------

:Description: The ``GTK3SocketMixin.plug_window()`` read-only property
              **SHALL** TBD. (Get the window of the GTK3Plug.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_socket.py::TestGTK3Socket::test_plug_window``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def plug_window(self: _SocketHost) -> Gdk.Window | None:
       return self.get_plug_window()

----

GTK3Stack
=========

.. _PTW-GTK3-CON-045:

PTW-GTK3-CON-045
----------------

:Description: The ``GTK3Stack`` class **SHALL** combine ``Gtk.Stack``
              and ``GTK3StackMixin``, which derives from
              ``GTK3ContainerMixin``. ``GTK3Stack.__init__()`` **SHALL**
              accept no parameters and **SHALL**:

              - ``Gtk.Stack.__init__(self)``
              - ``GTK3StackMixin.__init__(self)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_stack.py::TestGTK3Stack::test_init``

----

.. _PTW-GTK3-CON-046:

PTW-GTK3-CON-046
----------------

:Description: ``GTK3StackMixin.__init__()`` **SHALL** add the following
              properties to ``dic_properties``:

              - ``hhomogeneous``: ``True``
              - ``homogeneous``: ``True``
              - ``interpolate_size``: ``False``
              - ``transition_duration``: ``200``
              - ``transition_type``: ``Gtk.StackTransitionType.NONE``
              - ``vhomogeneous``: ``True``
              - ``visible_child``: ``None``
              - ``visible_child_name``: ``None``

              ``GTK3StackMixin.do_set_properties()`` **SHALL**, in
              order:

              - ``super().do_set_properties(properties)``
              - ``set_hhomogeneous(hhomogeneous)``
              - ``set_homogeneous(homogeneous)``
              - ``set_interpolate_size(interpolate_size)``
              - ``set_transition_duration(transition_duration)``
              - ``set_vhomogeneous(vhomogeneous)``
              - ``set_transition_type(transition_type)`` only if
                isinstance(transition_type, Gtk.StackTransitionType)
              - ``set_visible_child(visible_child)`` only if
                visible_child is not None
              - ``set_visible_child_name(visible_child_name)`` only if
                visible_child_name is not None
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_stack.py::TestGTK3Stack::test_do_set_properties``
              ``tests/gtk3/container/test_stack.py::TestGTK3Stack::test_do_set_properties_default``

----

.. _PTW-GTK3-CON-047:

PTW-GTK3-CON-047
----------------

:Description: The ``GTK3StackMixin.do_add_child()`` method **SHALL**
              TBD. (Add a child widget to the GTK3Stack.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_stack.py::TestGTK3Stack::test_do_add_child_named``
              ``tests/gtk3/container/test_stack.py::TestGTK3Stack::test_do_add_child_with_title``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def do_add_child(self: _StackHost, child: Gtk.Widget, name: str, title: str | None=None) -> None:
       if title is not None:
           self.add_titled(child, name, title)
       else:
           self.add_named(child, name)

----

.. _PTW-GTK3-CON-048:

PTW-GTK3-CON-048
----------------

:Description: The ``GTK3StackMixin.transition_running()`` read-only
              property **SHALL** TBD. (Get whether the GTK3Stack is
              currently in a transition between pages.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_stack.py::TestGTK3Stack::test_transition_running``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def transition_running(self: _StackHost) -> bool:
       return self.get_transition_running()

----

GTK3StackSidebar
================

.. _PTW-GTK3-CON-049:

PTW-GTK3-CON-049
----------------

:Description: The ``GTK3StackSidebar`` class **SHALL** combine
              ``Gtk.StackSidebar`` and ``GTK3StackSidebarMixin``, which
              derives from ``GTK3ContainerMixin``.
              ``GTK3StackSidebar.__init__()`` **SHALL** accept no
              parameters and **SHALL**:

              - ``Gtk.StackSidebar.__init__(self)``
              - ``GTK3StackSidebarMixin.__init__(self)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_stacksidebar.py::TestGTK3StackSidebar::test_init``

----

.. _PTW-GTK3-CON-050:

PTW-GTK3-CON-050
----------------

:Description: ``GTK3StackSidebarMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``stack``: ``None``

              ``GTK3StackSidebarMixin.do_set_properties()`` **SHALL**,
              in order:

              - ``super().do_set_properties(properties)``
              - ``set_stack(stack)`` only if stack is not None
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_stacksidebar.py::TestGTK3StackSidebar::test_do_set_properties``
              ``tests/gtk3/container/test_stacksidebar.py::TestGTK3StackSidebar::test_do_set_properties_default``

----

GTK3StackSwitcher
=================

.. _PTW-GTK3-CON-051:

PTW-GTK3-CON-051
----------------

:Description: The ``GTK3StackSwitcher`` class **SHALL** combine
              ``Gtk.StackSwitcher`` and ``GTK3StackSwitcherMixin``,
              which derives from ``GTK3BoxMixin``.
              ``GTK3StackSwitcher.__init__()`` **SHALL** accept no
              parameters and **SHALL**:

              - ``Gtk.StackSwitcher.__init__(self)``
              - ``GTK3StackSwitcherMixin.__init__(self)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_stackswitcher.py::TestGTK3StackSwitcher::test_init``

----

.. _PTW-GTK3-CON-052:

PTW-GTK3-CON-052
----------------

:Description: ``GTK3StackSwitcherMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``icon_size``: ``1``
              - ``stack``: ``None``

              ``GTK3StackSwitcherMixin.do_set_properties()`` **SHALL**,
              in order:

              - ``super().do_set_properties(properties)``
              - ``set_stack(stack)``
              - ``set_property("icon-size", icon_size)``
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_stackswitcher.py::TestGTK3StackSwitcher::test_do_set_properties``
              ``tests/gtk3/container/test_stackswitcher.py::TestGTK3StackSwitcher::test_do_set_properties_default``

----

GTK3Viewport
============

.. _PTW-GTK3-CON-053:

PTW-GTK3-CON-053
----------------

:Description: The ``GTK3Viewport`` class **SHALL** combine
              ``Gtk.Viewport`` and ``GTK3ViewportMixin``, which derives
              from ``GTK3ContainerMixin``. ``GTK3Viewport.__init__()``
              **SHALL** accept ``hadjustment: Gtk.Adjustment | None =
              None``, ``vadjustment: Gtk.Adjustment | None = None`` and
              **SHALL**:

              - ``Gtk.Viewport.__init__(self, hadjustment=hadjustment,
                vadjustment=vadjustment)``
              - ``GTK3ViewportMixin.__init__(self)``
              - ``dic_properties["hadjustment"] = hadjustment``
              - ``dic_properties["vadjustment"] = vadjustment``
:Rationale:   TBD
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_viewport.py::TestGTK3Viewport::test_init``
              ``tests/gtk3/container/test_viewport.py::TestGTK3Viewport::test_init_with_adjustments``

----

.. _PTW-GTK3-CON-054:

PTW-GTK3-CON-054
----------------

:Description: ``GTK3ViewportMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``shadow_type``: ``Gtk.ShadowType.IN``

              ``GTK3ViewportMixin.do_set_properties()`` **SHALL**, in
              order:

              - ``super().do_set_properties(properties)``
              - ``props.hadjustment = hadjustment``
              - ``set_shadow_type(shadow_type)``
              - ``props.vadjustment = vadjustment``
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_viewport.py::TestGTK3Viewport::test_do_set_properties``
              ``tests/gtk3/container/test_viewport.py::TestGTK3Viewport::test_do_set_properties_default``

----

.. _PTW-GTK3-CON-055:

PTW-GTK3-CON-055
----------------

:Description: The ``GTK3ViewportMixin.bin_window()`` read-only property
              **SHALL** TBD. (Get the bin window of the GTK3Viewport.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_viewport.py::TestGTK3Viewport::test_bin_window``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def bin_window(self: _ViewportHost) -> Gdk.Window | None:
       return self.get_bin_window()

----

.. _PTW-GTK3-CON-056:

PTW-GTK3-CON-056
----------------

:Description: The ``GTK3ViewportMixin.view_window()`` read-only property
              **SHALL** TBD. (Get the view window of the GTK3Viewport.)
:Rationale:   TBD
:Traces to:   :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-17) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_viewport.py::TestGTK3Viewport::test_view_window``

.. TODO: describe the behavior. Implementation for reference (this comment does not render):

   def view_window(self: _ViewportHost) -> Gdk.Window | None:
       return self.get_view_window()
