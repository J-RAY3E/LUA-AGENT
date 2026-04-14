# package.loadlib()

**Category**: Standard Libraries

### `package.loadlib (libname, funcname)`

Dynamically links the host program with the C library `libname`.

If `funcname` is "`*`", then it only links with the library, making the symbols exported by the library available to other dynamically linked libraries. Otherwise, it looks for a function `funcname` inside the library and returns this function as a C function. So, `funcname` must follow the [`lua_CFunction`](#lua_CFunction) prototype (see [`lua_CFunction`](#lua_CFunction)).

This is a low-level function. It completely bypasses the package and module system. Unlike [`require`](#pdf-require), it does not perform any path searching and does not automatically adds extensions. `libname` must be the complete file name of the C library, including if necessary a path and an extension. `funcname` must be the exact name exported by the C library (which may depend on the C compiler and linker used).

This functionality is not supported by ISO C. As such, `loadlib` is only available on some platforms: Linux, Windows, Mac OS X, Solaris, BSD, plus other Unix systems that support the `dlfcn` standard.

This function is inherently insecure, as it allows Lua to call any function in any readable dynamic library in the system. (Lua calls any function assuming the function has a proper prototype and respects a proper protocol (see [`lua_CFunction`](#lua_CFunction)). Therefore, calling an arbitrary function in an arbitrary dynamic library more often than not results in an access violation.)