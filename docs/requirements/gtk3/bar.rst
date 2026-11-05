.. _gtk3_bar:

==================================
GTK3 Layer — Bar Requirements
==================================

This document defines the software requirements for the bar-like
wrappers in the ``pytkwrap.gtk3.bar`` package: ``GTK3ActionBar``,
``GTK3HeaderBar``, ``GTK3InfoBar``, ``GTK3LevelBar``,
``GTK3PlacesSidebar``, ``GTK3ProgressBar``, ``GTK3ScrollBar``,
``GTK3SearchBar``, and ``GTK3Statusbar``. Each concrete wrapper
composes its native ``Gtk`` class with a GTK3 mixin; there is no
common bar base class.

All requirements in this document trace to one or more system
requirements defined in :ref:`system_requirements` and to GTK3 layer
widget requirements defined in :ref:`gtk3_widgets`.

.. contents:: Contents
   :local:
   :depth: 1

----

Package
=======

.. _PTW-GTK3-BAR-001:

PTW-GTK3-BAR-001
----------------

:Description: The ``pytkwrap.gtk3.bar`` package **SHALL** export
              ``GTK3ActionBar``, ``GTK3HeaderBar``, ``GTK3InfoBar``,
              ``GTK3LevelBar``, ``GTK3PlacesSidebar``,
              ``GTK3ProgressBar``, ``GTK3ScrollBar``,
              ``GTK3SearchBar``, and ``GTK3Statusbar`` through
              ``__all__``. Sub-modules of the package **SHALL** import
              sibling modules directly and **SHALL NOT** import through
              the package ``__init__.py``.
:Rationale:   A single public import location simplifies application
              code, while direct sibling imports avoid circular
              imports during package initialization.
:Traces to:   :ref:`PTW-SR-W-001`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-BAR-002:

PTW-GTK3-BAR-002
----------------

:Description: Each bar mixin's ``__init__()`` method **SHALL** accept
              arbitrary keyword arguments and **SHALL** forward them to
              ``super().__init__()`` before extending the inherited
              ``dic_attributes``, ``dic_handler_id``, and
              ``dic_properties`` mappings.
:Rationale:   Cooperative initialization allows the bar mixins to be
              composed in multiple-inheritance hierarchies without
              discarding configuration intended for parent mixins.
:Traces to:   :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-BAR-003:

PTW-GTK3-BAR-003
----------------

:Description: Each bar mixin that defines a ``do_set_properties()``
              method **SHALL** call ``super().do_set_properties()``
              before applying its bar-specific properties.
:Rationale:   Calling ``super()`` first merges the supplied values
              into ``dic_properties`` and applies inherited widget and
              container properties before the bar-specific values are
              applied.
:Traces to:   :ref:`PTW-SR-W-004`, :ref:`PTW-GTK3-X-013`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

GTK3ActionBar
=============

.. _PTW-GTK3-BAR-004:

PTW-GTK3-BAR-004
----------------

:Description: The ``GTK3ActionBar`` class **SHALL** combine
              ``Gtk.ActionBar`` with ``GTK3WidgetMixin``. Its
              ``__init__()`` method **SHALL** call
              ``Gtk.ActionBar.__init__()`` followed by
              ``GTK3WidgetMixin.__init__()`` and **SHALL NOT** add
              properties, attributes, or signals beyond those provided
              by ``GTK3WidgetMixin``.
:Rationale:   The action bar needs no pytkwrap-specific configuration;
              the native packing API (``pack_start()``,
              ``pack_end()``, ``set_center_widget()``) remains
              available directly.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-SR-W-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_actionbar.py::TestGTK3ActionBar``

----

GTK3HeaderBar
=============

.. _PTW-GTK3-BAR-005:

PTW-GTK3-BAR-005
----------------

:Description: The ``GTK3HeaderBar`` class **SHALL** combine
              ``Gtk.HeaderBar`` with ``GTK3HeaderBarMixin``, which
              derives from ``GTK3ContainerMixin``. Its ``__init__()``
              method **SHALL** call ``Gtk.HeaderBar.__init__()``
              followed by ``GTK3HeaderBarMixin.__init__()``.
