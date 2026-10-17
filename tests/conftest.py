# Standard Library Imports
import os
import sys
from io import StringIO

# Third Party Imports
import pytest
from pubsub import pub


def pytest_addoption(parser):
    parser.addoption(
        "--isolated",
        action="store_true",
        default=False,
        help="Run tests for the classes that must be run in isolation.",
    )


@pytest.fixture(autouse=True)
def pubsub_cleanup():
    yield
    pub.unsubAll()


@pytest.fixture(scope="class")
def suppress_stderr():
    _stderr = sys.stderr
    sys.stderr = StringIO()
    yield
    sys.stderr = _stderr


@pytest.fixture(scope="function")
def text_file():
    _parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    _text = os.path.join(_parent_dir, "data/pytkwrap.txt")
    return _text


@pytest.fixture
def logged_errors():
    """Collect messages published on the do_log_error topic."""
    _messages = []

    def _listener(message: str) -> None:
        _messages.append(message)

    pub.subscribe(_listener, "do_log_error")
    try:
        yield _messages
    finally:
        pub.unsubscribe(_listener, "do_log_error")
