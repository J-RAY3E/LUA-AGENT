# table.unpack()

**Category**: Standard Libraries

### `table.unpack (list [, i [, j]])`

Returns the elements from the given list. This function is equivalent to

```lua
return list[i], list[i+1], ···, list[j]
```

By default, `i` is 1 and `j` is `#list`.