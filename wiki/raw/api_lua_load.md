# lua_load

**Category**: API

### `lua_load`[-0, +1, –]

```lua
int lua_load (lua_State *L,
              lua_Reader reader,
              void *data,
              const char *chunkname,
              const char *mode);
```

Loads a Lua chunk without running it. If there are no errors, `lua_load` pushes the compiled chunk as a Lua function on top of the stack. Otherwise, it pushes an error message.

The `lua_load` function uses a user-supplied `reader` function to read the chunk (see [`lua_Reader`](#lua_Reader)). The `data` argument is an opaque value passed to the reader function.

The `chunkname` argument gives a name to the chunk, which is used for error messages and in debug information (see [§4.7](#4.7)).

`lua_load` automatically detects whether the chunk is text or binary and loads it accordingly (see program `luac`). The string `mode` works as in function [`load`](#pdf-load), with the addition that a `NULL` value is equivalent to the string "`bt`". Moreover, it may have a '`B`' instead of a '`b`', meaning a *fixed buffer* with the binary dump.

A fixed buffer means that the address returned by the reader function will contain the chunk until everything created by the chunk has been collected; therefore, Lua can avoid copying to internal structures some parts of the chunk. (In general, a fixed buffer would keep its contents until the end of the program, for instance with the chunk in ROM.) Moreover, for a fixed buffer, the reader function should return the entire chunk in the first read. (As an example, [`luaL_loadbufferx`](#luaL_loadbufferx) does that, which means that you can use it to load fixed buffers.)

The function [`lua_load`](#lua_load) fully preserves the Lua stack through the calls to the reader function, except that it may push some values for internal use before the first call, and it restores the stack size to its original size plus one (for the pushed result) after the last call.

`lua_load` can return [`LUA_OK`](#pdf-LUA_OK), [`LUA_ERRSYNTAX`](#pdf-LUA_ERRSYNTAX), or [`LUA_ERRMEM`](#pdf-LUA_ERRMEM). The function may also return other values corresponding to errors raised by the read function (see [§4.4.1](#4.4.1)).

If the resulting function has upvalues, its first upvalue is set to the value of the global environment stored at index `LUA_RIDX_GLOBALS` in the registry (see [§4.3](#4.3)). When loading main chunks, this upvalue will be the `_ENV` variable (see [§2.2](#2.2)). Other upvalues are initialized with **nil**.