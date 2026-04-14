# Garbage Collection

**Category**: Basic Concepts

## 2.5 – Garbage Collection

Lua performs automatic memory management. This means that you do not have to worry about allocating memory for new objects or freeing it when the objects are no longer needed. Lua manages memory automatically by running a *garbage collector* to collect all *dead* objects. All memory used by Lua is subject to automatic management: strings, tables, userdata, functions, threads, internal structures, etc.

An object is considered *dead* as soon as the collector can be sure the object will not be accessed again in the normal execution of the program. ("Normal execution" here excludes finalizers, which resurrect dead objects (see [§2.5.3](#2.5.3)), and it excludes also some operations using the debug library.) Note that the time when the collector can be sure that an object is dead may not coincide with the programmer's expectations. The only guarantees are that Lua will not collect an object that may still be accessed in the normal execution of the program, and it will eventually collect an object that is inaccessible from Lua. (Here, *inaccessible from Lua* means that neither a variable nor another live object refer to the object.) Because Lua has no knowledge about C code, it never collects objects accessible through the registry (see [§4.3](#4.3)), which includes the global environment (see [§2.2](#2.2)) and the main thread.

The garbage collector (GC) in Lua can work in two modes: incremental and generational.

The default GC mode with the default parameters are adequate for most uses. However, programs that waste a large proportion of their time allocating and freeing memory can benefit from other settings. Keep in mind that the GC behavior is non-portable both across platforms and across different Lua releases; therefore, optimal settings are also non-portable.

You can change the GC mode and parameters by calling [`lua_gc`](#lua_gc) in C or [`collectgarbage`](#pdf-collectgarbage) in Lua. You can also use these functions to control the collector directly, for instance to stop or restart it.