# lua_gc

**Category**: API

### `lua_gc`[-0, +0, –]

```lua
int lua_gc (lua_State *L, int what, ...);
```

Controls the garbage collector.

This function performs several tasks, according to the value of the parameter `what`. For options that need extra arguments, they are listed after the option.

* **`LUA_GCCOLLECT`**: Performs a full garbage-collection cycle.
* **`LUA_GCSTOP`**: Stops the garbage collector.
* **`LUA_GCRESTART`**: Restarts the garbage collector.
* **`LUA_GCCOUNT`**: Returns the current amount of memory (in Kbytes) in use by Lua.
* **`LUA_GCCOUNTB`**: Returns the remainder of dividing the current amount of bytes of memory in use by Lua by 1024.
* **`LUA_GCSTEP` (size\_t n)**: Performs a step of garbage collection.
* **`LUA_GCISRUNNING`**: Returns a boolean that tells whether the collector is running (i.e., not stopped).
* **`LUA_GCINC`**: Changes the collector to incremental mode. Returns the previous mode (`LUA_GCGEN` or `LUA_GCINC`).
* **`LUA_GCGEN`**: Changes the collector to generational mode. Returns the previous mode (`LUA_GCGEN` or `LUA_GCINC`).
* **`LUA_GCPARAM` (int param, int val)**: Changes and/or returns the value of a parameter of the collector. If `val` is -1, the call only returns the current value. The argument `param` must have one of the following values:
  + **`LUA_GCPMINORMUL`**: The minor multiplier.
  + **`LUA_GCPMAJORMINOR`**: The major-minor multiplier.
  + **`LUA_GCPMINORMAJOR`**: The minor-major multiplier.
  + **`LUA_GCPPAUSE`**: The garbage-collector pause.
  + **`LUA_GCPSTEPMUL`**: The step multiplier.
  + **`LUA_GCPSTEPSIZE`**: The step size.

For more details about these options, see [`collectgarbage`](#pdf-collectgarbage).

This function should not be called by a finalizer.