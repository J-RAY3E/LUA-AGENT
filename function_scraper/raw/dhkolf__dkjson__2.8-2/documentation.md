# dkjson – JSON Module for Lua [(dkolf.de)](https://dkolf.de/)
## Introduction
This is a JSON module written in [Lua](https://www.lua.org/). It supports UTF-8. 
[JSON (JavaScript Object Notation)](https://www.json.org/) is a format for serializing data based on the syntax for JavaScript data structures. It is an ideal format for transmitting data between different applications and commonly used for dynamic web pages. It can also be used to save Lua data structures, but you should be aware that not every Lua table can be represented by the JSON standard. For example tables that contain both string keys and an array part cannot be exactly represented by JSON. You can solve this by putting your array data in an explicit subtable. 
dkjson is written in Lua without any dependencies, but when [LPeg](https://www.inf.puc-rio.br/~roberto/lpeg/) is available dkjson can use it to speed up decoding. 
## Download
  * [dkjson.lua](https://dkolf.de/dkjson-lua/dkjson-2.8.lua)
  * Preview: [dkjson.lua version 2.9-beta.2](https://dkolf.de/dkjson-lua/dkjson-2.9-beta.2.lua)
  * All versions along with their SHA-256 hash can be found on the [downloads page](https://dkolf.de/downloads). 


## Usage
The full [documentation including the license](https://dkolf.de/dkjson-lua/documentation) is available online on this website or as Markdown text in the readme.txt file. 
dkjson is free software released under the same conditions as the Lua interpreter. Please remember to mention external code you are using in your software. 
## Examples
### Encoding
```

local json = require ("dkjson")

local tbl = {
  animals = { "dog", "cat", "aardvark" },
  instruments = { "violin", "trombone", "theremin" },
  bugs = json.null,
  trees = nil
}

local str = json.encode (tbl, { indent = true })

print (str)

```

#### Output
```

{
  "bugs":null,
  "instruments":["violin","trombone","theremin"],
  "animals":["dog","cat","aardvark"]
}

```

### Decoding
```

local json = require ("dkjson")

local str = [[
{
  "numbers": [ 2, 3, -20.23e+2, -4 ],
  "currency": "\u20AC"
}
]]

local obj, pos, err = json.decode (str, 1, nil)
if err then
  print ("Error:", err)
else
  print ("currency", obj.currency)
  for i = 1,#obj.numbers do
    print (i, obj.numbers[i])
  end
end


```

#### Output
```
currency	€
1	2
2	3
3	-2023
4	-4

```

## Related content on this site
### [async-await in Lua](https://dkolf.de/lua-async-await)
A short introduction to the async-await programming syntax for running asynchronous tasks and how it can be implemented in the Lua programming language. 
### [Software dependencies](https://dkolf.de/dependencies)
Package managers like npm, cargo and LuaRocks have made it easy to include external code in projects. I advocate that we need to complement this improvement in the ease of use with additional measures to ensure supply chain security. 
## dkjson Versions
### Preview: 2.9-beta.2 (2026-03-14)
  * Download [dkjson.lua version 2.9-beta.2](https://dkolf.de/dkjson-lua/dkjson-2.9-beta.2.lua)
  * Read the [documentation](https://dkolf.de/dkjson-lua/readme-2.9-beta.2.md)


Changes since version 2.8: 
  * Performance improvements for the pure-Lua decoder. 


### Version 2.8 (2024-06-17)
  * Download [dkjson.lua version 2.8](https://dkolf.de/dkjson-lua/dkjson-2.8.lua)
  * Read the [documentation](https://dkolf.de/dkjson-lua/readme-2.8.txt)


Changes since version 2.7: 
  * Fix handling of decoding errors when Lua is compiled with LUA_NOCVTN2S. 


### Version 1.4 (2024-06-17)
  * Download [dkjson.lua version 1.4](https://dkolf.de/dkjson-lua/dkjson-1.4.lua)


Changes since version 1.3: 
  * Fix handling of decoding errors when Lua is compiled with LUA_NOCVTN2S. 


### Version 2.7 (2024-02-20)
  * Download [dkjson.lua version 2.7](https://dkolf.de/dkjson-lua/dkjson-2.7.lua)
  * Read the [documentation](https://dkolf.de/dkjson-lua/readme-2.7.txt)


Changes since version 2.6: 
  * Enable working with newer versions of LPeg where the "version" field is no longer a function. 
  * Fix error messages when an encoding error happens in an ordered dictionary. 


### Version 2.6 (2021-12-19)
  * Download [dkjson.lua version 2.6](https://dkolf.de/dkjson-lua/dkjson-2.6.lua)
  * Read the [documentation](https://dkolf.de/dkjson-lua/readme-2.6.txt)


Changes since version 2.5: 
  * The decode function is no longer automatically replaced by the version implemented using LPeg, but an LPeg-enabled copy of the module has to be requested explicitly with the function use_lpeg. This was changed to improve the predictability of the code and make audits more reliable. 
  * The LPeg-version of the decode function now reports unterminated strings, arrays and objects with the position where they started rather than where parsing failed which was usually at the end of the input string. This was already the behavior of the pure-Lua-implementation. 
  * Fixed a bug where entries in a dictionary were not put in the desired order when their value was the boolean false. 


### Version 2.5 (2014-04-28)
  * Download [dkjson.lua version 2.5](https://dkolf.de/dkjson-lua/dkjson-2.5.lua)
  * Read the [documentation](https://dkolf.de/dkjson-lua/readme-2.5.txt)


Changes since version 2.4: 
  * Added customizable exception handling. 
  * Decode input that contains JavaScript comments. 


### Version 2.4 (2013-09-28)
  * Download [dkjson.lua version 2.4](https://dkolf.de/dkjson-lua/dkjson-2.4.lua)


Changes since version 2.3: 
  * Fixed encoding and decoding of numbers in different numeric locales. 
  * Prevent using version 0.11 of LPeg (causes segmentation faults on some systems). 


### Version 1.3 (2013-09-28)
  * Download [dkjson.lua version 1.3](https://dkolf.de/dkjson-lua/dkjson-1.3.lua)


Changes since version 1.2: 
  * Fixed encoding and decoding of numbers in different numeric locales. 


### Version 2.3 (2013-04-14)
  * Download [dkjson.lua version 2.3](https://dkolf.de/dkjson-lua/dkjson-2.3.lua)


Changes since version 2.2: 
  * Corrected the range of escaped characters. Among other characters U+2029 was missing, which would cause trouble when [parsed by a JavaScript interpreter.](https://web.archive.org/web/20201203234157/http://timelessrepo.com/json-isnt-a-javascript-subset)
  * Added options to register the module table in a global variable. This is useful in environments where functions similar to require are not available. 


### Version 1.2 (2013-04-14)
  * Download [dkjson.lua version 1.2](https://dkolf.de/dkjson-lua/dkjson-1.2.lua)


Changes since version 1.1: 
  * Corrected the range of escaped characters. Among other characters U+2029 was missing, which would cause trouble when parsed by a JavaScript interpreter. 
  * Locations for error messages were off by one in the first line. 


### Version 2.2 (2012-04-28)
  * Download [dkjson.lua version 2.2](https://dkolf.de/dkjson-lua/dkjson-2.2.lua)


Changes since version 2.1: 
  * __jsontype is only used for empty tables. 
  * It is possible to decode tables without assigning metatables. 
  * Locations for error messages were off by one in the first line. 
  * There is no LPeg version of json.quotestring anymore. 


### Version 2.1 (2011-07-08)
  * Download [dkjson.lua version 2.1](https://dkolf.de/dkjson-lua/dkjson-2.1.lua)


Changes since version 2.0: 
  * Changed the documentation to Markdown format. 
  * LPeg is now parsing only a single value at a time to avoid running out of Lua stack for big arrays and objects. 
  * Read __tojson, __jsontype and __jsonorder even from blocked metatables through the debug module. 
  * Fixed decoding single numbers (only affected the non-LPeg mode). 
  * Corrected the range of escaped Unicode control characters. 


### Version 1.1 (2011-07-08)
  * Download [dkjson.lua version 1.1](https://dkolf.de/dkjson-lua/dkjson-1.1.lua)


Changes since version 1.0: 
  * The values NaN/+Inf/-Inf are recognised and encoded as "null" like in the original JavaScript implementation. 
  * Read __tojson even from blocked metatables through the debug module. 
  * Fixed decoding single numbers. 
  * Corrected the range of escaped Unicode control characters. 


### Version 2.0 (2011-05-30)
  * Download [dkjson.lua version 2.0](https://dkolf.de/dkjson-lua/dkjson-2.0.lua)


Changes since version 1.0: 
  * Optional LPeg support. 
  * Invalid input data for encoding raises errors instead of returning nil and the error message. (Invalid data for encoding is usually a programming error. Raising an error removes the work of explicitly checking the result). 
  * The metatable field __jsontype can control whether a Lua table is encoded as a JSON array or object. (Mainly useful for empty tables). 
  * When decoding, two metatables are created. One is used to mark the arrays while the other one is used for the objects. (The metatables are created once for each decoding operation to make sandboxing possible. However, you can specify your own metatables as arguments). 
  * There are no spaces added any longer when encoding. 
  * It is possible to explicitly sort keys for encoding by providing an array with key names to the option "keyorder" or the metatable field __jsonorder. 
  * The values NaN/+Inf/-Inf are recognised and encoded as "null" like in the original JavaScript implementation. 


### Version 1.0 (2010-08-28)
Initial version. 
  * Download [dkjson.lua version 1.0](https://dkolf.de/dkjson-lua/dkjson-1.0.lua)


[dkolf.de](https://dkolf.de/) · [contact](https://dkolf.de/contact) · [RSS](https://dkolf.de/rss)
