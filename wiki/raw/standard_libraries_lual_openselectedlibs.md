# luaL_openselectedlibs

**Category**: Standard Libraries

### `luaL_openselectedlibs`[-0, +0, *e*]

```lua
void luaL_openselectedlibs (lua_State *L, int load, int preload);
```

Opens (loads) and preloads selected standard libraries into the state `L`. (To *preload* means to add the library loader into the table [`package.preload`](#pdf-package.preload), so that the library can be required later by the program. Keep in mind that [`require`](#pdf-require) itself is provided by the *package* library. If a program does not load that library, it will be unable to require anything.)

The integer `load` selects which libraries to load; the integer `preload` selects which to preload, among those not loaded. Both are masks formed by a bitwise OR of the following constants:

* **`LUA_GLIBK`** : the basic library.
* **`LUA_LOADLIBK`** : the package library.
* **`LUA_COLIBK`** : the coroutine library.
* **`LUA_STRLIBK`** : the string library.
* **`LUA_UTF8LIBK`** : the UTF-8 library.
* **`LUA_TABLIBK`** : the table library.
* **`LUA_MATHLIBK`** : the mathematical library.
* **`LUA_IOLIBK`** : the I/O library.
* **`LUA_OSLIBK`** : the operating system library.
* **`LUA_DBLIBK`** : the debug library.