.. _gtk3_frame:

===================================
GTK3 Layer — Frame Requirements
===================================

This document defines the software requirements for the
``GTK3Frame`` class defined in ``pytkwrap.gtk3.container.frame``. ``GTK3Frame``
is a structural widget that provides a decorative border and optional
label around a single child widget. Its ``GTK3FrameMixin`` combines
with native ``Gtk.Frame``; it inherits container behavior from
``GTK3ContainerMixin``.

All requirements in this document trace to one or more system
requirements defined in :ref:`system_requirements` and to GTK3 layer
widget requirements defined in :ref:`gtk3_widgets`.

.. contents:: Contents
   :local:
   :depth: 1

----

Initialization
==============

.. _PTW-GTK3-F-001:

PTW-GTK3-F-001
--------------

:Description: The ``GTK3Frame`` class **SHALL** combine ``Gtk.Frame``
              with ``GTK3FrameMixin``, which derives from
              ``GTK3ContainerMixin``.
:Rationale:   ``Gtk.Frame`` is a container widget that provides
              visual grouping for other widgets. The mixin supplies
              pytkwrap configuration behavior while the native class
              remains in the inheritance hierarchy.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_frame.py::TestGTK3Frame::test_init``

----

.. _PTW-GTK3-F-002:

PTW-GTK3-F-002
--------------

:Description: The ``GTK3Frame.__init__()`` method **SHALL** call
              ``Gtk.Frame.__init__()`` followed by
              ``GTK3FrameMixin.__init__()`` and **SHALL** initialize
              ``dic_properties`` with frame-specific defaults.
:Rationale:   Calling the GTK3 parent ``__init__()`` before the
              pytkwrap parent ``__init__()`` ensures the underlying
              GTK3 widget is fully constructed before pytkwrap
              attempts to configure it.
:Traces to:   :ref:`PTW-GTK3-W-018`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_frame.py::TestGTK3Frame::test_init``

----

.. _PTW-GTK3-F-003:

PTW-GTK3-F-003
--------------

:Description: ``GTK3FrameMixin`` **SHALL** obtain container signals
              from ``GTK3ContainerMixin``. The following signals
              **SHALL** be pre-registered in ``dic_handler_id`` with
              a default value of ``-1``:

              - ``"add"``
              - ``"check-resize"``
              - ``"remove"``
              - ``"set-focus-child"``

:Rationale:   These are the container signals registered by
              ``GTK3ContainerMixin``. Pre-registering them makes them
              available for connection via ``do_set_callbacks()``
              if the application requires callbacks for container
              events.
:Traces to:   :ref:`PTW-GTK3-W-003`, :ref:`PTW-GTK3-W-018`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_frame.py::TestGTK3Frame::test_init``

----

do_set_properties
=================

.. _PTW-GTK3-F-004:

PTW-GTK3-F-004
--------------

:Description: The ``GTK3Frame.do_set_properties()`` method **SHALL**
              support configuration of the following frame-specific
              properties via ``dic_properties``:

              - ``label``: the text to display in the frame's label.
              - ``label_widget``: an optional widget to use as the
                frame's label instead of a text string.
              - ``label_xalign``: the horizontal alignment of the
                label, defaulting to ``0.0``.
              - ``label_yalign``: the vertical alignment of the
                label, defaulting to ``0.5``.
              - ``shadow_type``: the shadow style of the frame,
                defaulting to ``Gtk.ShadowType.ETCHED_IN``.

:Rationale:   These properties are specific to ``Gtk.Frame`` and
              are not part of the base ``Gtk.Widget`` property set.
              They **SHALL** be supported by the pytkwrap frame
              wrapper to allow full frame configuration via the
              typed dictionary interface.
:Traces to:   :ref:`PTW-SR-W-004`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_frame.py::TestGTK3Frame::test_do_set_properties``
              ``tests/gtk3/test_frame.py::TestGTK3Frame::test_do_set_properties_defaults``

----

.. _PTW-GTK3-F-005:

PTW-GTK3-F-005
--------------

:Description: When ``label_widget`` is not ``None``,
              ``GTK3Frame.do_set_properties()`` **SHALL** call
              ``Gtk.Frame.set_label_widget()`` before calling
              ``Gtk.Frame.set_label()``.
:Rationale:   Setting the label widget before the label text ensures
              that the label widget takes precedence over the text
              label, consistent with GTK3's behavior where a label
              widget replaces the text label entirely.
:Traces to:   :ref:`PTW-SR-W-004`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_frame.py::TestGTK3Frame::test_do_set_properties_label_widget``

----

.. _PTW-GTK3-F-006:

PTW-GTK3-F-006
--------------

:Description: The ``GTK3Frame.do_set_properties()`` method **SHALL**
              call ``super().do_set_properties()`` before applying
              frame-specific properties.
:Rationale:   Calling ``super()`` first ensures that base widget
              properties such as sensitivity, visibility, and size
              are applied before frame-specific properties, maintaining
              the correct property application order across the
              inheritance hierarchy.
:Traces to:   :ref:`PTW-GTK3-X-013`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_frame.py::TestGTK3Frame::test_do_set_properties_calls_super``
