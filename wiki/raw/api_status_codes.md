# Status Codes

**Category**: API

### 4.4.1 – Status Codes

Several functions that report errors in the API use the following status codes to indicate different kinds of errors or other conditions:

* **`LUA_OK` (0)**: no errors.
* **`LUA_ERRRUN`**: a runtime error.
* **`LUA_ERRMEM`**: memory allocation error. For such errors, Lua does not call the message handler.
* **`LUA_ERRERR`**: stack overflow while running the message handler due to another stack overflow. More often than not, this error is the result of some other error while running a message handler. An error in a message handler will call the handler again, which will generate the error again, and so on, until this loop exhausts the stack and cause this error.
* **`LUA_ERRSYNTAX`**: syntax error during precompilation or format error in a binary chunk.
* **`LUA_YIELD`**: the thread (coroutine) yields.
* **`LUA_ERRFILE`**: a file-related error; e.g., it cannot open or read the file.

These constants are defined in the header file `lua.h`.