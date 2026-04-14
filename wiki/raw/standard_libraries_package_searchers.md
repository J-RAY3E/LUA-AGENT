# package.searchers

**Category**: Standard Libraries

### `package.searchers`

A table used by [`require`](#pdf-require) to control how to find modules.

Each entry in this table is a *searcher function*. When looking for a module, [`require`](#pdf-require) calls each of these searchers in ascending order, with the module name (the argument given to [`require`](#pdf-require)) as its sole argument. If the searcher finds the module, it returns another function, the module *loader*, plus an extra value, a *loader data*, that will be passed to that loader and returned as a second result by [`require`](#pdf-require). If it cannot find the module, it returns a string explaining why (or **nil** if it has nothing to say).

Lua initializes this table with four searcher functions.

The first searcher simply looks for a loader in the [`package.preload`](#pdf-package.preload) table.

The second searcher looks for a loader as a Lua library, using the path stored at [`package.path`](#pdf-package.path). The search is done as described in function [`package.searchpath`](#pdf-package.searchpath).

The third searcher looks for a loader as a C library, using the path given by the variable [`package.cpath`](#pdf-package.cpath). Again, the search is done as described in function [`package.searchpath`](#pdf-package.searchpath). For instance, if the C path is the string

```lua
"./?.so;./?.dll;/usr/local/?/init.so"
```

the searcher for module `foo` will try to open the files `./foo.so`, `./foo.dll`, and `/usr/local/foo/init.so`, in that order. Once it finds a C library, this searcher first uses a dynamic link facility to link the application with the library. Then it tries to find a C function inside the library to be used as the loader. The name of this C function is the string "`luaopen_`" concatenated with a copy of the module name where each dot is replaced by an underscore. Moreover, if the module name has a hyphen, its suffix after (and including) the first hyphen is removed. For instance, if the module name is `a.b.c-v2.1`, the function name will be `luaopen_a_b_c`.

The fourth searcher tries an *all-in-one loader*. It searches the C path for a library for the root name of the given module. For instance, when requiring `a.b.c`, it will search for a C library for `a`. If found, it looks into it for an open function for the submodule; in our example, that would be `luaopen_a_b_c`. With this facility, a package can pack several C submodules into one single library, with each submodule keeping its original open function.

All searchers except the first one (preload) return as the extra value the file path where the module was found, as returned by [`package.searchpath`](#pdf-package.searchpath). The first searcher always returns the string "`:preload:`".

Searchers should raise no errors and have no side effects in Lua. (They may have side effects in C, for instance by linking the application with a library.)