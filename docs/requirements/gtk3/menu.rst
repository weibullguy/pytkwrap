.. _gtk3_menu_requirements:

================================
GTK3 Layer — Menu Requirements
================================

This document defines the menu data, loading, and rendering behavior
implemented by ``pytkwrap.gtk3.menu``. ``GTK3MenuShell`` combines the
native GTK menu-shell API with ``GTK3MenuShellMixin``.

All requirements in this document trace to one or more system
requirements defined in :ref:`system_requirements` and the GTK3 mixin
requirements in :ref:`gtk3_mixins`.

.. contents:: Contents
   :local:
   :depth: 1

----

Menu Data Model
===============

.. _PTW-GTK3-MU-001:

PTW-GTK3-MU-001
---------------

:Description: The menu model **SHALL** represent a menu as an optional
              ID and an ordered sequence of submenus. A submenu
              **SHALL** contain attributes and ordered sections; a
              section **SHALL** contain optional attributes and ordered
              child items or nested submenus. Menu attributes **SHALL**
              support ``action``, ``action_namespace``, ``callback``,
              ``custom``, ``display_hint``, ``hidden_when``, ``icon``,
              ``id``, ``label``, ``signal``, ``submenu_action``,
              ``target``, ``text_direction``, ``translatable``, and
              ``use_markup``. ``translatable`` **SHALL** default to
              ``"yes"`` and ``use_markup`` **SHALL** default to
              ``False``.
:Rationale:   A structured tree preserves menu order and grouping while
              allowing the same menu definition to be rendered using
              either supported GTK3 menu API.
:Traces to:   :ref:`PTW-SR-W-001`, :ref:`PTW-GTK3-X-013`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

TOML Menu Loading
=================

.. _PTW-GTK3-MU-002:

PTW-GTK3-MU-002
---------------

:Description: ``do_build_menu_from_file()`` **SHALL** accept a string
              path or ``pathlib.Path`` and load a TOML document whose
              required ``menu`` table containing an optional ID and an
              optional ``submenus`` array. Submenu entries **SHALL**
              contain an attributes table and sections array. Section
              children **SHALL** default to an empty array, and section
              attributes **MAY** be omitted.
:Rationale:   A TOML menu file provides an external, editable
              representation of the structured menu data.
:Traces to:   :ref:`PTW-SR-W-001`, :ref:`PTW-GTK3-MU-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-MU-003:

PTW-GTK3-MU-003
---------------

:Description: The menu loader **SHALL** reject unknown attributes,
              missing required nested tables, and malformed menu
              structures with ``MenuError``. Values with invalid types
              **SHALL** raise ``WrongTypeError``. File access and TOML
              parsing errors **SHALL** be reported as ``MenuError``
              with the original error available through exception
              chaining.
:Rationale:   Validating external menu data before rendering identifies
              malformed configuration at its source.
:Traces to:   :ref:`PTW-GTK3-MU-002`, :ref:`PTW-SR-W-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

Callback References
===================

.. _PTW-GTK3-MU-004:

PTW-GTK3-MU-004
---------------

:Description: Menu callback references **SHALL** use dotted Python
              identifiers and resolve to callable objects in the
              calling context. The loader **SHALL NOT** evaluate
              callback text as a Python expression. A reference
              beginning with ``self`` **SHALL** resolve from the
              calling frame's local ``self`` object.
:Rationale:   Resolving named callbacks supports declarative menu
              configuration without executing arbitrary expressions
              from the menu file.
:Traces to:   :ref:`PTW-GTK3-MU-002`, :ref:`PTW-SR-W-001`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

Menu Building
=============

.. _PTW-GTK3-MU-005:

PTW-GTK3-MU-005
---------------

:Description: ``GTK3MenuShellMixin.do_build_menu()`` **SHALL** support
              ``"gio"`` as its default method, ``"gtk"`` for native GTK
              menu items, and ``"file"`` as a TOML-file-loading method
              that builds a Gio menu model. For ``"gio"`` and ``"gtk"``,
              a supplied menu structure **SHALL** take precedence over a
              file path; ``"file"`` **SHALL** require a file path.
              Unsupported methods or missing required menu input
              **SHALL** raise ``MenuError``.
:Rationale:   The menu-shell API allows callers to choose the GTK menu
              representation while reusing the same menu tree.
:Traces to:   :ref:`PTW-SR-W-001`, :ref:`PTW-GTK3-MU-001`,
              :ref:`PTW-GTK3-MU-002`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.

----

.. _PTW-GTK3-MU-006:

PTW-GTK3-MU-006
---------------

:Description: Gio menu rendering **SHALL** return a menu ID and a
              ``Gio.MenuModel``; labels marked translatable **SHALL** be
              passed through gettext and boolean attributes **SHALL**
              be encoded as lowercase strings. Native GTK menu rendering
              **SHALL** connect a configured callback to its configured
              signal and **SHALL** raise ``MenuError`` when a callback
              is supplied without a signal or its signal connection
              fails. GTK3 menu-shell callbacks **SHALL NOT** receive a
              widget argument from the wrapper.
:Rationale:   These rules preserve the menu definition's translation
              metadata and make callback wiring failures explicit.
:Traces to:   :ref:`PTW-GTK3-MU-001`, :ref:`PTW-GTK3-MU-005`,
              :ref:`PTW-GTK3-X-004`
:Issues:      None
:Status:      Active
:Version:     0.1.0
:History:     0.1.0 (2026-10-29) - Initial baseline.
:Tests:       TBD — to be reconciled in the test review pass.
