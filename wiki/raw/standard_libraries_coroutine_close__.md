# coroutine.close()

**Category**: Standard Libraries

### `coroutine.close ([co])`

Closes coroutine `co`, that is, closes all its pending to-be-closed variables and puts the coroutine in a dead state. The default for `co` is the running coroutine.

The given coroutine must be dead, suspended, or be the running coroutine. For the running coroutine, this function does not return. Instead, the resume that (re)started the coroutine returns.

For other coroutines, in case of error (either the original error that stopped the coroutine or errors in closing methods), this function returns **false** plus the error object; otherwise it returns **true**.