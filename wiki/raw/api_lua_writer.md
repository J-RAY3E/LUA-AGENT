# lua_Writer

**Category**: API

### `lua_Writer`

```lua
typedef int (*lua_Writer) (lua_State *L,
                           const void* p,
                           size_t sz,
                           void* ud);
```

The type of the writer function used by [`lua_dump`](#lua_dump). Every time [`lua_dump`](#lua_dump) produces another piece of chunk, it calls the writer, passing along the buffer to be written (`p`), its size (`sz`), and the `ud` parameter supplied to [`lua_dump`](#lua_dump).

After [`lua_dump`](#lua_dump) writes its last piece, it will signal that by calling the writer function one more time, with a `NULL` buffer (and size 0).

The writer returns an error code: 0 means no errors; any other value means an error and stops [`lua_dump`](#lua_dump) from calling the writer again.