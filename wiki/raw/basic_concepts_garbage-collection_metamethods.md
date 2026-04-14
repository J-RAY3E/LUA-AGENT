# Garbage-Collection Metamethods

**Category**: Basic Concepts

### 2.5.3 – Garbage-Collection Metamethods

You can set garbage-collector metamethods for tables and, using the C API, for full userdata (see [§2.4](#2.4)). These metamethods, called *finalizers*, are called when the garbage collector detects that the corresponding table or userdata is dead. Finalizers allow you to coordinate Lua's garbage collection with external resource management such as closing files, network or database connections, or freeing your own memory.

For an object (table or userdata) to be finalized when collected, you must *mark* it for finalization. You mark an object for finalization when you set its metatable and the metatable has a `__gc` metamethod. Note that if you set a metatable without a `__gc` field and later create that field in the metatable, the object will not be marked for finalization.

When a marked object becomes dead, it is not collected immediately by the garbage collector. Instead, Lua puts it in a list. After the collection, Lua goes through that list. For each object in the list, it checks the object's `__gc` metamethod: If it is present, Lua calls it with the object as its single argument.

At the end of each garbage-collection cycle, the finalizers are called in the reverse order that the objects were marked for finalization, among those collected in that cycle; that is, the first finalizer to be called is the one associated with the object marked last in the program. The execution of each finalizer may occur at any point during the execution of the regular code.

Because the object being collected must still be used by the finalizer, that object (and other objects accessible only through it) must be *resurrected* by Lua. Usually, this resurrection is transient, and the object memory is freed in the next garbage-collection cycle. However, if the finalizer stores the object in some global place (e.g., a global variable), then the resurrection is permanent. Moreover, if the finalizer marks a finalizing object for finalization again, its finalizer will be called again in the next cycle where the object is dead. In any case, the object memory is freed only in a GC cycle where the object is dead and not marked for finalization.

When you close a state (see [`lua_close`](#lua_close)), Lua calls the finalizers of all objects marked for finalization, following the reverse order that they were marked. If any finalizer marks objects for collection during that phase, these marks have no effect.

Finalizers cannot yield nor run the garbage collector. Because they can run in unpredictable times, it is good practice to restrict each finalizer to the minimum necessary to properly release its associated resource.

Any error while running a finalizer generates a warning; the error is not propagated.