# collectgarbage()

**Category**: Standard Libraries

### `collectgarbage ([opt [, arg]])`

This function is a generic interface to the garbage collector. It performs different functions according to its first argument, `opt`:

* "`collect`": Performs a full garbage-collection cycle. This is the default option.
* "`stop`": Stops automatic execution of the garbage collector. The collector will run only when explicitly invoked, until a call to restart it.
* "`restart`": Restarts automatic execution of the garbage collector.
* "`count`": Returns the total memory in use by Lua in Kbytes. The value has a fractional part, so that it multiplied by 1024 gives the exact number of bytes in use by Lua.
* "`step`": Performs a garbage-collection step. This option may be followed by an extra argument, an integer with the step size.

  If the size is a positive `n`, the collector acts as if `n` new bytes have been allocated. If the size is zero, the collector performs a basic step. In incremental mode, a basic step corresponds to the current step size. In generational mode, a basic step performs a full minor collection or an incremental step, if the collector has scheduled one.

  In incremental mode, the function returns **true** if the step finished a collection cycle. In generational mode, the function returns **true** if the step finished a major collection.
* "`isrunning`": Returns a boolean that tells whether the collector is running (i.e., not stopped).
* "`incremental`": Changes the collector mode to incremental and returns the previous mode.
* "`generational`": Changes the collector mode to generational and returns the previous mode.
* "`param`": Changes and/or retrieves the values of a parameter of the collector. This option must be followed by one or two extra arguments: The name of the parameter being changed or retrieved (a string) and an optional new value for that parameter, an integer in the range *[0,100000]*. The first argument must have one of the following values:
  + "`minormul`": The minor multiplier.
  + "`majorminor`": The major-minor multiplier.
  + "`minormajor`": The minor-major multiplier.
  + "`pause`": The garbage-collector pause.
  + "`stepmul`": The step multiplier.
  + "`stepsize`": The step size.

  The call always returns the previous value of the parameter. If the call does not give a new value, the value is left unchanged.

  Lua stores these values in a compressed format, so, the value returned as the previous value may not be exactly the last value set.

See [§2.5](#2.5) for more details about garbage collection and some of these options.

This function should not be called by a finalizer.