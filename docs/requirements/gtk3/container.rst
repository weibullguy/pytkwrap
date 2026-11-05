.. _gtk3_base_container:

=========================================
GTK3 Layer — Container Requirements
=========================================

This document defines the software requirements for
``GTK3ContainerMixin`` and the container wrappers in the
``pytkwrap.gtk3.container`` package: ``GTK3Container``, ``GTK3Bin``,
``GTK3Box``, ``GTK3ButtonBox``, ``GTK3Expander``, ``GTK3Frame``,
``GTK3ListBox``, ``GTK3Paned``, ``GTK3Revealer``, ``GTK3Socket``,
``GTK3Stack``, ``GTK3StackSidebar``, ``GTK3StackSwitcher``, and
``GTK3Viewport``, together with the ``do_make_buttonbox()`` factory
function. Concrete wrappers compose a container mixin with their native
GTK3 class; there is no ``GTK3BaseContainer`` class.

The container mixin hierarchy is:

.. code-block:: text

    GTK3WidgetMixin
        └── GTK3ContainerMixin
                ├── GTK3BoxMixin
                │       ├── GTK3ButtonBoxMixin
                │       └── GTK3StackSwitcherMixin
                ├── GTK3ExpanderMixin
                ├── GTK3FrameMixin
                ├── GTK3ListBoxMixin
                ├── GTK3PanedMixin
                ├── GTK3RevealerMixin
                ├── GTK3SocketMixin
                ├── GTK3StackMixin
                ├── GTK3StackSidebarMixin
                └── GTK3ViewportMixin

``GTK3Container`` and ``GTK3Bin`` use ``GTK3ContainerMixin`` directly.

All requirements in this document trace to one or more system
requirements defined in :ref:`system_requirements` and to GTK3 layer
widget requirements defined in :ref:`gtk3_widgets`.

.. contents:: Contents
   :local:
   :depth: 1

----

Package
=======

.. _PTW-GTK3-BC-021:

PTW-GTK3-BC-021
---------------

:Description: The ``pytkwrap.gtk3.container`` package **SHALL** export
              ``GTK3Bin``, ``GTK3Box``, ``GTK3ButtonBox``,
              ``GTK3Container``, ``GTK3ContainerMixin``,
              ``GTK3Expander``, ``GTK3Frame``, ``GTK3ListBox``,
              ``GTK3Paned``, ``GTK3Revealer``, ``GTK3Socket``,
              ``GTK3Stack``, ``GTK3StackSidebar``,
              ``GTK3StackSwitcher``, ``GTK3Viewport``, and
              ``do_make_buttonbox`` through ``__all__``. Sub-modules
              of the package **SHALL** import sibling modules directly
              and **SHALL NOT** import through the package
              ``__init__.py``.
:Rationale:   A single public import location simplifies application
              code, and ``GTK3ContainerMixin`` is exported so other
              packages can build container-derived wrappers. Direct
              sibling imports avoid circular imports during package
              initialization.
:Traces to:   :ref:`PTW-SR-W-001`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       TBD

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
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Corrected test references.
:Tests:       ``tests/gtk3/container/test_container.py::TestGTK3Container::test_init``

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
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Corrected test references.
:Tests:       ``tests/gtk3/container/test_container.py::TestGTK3Container::test_init``

----

.. _PTW-GTK3-BC-022:

PTW-GTK3-BC-022
---------------

:Description: ``GTK3Container.__init__()`` **SHALL** take no parameters
              and **SHALL** call ``Gtk.Container.__init__()`` followed
              by ``GTK3ContainerMixin.__init__()``.
:Rationale:   Initializing the native class first ensures the GTK
              object exists before pytkwrap configures it.
:Traces to:   :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_container.py::TestGTK3Container::test_init``

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
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Corrected test references.
:Tests:       ``tests/gtk3/container/test_container.py::TestGTK3Container::test_init``
              ``tests/gtk3/container/test_container.py::TestGTK3Container::test_do_set_properties_default``

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
:Traces to:   :ref:`PTW-GTK3-W-018`, :ref:`PTW-GTK3-X-010`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Corrected traces and test
              references.
:Tests:       ``tests/gtk3/container/test_container.py::TestGTK3Container::test_init``

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
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Corrected test references.
:Tests:       ``tests/gtk3/container/test_container.py::TestGTK3Container::test_init``

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
:Traces to:   :ref:`PTW-GTK3-W-003`, :ref:`PTW-GTK3-X-003`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Corrected traces and test
              references.
