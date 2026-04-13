# -*- coding: utf-8 -*-
#
#       pytkwrap.exceptions.py is part of the pytkwrap Project
#
# All rights reserved.
# Copyright since 2007 Doyle "weibullguy" Rowland doyle.rowland <AT> reliaqual <DOT> com
"""pytkwrap exceptions module."""


class PytkwrapError(Exception):
    """Base exception class for pytkwrap errors.

    :param msg: Custom error message.
    :type msg: str
    """

    def __init__(self, msg: str = "An error occurred with pytkwrap.") -> None:
        """Initialize the basic pytkwrap exception."""
        super().__init__(msg)
        self.msg = msg

    def __str__(self) -> str:
        """Return the error message."""
        return self.msg


class UnkSignalError(PytkwrapError):
    """Exception class raised when an unknown signal name is used."""

    def __init__(self, msg: str = "Unknown signal name.") -> None:
        """Initialize UnkSignalError instance."""
        super().__init__(msg)
