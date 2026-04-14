# coroutine.status()

**Category**: Standard Libraries

### `coroutine.status (co)`

Returns the status of the coroutine `co`, as a string: `"running"`, if the coroutine is running (that is, it is the one that called `status`); `"suspended"`, if the coroutine is suspended in a call to `yield`, or if it has not started running yet; `"normal"` if the coroutine is active but not running (that is, it has resumed another coroutine); and `"dead"` if the coroutine has finished its body function, or if it has stopped with an error.