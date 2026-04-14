# package.cpath

**Category**: Standard Libraries

### `package.cpath`

A string with the path used by [`require`](#pdf-require) to search for a C loader.

Lua initializes the C path [`package.cpath`](#pdf-package.cpath) in the same way it initializes the Lua path [`package.path`](#pdf-package.path), using the environment variable `LUA_CPATH_5_5`, or the environment variable `LUA_CPATH`, or a default path defined in `luaconf.h`.