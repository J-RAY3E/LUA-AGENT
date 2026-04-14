# string.gmatch()

**Category**: Standard Libraries

### `string.gmatch (s, pattern [, init])`

`pattern`[§6.5.1](#6.5.1)`s``pattern``init`

As an example, the following loop will iterate over all the words from string `s`, printing one per line:

```lua
s = "hello world from Lua"
for w in string.gmatch(s, "%a+") do
  print(w)
end
```

The next example collects all pairs `key=value` from the given string into a table:

```lua
t = {}
s = "from=world, to=Lua"
for k, v in string.gmatch(s, "(%w+)=(%w+)") do
  t[k] = v
end
```

For this function, a caret '`^`' at the start of a pattern does not work as an anchor, as this would prevent the iteration.