:Rationale:   The native class supplies the header bar behavior while
              the mixin supplies pytkwrap configuration and inherited
              container signal bookkeeping.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_headerbar.py::TestGTK3HeaderBar``

----

.. _PTW-GTK3-BAR-006:

PTW-GTK3-BAR-006
----------------

:Description: ``GTK3HeaderBarMixin.__init__()`` **SHALL** add the
              following header-bar properties to ``dic_properties``
              with the stated defaults:

              - ``custom_title``: ``None``
              - ``decoration_layout``: ``None``
              - ``decoration_layout_set``: ``False``
              - ``has_subtitle``: ``True``
              - ``show_close_button``: ``False``
              - ``spacing``: ``6``
              - ``subtitle``: ``None``
              - ``title``: ``None``

:Rationale:   The defaults match the GTK3 ``Gtk.HeaderBar`` defaults
              so an unconfigured wrapper behaves like the native widget.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_headerbar.py::TestGTK3HeaderBar::test_do_set_properties_default``

----

.. _PTW-GTK3-BAR-007:

PTW-GTK3-BAR-007
----------------

:Description: ``GTK3HeaderBarMixin.do_set_properties()`` **SHALL**
              apply ``custom_title``, ``decoration_layout``,
              ``has_subtitle``, ``show_close_button``, ``subtitle``,
              and ``title`` through their corresponding
              ``Gtk.HeaderBar`` setter methods, and **SHALL** apply
              ``decoration_layout_set`` and ``spacing`` through
              ``set_property()`` using the hyphenated GObject property
              names ``decoration-layout-set`` and ``spacing``.
:Rationale:   ``decoration-layout-set`` and ``spacing`` have no
              dedicated setter in ``Gtk.HeaderBar`` and must be applied
              as GObject properties.
:Traces to:   :ref:`PTW-SR-W-004`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_headerbar.py::TestGTK3HeaderBar::test_do_set_properties``

----

GTK3InfoBar
===========

.. _PTW-GTK3-BAR-008:

PTW-GTK3-BAR-008
----------------

:Description: The ``GTK3InfoBar`` class **SHALL** combine
              ``Gtk.InfoBar`` with ``GTK3InfoBarMixin``, which derives
              from ``GTK3BoxMixin``. Its ``__init__()`` method
              **SHALL** call ``Gtk.InfoBar.__init__()`` followed by
              ``GTK3InfoBarMixin.__init__()``.
:Rationale:   ``Gtk.InfoBar`` is a ``Gtk.Box`` subclass; the box mixin
              supplies the inherited box and container configuration.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_infobar.py::TestGTK3InfoBar``

----

.. _PTW-GTK3-BAR-009:

PTW-GTK3-BAR-009
----------------

:Description: ``GTK3InfoBarMixin.__init__()`` **SHALL** pre-register
              the ``"close"`` and ``"response"`` signals in
              ``dic_handler_id`` with a value of ``-1`` and **SHALL**
              add the following properties to ``dic_properties``:

              - ``message_type``: ``Gtk.MessageType.INFO``
              - ``revealed``: ``True``
              - ``show_close_button``: ``False``

:Rationale:   Pre-registering the info bar signals makes them
              available to ``do_set_callbacks()``; the property
              defaults match the native widget.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_infobar.py::TestGTK3InfoBar::test_do_set_properties_default``

----

.. _PTW-GTK3-BAR-010:

PTW-GTK3-BAR-010
----------------

:Description: ``GTK3InfoBarMixin.do_set_properties()`` **SHALL** apply
              ``message_type``, ``revealed``, and
              ``show_close_button`` using ``set_message_type()``,
              ``set_revealed()``, and ``set_show_close_button()``
              respectively.
:Rationale:   These are the info-bar-specific properties exposed by
              ``Gtk.InfoBar``.
:Traces to:   :ref:`PTW-SR-W-004`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_infobar.py::TestGTK3InfoBar::test_do_set_properties``

----

GTK3LevelBar
============

.. _PTW-GTK3-BAR-011:

PTW-GTK3-BAR-011
----------------

