# Coding Conventions

This document records project conventions as they are established. Add to it
when new conventions are agreed upon, and update it when an existing convention
changes.

## Function and method names

- Use the `do_` prefix for functions and methods that perform an action, such as
  `do_get_properties()`.
- Use the `on_` prefix for functions and methods that respond to an event, such
  as `on_changed()`.
- Omit these prefixes from private functions and methods. Private names begin
  with a single underscore, such as `_block_edit_handlers()` or
  `_get_signal_owner()`.
- List public functions and methods before private functions and methods where
  practical. Keep each group in alphabetical order where practical.

## Docstrings

- Write docstrings in NumPy format.
- Document parameters, non-`None` return values, and exceptions explicitly
  raised by the documented function or method. Include notes when they clarify
  behavior that is not apparent from the signature.
- Do not include a `Returns` section for a function or method that returns
  `None`.
- Document only exceptions explicitly raised by that function or method; do not
  list exceptions that may merely propagate from calls it makes.

## Exceptions and error reporting

- Use pytkwrap-specific exception classes for errors raised by pytkwrap APIs.
- When reporting an error through the established PyPubSub pattern, use
  `raise_pytkwrap_exception()` from `pytkwrap.exceptions`. It publishes the
  message on `do_log_error` and raises the requested pytkwrap exception.
- When wrapping an underlying exception, pass it as `cause` so the original
  error remains available through exception chaining.

## Shared utilities

- Put generally reusable helpers in `pytkwrap.utilities` when they are useful
  across unrelated parts of the package.
- Keep helpers in a domain module when their validation rules, messages, or
  behavior belong to that domain; do not move them to the general utilities
  module solely because they could be generalized.

## Test organization

- Prefer a one-to-one mapping between implementation modules and test modules
  (for example, `menuloader.py` with `test_menuloader.py`).
- Keep tests with the source module they exercise rather than grouping them in
  a catch-all test file based on a shared symptom.

## Validation workflow

- Run targeted tests with the project's Hatch scripts:
  `hatch run test:unit <path to test file>`.
- Add `--isolated` when the test class uses
  `@pytest.mark.usefixtures("skip_if_not_isolated")`.
- Run type checks with `hatch run type:all <path to file>` and lint checks with
  `hatch run lint:all <path to file>`.
- Treat passing `lint:all` as a requirement for implementation and stub files.
- Run `lint:all` on test files when practical, but treat it as a recommendation
  rather than a requirement.
- Run type checks on both implementation and corresponding stub files.
- The lint script formats files before checking them. Rerun it as needed until
  the formatters have settled and all checks pass.
