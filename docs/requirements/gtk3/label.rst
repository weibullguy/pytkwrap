.. _gtk3_label:

===================================
GTK3 Layer — Label Requirements
===================================

This document defines the software requirements for the
``GTK3Label`` class defined in ``pytkwrap.gtk3.io.label``. These
requirements cover both the standard pytkwrap widget interface and
the Label-specific methods for font configuration, markup handling,
and the ``do_make_label_group()`` utility function.

All requirements in this document trace to one or more system
requirements defined in :ref:`system_requirements` and to GTK3 layer
widget requirements defined in :ref:`gtk3_widgets`.

.. contents:: Contents
   :local:
   :depth: 1

----

Initialization
==============

.. _PTW-GTK3-L-001:

PTW-GTK3-L-001
--------------

:Description: The ``GTK3Label`` class **SHALL** combine ``Gtk.Label``
              and ``GTK3LabelMixin`` and **SHALL** define
              ``_DEFAULT_HEIGHT`` as ``30`` and ``_DEFAULT_WIDTH`` as
              ``200``. The mixin **SHALL** provide ``data_type=str``
              and ``default_value="..."`` attributes; it does not
              define a separate ``edit_signal``.
:Rationale:   Labels do not emit user edit signals — they display
              values but do not accept user input. An empty edit
              signal reflects this read-only nature and prevents
              spurious signal blocking.
:Traces to:   :ref:`PTW-GTK3-M-005`, :ref:`PTW-GTK3-W-019`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_label.py::TestGTK3Label::test_init``

----

.. _PTW-GTK3-L-002:

PTW-GTK3-L-002
--------------

:Description: The ``GTK3Label.__init__()`` method **SHALL** accept
              a ``text`` string parameter and **SHALL** call
              ``do_set_font_description()`` and ``do_set_value()``
              with the provided text during initialization.
:Rationale:   Displaying the initial text and applying the default
              font during initialization ensures the label is
              immediately usable without requiring post-construction
              configuration calls.
:Traces to:   :ref:`PTW-SR-W-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_label.py::TestGTK3Label::test_init``

----

.. _PTW-GTK3-L-003:

PTW-GTK3-L-003
--------------

:Description: The ``GTK3Label.__init__()`` method **SHALL** set
              ``default`` to ``"..."``.
:Rationale:   An ellipsis is a standard placeholder that indicates
              content is pending or unavailable, which is more
              informative than an empty string for a display-only
              widget.
:Traces to:   :ref:`PTW-SR-W-003`, :ref:`PTW-COM-M-010`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_label.py::TestGTK3Label::test_init``

----

do_get_value and do_set_value
==============================

.. _PTW-GTK3-L-004:

PTW-GTK3-L-004
--------------

:Description: The ``GTK3Label.do_get_value()`` method **SHALL**
              return the current text content of the label as
              returned by ``Gtk.Label.get_text()``.
:Rationale:   ``get_text()`` returns the plain text content of the
              label, stripping any Pango markup. This provides a
              consistent return value regardless of whether the label
              is using markup or plain text mode.
:Traces to:   :ref:`PTW-SR-W-006`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_label.py::TestGTK3Label::test_do_get_value``

----

.. _PTW-GTK3-L-005:

PTW-GTK3-L-005
--------------

:Description: The ``GTK3Label.do_set_value()`` method **SHALL**
              accept a ``bool | float | int | str | None`` value
              and **SHALL** update the label's displayed text
              according to the following rules:

              - A ``None`` value **SHALL** be converted to an
                empty string ``""``.
              - When ``use_markup`` is ``True``: the label
                **SHALL** be set using the markup string constructed
                from the ``font_description`` in ``dic_attributes``
                and the value, followed by ``</span>``. If
                ``use_underline`` is also ``True``,
                ``set_markup_with_mnemonic()`` **SHALL** be used.
              - When ``use_underline`` is ``True`` and
                ``use_markup`` is ``False``:
                ``set_text_with_mnemonic()`` **SHALL** be used.
              - Otherwise: ``set_text()`` **SHALL** be used.

:Rationale:   The label display method depends on whether markup
              and mnemonic underlines are enabled. Handling all
              combinations in ``do_set_value()`` allows the caller
              to simply pass a value without knowing which GTK3
              setter to call.
:Traces to:   :ref:`PTW-SR-W-007`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_label.py::TestGTK3Label::test_do_set_value_plain``
              ``tests/gtk3/test_label.py::TestGTK3Label::test_do_set_value_markup``
              ``tests/gtk3/test_label.py::TestGTK3Label::test_do_set_value_underline``
              ``tests/gtk3/test_label.py::TestGTK3Label::test_do_set_value_markup_and_underline``
              ``tests/gtk3/test_label.py::TestGTK3Label::test_do_set_value_none``

----

do_update Behavior
==================

.. _PTW-GTK3-L-006:

PTW-GTK3-L-006
--------------

:Description: The ``GTK3Label.do_update()`` method **SHALL** accept
              a value and **SHALL** call ``do_set_value()`` with the
              string representation of the value. If the value is
              ``None`` or the string ``"None"``, the update
              **SHALL** be silently ignored.
:Rationale:   Labels display read-only data and do not have an edit
              signal to block. Ignoring ``None`` and ``"None"``
              values prevents the label from displaying these
              uninformative strings when data is unavailable.
:Traces to:   :ref:`PTW-SR-M-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_label.py::TestGTK3Label::test_do_update``
              ``tests/gtk3/test_label.py::TestGTK3Label::test_do_update_none``
              ``tests/gtk3/test_label.py::TestGTK3Label::test_do_update_none_string``

