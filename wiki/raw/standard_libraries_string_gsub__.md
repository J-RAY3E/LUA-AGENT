# string.gsub()

**Category**: Standard Libraries

### `string.gsub (s, pattern, repl [, n])`

`s``n``pattern`[§6.5.1](#6.5.1)`repl``gsub``gsub`*Global SUBstitution*

If `repl` is a string, then its value is used for replacement. The character `%` works as an escape character: any sequence in `repl` of the form `%d`, with *d* between 1 and 9, stands for the value of the *d*-th captured substring; the sequence `%0` stands for the whole match; the sequence `%%` stands for a single `%`.

If `repl` is a table, then the table is queried for every match, using the first capture as the key.

If `repl` is a function, then this function is called every time a match occurs, with all captured substrings passed as arguments, in order.

In any case, if the pattern specifies no captures, then it behaves as if the whole pattern was inside a capture.

If the value returned by the table query or by the function call is a string or a number, then it is used as the replacement string; otherwise, if it is **false** or **nil**, then there is no replacement (that is, the original match is kept in the string).

Here are some examples:

```lua
x = string.gsub("hello world", "(%w+)", "%1 %1")
-- x="hello hello world world"

x = string.gsub("hello world", "%w+", "%0 %0", 1)
-- x="hello hello world"

x = string.gsub("hello world from Lua", "(%w+)%s*(%w+)", "%2 %1")
-- x="world hello Lua from"

x = string.gsub("home = $HOME, user = $USER", "%$(%w+)", os.getenv)
-- x="home = /home/roberto, user = roberto"

x = string.gsub("4+5 = $return 4+5$", "%$(.-)%$", function (s)
      return load(s)()
    end)
-- x="4+5 = 9"

local t = {name="lua", version="5.5"}
x = string.gsub("$name-$version.tar.gz", "%$(%w+)", t)
-- x="lua-5.5.tar.gz"
```