# io.open()

**Category**: Standard Libraries

### `io.open (filename [, mode])`

This function opens a file, in the mode specified in the string `mode`. In case of success, it returns a new file handle.

The `mode` string can be any of the following:

* "`r`": read mode (the default);
* "`w`": write mode;
* "`a`": append mode;
* "`r+`": update mode, all previous data is preserved;
* "`w+`": update mode, all previous data is erased;
* "`a+`": append update mode, previous data is preserved, writing is only allowed at the end of file.

The `mode` string can also have a '`b`' at the end, which is needed in some systems to open the file in binary mode.