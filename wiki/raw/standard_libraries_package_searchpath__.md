# package.searchpath()

**Category**: Standard Libraries

### `package.searchpath (name, path [, sep [, rep]])`

Searches for the given `name` in the given `path`.

A path is a string containing a sequence of *templates* separated by semicolons. For each template, the function replaces each interrogation mark (if any) in the template with a copy of `name` wherein all occurrences of `sep` (a dot, by default) were replaced by `rep` (the system's directory separator, by default), and then tries to open the resulting file name.

For instance, if the path is the string

```lua
"./?.lua;./?.lc;/usr/local/?/init.lua"
```

the search for the name `foo.a` will try to open the files `./foo/a.lua`, `./foo/a.lc`, and `/usr/local/foo/a/init.lua`, in that order.

Returns the resulting name of the first file that it can open in read mode (after closing the file), or **fail** plus an error message if none succeeds. (This error message lists all file names it tried to open.)