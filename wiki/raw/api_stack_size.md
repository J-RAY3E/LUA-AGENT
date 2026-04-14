# Stack Size

**Category**: API

### 4.1.1 – Stack Size

When you interact with the Lua API, you are responsible for ensuring consistency. In particular, *you are responsible for controlling stack overflow*. When you call any API function, you must ensure the stack has enough room to accommodate the results.

There is one exception to the above rule: When you call a Lua function without a fixed number of results (see [`lua_call`](#lua_call)), Lua ensures that the stack has enough space for all results. However, it does not ensure any extra space. So, before pushing anything on the stack after such a call you should use [`lua_checkstack`](#lua_checkstack).

Whenever Lua calls C, it ensures that the stack has space for at least `LUA_MINSTACK` extra elements; that is, you can safely push up to `LUA_MINSTACK` values into it. `LUA_MINSTACK` is defined as 20, so that usually you do not have to worry about stack space unless your code has loops pushing elements onto the stack. Whenever necessary, you can use the function [`lua_checkstack`](#lua_checkstack) to ensure that the stack has enough space for pushing new elements.