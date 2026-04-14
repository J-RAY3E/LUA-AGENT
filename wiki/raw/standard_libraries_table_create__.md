# table.create()

**Category**: Standard Libraries

### `table.create (nseq [, nrec])`

Creates a new empty table, preallocating memory. This preallocation may help performance and save memory when you know in advance how many elements the table will have.

Parameter `nseq` is a hint for how many elements the table will have as a sequence. Optional parameter `nrec` is a hint for how many other elements the table will have; its default is zero.