# lua_Reader

**Category**: API

### `lua_Reader`

```lua
typedef const char * (*lua_Reader) (lua_State *L,
                                    void *data,
                                    size_t *size);
```

The reader function used by [`lua_load`](#lua_load). Every time [`lua_load`](#lua_load) needs another piece of the chunk, it calls the reader, passing along its `data` parameter. The reader must return a pointer to a block of memory with a new piece of the chunk and set `size` to the block size. The block must exist until the reader function is called again. To signal the end of the chunk, the reader must return `NULL` or set `size` to zero. The reader function may return pieces of any size greater than zero.