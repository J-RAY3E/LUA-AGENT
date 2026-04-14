# coroutine.isyieldable()

**Category**: Standard Libraries

### `coroutine.isyieldable ([co])`

Returns **true** when the coroutine `co` can yield. The default for `co` is the running coroutine.

A coroutine is yieldable if it is not the main thread and it is not inside a non-yieldable C function.