:Tests:       ``tests/gtk3/container/test_container.py::TestGTK3Container::test_init``

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
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Corrected test references.
:Tests:       ``tests/gtk3/container/test_container.py::TestGTK3Container::test_do_set_properties``
              ``tests/gtk3/container/test_container.py::TestGTK3Container::test_do_set_properties_default``

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
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Removed references to tests that do
              not exist.
:Tests:       TBD

----

GTK3Bin
=======

.. _PTW-GTK3-BC-009:

PTW-GTK3-BC-009
---------------

:Description: The ``GTK3Bin`` wrapper **SHALL** combine ``Gtk.Bin``
              with ``GTK3ContainerMixin``.
:Rationale:   ``Gtk.Bin`` is a single-child container that adds no
              additional signals beyond those defined by
              ``Gtk.Container``. The wrapper retains the native
              ``Gtk.Bin`` class and reuses the container mixin.
:Traces to:   :ref:`PTW-GTK3-W-017`, :ref:`PTW-GTK3-BC-008`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Moved from ``bin.rst`` (formerly
              PTW-GTK3-BB-001); corrected test references.
:Tests:       ``tests/gtk3/container/test_bin.py::TestGTK3Bin::test_init``

----

.. _PTW-GTK3-BC-010:

PTW-GTK3-BC-010
---------------

:Description: ``GTK3Bin`` **SHALL** remain a wrapper around the native
              ``Gtk.Bin`` type and **SHALL NOT** be treated as a
              pytkwrap intermediate base class required by other
              concrete wrappers.
:Rationale:   GTK3 wrappers compose their native class with mixins;
              the existence of ``GTK3Bin`` does not impose a
              pytkwrap inheritance hierarchy on other wrappers.
:Traces to:   :ref:`PTW-GTK3-W-017`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Moved from ``bin.rst`` (formerly
              PTW-GTK3-BB-002); removed a reference to a test that
              does not exist.
:Tests:       TBD

----

.. _PTW-GTK3-BC-011:

PTW-GTK3-BC-011
---------------

:Description: ``GTK3Bin.__init__()`` **SHALL** take no parameters and
              **SHALL** initialize ``Gtk.Bin`` and then
              ``GTK3ContainerMixin``.
:Rationale:   Initializing both bases creates the native GTK object
              and the pytkwrap container configuration dictionaries.
:Traces to:   :ref:`PTW-GTK3-W-018`, :ref:`PTW-GTK3-BC-004`,
              :ref:`PTW-GTK3-BC-006`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Moved from ``bin.rst`` (formerly
              PTW-GTK3-BB-003); corrected traces and test references.
:Tests:       ``tests/gtk3/container/test_bin.py::TestGTK3Bin::test_init``

----

.. _PTW-GTK3-BC-012:

PTW-GTK3-BC-012
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
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Moved from ``bin.rst`` (formerly
              PTW-GTK3-BB-004); corrected test references.
:Tests:       ``tests/gtk3/container/test_bin.py::TestGTK3Bin::test_init``

----

.. _PTW-GTK3-BC-013:

PTW-GTK3-BC-013
---------------

:Description: ``GTK3Bin`` **SHALL NOT** define a bin-specific
              ``do_set_properties()`` override; container properties
              are applied by ``GTK3ContainerMixin``.
:Rationale:   ``Gtk.Bin`` adds no pytkwrap configuration properties
              beyond those provided by ``Gtk.Container``.
:Traces to:   :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Moved from ``bin.rst`` (formerly
              PTW-GTK3-BB-005); corrected test references.
:Tests:       ``tests/gtk3/container/test_bin.py::TestGTK3Bin::test_do_set_properties``

----

.. _PTW-GTK3-BC-014:

PTW-GTK3-BC-014
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
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Moved from ``bin.rst`` (formerly
              PTW-GTK3-BB-006); removed references to tests that do
              not exist.
:Tests:       TBD

----

GTK3Box
=======

.. _PTW-GTK3-BC-023:

PTW-GTK3-BC-023
---------------

:Description: The ``GTK3Box`` class **SHALL** combine ``Gtk.Box`` and
              ``GTK3BoxMixin``, which derives from
              ``GTK3ContainerMixin``. ``GTK3Box.__init__()`` **SHALL**
              accept an ``orientation`` parameter defaulting to
              ``Gtk.Orientation.HORIZONTAL`` and a ``spacing``
              parameter defaulting to ``0``, pass both as keyword
              arguments to ``Gtk.Box.__init__()``, call
              ``GTK3BoxMixin.__init__()``, and store ``spacing`` in
              ``dic_properties["spacing"]``.
