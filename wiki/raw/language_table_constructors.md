# Table Constructors

**Category**: Language

### 3.4.9 – Table Constructors

Table constructors are expressions that create tables. Every time a constructor is evaluated, a new table is created. A constructor can be used to create an empty table or to create a table and initialize some of its fields. The general syntax for constructors is

```lua
tableconstructor ::= ‘{’ [fieldlist] ‘}’
fieldlist ::= field {fieldsep field} [fieldsep]
field ::= ‘[’ exp ‘]’ ‘=’ exp | Name ‘=’ exp | exp
fieldsep ::= ‘,’ | ‘;’
```

Each field of the form `[exp1] = exp2` adds to the new table an entry with key `exp1` and value `exp2`. A field of the form `name = exp` is equivalent to `["name"] = exp`. Fields of the form `exp` are equivalent to `[i] = exp`, where `i` are consecutive integers starting with 1; fields in the other formats do not affect this counting. For example,

```lua
a = { [f(1)] = g; "x", "y"; x = 1, f(x), [30] = 23; 45 }
```

is equivalent to

```lua
do
  local t = {}
  t[f(1)] = g
  t[1] = "x"         -- 1st exp
  t[2] = "y"         -- 2nd exp
  t.x = 1            -- t["x"] = 1
  t[3] = f(x)        -- 3rd exp
  t[30] = 23
  t[4] = 45          -- 4th exp
  a = t
end
```

The order of the assignments in a constructor is undefined. (This order would be relevant only when there are repeated keys.)

If the last field in the list has the form `exp` and the expression is a multires expression, then all values returned by this expression enter the list consecutively (see [§3.4.12](#3.4.12)).

The field list can have an optional trailing separator, as a convenience for machine-generated code.