:Description: The ``GTK3LevelBar`` class **SHALL** combine
              ``Gtk.LevelBar`` with ``GTK3LevelBarMixin``, which
              derives from ``GTK3WidgetMixin``. Its ``__init__()``
              method **SHALL** call ``Gtk.LevelBar.__init__()``
              followed by ``GTK3LevelBarMixin.__init__()``.
              ``GTK3LevelBar`` **SHALL** define a custom
              ``GObject.Signal`` named ``"changed"`` with no
              arguments.
:Rationale:   ``Gtk.LevelBar`` has no native value-changed signal; the
              custom ``"changed"`` signal provides the edit signal
              used by the pytkwrap value-update machinery.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-SR-M-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_levelbar.py::TestGTK3LevelBar``

----

.. _PTW-GTK3-BAR-012:

PTW-GTK3-BAR-012
----------------

:Description: ``GTK3LevelBarMixin.__init__()`` **SHALL** set
              ``dic_attributes["default_value"]`` to ``0.0`` and
              ``dic_attributes["edit_signal"]`` to ``"changed"``, and
              **SHALL** pre-register the ``"offset-changed"`` signal in
              ``dic_handler_id`` with a value of ``-1``.
:Rationale:   The default value is substituted for ``None`` packages
              in ``do_update()``; the edit signal identifies the
              handler to block during programmatic updates.
