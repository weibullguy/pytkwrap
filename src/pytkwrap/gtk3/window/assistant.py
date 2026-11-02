"""The pytkwrap GTK3Assistant module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# pytkwrap Package Imports
from pytkwrap.gtk3._libs import Gtk
from pytkwrap.gtk3.mixins import GTK3WidgetProperties
from pytkwrap.gtk3.widget import GTK3Widget
from pytkwrap.gtk3.window.window import GTK3WindowMixin


class GTK3AssistantMixin(GTK3WindowMixin):
    """Mixin class for GTK3Assistant.

    Attributes
    ----------
    _GTK3_ASSISTANT_PROPERTIES : GTK3WidgetProperties
        Properties unique to the GTK3Assistant.
    _GTK3_ASSISTANT_SIGNALS : list[str]
        Signals unique to the GTK3Assistant.
    """

    _GTK3_ASSISTANT_PROPERTIES = GTK3WidgetProperties(
        use_header_bar=-1,
    )
    _GTK3_ASSISTANT_SIGNALS = [
        "apply",
        "cancel",
        "close",
        "escape",
        "prepare",
    ]

    def __init__(self, **kwargs) -> None:
        """Initialize an instance of the GTK3Assistant."""
        super().__init__(**kwargs)

        # Initialize public instance attributes.
        self.dic_handler_id.update(
            {_signal: -1 for _signal in self._GTK3_ASSISTANT_SIGNALS}
        )
        self.dic_properties.update(self._GTK3_ASSISTANT_PROPERTIES)

    def do_add_page(self, page: GTK3Widget, position: int = -1) -> int:
        """Add a page to the GTK3Assistant.

        Parameters
        ----------
        page : GTK3Widget
            The page to add to the assistant.
        position : int, optional
            The position at which to add the page.  Pass -1 to append the page, 0 to
            prepend the page, or a positive integer to insert the page at that position.

        Returns
        -------
        int
            The index of the added page.
        """
        if position == -1:
            return self.append_page(page)

        if position == 0:
            return self.prepend_page(page)

        return self.insert_page(page, position)

    @property
    def n_pages(self) -> int:
        """Get the number of pages in the GTK3Assistant.

        Returns
        -------
        int
            The number of pages in the GTK3Assistant.
        """
        return self.get_n_pages()


class GTK3Assistant(Gtk.Assistant, GTK3AssistantMixin):
    """Wrapper for version 3.0 Gtk.Assistant."""

    def __init__(self, use_header_bar: bool = False) -> None:
        """Initialize an instance of the GTK3Assistant.

        Parameters
        ----------
        use_header_bar : bool, optional
            Whether to use the header-bar for action buttons.
        """
        Gtk.Assistant.__init__(self, use_header_bar=use_header_bar)
        GTK3AssistantMixin.__init__(self)


def do_construct_assistant(
    pages: list[GTK3Widget],
    titles: list[str] | None = None,
    types: list[Gtk.AssistantPageType] | None = None,
    use_header_bar: bool = False,
) -> GTK3Assistant:
    """Construct a GTK3Assistant.

    Parameters
    ----------
    pages : list[GTK3Widget]
        The pages to add to the assistant.
    titles : list[str] | None, optional
        The titles for each page.
    types : list[Gtk.AssistantPageType] | None, optional
        The types for each page.  Options are:
            * Gtk.AssistantPageType.CONTENT
            * Gtk.AssistantPageType.INTRO
            * Gtk.AssistantPageType.CONFIRM
            * Gtk.AssistantPageType.SUMMARY
            * Gtk.AssistantPageType.PROGRESS
            * Gtk.AssistantPageType.CUSTOM
    use_header_bar : bool, optional
        Whether to use the header-bar for action buttons.

    Returns
    -------
    GTK3Assistant
        The built GTK3Assistant.
    """
    _assistant = GTK3Assistant(use_header_bar=use_header_bar)

    for _idx, _page in enumerate(pages):
        _assistant.do_add_page(_page)

        if titles is not None and _idx < len(titles):
            _assistant.set_page_title(_page, titles[_idx])

        if types is not None and _idx < len(types):
            _assistant.set_page_type(_page, types[_idx])

    return _assistant
