"""The pytkwrap GTK3Statusbar module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.exceptions import PytkwrapError
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.container.box import GTK3BoxMixin


class GTK3StatusbarMixin(GTK3BoxMixin):
    """Mixin for GTK3Statusbar."""

    _GTK3_STATUSBAR_SIGNALS = ["text-popped", "text-pushed"]

    def __init__(self) -> None:
        """Initialize an instance of the GTK3Statusbar mixin."""
        GTK3BoxMixin.__init__(self)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_STATUSBAR_SIGNALS}
        )
        self.dic_context_id: dict[str, int] = {}
        self.dic_message_id: dict[str, int] = {}

    def do_add_message(self, context: str, message: str) -> None:
        """Add the message to the GTK3Statusbar stack.

        Parameters
        ----------
        context : str
            The context description for the message.
        message : str
            The message to display in the GTK3Statusbar.

        Raises
        ------
        PytkwrapError
            If the context is not found in the GTK3Statusbar or the message is not a
            string.
        """
        try:
            self.dic_message_id[message] = self.push(
                self.dic_context_id[context], message
            )
        except KeyError as err:
            raise PytkwrapError(
                f"Context '{context}' not found in GTK3Statusbar."
            ) from err
        except TypeError as err:
            raise PytkwrapError(
                f"Message for GTK3Statusbar must be a string, not {type(message)}."
            ) from err

    def do_remove_message(
        self,
        context: str,
        message: str = "",
        remove_all: bool = False,
    ) -> None:
        """Remove the message from the GTK3Statusbar stack for context.

        Parameters
        ----------
        context : str
            The context description for the message.
        message : str
            The message to remove from the GTK3Statusbar.  Pass an empty string to
            remove the first message in the stack.
        remove_all : bool
            Whether to remove all messages for the context.

        Raises
        ------
        PytkwrapError
            If the context is not found in the GTK3Statusbar or the message is not
            found.
        """
        try:
            if remove_all:
                self.remove_all(self.dic_context_id[context])
            elif not message:
                self.pop(self.dic_context_id[context])
            else:
                self.remove(self.dic_context_id[context], self.dic_message_id[message])
        except KeyError as err:
            raise PytkwrapError(
                f"Context '{context}' not found in GTK3Statusbar or message "
                f"'{message}' not found in GTK3Statusbar {context} stack."
            ) from err


class GTK3Statusbar(Gtk.Statusbar, GTK3StatusbarMixin):
    """Wrapper for version 3.0 Gtk.Statusbar."""

    def __init__(self, contexts: list[str] | None = None) -> None:
        """Initialize an instance of the GTK3Statusbar.

        Parameters
        ----------
        contexts : list[str] | None
            The list of context descriptions to associate with the GTK3Statusbar.
        """
        Gtk.Statusbar.__init__(self)
        GTK3StatusbarMixin.__init__(self)

        if contexts is not None:
            for _context in contexts:
                self.dic_context_id[_context] = self.get_context_id(_context)