:Rationale:   Orientation and spacing are normally chosen when a box is
              created. ``GTK3BoxMixin`` is also the base for other
              ``Gtk.Box`` subclasses such as ``GTK3InfoBar`` and
              ``GTK3Statusbar``.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-BC-008`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_box.py::TestGTK3Box::test_init``
              ``tests/gtk3/container/test_box.py::TestGTK3Box::test_init_with_orientation``
              ``tests/gtk3/container/test_box.py::TestGTK3Box::test_init_with_spacing``

----

.. _PTW-GTK3-BC-024:

PTW-GTK3-BC-024
---------------

:Description: ``GTK3BoxMixin.__init__()`` **SHALL** add the following
              properties to ``dic_properties``:

              - ``baseline_position``: ``Gtk.BaselinePosition.CENTER``
              - ``homogeneous``: ``False``
              - ``spacing``: ``0``

              ``GTK3BoxMixin.do_set_properties()`` **SHALL** call
              ``super().do_set_properties()`` first and then apply
              these with ``set_baseline_position()``,
              ``set_homogeneous()``, and ``set_spacing()``.
:Rationale:   The defaults match the native ``Gtk.Box``.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_box.py::TestGTK3Box::test_do_set_properties_default``
              ``tests/gtk3/container/test_box.py::TestGTK3Box::test_do_set_properties``

----

GTK3ButtonBox
=============

.. _PTW-GTK3-BC-025:

PTW-GTK3-BC-025
---------------

:Description: The ``GTK3ButtonBox`` class **SHALL** combine
              ``Gtk.ButtonBox`` and ``GTK3ButtonBoxMixin``, which
              derives from ``GTK3BoxMixin``. ``GTK3ButtonBox.__init__()``
              **SHALL** accept an ``orientation`` parameter defaulting
              to ``Gtk.Orientation.HORIZONTAL``, pass it to
              ``Gtk.ButtonBox.__init__()``, and then call
              ``GTK3ButtonBoxMixin.__init__()``.
:Rationale:   ``Gtk.ButtonBox`` is a ``Gtk.Box`` subclass, so the box
              mixin supplies its inherited configuration.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-BC-008`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_buttonbox.py::TestGTK3ButtonBox::test_init``
              ``tests/gtk3/container/test_buttonbox.py::TestGTK3ButtonBox::test_init_with_orientation``

----

.. _PTW-GTK3-BC-026:

PTW-GTK3-BC-026
---------------

:Description: ``GTK3ButtonBoxMixin.__init__()`` **SHALL** add
              ``layout_style`` (default ``Gtk.ButtonBoxStyle.END``) to
              ``dic_properties``. ``GTK3ButtonBoxMixin.do_set_properties()``
              **SHALL** call ``super().do_set_properties()`` first and
              then apply ``layout_style`` with ``set_layout()``.
:Rationale:   The property key follows the GObject property name
              ``layout-style``, while the setter follows the GTK method
              name ``set_layout()``.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_buttonbox.py::TestGTK3ButtonBox::test_do_set_properties_default``
              ``tests/gtk3/container/test_buttonbox.py::TestGTK3ButtonBox::test_do_set_properties``

----

do_make_buttonbox
=================

.. _PTW-GTK3-BC-027:

PTW-GTK3-BC-027
---------------

:Description: The ``do_make_buttonbox()`` function **SHALL** accept a
              list of icon file paths (``icons``), a list of tooltip
              markup strings (``tooltips``), a list of callbacks
              (``callbacks``), and optional ``height`` (default
              ``-1``), ``layout`` (default
              ``Gtk.ButtonBoxStyle.START``), ``orientation`` (default
              ``"horizontal"``), and ``width`` (default ``-1``)
              arguments, and **SHALL** return a ``GTK3ButtonBox``. The
              button box **SHALL** be horizontal when ``orientation``
              is ``"horizontal"`` and vertical otherwise, and **SHALL**
              have its layout set to ``layout``. For each icon, the
              function **SHALL** create a ``GTK3Button`` whose image is
              a ``Gtk.Image`` loaded from the icon file at the
              requested size, apply ``height`` and ``width`` as the
              button's ``height_request`` and ``width_request``
              through ``do_set_properties()``, and pack the button into
              the box with ``pack_start(button, True, True, 0)``.
