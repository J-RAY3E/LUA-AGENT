# load()

**Category**: Standard Libraries

### `load (chunk [, chunkname [, mode [, env]]])`

Loads a chunk.

If `chunk` is a string, the chunk is this string. If `chunk` is a function, `load` calls it repeatedly to get the chunk pieces. Each call to `chunk` must return a string that concatenates with previous results. A return of an empty string, **nil**, or no value signals the end of the chunk.

If there are no syntactic errors, `load` returns the compiled chunk as a function; otherwise, it returns **fail** plus the error message.

When you load a main chunk, the resulting function will always have exactly one upvalue, the `_ENV` variable (see [§2.2](#2.2)). However, when you load a binary chunk created from a function (see [`string.dump`](#pdf-string.dump)), the resulting function can have an arbitrary number of upvalues, and there is no guarantee that its first upvalue will be the `_ENV` variable. (A non-main function may not even have an `_ENV` upvalue.)

Regardless, if the resulting function has any upvalues, its first upvalue is set to the value of `env`, if that parameter is given, or to the value of the global environment. Other upvalues are initialized with **nil**. All upvalues are fresh, that is, they are not shared with any other function.

`chunkname` is used as the name of the chunk for error messages and debug information (see [§4.7](#4.7)). When absent, it defaults to `chunk`, if `chunk` is a string, or to "`=(load)`" otherwise.

The string `mode` controls whether the chunk can be text or binary (that is, a precompiled chunk). It may be the string "`b`" (only binary chunks), "`t`" (only text chunks), or "`bt`" (both binary and text). The default is "`bt`".

Lua does not check the consistency of binary chunks. Maliciously crafted binary chunks can crash the interpreter. You can use the `mode` parameter to prevent loading binary chunks.