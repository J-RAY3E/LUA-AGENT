# os.exit()

**Category**: Standard Libraries

### `os.exit ([code [, close]])`

Calls the ISO C function `exit` to terminate the host program. If `code` is **true**, the returned status is `EXIT_SUCCESS`; if `code` is **false**, the returned status is `EXIT_FAILURE`; if `code` is a number, the returned status is this number. The default value for `code` is **true**.

If the optional second argument `close` is true, the function closes the Lua state before exiting (see [`lua_close`](#lua_close)).