:Rationale:   A factory function for button boxes reduces the
              boilerplate required to create a row or column of
              icon buttons, which is a common UI pattern in
              application toolbars.
:Traces to:   :ref:`PTW-SR-W-001`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Moved from ``button.rst`` (formerly
              PTW-GTK3-B-007). Revised to match the implementation:
              returns a ``GTK3ButtonBox`` rather than a
              ``Gtk.HButtonBox`` or ``Gtk.VButtonBox``; added argument
              defaults and button construction; corrected test
              references.
:Tests:       ``tests/gtk3/container/test_buttonbox.py::TestGTK3ButtonBox::test_do_make_buttonbox_horizontal``
              ``tests/gtk3/container/test_buttonbox.py::TestGTK3ButtonBox::test_do_make_buttonbox_vertical``

----

.. _PTW-GTK3-BC-028:

PTW-GTK3-BC-028
---------------

:Description: For each button, ``do_make_buttonbox()`` **SHALL** set
              the tooltip markup from the tooltip at the same index,
              or ``""`` when no tooltip is provided for that index.
              It **SHALL** connect the callback at the same index to
              the button's ``"clicked"`` signal, or set the button
              insensitive when no callback is provided for that index.
:Rationale:   Graceful handling of mismatched list lengths prevents
              ``IndexError`` exceptions when the number of callbacks
              or tooltips does not match the number of icons, allowing
              partial configuration of button boxes without raising
              exceptions.
:Traces to:   :ref:`PTW-SR-W-001`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Moved from ``button.rst`` (formerly
              PTW-GTK3-B-008); corrected test references.
:Tests:       ``tests/gtk3/container/test_buttonbox.py::TestGTK3ButtonBox::test_do_make_buttonbox_no_tooltip``

----

GTK3Expander
============

.. _PTW-GTK3-BC-029:

PTW-GTK3-BC-029
---------------

:Description: The ``GTK3Expander`` class **SHALL** combine
              ``Gtk.Expander`` and ``GTK3ExpanderMixin``, which derives
              from ``GTK3ContainerMixin``. ``GTK3ExpanderMixin``
              **SHALL** pre-register the ``"activate"`` signal in
              ``dic_handler_id`` with a value of ``-1``.
              ``GTK3Expander.__init__()`` **SHALL** accept a ``label``
              parameter (``str | None``, default ``None``), pass it to
              ``Gtk.Expander.__init__()``, call
              ``GTK3ExpanderMixin.__init__()``, and store the label in
              ``dic_properties["label"]``.
