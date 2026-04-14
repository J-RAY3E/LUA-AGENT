# Precedence

**Category**: Language

### 3.4.8 – Precedence

Operator precedence in Lua follows the table below, from lower to higher priority:

```lua
or
and
<     >     <=    >=    ~=    ==
|
~
&
<<    >>
..
+     -
*     /     //    %
unary operators (not   #     -     ~)
^
```

As usual, you can use parentheses to change the precedences of an expression. The concatenation ('`..`') and exponentiation ('`^`') operators are right associative. All other binary operators are left associative.