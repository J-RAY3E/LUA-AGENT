# package.config

**Category**: Standard Libraries

### `package.config`

A string describing some compile-time configurations for packages. This string is a sequence of lines:

* The first line is the directory separator string. Default is '`\`' for Windows and '`/`' for all other systems.
* The second line is the character that separates templates in a path. Default is '`;`'.
* The third line is the string that marks the substitution points in a template. Default is '`?`'.
* The fourth line is a string that, in a path in Windows, is replaced by the executable's directory. Default is '`!`'.
* The fifth line is a mark to ignore all text after it when building the `luaopen_` function name. Default is '`-`'.