:Rationale:   ``"activate"`` is emitted when the expander is toggled.
              The label is normally known when the expander is
              created.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-017`, :ref:`PTW-GTK3-BC-008`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_expander.py::TestGTK3Expander::test_init``
              ``tests/gtk3/container/test_expander.py::TestGTK3Expander::test_init_with_label``
              ``tests/gtk3/container/test_expander.py::TestGTK3Expander::test_init_with_mnemonic``

----

.. _PTW-GTK3-BC-030:

PTW-GTK3-BC-030
---------------

:Description: ``GTK3ExpanderMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``expanded``: ``False``
              - ``label``: ``None``
              - ``label_fill``: ``False``
              - ``label_widget``: ``None``
              - ``resize_toplevel``: ``False``
              - ``use_markup``: ``False``
              - ``use_underline``: ``False``

              ``GTK3ExpanderMixin.do_set_properties()`` **SHALL** call
              ``super().do_set_properties()`` first and then apply
              ``expanded``, ``label``, ``label_fill``,
              ``label_widget``, ``resize_toplevel``, ``use_markup``,
              and ``use_underline``, in that order, through their
              corresponding ``Gtk.Expander`` setters.
:Rationale:   These properties are specific to ``Gtk.Expander`` and
              allow full expander configuration through the typed
              dictionary interface.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_expander.py::TestGTK3Expander::test_do_set_properties_default``
              ``tests/gtk3/container/test_expander.py::TestGTK3Expander::test_do_set_properties``

----

GTK3Frame
=========

.. _PTW-GTK3-BC-015:

PTW-GTK3-BC-015
---------------

:Description: The ``GTK3Frame`` class **SHALL** combine ``Gtk.Frame``
              with ``GTK3FrameMixin``, which derives from
              ``GTK3ContainerMixin``.
:Rationale:   ``Gtk.Frame`` is a container widget that provides
              visual grouping for other widgets. The mixin supplies
              pytkwrap configuration behavior while the native class
              remains in the inheritance hierarchy.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Moved from ``frame.rst`` (formerly
              PTW-GTK3-F-001); corrected test references.
:Tests:       ``tests/gtk3/container/test_frame.py::TestFrame::test_init``

----

.. _PTW-GTK3-BC-016:

PTW-GTK3-BC-016
---------------

:Description: ``GTK3Frame.__init__()`` **SHALL** accept a ``label``
              parameter (``str | None``, default ``None``), call
              ``Gtk.Frame.__init__()`` with that label followed by
              ``GTK3FrameMixin.__init__()``, and store the label in
              ``dic_properties["label"]``.
:Rationale:   Calling the GTK3 parent ``__init__()`` before the
              pytkwrap parent ``__init__()`` ensures the underlying
              GTK3 widget is fully constructed before pytkwrap
              attempts to configure it.
:Traces to:   :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Moved from ``frame.rst`` (formerly
              PTW-GTK3-F-002). Added the ``label`` parameter; the
              frame defaults are covered by PTW-GTK3-BC-018. Corrected
              test references.
:Tests:       ``tests/gtk3/container/test_frame.py::TestFrame::test_init``
              ``tests/gtk3/container/test_frame.py::TestFrame::test_init_with_label``

----

.. _PTW-GTK3-BC-017:

PTW-GTK3-BC-017
---------------

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
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Moved from ``frame.rst`` (formerly
              PTW-GTK3-F-003); corrected test references.
:Tests:       ``tests/gtk3/container/test_frame.py::TestFrame::test_init``

----

.. _PTW-GTK3-BC-018:

PTW-GTK3-BC-018
---------------

:Description: ``GTK3FrameMixin.__init__()`` **SHALL** add the following
              frame-specific properties to ``dic_properties``:

              - ``label``: the text to display in the frame's label,
                defaulting to ``None``.
              - ``label_widget``: an optional widget to use as the
                frame's label instead of a text string, defaulting to
                ``None``.
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
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Moved from ``frame.rst`` (formerly
              PTW-GTK3-F-004); added the ``label`` and
              ``label_widget`` defaults; corrected test references.
:Tests:       ``tests/gtk3/container/test_frame.py::TestFrame::test_do_set_properties_default``
              ``tests/gtk3/container/test_frame.py::TestFrame::test_do_set_properties``

----

.. _PTW-GTK3-BC-019:

PTW-GTK3-BC-019
---------------

:Description: ``GTK3FrameMixin.do_set_properties()`` **SHALL** call
              ``set_label_widget()`` only when ``label_widget`` is not
              ``None``, then call ``set_label()`` only when ``label``
              is not ``None``, then apply ``label_xalign`` and
              ``label_yalign`` together with ``set_label_align()``,
              and then apply ``shadow_type`` with
              ``set_shadow_type()``.
:Rationale:   Skipping ``None`` values preserves a label or label
              widget that was set at construction or by an earlier
              call. Because ``set_label()`` replaces the label widget
              with a text label, a non-``None`` ``label`` takes
              precedence when both are supplied.
:Traces to:   :ref:`PTW-SR-W-004`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Moved from ``frame.rst`` (formerly
              PTW-GTK3-F-005). Revised to match the implementation: a
              non-``None`` ``label`` replaces the label widget rather
              than the label widget taking precedence; added the
              ``None`` checks and the alignment and shadow setters.
              Corrected test references.
:Tests:       ``tests/gtk3/container/test_frame.py::TestFrame::test_do_set_properties``
              ``tests/gtk3/container/test_frame.py::TestFrame::test_do_set_properties_label_widget``

----

.. _PTW-GTK3-BC-020:

PTW-GTK3-BC-020
---------------

:Description: The ``GTK3Frame.do_set_properties()`` method **SHALL**
              call ``super().do_set_properties()`` before applying
              frame-specific properties.
:Rationale:   Calling ``super()`` first ensures that base widget
              properties such as sensitivity, visibility, and size
              are applied before frame-specific properties, maintaining
              the correct property application order across the
              inheritance hierarchy.
:Traces to:   :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.1
:History:     0.1.0 (2026-10-29) - Initial baseline.
              0.1.1 (2026-11-04) - Moved from ``frame.rst`` (formerly
              PTW-GTK3-F-006); corrected test references.
:Tests:       ``tests/gtk3/container/test_frame.py::TestFrame::test_do_set_properties``

----

GTK3ListBox
===========

.. _PTW-GTK3-BC-031:

PTW-GTK3-BC-031
---------------

:Description: The ``GTK3ListBox`` class **SHALL** combine
              ``Gtk.ListBox`` and ``GTK3ListBoxMixin``, which derives
              from ``GTK3ContainerMixin``. ``GTK3ListBox.__init__()``
              **SHALL** take no parameters and **SHALL** call
              ``Gtk.ListBox.__init__()`` followed by
              ``GTK3ListBoxMixin.__init__()``. ``GTK3ListBoxMixin``
              **SHALL** pre-register the following signals in
              ``dic_handler_id`` with a value of ``-1``:

              - ``"activate-cursor-row"``
              - ``"move-cursor"``
              - ``"row-activated"``
              - ``"row-selected"``
              - ``"select-all"``
              - ``"selected-rows-changed"``
              - ``"toggle-cursor-row"``
              - ``"unselect-all"``

:Rationale:   Pre-registering the list box signals makes them
              available for connection via ``do_set_callbacks()``.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-017`, :ref:`PTW-GTK3-BC-008`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_listbox.py::TestGTK3ListBox::test_init``

