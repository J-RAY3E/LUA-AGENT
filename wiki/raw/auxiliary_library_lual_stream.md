# luaL_Stream

**Category**: Auxiliary Library

### `luaL_Stream`

```lua
typedef struct luaL_Stream {
  FILE *f;
  lua_CFunction closef;
} luaL_Stream;
```

The standard representation for file handles used by the standard I/O library.

A file handle is implemented as a full userdata, with a metatable called `LUA_FILEHANDLE` (where `LUA_FILEHANDLE` is a macro with the actual metatable's name). The metatable is created by the I/O library (see [`luaL_newmetatable`](#luaL_newmetatable)).

This userdata must start with the structure `luaL_Stream`; it can contain other data after this initial structure. The field `f` points to the corresponding C stream, or it is `NULL` to indicate an incompletely created handle. The field `closef` points to a Lua function that will be called to close the stream when the handle is closed or collected; this function receives the file handle as its sole argument and must return either a true value, in case of success, or a false value plus an error message, in case of error. Once Lua calls this field, it changes the field value to `NULL` to signal that the handle is closed.