:Traces to:   :ref:`PTW-SR-W-005`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-010`, :ref:`PTW-GTK3-W-011`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_levelbar.py::TestGTK3LevelBar::test_do_set_default_attributes``
              ``tests/gtk3/bar/test_levelbar.py::TestGTK3LevelBar::test_do_set_attributes``

----

.. _PTW-GTK3-BAR-013:

PTW-GTK3-BAR-013
----------------

:Description: ``GTK3LevelBarMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``inverted``: ``False``
              - ``max_value``: ``1.0``
              - ``min_value``: ``0.0``
              - ``mode``: ``Gtk.LevelBarMode.CONTINUOUS``
              - ``value``: ``0.0``

              ``GTK3LevelBarMixin.do_set_properties()`` **SHALL**
              apply these using ``set_inverted()``,
              ``set_max_value()``, ``set_min_value()``,
              ``set_mode()``, and ``set_value()``, in that order.
:Rationale:   The defaults match the native ``Gtk.LevelBar``. Setting
              the bounds before the value ensures the value is
              interpreted against the configured range.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_levelbar.py::TestGTK3LevelBar::test_do_set_properties_default``
              ``tests/gtk3/bar/test_levelbar.py::TestGTK3LevelBar::test_do_set_properties``

----

.. _PTW-GTK3-BAR-014:

PTW-GTK3-BAR-014
----------------

:Description: ``GTK3LevelBarMixin.do_get_value()`` **SHALL** return
              the current level bar value as a ``float``.
:Rationale:   A level bar value is always numeric; returning a
              ``float`` gives callers a consistent type.
:Traces to:   :ref:`PTW-SR-W-006`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_levelbar.py::TestGTK3LevelBar::test_do_get_value``

----

.. _PTW-GTK3-BAR-015:

PTW-GTK3-BAR-015
----------------

:Description: ``GTK3LevelBarMixin.do_set_value()`` **SHALL** accept a
              ``float``, ``int``, or ``str`` value, convert it to
              ``float``, clamp it to the range
              [``dic_properties["min_value"]``,
              ``dic_properties["max_value"]``], apply it with
              ``set_value()``, store it in
              ``dic_properties["value"]``, and emit the ``"changed"``
              signal.
:Rationale:   Clamping keeps the stored value consistent with the
              displayed value, and emitting ``"changed"`` notifies
              listeners of the new value.
:Traces to:   :ref:`PTW-SR-W-007`, :ref:`PTW-COM-U-011`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_levelbar.py::TestGTK3LevelBar::test_do_set_value_float``
              ``tests/gtk3/bar/test_levelbar.py::TestGTK3LevelBar::test_do_set_value_int``
              ``tests/gtk3/bar/test_levelbar.py::TestGTK3LevelBar::test_do_set_value_str``
              ``tests/gtk3/bar/test_levelbar.py::TestGTK3LevelBar::test_do_set_value_by_property``
              ``tests/gtk3/bar/test_levelbar.py::TestGTK3LevelBar::test_do_set_value_out_of_range``
              ``tests/gtk3/bar/test_levelbar.py::TestGTK3LevelBar::test_do_set_value_discrete``

----

.. _PTW-GTK3-BAR-016:

PTW-GTK3-BAR-016
----------------

:Description: When ``GTK3LevelBarMixin.do_set_value()`` receives a
              value that is not a ``float``, ``int``, or ``str``, it
              **SHALL** delegate to the base ``do_set_value()``, which
              publishes a ``do_log_error`` message and raises
              ``WrongTypeError``.
:Rationale:   Unsupported value types are reported consistently with
              all other value-bearing wrappers.
:Traces to:   :ref:`PTW-SR-W-007`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_levelbar.py::TestGTK3LevelBar::test_do_set_value_invalid_type``

----

GTK3PlacesSidebar
=================

.. _PTW-GTK3-BAR-017:

PTW-GTK3-BAR-017
----------------

:Description: The ``GTK3PlacesSidebar`` class **SHALL** combine
              ``Gtk.PlacesSidebar`` with ``GTK3PlacesSidebarMixin``,
              which derives from ``GTK3ScrolledWindowMixin``. Its
              ``__init__()`` method **SHALL** call
              ``Gtk.PlacesSidebar.__init__()`` followed by
              ``GTK3PlacesSidebarMixin.__init__()``.
:Rationale:   ``Gtk.PlacesSidebar`` is a ``Gtk.ScrolledWindow``
              subclass; the scrolled window mixin supplies the
              inherited configuration.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_placessidebar.py::TestGTK3PlacesSidebar``

----

.. _PTW-GTK3-BAR-018:

PTW-GTK3-BAR-018
----------------

:Description: ``GTK3PlacesSidebarMixin.__init__()`` **SHALL**
              pre-register the following signals in
              ``dic_handler_id`` with a value of ``-1``:

              - ``"drag-action-ask"``
              - ``"drag-action-requested"``
              - ``"drag-perform-drop"``
              - ``"mount"``
              - ``"open-location"``
              - ``"populate-popup"``
              - ``"show-connect-to-server"``
              - ``"show-enter-location"``
              - ``"show-error-message"``
              - ``"show-other-locations"``
              - ``"show-other-locations-with-flags"``
              - ``"show-starred-location"``
              - ``"unmount"``

:Rationale:   Pre-registering the places sidebar signals makes them
              available for connection via ``do_set_callbacks()``.
:Traces to:   :ref:`PTW-GTK3-W-003`, :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_placessidebar.py::TestGTK3PlacesSidebar``

----

.. _PTW-GTK3-BAR-019:

PTW-GTK3-BAR-019
----------------

:Description: ``GTK3PlacesSidebarMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``local_only``: ``False``
              - ``location``: ``None``
              - ``open_flags``: ``Gtk.PlacesOpenFlags.NORMAL``
              - ``populate_all``: ``False``
              - ``show_desktop``: ``True``
              - ``show_enter_location``: ``False``
              - ``show_other_locations``: ``False``
              - ``show_recent``: ``True``
              - ``show_starred_location``: ``False``
              - ``show_trash``: ``True``

:Rationale:   The defaults match the native ``Gtk.PlacesSidebar``.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-GTK3-W-018`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_placessidebar.py::TestGTK3PlacesSidebar::test_do_set_properties_default``

----

.. _PTW-GTK3-BAR-020:

PTW-GTK3-BAR-020
----------------

:Description: ``GTK3PlacesSidebarMixin.do_set_properties()`` **SHALL**
              apply ``local_only``, ``open_flags``, ``show_desktop``,
              ``show_enter_location``, ``show_other_locations``,
              ``show_recent``, ``show_starred_location``, and
              ``show_trash`` through their corresponding setter
              methods; **SHALL** call ``set_location()`` only when
              ``location`` is not ``None``; and **SHALL** apply
              ``populate_all`` through ``set_property("populate-all",
              ...)``.