----

.. _PTW-GTK3-BC-032:

PTW-GTK3-BC-032
---------------

:Description: ``GTK3ListBoxMixin.__init__()`` **SHALL** add
              ``activate_on_single_click`` (default ``True``) and
              ``selection_mode`` (default ``Gtk.SelectionMode.SINGLE``)
              to ``dic_properties``. ``GTK3ListBoxMixin.do_set_properties()``
              **SHALL** call ``super().do_set_properties()`` first and
              then apply them with ``set_activate_on_single_click()``
              and ``set_selection_mode()``.
:Rationale:   The defaults match the native ``Gtk.ListBox``.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_listbox.py::TestGTK3ListBox::test_do_set_properties_default``
              ``tests/gtk3/container/test_listbox.py::TestGTK3ListBox::test_do_set_properties``

----

GTK3Paned
=========

.. _PTW-GTK3-BC-033:

PTW-GTK3-BC-033
---------------

:Description: The ``GTK3Paned`` class **SHALL** combine ``Gtk.Paned``
              and ``GTK3PanedMixin``, which derives from
              ``GTK3ContainerMixin``. ``GTK3Paned.__init__()``
              **SHALL** accept an ``orientation`` parameter defaulting
              to ``Gtk.Orientation.HORIZONTAL``, pass it to
              ``Gtk.Paned.__init__()``, call
              ``GTK3PanedMixin.__init__()``, and store the orientation
              in the instance attribute ``orientation``.
              ``GTK3PanedMixin`` **SHALL** pre-register the following
              signals in ``dic_handler_id`` with a value of ``-1``:

              - ``"accept-position"``
              - ``"cancel-position"``
              - ``"cycle-child-focus"``
              - ``"cycle-handle-focus"``
              - ``"move-handle"``
              - ``"toggle-handle-focus"``

:Rationale:   The orientation determines whether the panes are side
              by side or stacked and is fixed at construction.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-017`, :ref:`PTW-GTK3-BC-008`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_paned.py::TestGTK3Paned::test_init``
              ``tests/gtk3/container/test_paned.py::TestGTK3Paned::test_init_vertical_paned``

----

.. _PTW-GTK3-BC-034:

PTW-GTK3-BC-034
---------------

:Description: ``GTK3PanedMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``position``: ``0``
              - ``position_set``: ``False``
              - ``wide_handle``: ``False``

              ``GTK3PanedMixin.do_set_properties()`` **SHALL** call
              ``super().do_set_properties()`` first, apply
              ``position`` with ``set_position()`` and
              ``wide_handle`` with ``set_wide_handle()``, and then
              apply ``position_set`` through
              ``set_property("position-set", ...)``.
:Rationale:   ``position-set`` has no dedicated setter in
              ``Gtk.Paned``.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_paned.py::TestGTK3Paned::test_do_set_properties_default``
              ``tests/gtk3/container/test_paned.py::TestGTK3Paned::test_do_set_properties``

----

GTK3Revealer
============

.. _PTW-GTK3-BC-035:

PTW-GTK3-BC-035
---------------

:Description: The ``GTK3Revealer`` class **SHALL** combine
              ``Gtk.Revealer`` and ``GTK3RevealerMixin``, which derives
              from ``GTK3ContainerMixin``. ``GTK3Revealer.__init__()``
              **SHALL** take no parameters and **SHALL** call
              ``Gtk.Revealer.__init__()`` followed by
              ``GTK3RevealerMixin.__init__()``.
:Rationale:   ``Gtk.Revealer`` is a single-child container that
              animates showing and hiding its child.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-BC-014`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_revealer.py::TestGTK3Revealer::test_init``

