"""The pytkwrap exceptions module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""

# Standard Library Imports
from typing import NoReturn

# Third Party Imports
from pubsub import pub


class PytkwrapError(Exception):
    """Base exception class for pytkwrap errors."""

    def __init__(self, msg: str = "An error occurred with pytkwrap.") -> None:
        """Initialize the basic pytkwrap exception.

        Parameters
        ----------
        msg : str
            Custom error message.
        """
        super().__init__(msg)
        self.msg = msg

    def __str__(self) -> str:
        """Return the error message.

        Returns
        -------
        str
            The custom error message.
        """
        return self.msg


class PytkwrapWarning(Warning):
    """Base warning class for pytkwrap warnings."""

    def __init__(self, msg: str = "A warning occurred with pytkwrap.") -> None:
        """Initialize the basic pytkwrap warning.

        Parameters
        ----------
        msg : str
            Custom warning message.
        """
        super().__init__(msg)


class NoValueError(PytkwrapError):
    """Exception class raised when no value or method to retrieve value is available."""

    def __init__(self, msg: str = "No value to return.") -> None:
        """Initialize a NoValueError instance.

        Parameters
        ----------
        msg : str
            Custom error message.
        """
        super().__init__(msg)


class UnkAttributeError(PytkwrapError):
    """Exception class raised when an unknown attribute is requested."""

    def __init__(self, msg: str = "Unknown attribute name.") -> None:
        """Initialize an UnkAttributeError instance.

        Parameters
        ----------
        msg : str
            Custom error message.
        """
        super().__init__(msg)


class UnkPropertyError(PytkwrapError):
    """Exception class raised when an unknown property is requested."""

    def __init__(self, msg: str = "Unknown property name.") -> None:
        """Initialize an UnkPropertyError instance.

        Parameters
        ----------
        msg : str
            Custom error message.
        """
        super().__init__(msg)


class UnkSignalError(PytkwrapError):
    """Exception class raised when an unknown signal name is used."""

    def __init__(self, msg: str = "Unknown signal name.") -> None:
        """Initialize an UnkSignalError instance.

        Parameters
        ----------
        msg : str
            Custom error message.
        """
        super().__init__(msg)


class WrongTypeError(PytkwrapError):
    """Exception class raised when wrong data type is used."""

    def __init__(self, msg: str = "Wrong data type.") -> None:
        """Initialize a WrongTypeError instance.

        Parameters
        ----------
        msg : str
            Custom error message.
        """
        super().__init__(msg)


class MenuError(PytkwrapError):
    """Exception class raised when menu data cannot be loaded or built."""

    def __init__(self, msg: str = "Invalid menu data or build request.") -> None:
        """Initialize a MenuError instance.

        Parameters
        ----------
        msg : str
            Custom error message.
        """
        super().__init__(msg)


def raise_pytkwrap_exception(
    message: str,
    error_type: type[PytkwrapError] = MenuError,
    cause: Exception | None = None,
) -> NoReturn:
    """Log an exception message and raise it as a pytkwrap exception.

    Parameters
    ----------
    message : str
        Error message to log and attach to the exception.
    error_type : type[PytkwrapError]
        Pytkwrap exception class to raise.
    cause : Exception or None
        Optional exception to chain as the cause.
    """
    pub.sendMessage("do_log_error", message=message)

    if cause is None:
        raise error_type(message)

    raise error_type(message) from cause
