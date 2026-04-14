# os.execute()

**Category**: Standard Libraries

### `os.execute ([command])`

This function is equivalent to the ISO C function `system`. It passes `command` to be executed by an operating system shell. Its first result is **true** if the command terminated successfully, or **fail** otherwise. After this first result the function returns a string plus a number, as follows:

* "`exit`": the command terminated normally; the following number is the exit status of the command.
* "`signal`": the command was terminated by a signal; the following number is the signal that terminated the command.

When called without a `command`, `os.execute` returns a boolean that is true if a shell is available.