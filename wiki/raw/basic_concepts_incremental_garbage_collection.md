# Incremental Garbage Collection

**Category**: Basic Concepts

### 2.5.1 – Incremental Garbage Collection

In incremental mode, each GC cycle performs a mark-and-sweep collection in small steps interleaved with the program's execution. In this mode, the collector uses three numbers to control its garbage-collection cycles: the *garbage-collector pause*, the *garbage-collector step multiplier*, and the *garbage-collector step size*.

The garbage-collector pause controls how long the collector waits before starting a new cycle. The collector starts a new cycle when the number of bytes hits *n%* of the total after the previous collection. Larger values make the collector less aggressive. Values equal to or less than 100 mean the collector will not wait to start a new cycle. A value of 200 means that the collector waits for the total number of bytes to double before starting a new cycle.

The garbage-collector step size controls the size of each incremental step, specifically how many bytes the interpreter allocates before performing a step: A value of *n* means the interpreter will allocate approximately *n* bytes between steps.

The garbage-collector step multiplier controls how much work each incremental step does. A value of *n* means the interpreter will execute *n%* *units of work* for each word allocated. A unit of work corresponds roughly to traversing one slot or sweeping one object. Larger values make the collector more aggressive. Beware that values too small can make the collector too slow to ever finish a cycle. As a special case, a zero value means unlimited work, effectively producing a non-incremental, stop-the-world collector.