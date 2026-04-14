# debug.sethook()

**Category**: Standard Libraries

### `debug.sethook ([thread,] hook, mask [, count])`

Sets the given function as the debug hook. The string `mask` and the number `count` describe when the hook will be called. The string mask may have any combination of the following characters, with the given meaning:

* '`c`': the hook is called every time Lua calls a function;
* '`r`': the hook is called every time Lua returns from a function;
* '`l`': the hook is called every time Lua enters a new line of code.

Moreover, with a `count` different from zero, the hook is called also after every `count` instructions.

When called without arguments, [`debug.sethook`](#pdf-debug.sethook) turns off the hook.

When the hook is called, its first parameter is a string describing the event that has triggered its call: `"call"`, `"tail call"`, `"return"`, `"line"`, and `"count"`. For line events, the hook also gets the new line number as its second parameter. Inside a hook, you can call `getinfo` with level 2 to get more information about the running function. (Level 0 is the `getinfo` function, and level 1 is the hook function.)