----

.. _PTW-GTK3-BC-036:

PTW-GTK3-BC-036
---------------

:Description: ``GTK3RevealerMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``reveal_child``: ``False``
              - ``transition_duration``: ``250``
              - ``transition_type``:
                ``Gtk.RevealerTransitionType.SLIDE_DOWN``

              ``GTK3RevealerMixin.do_set_properties()`` **SHALL** call
              ``super().do_set_properties()`` first and then apply
              these with ``set_reveal_child()``,
              ``set_transition_duration()``, and
              ``set_transition_type()``.
:Rationale:   The defaults match the native ``Gtk.Revealer``.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_revealer.py::TestGTK3Revealer::test_do_set_properties_default``
              ``tests/gtk3/container/test_revealer.py::TestGTK3Revealer::test_do_set_properties``

----

GTK3Socket
==========

.. _PTW-GTK3-BC-037:

PTW-GTK3-BC-037
---------------

:Description: The ``GTK3Socket`` class **SHALL** combine ``Gtk.Socket``
              and ``GTK3SocketMixin``, which derives from
              ``GTK3ContainerMixin``. ``GTK3Socket.__init__()``
              **SHALL** take no parameters and **SHALL** call
              ``Gtk.Socket.__init__()`` followed by
              ``GTK3SocketMixin.__init__()``. ``GTK3SocketMixin``
              **SHALL** pre-register the ``"plug-added"`` and
              ``"plug-removed"`` signals in ``dic_handler_id`` with a
              value of ``-1`` and **SHALL NOT** add socket-specific
              properties.
:Rationale:   ``Gtk.Socket`` embeds a ``Gtk.Plug`` from another
              process; its plug signals are the events applications
              need to observe.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-017`, :ref:`PTW-GTK3-BC-008`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_socket.py::TestGTK3Socket::test_init``
              ``tests/gtk3/container/test_socket.py::TestGTK3Socket::test_do_set_properties_default``

----

GTK3Stack
=========

.. _PTW-GTK3-BC-038:

PTW-GTK3-BC-038
---------------

:Description: The ``GTK3Stack`` class **SHALL** combine ``Gtk.Stack``
              and ``GTK3StackMixin``, which derives from
              ``GTK3ContainerMixin``. ``GTK3Stack.__init__()`` **SHALL**
              take no parameters and **SHALL** call
              ``Gtk.Stack.__init__()`` followed by
              ``GTK3StackMixin.__init__()``.
:Rationale:   ``Gtk.Stack`` shows one of several children at a time.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-BC-008`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_stack.py::TestGTK3Stack::test_init``

----

.. _PTW-GTK3-BC-039:

PTW-GTK3-BC-039
---------------

:Description: ``GTK3StackMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``hhomogeneous``: ``True``
              - ``homogeneous``: ``True``
              - ``interpolate_size``: ``False``
              - ``transition_duration``: ``200``
              - ``transition_type``: ``Gtk.StackTransitionType.NONE``
              - ``vhomogeneous``: ``True``
              - ``visible_child``: ``None``
              - ``visible_child_name``: ``None``

              ``GTK3StackMixin.do_set_properties()`` **SHALL** call
              ``super().do_set_properties()`` first and then apply
              ``hhomogeneous``, ``homogeneous``, ``interpolate_size``,
              ``transition_duration``, ``transition_type``, and
              ``vhomogeneous``, in that order, through their
              corresponding ``Gtk.Stack`` setters. It **SHALL** call
              ``set_visible_child()`` only when ``visible_child`` is
              not ``None`` and ``set_visible_child_name()`` only when
              ``visible_child_name`` is not ``None``.
:Rationale:   Skipping ``None`` values preserves the stack's current
              visible child.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_stack.py::TestGTK3Stack::test_do_set_properties_default``
              ``tests/gtk3/container/test_stack.py::TestGTK3Stack::test_do_set_properties``

----

GTK3StackSidebar
================

.. _PTW-GTK3-BC-040:

PTW-GTK3-BC-040
---------------

:Description: The ``GTK3StackSidebar`` class **SHALL** combine
              ``Gtk.StackSidebar`` and ``GTK3StackSidebarMixin``, which
              derives from ``GTK3ContainerMixin``.
              ``GTK3StackSidebar.__init__()`` **SHALL** take no
              parameters and **SHALL** call
              ``Gtk.StackSidebar.__init__()`` followed by
              ``GTK3StackSidebarMixin.__init__()``.
