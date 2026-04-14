# require()

**Category**: Standard Libraries

### `require (modname)`

Loads the given module. The function starts by looking into the [`package.loaded`](#pdf-package.loaded) table to determine whether `modname` is already loaded. If it is, then `require` returns the value stored at `package.loaded[modname]`. (The absence of a second result in this case signals that this call did not have to load the module.) Otherwise, it tries to find a *loader* for the module.

To find a loader, `require` is guided by the table [`package.searchers`](#pdf-package.searchers). Each item in this table is a search function, that searches for the module in a particular way. By changing this table, we can change how `require` looks for a module. The following explanation is based on the default configuration for [`package.searchers`](#pdf-package.searchers).

First `require` queries `package.preload[modname]`. If it has a value, this value (which must be a function) is the loader. Otherwise `require` searches for a Lua loader using the path stored in [`package.path`](#pdf-package.path). If that also fails, it searches for a C loader using the path stored in [`package.cpath`](#pdf-package.cpath). If that also fails, it tries an *all-in-one* loader (see [`package.searchers`](#pdf-package.searchers)).

Once a loader is found, `require` calls the loader with two arguments: `modname` and an extra value, a *loader data*, also returned by the searcher. The loader data can be any value useful to the module; for the default searchers, it indicates where the loader was found. (For instance, if the loader came from a file, this extra value is the file path.) If the loader returns any non-nil value, `require` assigns the returned value to `package.loaded[modname]`. If the loader does not return a non-nil value and has not assigned any value to `package.loaded[modname]`, then `require` assigns **true** to this entry. In any case, `require` returns the final value of `package.loaded[modname]`. Besides that value, `require` also returns as a second result the loader data returned by the searcher, which indicates how `require` found the module.

If there is any error loading or running the module, or if it cannot find any loader for the module, then `require` raises an error.