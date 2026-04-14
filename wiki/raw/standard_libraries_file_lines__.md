# file:lines()

**Category**: Standard Libraries

### `file:lines (···)`

Returns an iterator function that, each time it is called, reads the file according to the given formats. When no format is given, uses "`l`" as a default. As an example, the construction

```lua
for c in file:lines(1) do body end
```

will iterate over all characters of the file, starting at the current position. Unlike [`io.lines`](#pdf-io.lines), this function does not close the file when the loop ends.