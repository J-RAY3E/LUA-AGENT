# luaL_Buffer

**Category**: Auxiliary Library

### `luaL_Buffer`

```lua
typedef struct luaL_Buffer luaL_Buffer;
```

Type for a *string buffer*.

A string buffer allows C code to build Lua strings piecemeal. Its pattern of use is as follows:

* First declare a variable `b` of type [`luaL_Buffer`](#luaL_Buffer).
* Then initialize it with a call `luaL_buffinit(L,&b)`.
* Then add string pieces to the buffer calling any of the `luaL_add*` functions.
* Finish by calling `luaL_pushresult(&b)`. This call leaves the final string on the top of the stack.

If you know beforehand the maximum size of the resulting string, you can use the buffer like this:

* First declare a variable `b` of type [`luaL_Buffer`](#luaL_Buffer).
* Then initialize it and preallocate a space of size `sz` with a call `luaL_buffinitsize(L,&b,sz)`.
* Then produce the string into that space.
* Finish by calling `luaL_pushresultsize(&b,sz)`, where `sz` is the total size of the resulting string copied into that space (which may be less than or equal to the preallocated size).

During its normal operation, a string buffer uses a variable number of stack slots. So, while using a buffer, you cannot assume that you know where the top of the stack is. You can use the stack between successive calls to buffer operations as long as that use is balanced; that is, when you call a buffer operation, the stack is at the same level it was immediately after the previous buffer operation. (The only exception to this rule is [`luaL_addvalue`](#luaL_addvalue).) After calling [`luaL_pushresult`](#luaL_pushresult), the stack is back to its level when the buffer was initialized, plus the final string on its top.