:Rationale:   ``set_location()`` does not accept ``None`` as "no
              selection", and ``populate-all`` has no dedicated setter.
:Traces to:   :ref:`PTW-SR-W-004`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_placessidebar.py::TestGTK3PlacesSidebar::test_do_set_properties``

----

GTK3ProgressBar
===============

.. _PTW-GTK3-BAR-021:

PTW-GTK3-BAR-021
----------------

:Description: The ``GTK3ProgressBar`` class **SHALL** combine
              ``Gtk.ProgressBar`` with ``GTK3ProgressBarMixin``, which
              derives from ``GTK3WidgetMixin``. Its ``__init__()``
              method **SHALL** call ``Gtk.ProgressBar.__init__()``
              followed by ``GTK3ProgressBarMixin.__init__()``.
              ``GTK3ProgressBar`` **SHALL** define a custom
              ``GObject.Signal`` named ``"changed"`` with no
              arguments.
:Rationale:   ``Gtk.ProgressBar`` has no native value-changed signal;
              the custom signal provides the edit signal used by the
              pytkwrap value-update machinery.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-SR-M-002`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_progressbar.py::TestGTK3ProgressBar``

----

.. _PTW-GTK3-BAR-022:

PTW-GTK3-BAR-022
----------------

:Description: ``GTK3ProgressBarMixin.__init__()`` **SHALL** set
              ``dic_attributes["default_value"]`` to ``0.0``,
              ``dic_attributes["data_type"]`` to ``float``, and
              ``dic_attributes["edit_signal"]`` to ``"changed"``, and
              **SHALL NOT** pre-register any progress-bar-specific
              signals in ``dic_handler_id``.
:Rationale:   ``data_type`` determines the Python type used when
              reading and writing the progress value.
:Traces to:   :ref:`PTW-SR-W-005`, :ref:`PTW-GTK3-W-010`,
              :ref:`PTW-GTK3-W-011`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_progressbar.py::TestGTK3ProgressBar::test_do_set_attributes_default``
              ``tests/gtk3/bar/test_progressbar.py::TestGTK3ProgressBar::test_do_set_attributes``

----

.. _PTW-GTK3-BAR-023:

PTW-GTK3-BAR-023
----------------

:Description: ``GTK3ProgressBarMixin.__init__()`` **SHALL** add the
              following properties to ``dic_properties``:

              - ``ellipsize``: ``Pango.EllipsizeMode.NONE``
              - ``fraction``: ``0.0``
              - ``inverted``: ``False``
              - ``pulse_step``: ``0.1``
              - ``show_text``: ``False``
              - ``text``: ``None``

              ``GTK3ProgressBarMixin.do_set_properties()`` **SHALL**
              apply each of these through its corresponding
              ``Gtk.ProgressBar`` setter method.
:Rationale:   The defaults match the native ``Gtk.ProgressBar``.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_progressbar.py::TestGTK3ProgressBar::test_do_set_properties_default``
              ``tests/gtk3/bar/test_progressbar.py::TestGTK3ProgressBar::test_do_set_properties``

----

.. _PTW-GTK3-BAR-024:

PTW-GTK3-BAR-024
----------------

:Description: ``GTK3ProgressBarMixin.do_get_value()`` **SHALL** return
              the current fraction converted with
              ``dic_attributes["data_type"]``.
:Rationale:   The configurable data type lets the progress value match
              the type of the underlying data field.
:Traces to:   :ref:`PTW-SR-W-006`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_progressbar.py::TestGTK3ProgressBar::test_do_get_value``

----

.. _PTW-GTK3-BAR-025:

PTW-GTK3-BAR-025
----------------

:Description: ``GTK3ProgressBarMixin.do_set_value()`` **SHALL** accept
              a ``float``, ``int``, or ``str`` value and convert it
              with ``dic_attributes["data_type"]``. A converted value
              greater than ``1.0`` **SHALL** be treated as a
              percentage and divided by ``100.0``. The resulting
              fraction **SHALL** be applied with ``set_fraction()``,
              stored in ``dic_properties["fraction"]``, and followed by
              emission of the ``"changed"`` signal. Any other value
              type **SHALL** be delegated to the base
              ``do_set_value()``, which logs and raises
              ``WrongTypeError``.
:Rationale:   Callers may supply progress as a fraction (0.0–1.0) or a
              percentage (0–100) without converting it first.
:Traces to:   :ref:`PTW-SR-W-007`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_progressbar.py::TestGTK3ProgressBar::test_do_set_value``
              ``tests/gtk3/bar/test_progressbar.py::TestGTK3ProgressBar::test_do_set_value_int``
              ``tests/gtk3/bar/test_progressbar.py::TestGTK3ProgressBar::test_do_set_value_str``

----

GTK3ScrollBar
=============

.. _PTW-GTK3-BAR-026:

PTW-GTK3-BAR-026
----------------

:Description: The ``GTK3ScrollBar`` class **SHALL** combine
              ``Gtk.Scrollbar`` with ``GTK3RangeMixin``. Its
              ``__init__()`` method **SHALL** accept an
              ``orientation`` argument defaulting to
              ``Gtk.Orientation.VERTICAL`` and an ``adjustment``
              argument defaulting to ``None``, **SHALL** pass both as
              keyword arguments to ``Gtk.Scrollbar.__init__()``, and
              **SHALL** then call ``GTK3RangeMixin.__init__()``.
:Rationale:   Orientation and adjustment are construct-time properties
              of ``Gtk.Scrollbar``. All other configuration comes from
              the range mixin, so no scrollbar-specific mixin is
              needed.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`,
              :ref:`PTW-SR-W-003`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_scrollbar.py::TestGTK3ScrollBar::test_init_with_orientation``
              ``tests/gtk3/bar/test_scrollbar.py::TestGTK3ScrollBar::test_init_with_adjustment``

