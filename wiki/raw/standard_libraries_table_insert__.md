# table.insert()

**Category**: Standard Libraries

### `table.insert (list, [pos,] value)`

Inserts element `value` at position `pos` in `list`, shifting up the elements `list[pos],list[pos+1],···,list[#list]`. The default value for `pos` is `#list+1`, so that a call `table.insert(t,x)` inserts `x` at the end of the list `t`.