:Rationale:   ``Gtk.StackSidebar`` is a ``Gtk.Bin`` that provides a
              sidebar for switching between the pages of a
              ``Gtk.Stack``.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-BC-014`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_stacksidebar.py::TestGTK3StackSidebar::test_init``

----

.. _PTW-GTK3-BC-041:

PTW-GTK3-BC-041
---------------

:Description: ``GTK3StackSidebarMixin.__init__()`` **SHALL** add
              ``stack`` (default ``None``) to ``dic_properties``.
              ``GTK3StackSidebarMixin.do_set_properties()`` **SHALL**
              call ``super().do_set_properties()`` first and then call
              ``set_stack()`` only when ``stack`` is not ``None``.
:Rationale:   Skipping a ``None`` stack preserves a stack that was
              attached directly through the native API.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_stacksidebar.py::TestGTK3StackSidebar::test_do_set_properties_default``
              ``tests/gtk3/container/test_stacksidebar.py::TestGTK3StackSidebar::test_do_set_properties``

----

GTK3StackSwitcher
=================

.. _PTW-GTK3-BC-042:

PTW-GTK3-BC-042
---------------

:Description: The ``GTK3StackSwitcher`` class **SHALL** combine
              ``Gtk.StackSwitcher`` and ``GTK3StackSwitcherMixin``,
              which derives from ``GTK3BoxMixin``.
              ``GTK3StackSwitcher.__init__()`` **SHALL** take no
              parameters and **SHALL** call
              ``Gtk.StackSwitcher.__init__()`` followed by
              ``GTK3StackSwitcherMixin.__init__()``.
:Rationale:   ``Gtk.StackSwitcher`` is a ``Gtk.Box`` of buttons for
              switching between the pages of a ``Gtk.Stack``.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-BC-008`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_stackswitcher.py::TestGTK3StackSwitcher::test_init``

----

.. _PTW-GTK3-BC-043:

PTW-GTK3-BC-043
---------------

:Description: ``GTK3StackSwitcherMixin.__init__()`` **SHALL** add
              ``icon_size`` (default ``1``) and ``stack`` (default
              ``None``) to ``dic_properties``.
              ``GTK3StackSwitcherMixin.do_set_properties()`` **SHALL**
              call ``super().do_set_properties()`` first, apply
              ``stack`` with ``set_stack()``, and apply ``icon_size``
              through ``set_property("icon-size", ...)``.
:Rationale:   ``icon-size`` has no dedicated setter in
              ``Gtk.StackSwitcher``.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_stackswitcher.py::TestGTK3StackSwitcher::test_do_set_properties_default``
              ``tests/gtk3/container/test_stackswitcher.py::TestGTK3StackSwitcher::test_do_set_properties``

----

GTK3Viewport
============

.. _PTW-GTK3-BC-044:

PTW-GTK3-BC-044
---------------

:Description: The ``GTK3Viewport`` class **SHALL** combine
              ``Gtk.Viewport`` and ``GTK3ViewportMixin``, which derives
              from ``GTK3ContainerMixin``. ``GTK3Viewport.__init__()``
              **SHALL** accept ``hadjustment`` and ``vadjustment``
              parameters (``Gtk.Adjustment | None``, default ``None``),
              pass both as keyword arguments to
              ``Gtk.Viewport.__init__()``, and then call
              ``GTK3ViewportMixin.__init__()``.
:Rationale:   A viewport's adjustments are normally shared with the
              scrollbars of an enclosing scrolled window and are
              supplied at construction.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-GTK3-BC-014`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_viewport.py::TestGTK3Viewport::test_init``

----

.. _PTW-GTK3-BC-045:

PTW-GTK3-BC-045
---------------

:Description: ``GTK3ViewportMixin.__init__()`` **SHALL** add
              ``shadow_type`` (default ``Gtk.ShadowType.IN``) to
              ``dic_properties``. ``GTK3ViewportMixin.do_set_properties()``
              **SHALL** call ``super().do_set_properties()`` first and
              then apply ``shadow_type`` with ``set_shadow_type()``.
:Rationale:   The default matches the native ``Gtk.Viewport``.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`,
              :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/container/test_viewport.py::TestGTK3Viewport::test_do_set_properties_default``
              ``tests/gtk3/container/test_viewport.py::TestGTK3Viewport::test_do_set_properties``