----

GTK3SearchBar
=============

.. _PTW-GTK3-BAR-027:

PTW-GTK3-BAR-027
----------------

:Description: The ``GTK3SearchBar`` class **SHALL** combine
              ``Gtk.SearchBar`` with ``GTK3SearchBarMixin``, which
              derives from ``GTK3ContainerMixin``. Its ``__init__()``
              method **SHALL** call ``Gtk.SearchBar.__init__()``
              followed by ``GTK3SearchBarMixin.__init__()``.
:Rationale:   The mixin supplies pytkwrap configuration and inherited
              container signal bookkeeping.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-017`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_searchbar.py::TestGTK3SearchBar``

----

.. _PTW-GTK3-BAR-028:

PTW-GTK3-BAR-028
----------------

:Description: ``GTK3SearchBarMixin.__init__()`` **SHALL** add
              ``search_mode_enabled`` (default ``False``) and
              ``show_close_button`` (default ``False``) to
              ``dic_properties``. ``GTK3SearchBarMixin.do_set_properties()``
              **SHALL** apply ``search_mode_enabled`` with
              ``set_search_mode()`` and ``show_close_button`` with
              ``set_show_close_button()``.
:Rationale:   The property key follows the GObject property name
              ``search-mode-enabled`` while the setter follows the GTK
              method name ``set_search_mode()``.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-SR-W-004`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_searchbar.py::TestGTK3SearchBar::test_do_set_properties_default``
              ``tests/gtk3/bar/test_searchbar.py::TestGTK3SearchBar::test_do_set_properties``

----

GTK3Statusbar
=============

.. _PTW-GTK3-BAR-029:

PTW-GTK3-BAR-029
----------------

:Description: The ``GTK3Statusbar`` class **SHALL** combine
              ``Gtk.Statusbar`` with ``GTK3StatusbarMixin``, which
              derives from ``GTK3BoxMixin``. ``GTK3StatusbarMixin``
              **SHALL** pre-register the ``"text-popped"`` and
              ``"text-pushed"`` signals in ``dic_handler_id`` with a
              value of ``-1``.
:Rationale:   ``Gtk.Statusbar`` is a ``Gtk.Box`` subclass; its
              push/pop signals are made available to
              ``do_set_callbacks()``.
