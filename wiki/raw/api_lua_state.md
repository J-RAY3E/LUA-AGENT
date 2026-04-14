# lua_State

**Category**: API

### `lua_State`

```lua
typedef struct lua_State lua_State;
```

An opaque structure that points to a thread and indirectly (through the thread) to the whole state of a Lua interpreter. The Lua library is fully reentrant: it has no global variables. All information about a state is accessible through this structure.

A pointer to this structure must be passed as the first argument to every function in the library, except to [`lua_newstate`](#lua_newstate), which creates a Lua state from scratch.