.. _gtk3_base_bin:

=========================================
GTK3 Layer — Bin Wrapper Requirements
=========================================

This document defines the software requirements for the ``GTK3Bin``
wrapper in ``pytkwrap.gtk3.container.bin``. It combines the native
``Gtk.Bin`` class with ``GTK3ContainerMixin``. Other wrappers whose
native GTK class derives from ``Gtk.Bin`` compose that native class
with an appropriate specialized mixin; they need not inherit from
``GTK3Bin``.

All requirements in this document trace to one or more system
requirements defined in :ref:`system_requirements` and to GTK3 layer
base container requirements defined in :ref:`gtk3_base_container`.

.. contents:: Contents
   :local:
   :depth: 1

----

Inheritance and Role
====================

.. _PTW-GTK3-BB-001:

PTW-GTK3-BB-001
---------------

:Description: The ``GTK3Bin`` wrapper **SHALL** combine ``Gtk.Bin``
              with ``GTK3ContainerMixin``.

:Rationale:   ``Gtk.Bin`` is a single-child container that adds no
              additional signals beyond those defined by
              ``Gtk.Container``. The wrapper retains the native
              ``Gtk.Bin`` class and reuses the container mixin.
:Traces to:   :ref:`PTW-GTK3-W-017`, :ref:`PTW-GTK3-BC-008`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_widget.py::TestGTK3BaseBin::test_init``

----

.. _PTW-GTK3-BB-002:

PTW-GTK3-BB-002
---------------

:Description: ``GTK3Bin`` **SHALL** remain a wrapper around the native
              ``Gtk.Bin`` type and **SHALL NOT** be treated as a
              pytkwrap intermediate base class required by other
              concrete wrappers.
:Rationale:   GTK3 wrappers compose their native class with mixins;
              the existence of ``GTK3Bin`` does not impose a
              pytkwrap inheritance hierarchy on other wrappers.
:Traces to:   :ref:`PTW-GTK3-W-017`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_widget.py::TestGTK3BaseBin::test_cannot_instantiate``

----

Initialization
==============

.. _PTW-GTK3-BB-003:

PTW-GTK3-BB-003
---------------

:Description: ``GTK3Bin.__init__()`` **SHALL** initialize
              ``Gtk.Bin`` and then ``GTK3ContainerMixin``.
:Rationale:   Initializing both bases creates the native GTK object
              and the pytkwrap container configuration dictionaries.
:Traces to:   :ref:`PTW-COM-X-003`, :ref:`PTW-GTK3-BC-004`,
              :ref:`PTW-GTK3-BC-006`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_widget.py::TestGTK3BaseBin::test_init``

----

.. _PTW-GTK3-BB-004:

PTW-GTK3-BB-004
---------------

:Description: ``GTK3Bin`` **SHALL** obtain its pytkwrap container
              properties and signals from ``GTK3ContainerMixin`` and
              **SHALL NOT** define separate bin-specific properties
              or signals.
:Rationale:   ``Gtk.Bin`` adds no properties or signals beyond those
              defined by ``Gtk.Container`` — it simply constrains
              the number of child widgets to one. ``GTK3Bin`` adds no
              separate pytkwrap properties or signals.
:Traces to:   :ref:`PTW-GTK3-W-017`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_widget.py::TestGTK3BaseBin::test_init``

----

do_set_properties
=================

.. _PTW-GTK3-BB-005:

PTW-GTK3-BB-005
---------------

:Description: ``GTK3Bin`` **SHALL NOT** define a bin-specific
              ``do_set_properties()`` override; container properties
              are applied by ``GTK3ContainerMixin``.
:Rationale:   ``Gtk.Bin`` adds no pytkwrap configuration properties
              beyond those provided by ``Gtk.Container``.
:Traces to:   :ref:`PTW-GTK3-X-013`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_widget.py::TestGTK3BaseBin::test_do_set_properties``

----

Subclass Constraints
====================

.. _PTW-GTK3-BB-006:

PTW-GTK3-BB-006
---------------

:Description: Wrappers for native GTK classes derived from
              ``Gtk.Bin`` **SHALL** retain that native class in their
              inheritance hierarchy and **SHALL** compose it with
              ``GTK3ContainerMixin`` or a specialized mixin derived
              from it.
:Rationale:   This preserves the GTK class API and provides the
              container behavior without requiring inheritance from
              the ``GTK3Bin`` wrapper.
:Traces to:   :ref:`PTW-GTK3-W-017`, :ref:`PTW-GTK3-BC-008`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_widget.py::TestGTK3BaseBin::test_subclass_constraints``
              ``tests/gtk3/test_frame.py::TestGTK3Frame::test_inherits_from_base_bin``
              ``tests/gtk3/test_scrolledwindow.py::TestGTK3ScrolledWindow::test_inherits_from_base_bin``
              ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_inherits_from_base_bin``
              ``tests/gtk3/test_buttons/test_base_button.py::TestGTK3BaseButton::test_inherits_from_base_bin``

----

Future Composite Views
======================

.. note::

   The former ``GTK3BaseBox`` requirements described an intermediate
   class that does not exist in the current implementation. Detailed
   MatrixView and PlotView requirements remain planned and are not
   baselined here.

.. _PTW-GTK3-BB-007:

PTW-GTK3-BB-007
---------------

:Description: Requirements for the future MatrixView and PlotView
              wrappers **SHALL** be specified in their feature
              requirement documents before those features are
              considered baselined.
:Rationale:   Their detailed behavior and composition have not yet
              been reconciled with the current API baseline.
:Traces to:   :ref:`PTW-GTK3-W-017`, :ref:`PTW-GTK3-BC-008`
:Issues:      None
:Status:      Planned
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_widget.py::TestGTK3BaseBox::test_init``

----

.. _PTW-GTK3-BB-008:

PTW-GTK3-BB-008
---------------

:Description: The future MatrixView and PlotView requirements
              **SHALL** describe their concrete wrapper APIs rather
              than assume an intermediate ``GTK3BaseBox`` class.
:Rationale:   No such intermediate class is part of the current
              implementation baseline.
:Traces to:   :ref:`PTW-GTK3-W-017`
:Issues:      None
:Status:      Planned
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_widget.py::TestGTK3BaseBox::test_cannot_instantiate``

----

.. _PTW-GTK3-BB-009:

PTW-GTK3-BB-009
---------------

:Description: Future MatrixView and PlotView wrappers **SHALL**
              retain their native GTK classes and use the container
              mixin behavior appropriate to each wrapper. Their
              detailed composition requirements remain to be defined.
:Rationale:   The current implementation does not define a
              ``GTK3BaseBox`` intermediary.
:Traces to:   :ref:`PTW-GTK3-W-017`, :ref:`PTW-GTK3-BC-008`
:Issues:      None
:Status:      Planned
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_matrixview.py::TestGTK3MatrixView::test_inherits_from_base_box``
              ``tests/gtk3/test_plotview.py::TestGTK3PlotView::test_inherits_from_base_box``
