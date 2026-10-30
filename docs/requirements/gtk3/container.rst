.. _gtk3_base_container:

=========================================
GTK3 Layer — Container Requirements
=========================================

This document defines the software requirements for
``GTK3ContainerMixin`` and the ``GTK3Container`` wrapper. The mixin is
defined in ``pytkwrap.gtk3.container.container`` and provides common
container properties and signals. Concrete wrappers compose the mixin
with their native GTK3 class; there is no ``GTK3BaseContainer`` class.

All requirements in this document trace to one or more system
requirements defined in :ref:`system_requirements` and to GTK3 layer
widget requirements defined in :ref:`gtk3_widgets`.

.. contents:: Contents
   :local:
   :depth: 1

----

Inheritance and Role
====================

.. _PTW-GTK3-BC-001:

PTW-GTK3-BC-001
---------------

:Description: ``GTK3ContainerMixin`` **SHALL** inherit from
              ``GTK3WidgetMixin``. The ``GTK3Container`` wrapper
              **SHALL** combine ``Gtk.Container`` with
              ``GTK3ContainerMixin``.
:Rationale:   ``Gtk.Container`` defines properties and signals common
              to all GTK3 container widgets, including ``border_width``
              and the ``"add"``, ``"remove"``, ``"check-resize"``,
              and ``"set-focus-child"`` signals. Keeping container behavior
              in a mixin allows concrete
              wrappers to compose it with their native GTK class without
              requiring an intermediate wrapper base class.
:Traces to:   :ref:`PTW-GTK3-W-017`, :ref:`PTW-SR-A-004`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_widget.py::TestGTK3BaseContainer::test_init``

----

.. _PTW-GTK3-BC-002:

PTW-GTK3-BC-002
---------------

:Description: ``GTK3ContainerMixin`` **SHALL** provide mixin behavior
              only; native GTK classes **SHALL** remain in the concrete
              wrapper inheritance hierarchy.
:Rationale:   The mixin supplies pytkwrap behavior and does not replace
              the native GTK class.
:Traces to:   :ref:`PTW-GTK3-W-017`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_widget.py::TestGTK3BaseContainer::test_cannot_instantiate``

----

Container Properties
====================

.. _PTW-GTK3-BC-003:

PTW-GTK3-BC-003
---------------

:Description: ``GTK3ContainerMixin`` **SHALL** define a
              class-level ``_GTK3_CONTAINER_PROPERTIES`` typed dictionary
              of type ``GTK3WidgetProperties`` containing the
              following ``Gtk.Container``-level properties with their
              default values:

              - ``border_width``: ``0``

:Rationale:   ``border_width`` is the only property defined directly
              on ``Gtk.Container`` that applies to all container
              subclasses. Defining it in ``GTK3ContainerMixin``
              ensures it is available to container widget
              wrappers without being duplicated in each subclass.
:Traces to:   :ref:`PTW-GTK3-W-018`, :ref:`PTW-SR-W-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_widget.py::TestGTK3BaseContainer::test_init``

----

.. _PTW-GTK3-BC-004:

PTW-GTK3-BC-004
---------------

:Description: ``GTK3ContainerMixin.__init__()`` **SHALL** update
              ``dic_properties`` with ``_GTK3_CONTAINER_PROPERTIES``
              after initializing its parent mixin.
:Rationale:   Updating ``dic_properties`` rather than replacing it
              preserves the properties initialized by the parent mixin
              and extends them with container-specific properties.
:Traces to:   :ref:`PTW-GTK3-X-011`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_widget.py::TestGTK3BaseContainer::test_init``

----

Container Signals
=================

.. _PTW-GTK3-BC-005:

PTW-GTK3-BC-005
---------------

:Description: ``GTK3ContainerMixin`` **SHALL** define a
              class-level ``_GTK3_CONTAINER_SIGNALS`` list containing the
              following ``Gtk.Container``-level signal names:

              - ``"add"``
              - ``"check-resize"``
              - ``"remove"``
              - ``"set-focus-child"``

:Rationale:   These four signals are defined directly on
              ``Gtk.Container`` and apply to all container subclasses.
              Defining them in ``GTK3ContainerMixin`` ensures
              they are pre-registered in ``dic_handler_id`` for all
              container widget wrappers without duplication, and
              prevents them from appearing on non-container widgets
              such as ``GTK3Entry`` or ``GTK3Label``.
:Traces to:   :ref:`PTW-GTK3-W-003`, :ref:`PTW-GTK3-W-018`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_widget.py::TestGTK3BaseContainer::test_init``

----

.. _PTW-GTK3-BC-006:

PTW-GTK3-BC-006
---------------

:Description: ``GTK3ContainerMixin.__init__()`` **SHALL**
              update ``dic_handler_id`` with the signal names from
              ``_GTK3_CONTAINER_SIGNALS`` as keys and ``-1`` as the
              default value for each, after calling
              its parent mixin initialization.
:Rationale:   Pre-registering container signals in ``dic_handler_id``
              makes them available for connection via
              ``do_set_callbacks()`` without requiring each concrete
              container class to register them individually.
:Traces to:   :ref:`PTW-GTK3-X-012`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_widget.py::TestGTK3BaseContainer::test_init``

----

do_set_properties
=================

.. _PTW-GTK3-BC-007:

PTW-GTK3-BC-007
---------------

:Description: ``GTK3ContainerMixin.do_set_properties()`` **SHALL**
              call ``super().do_set_properties()`` before applying
              container-specific properties and **SHALL**
              call ``Gtk.Container.set_border_width()`` with the
              value from ``dic_properties["border_width"]``.
:Rationale:   Calling ``super()`` first ensures base widget properties
              are applied before container-specific properties.
              Applying ``border_width`` at the container level ensures
              container wrappers support this property without
              duplicating the setter call in each concrete mixin.
:Traces to:   :ref:`PTW-GTK3-X-013`, :ref:`PTW-SR-W-004`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_widget.py::TestGTK3BaseContainer::test_do_set_properties``
              ``tests/gtk3/test_widget.py::TestGTK3BaseContainer::test_do_set_properties_border_width``

----

Subclass Constraints
====================

.. _PTW-GTK3-BC-008:

PTW-GTK3-BC-008
---------------

:Description: Container widget wrappers **SHALL** combine their native
              GTK class with ``GTK3ContainerMixin`` or a specialized
              mixin derived from it.
:Rationale:   This composition provides container properties and
              signals while preserving the native GTK class in the
              wrapper's inheritance hierarchy.
:Traces to:   :ref:`PTW-GTK3-W-017`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_widget.py::TestGTK3BaseContainer::test_subclass_constraints``
              ``tests/gtk3/test_frame.py::TestGTK3Frame::test_inherits_from_base_container``
              ``tests/gtk3/test_scrolledwindow.py::TestGTK3ScrolledWindow::test_inherits_from_base_container``
              ``tests/gtk3/test_combo.py::TestGTK3ComboBox::test_inherits_from_base_container``
