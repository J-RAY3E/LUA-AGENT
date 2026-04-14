# setmetatable()

**Category**: Standard Libraries

### `setmetatable (table, metatable)`

Sets the metatable for the given table. If `metatable` is **nil**, removes the metatable of the given table. If the original metatable has a `__metatable` field, raises an error.

This function returns `table`.

To change the metatable of other types from Lua code, you must use the debug library ([§6.11](#6.11)).