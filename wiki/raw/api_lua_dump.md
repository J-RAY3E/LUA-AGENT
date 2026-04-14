# lua_dump

**Category**: API

### `lua_dump`[-0, +0, –]

```lua
int lua_dump (lua_State *L,
                        lua_Writer writer,
                        void *data,
                        int strip);
```

Dumps a function as a binary chunk. Receives a Lua function on the top of the stack and produces a binary chunk that, if loaded again, results in a function equivalent to the one dumped. As it produces parts of the chunk, [`lua_dump`](#lua_dump) calls function `writer` (see [`lua_Writer`](#lua_Writer)) with the given `data` to write them.

The function [`lua_dump`](#lua_dump) fully preserves the Lua stack through the calls to the writer function, except that it may push some values for internal use before the first call, and it restores the stack size to its original size after the last call.

If `strip` is true, the binary representation may not include all debug information about the function, to save space.

The value returned is the error code returned by the last call to the writer; 0 means no errors.