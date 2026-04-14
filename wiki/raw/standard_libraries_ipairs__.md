# ipairs()

**Category**: Standard Libraries

### `ipairs (t)`

Returns three values (an iterator function, the value `t`, and 0) so that the construction

```lua
for i,v in ipairs(t) do body end
```

will iterate over the key–value pairs (`1,t[1]`), (`2,t[2]`), ..., up to the first absent index.