----

Font Configuration
==================

.. _PTW-GTK3-L-007:

PTW-GTK3-L-007
--------------

:Description: The ``GTK3Label`` class **SHALL** provide a
              ``do_set_font_description()`` method that accepts an
              optional ``FontDescription | None`` parameter
              defaulting to ``None`` and **SHALL** apply the font
              to the label widget.
:Rationale:   Font configuration is essential for labels that
              display data with specific formatting requirements
              such as bold headings, colored text, or custom sizing.
              Encapsulating the font application logic in a dedicated
              method provides a consistent interface.
:Traces to:   :ref:`PTW-SR-W-001`, :ref:`PTW-COM-X-012`,
              :ref:`PTW-COM-X-013`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_label.py::TestGTK3Label::test_do_set_font_description``
              ``tests/gtk3/test_label.py::TestGTK3Label::test_do_set_font_description_none``

----

.. _PTW-GTK3-L-008:

PTW-GTK3-L-008
--------------

:Description: The ``GTK3Label.do_set_font_description()`` method
              **SHALL** store the ``FontDescription`` instance in
              ``dic_attributes["font_description"]``. When
              ``use_markup`` is ``True``, it **SHALL** apply the
              font by calling ``set_markup()`` with the markup string
              constructed from ``FontDescription.to_markup()``
              wrapped around the current label text. When
              ``use_markup`` is ``False``, it **SHALL** apply the
              font by calling ``Gtk.Widget.override_font()`` with a
              ``Pango.FontDescription`` constructed from
              ``FontDescription.to_string()``.
:Rationale:   The font application method differs between markup
              and non-markup labels. For markup labels the font is
              embedded in the markup string via ``to_markup()``. For
              non-markup labels the font is applied via
              ``override_font()`` using ``to_string()``. Both paths
              keep the ``FontDescription`` dataclass toolkit-agnostic
              as required by :ref:`PTW-COM-X-011`.
:Traces to:   :ref:`PTW-COM-X-011`, :ref:`PTW-COM-X-012`,
              :ref:`PTW-COM-X-013`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_label.py::TestGTK3Label::test_do_set_font_description_markup``
              ``tests/gtk3/test_label.py::TestGTK3Label::test_do_set_font_description_no_markup``
              ``tests/gtk3/test_label.py::TestGTK3Label::test_do_set_font_description_stored_in_dic_attributes``

----

.. _PTW-GTK3-L-009:

PTW-GTK3-L-009
--------------

:Description: When ``do_set_font_description()`` is called with
              ``None``, a default ``FontDescription()`` instance
              **SHALL** be used.
:Rationale:   Using a default ``FontDescription()`` when ``None``
              is passed ensures the label always has a valid font
              applied, consistent with the behavior of
              ``GTK3Entry.do_set_font_description()`` as defined
              in :ref:`PTW-GTK3-E-008`.
:Traces to:   :ref:`PTW-SR-W-003`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_label.py::TestGTK3Label::test_do_set_font_description_none``

----

do_set_properties Behavior
==========================

.. _PTW-GTK3-L-010:

PTW-GTK3-L-010
--------------

:Description: The ``GTK3Label.do_set_properties()`` method **SHALL**
              set the label's horizontal alignment based on the
              ``justify`` property as follows:

              - ``Gtk.Justification.CENTER``: ``xalign`` **SHALL**
                be set to ``0.5``.
              - ``Gtk.Justification.LEFT``: ``xalign`` **SHALL**
                be set to ``0.05``.
              - Any other value: ``xalign`` **SHALL** be set to
                ``0.95``.

:Rationale:   The ``xalign`` property controls the horizontal
              position of the text within the label widget.
              Automatically deriving ``xalign`` from ``justify``
              ensures consistent visual alignment without requiring
              the caller to set both properties.
:Traces to:   :ref:`PTW-SR-W-004`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_label.py::TestGTK3Label::test_do_set_properties_justify_center``
              ``tests/gtk3/test_label.py::TestGTK3Label::test_do_set_properties_justify_left``
              ``tests/gtk3/test_label.py::TestGTK3Label::test_do_set_properties_justify_right``

----

do_make_label_group
===================

.. _PTW-GTK3-L-011:

PTW-GTK3-L-011
--------------

:Description: The ``do_make_label_group()`` function **SHALL**
              accept a list of text strings and **SHALL** return a
              tuple containing the maximum label width in pixels and
              a list of ``GTK3Label`` instances, one per text string.
:Rationale:   A group of labels that describe related data entry
              fields **SHALL** all have the same width so that the
              corresponding data entry widgets align vertically.
              The maximum width is returned so the caller can
              position the data entry widgets at the correct
              horizontal offset.
:Traces to:   :ref:`PTW-SR-W-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_label.py::test_do_make_label_group``
              ``tests/gtk3/test_label.py::test_do_make_label_group_single``
              ``tests/gtk3/test_label.py::test_do_make_label_group_empty``

----

.. _PTW-GTK3-L-012:

PTW-GTK3-L-012
--------------

:Description: The ``do_make_label_group()`` function **SHALL** set
              the width in characters of each label to the length
              of the longest text string in the list, ensuring all
              labels have the same natural width.
:Rationale:   Setting all labels to the same character width ensures
              that the labels occupy the same horizontal space
              regardless of their text content, which is required
              for consistent vertical alignment of data entry widgets.
:Traces to:   :ref:`PTW-SR-W-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       ``tests/gtk3/test_label.py::test_do_make_label_group``
              ``tests/gtk3/test_label.py::test_do_make_label_group_uniform_width``
