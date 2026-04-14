# lua_pushcclosure

**Category**: API

### `lua_pushcclosure`[-n, +1, *m*]

```lua
void lua_pushcclosure (lua_State *L, lua_CFunction fn, int n);
```

Pushes a new C closure onto the stack. This function receives a pointer to a C function and pushes onto the stack a Lua value of type `function` that, when called, invokes the corresponding C function. The parameter `n` tells how many upvalues this function will have (see [§4.2](#4.2)).

Any function to be callable by Lua must follow the correct protocol to receive its parameters and return its results (see [`lua_CFunction`](#lua_CFunction)).

When a C function is created, it is possible to associate some values with it, the so called upvalues; these upvalues are then accessible to the function whenever it is called. This association is called a C closure (see [§4.2](#4.2)). To create a C closure, first the initial values for its upvalues must be pushed onto the stack. (When there are multiple upvalues, the first value is pushed first.) Then [`lua_pushcclosure`](#lua_pushcclosure) is called to create and push the C function onto the stack, with the argument `n` telling how many values will be associated with the function. [`lua_pushcclosure`](#lua_pushcclosure) also pops these values from the stack.

The maximum value for `n` is 255.

When `n` is zero, this function creates a *light C function*, which is just a pointer to the C function. In that case, it never raises a memory error.