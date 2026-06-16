"""The pytkwrap GTK3 dialog package.

NOTE: Sub-modules in this package must import siblings directly
(e.g. from pytkwrap.gtk3.combo import GTK3ComboBox)
and never through this __init__.py to avoid circular imports.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Local Imports
from .aboutdialog import GTK3AboutDialog
from .dialog import GTK3Dialog

__all__ = [
    "GTK3AboutDialog",
    "GTK3Dialog",
]
