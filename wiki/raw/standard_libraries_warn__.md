# warn()

**Category**: Standard Libraries

### `warn (msg1, ···)`

Emits a warning with a message composed by the concatenation of all its arguments (which should be strings).

By convention, a one-piece message starting with '`@`' is intended to be a *control message*, which is a message to the warning system itself. In particular, the standard warning function in Lua recognizes the control messages "`@off`", to stop the emission of warnings, and "`@on`", to (re)start the emission; it ignores unknown control messages.