:Traces to:   :ref:`PTW-GTK3-W-001`, :ref:`PTW-GTK3-W-003`,
              :ref:`PTW-GTK3-W-017`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_statusbar.py::TestGTK3Statusbar::test_init``

----

.. _PTW-GTK3-BAR-030:

PTW-GTK3-BAR-030
----------------

:Description: ``GTK3StatusbarMixin.__init__()`` **SHALL** initialize
              two instance-local mappings: ``dic_context_id``
              (context description to GTK context ID) and
              ``dic_message_id`` (message text to GTK message ID),
              both initially empty.
:Rationale:   The mappings let applications address contexts and
              messages by their descriptive strings rather than the
              integer IDs returned by GTK.
:Traces to:   :ref:`PTW-SR-W-001`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_statusbar.py::TestGTK3Statusbar::test_init``

----

.. _PTW-GTK3-BAR-031:

PTW-GTK3-BAR-031
----------------

:Description: ``GTK3Statusbar.__init__()`` **SHALL** accept an optional
              ``contexts`` list of context descriptions. For each
              description it **SHALL** obtain a context ID using
              ``Gtk.Statusbar.get_context_id()`` and store it in
              ``dic_context_id``.
:Rationale:   Registering contexts at construction makes them
              immediately available to ``do_add_message()`` and
              ``do_remove_message()``.
:Traces to:   :ref:`PTW-SR-W-001`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_statusbar.py::TestGTK3Statusbar::test_init_with_context_id``

----

.. _PTW-GTK3-BAR-032:

PTW-GTK3-BAR-032
----------------

:Description: ``GTK3StatusbarMixin.do_add_message()`` **SHALL** push
              the message onto the stack for the named context and
              **SHALL** record the returned message ID in
              ``dic_message_id`` keyed by the message text. If the
              context is not registered, it **SHALL** raise
              ``PytkwrapError`` chained from the ``KeyError``. If GTK
              rejects the message with ``TypeError`` (for example, a
              non-``str`` message), it **SHALL** raise
              ``PytkwrapError`` chained from the ``TypeError``.
:Rationale:   Addressing messages by context description and text
              hides GTK's integer IDs from application code.
:Traces to:   :ref:`PTW-SR-W-001`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_statusbar.py::TestGTK3Statusbar::test_do_add_message``
              ``tests/gtk3/bar/test_statusbar.py::TestGTK3Statusbar::test_do_add_message_no_context``
              ``tests/gtk3/bar/test_statusbar.py::TestGTK3Statusbar::test_do_add_message_no_message``

----

.. _PTW-GTK3-BAR-033:

PTW-GTK3-BAR-033
----------------

:Description: ``GTK3StatusbarMixin.do_remove_message()`` **SHALL**
              accept a context description, an optional message text
              (default ``""``), and an optional ``remove_all`` flag
              (default ``False``), and **SHALL**:

              - call ``remove_all()`` for the context when
                ``remove_all`` is ``True``;
              - otherwise call ``pop()`` for the context when the
                message text is empty;
              - otherwise call ``remove()`` with the context ID and
                the message ID recorded in ``dic_message_id``.

              If the context or message is not registered, it
              **SHALL** raise ``PytkwrapError`` chained from the
              ``KeyError``.
:Rationale:   A single method covers the three GTK removal operations
              while keeping integer IDs internal.
:Traces to:   :ref:`PTW-SR-W-001`
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-11-04) - Initial baseline.
:Tests:       ``tests/gtk3/bar/test_statusbar.py::TestGTK3Statusbar::test_do_remove_message``
              ``tests/gtk3/bar/test_statusbar.py::TestGTK3Statusbar::test_do_remove_all_messages``
              ``tests/gtk3/bar/test_statusbar.py::TestGTK3Statusbar::test_do_remove_first_message``
              ``tests/gtk3/bar/test_statusbar.py::TestGTK3Statusbar::test_do_remove_message_no_context``
              ``tests/gtk3/bar/test_statusbar.py::TestGTK3Statusbar::test_do_remove_all_messages_no_context``
              ``tests/gtk3/bar/test_statusbar.py::TestGTK3Statusbar::test_do_remove_message_no_message``
