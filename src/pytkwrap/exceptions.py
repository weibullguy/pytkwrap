"""The pytkwrap exceptions module.

.. author:: Doyle Rowland
.. copyright:: Since 2007, all rights reserved.
"""


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
