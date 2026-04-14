# file:read()

**Category**: Standard Libraries

### `file:read (···)`

Reads the file `file`, according to the given formats, which specify what to read. For each format, the function returns a string or a number with the characters read, or **fail** if it cannot read data with the specified format. (In this latter case, the function does not read subsequent formats.) When called without arguments, it uses a default format that reads the next line (see below).

The available formats are

* "`n`": reads a numeral and returns it as a float or an integer, following the lexical conventions of Lua. (The numeral may have leading whitespaces and a sign.) This format always reads the longest input sequence that is a valid prefix for a numeral; if that prefix does not form a valid numeral (e.g., an empty string, "`0x`", or "`3.4e-`") or it is too long (more than 200 characters), it is discarded and the format returns **fail**.
* "`a`": reads the whole file, starting at the current position. On end of file, it returns the empty string; this format never fails.
* "`l`": reads the next line skipping the end of line, returning **fail** on end of file. This is the default format.
* "`L`": reads the next line keeping the end-of-line character (if present), returning **fail** on end of file.
* ***number***: reads a string with up to this number of bytes, returning **fail** on end of file. If `number` is zero, it reads nothing and returns an empty string, or **fail** on end of file.

The formats "`l`" and "`L`" should be used only for text files.