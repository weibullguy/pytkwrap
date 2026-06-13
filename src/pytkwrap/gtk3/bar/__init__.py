# pylint: disable=disallowed-name
"""The pytkwrap GTK3 bar-like container package.

NOTE: Sub-modules in this package must import siblings directly
(e.g. from pytkwrap.gtk3.combo import GTK3ComboBox)
and never through this __init__.py to avoid circular imports.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Local Imports
from .actionbar import GTK3ActionBar
from .placessidebar import GTK3PlacesSidebar

__all__ = [
    "GTK3ActionBar",
    "GTK3PlacesSidebar",
]
