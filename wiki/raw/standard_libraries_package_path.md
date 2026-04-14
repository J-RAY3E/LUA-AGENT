# package.path

**Category**: Standard Libraries

### `package.path`

A string with the path used by [`require`](#pdf-require) to search for a Lua loader.

At start-up, Lua initializes this variable with the value of the environment variable `LUA_PATH_5_5` or the environment variable `LUA_PATH` or with a default path defined in `luaconf.h`, if those environment variables are not defined. A "`;;`" in the value of the environment variable is replaced by the default path.