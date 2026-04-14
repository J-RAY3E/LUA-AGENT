# Function Calls as Statements

**Category**: Language

### 3.3.6 – Function Calls as Statements

To allow possible side-effects, function calls can be executed as statements:

```lua
stat ::= functioncall
```

In this case, all returned values are thrown away. Function calls are explained in [§3.4.10](#3.4.10).