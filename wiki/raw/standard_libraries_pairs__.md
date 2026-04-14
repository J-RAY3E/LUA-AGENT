# pairs()

**Category**: Standard Libraries

### `pairs (t)`

If `t` has a metamethod `__pairs`, calls it with `t` as argument and returns the first four results from the call.

Otherwise, returns the [`next`](#pdf-next) function, the table `t`, plus two **nil** values, so that the construction

```lua
for k,v in pairs(t) do body end
```

will iterate over all key–value pairs of table `t`.

See function [`next`](#pdf-next) for the caveats of modifying the table during its traversal.