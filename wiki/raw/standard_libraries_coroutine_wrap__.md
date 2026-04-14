# coroutine.wrap()

**Category**: Standard Libraries

### `coroutine.wrap (f)`

Creates a new coroutine, with body `f`; `f` must be a function. Returns a function that resumes the coroutine each time it is called. Any arguments passed to this function behave as the extra arguments to `resume`. The function returns the same values returned by `resume`, except the first boolean. In case of error, the function closes the coroutine and propagates the error.