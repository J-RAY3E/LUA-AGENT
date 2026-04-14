# To-be-closed Variables

**Category**: Language

### 3.3.8 – To-be-closed Variables

A to-be-closed variable behaves like a constant local variable, except that its value is *closed* whenever the variable goes out of scope, including normal block termination, exiting its block by **break**/**goto**/**return**, or exiting by an error.

Here, to *close* a value means to call its `__close` metamethod. When calling the metamethod, the value itself is passed as the first argument. If there was an error, the error object that caused the exit is passed as a second argument; otherwise, there is no second argument.

The value assigned to a to-be-closed variable must have a `__close` metamethod or be a false value. (**nil** and **false** are ignored as to-be-closed values.)

If several to-be-closed variables go out of scope at the same event, they are closed in the reverse order that they were declared.

If there is any error while running a closing method, that error is handled like an error in the regular code where the variable was defined. After an error, the other pending closing methods will still be called.

If a coroutine yields and is never resumed again, some variables may never go out of scope, and therefore they will never be closed. (These variables are the ones created inside the coroutine and in scope at the point where the coroutine yielded.) Similarly, if a coroutine ends with an error, it does not unwind its stack, so it does not close any variable. In both cases, you can either use finalizers or call [`coroutine.close`](#pdf-coroutine.close) to close the variables. However, if the coroutine was created through [`coroutine.wrap`](#pdf-coroutine.wrap), then its corresponding function will close the coroutine in case of errors.