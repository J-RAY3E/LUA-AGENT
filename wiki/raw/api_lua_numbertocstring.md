# lua_numbertocstring

**Category**: API

### `lua_numbertocstring`[-0, +0, –]

```lua
unsigned lua_numbertocstring (lua_State *L, int idx,
                                        char *buff);
```

Converts the number at acceptable index `idx` to a string and puts the result in `buff`. The buffer must have a size of at least `LUA_N2SBUFFSZ` bytes. The conversion follows a non-specified format (see [§3.4.3](#3.4.3)). The function returns the number of bytes written to the buffer (including the final zero), or zero if the value at `idx` is not a number.