# package.preload

**Category**: Standard Libraries

### `package.preload`

A table to store loaders for specific modules (see [`require`](#pdf-require)).

This variable is only a reference to the real table; assignments to this variable do not change the table used by [`require`](#pdf-require). The real table is stored in the C registry (see [§4.3](#4.3)), indexed by the key `LUA_PRELOAD_TABLE`, a string.