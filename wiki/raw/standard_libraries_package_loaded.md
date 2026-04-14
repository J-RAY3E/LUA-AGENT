# package.loaded

**Category**: Standard Libraries

### `package.loaded`

A table used by [`require`](#pdf-require) to control which modules are already loaded. When you require a module `modname` and `package.loaded[modname]` is not false, [`require`](#pdf-require) simply returns the value stored there.

This variable is only a reference to the real table; assignments to this variable do not change the table used by [`require`](#pdf-require). The real table is stored in the C registry (see [§4.3](#4.3)), indexed by the key `LUA_LOADED_TABLE`, a string.