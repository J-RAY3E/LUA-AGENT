# lua_arith

**Category**: API

### `lua_arith`[-(2|1), +1, *e*]

```lua
void lua_arith (lua_State *L, int op);
```

Performs an arithmetic or bitwise operation over the two values (or one, in the case of negations) at the top of the stack, with the value on the top being the second operand, pops these values, and pushes the result of the operation. The function follows the semantics of the corresponding Lua operator (that is, it may call metamethods).

The value of `op` must be one of the following constants:

* **`LUA_OPADD`**: performs addition (`+`)
* **`LUA_OPSUB`**: performs subtraction (`-`)
* **`LUA_OPMUL`**: performs multiplication (`*`)
* **`LUA_OPDIV`**: performs float division (`/`)
* **`LUA_OPIDIV`**: performs floor division (`//`)
* **`LUA_OPMOD`**: performs modulo (`%`)
* **`LUA_OPPOW`**: performs exponentiation (`^`)
* **`LUA_OPUNM`**: performs mathematical negation (unary `-`)
* **`LUA_OPBNOT`**: performs bitwise NOT (`~`)
* **`LUA_OPBAND`**: performs bitwise AND (`&`)
* **`LUA_OPBOR`**: performs bitwise OR (`|`)
* **`LUA_OPBXOR`**: performs bitwise exclusive OR (`~`)
* **`LUA_OPSHL`**: performs left shift (`<<`)
* **`LUA_OPSHR`**: performs right shift (`>>`)