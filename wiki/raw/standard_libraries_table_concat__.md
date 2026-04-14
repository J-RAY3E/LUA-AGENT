# table.concat()

**Category**: Standard Libraries

### `table.concat (list [, sep [, i [, j]]])`

Given a list where all elements are strings or numbers, returns the string `list[i]..sep..list[i+1] ··· sep..list[j]`. The default value for `sep` is the empty string, the default for `i` is 1, and the default for `j` is `#list`. If `i` is greater than `j`, returns the empty string.