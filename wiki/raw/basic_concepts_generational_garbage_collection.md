# Generational Garbage Collection

**Category**: Basic Concepts

### 2.5.2 – Generational Garbage Collection

In generational mode, the collector does frequent *minor* collections, which traverses only objects recently created. If after a minor collection the number of bytes is above a limit, the collector shifts to a *major* collection, which traverses all objects. The collector will then stay doing major collections until it detects that the program is generating enough garbage to justify going back to minor collections.

The generational mode uses three parameters: the *minor multiplier*, the *minor-major multiplier*, and the *major-minor multiplier*.

The minor multiplier controls the frequency of minor collections. For a minor multiplier *x*, a new minor collection will be done when the number of bytes grows *x%* larger than the number in use just after the last major collection. For instance, for a multiplier of 20, the collector will do a minor collection when the number of bytes gets 20% larger than the total after the last major collection.

The minor-major multiplier controls the shift to major collections. For a multiplier *x*, the collector will shift to a major collection when the number of bytes from old objects grows *x%* larger than the total after the previous major collection. For instance, for a multiplier of 100, the collector will do a major collection when the number of old bytes gets larger than twice the total after the previous major collection. As a special case, a value of 0 stops the collector from doing major collections.

The major-minor multiplier controls the shift back to minor collections. For a multiplier *x*, the collector will shift back to minor collections after a major collection collects at least *x%* of the bytes allocated during the last cycle. In particular, for a multiplier of 0, the collector will immediately shift back to minor collections after doing one major collection.