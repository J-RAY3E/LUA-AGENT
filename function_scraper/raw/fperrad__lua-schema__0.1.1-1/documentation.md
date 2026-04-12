[lua-schema](https://lua-schema-37dc08.frama.io/)
  * [Home](https://lua-schema-37dc08.frama.io/)
  * [API](https://lua-schema-37dc08.frama.io/)
    * [schema](https://lua-schema-37dc08.frama.io/schema/)


  * [ ](https://lua-schema-37dc08.frama.io/)
  *   * [ Next ](https://lua-schema-37dc08.frama.io/schema/)
  * [Framagit](https://framagit.org/fperrad/lua-schema)


  * [lua-schema](https://lua-schema-37dc08.frama.io/#lua-schema)
    * [Overview](https://lua-schema-37dc08.frama.io/#overview)
    * [References](https://lua-schema-37dc08.frama.io/#references)
    * [Status](https://lua-schema-37dc08.frama.io/#status)
    * [Download](https://lua-schema-37dc08.frama.io/#download)
    * [Installation](https://lua-schema-37dc08.frama.io/#installation)
    * [Test](https://lua-schema-37dc08.frama.io/#test)
    * [Copyright and License](https://lua-schema-37dc08.frama.io/#copyright-and-license)


# lua-schema
* * *
## Overview
lua-schema is a JSON Schema (_classical_ & _modern_) data validator.
It validates data from a JSON instance or from any equivalent data model, for example [CBOR](https://cbor.io/), [Message Pack](https://msgpack.org/), [UBJSON](https://ubjson.org/) or just plain Lua.
## References
The JSON Schema specifications are available on <https://json-schema.org/>.
The following versions are supported:
  * [draft-04](https://json-schema.org/draft-05)
  * [draft-06](https://json-schema.org/draft-06)
  * [draft-07](https://json-schema.org/draft-07)
  * [Draft 2019-09](https://json-schema.org/draft/2019-09)
  * [Draft 2020-12](https://json-schema.org/draft/2020-12)
  * _upcoming_ v1-2026


## Status
lua-schema is in beta stage.
It's developed for Lua 5.1, 5.2, 5.3, 5.4 & 5.5.
The keyword `$dynamicRef` is not fully supported, especially for extendible schema.
For the semantic content validation (keyword `format`):
  * `date-time`, `date`, `time`, `duration`, `email`, `hostname`, `ipv4`, `ipv6`, `uri`, `uri-reference`, `iri`, `iri-reference`, `uuid`, `uri-template`, `json-pointer`, `relative-json-pointer` & `regex` are implemented
  * `idn-email` & `idn-hostname` are not yet implemented


Punycode for format `hostname` is not yet implemented.
The leap second is not supported (format `date-time` & `time`).
lua-schema is monitored by [Bowtie](https://github.com/bowtie-json-schema/bowtie), which gives independent [reports](https://bowtie.report/#/implementations/lua-schema).
## Download
lua-schema source can be downloaded from [Framagit](https://framagit/fperrad/lua-schema).
## Installation
With Lua 5.1 & 5.2, lua-schema depends on [compat53](https://github.com/lunarmodules/lua-compat-5.3).
lua-schema depends on [LPeg](https://www.inf.puc-rio.br/~roberto/lpeg/lpeg.html) which is heavily used by the semantic content validation (keyword `format`).
The use of regular expression (keyword `pattern` & `patternProperties`) depends on [Lrexlib-PCRE2](https://rrthomas.github.io/lrexlib/), but it is optional.
lua-schema is available via LuaRocks:
```
luarocks install lua-schema

```

or manually, with:
```
make install

```

## Test
The test suite requires the modules [lua-TestAssertion](https://fperrad.frama.io/lua-testassertion/) & [dkjson](http://dkolf.de/src/dkjson-lua.fsl/home).
```
make test

```

It run against the [official JSON Schema Test Suite](https://github.com/json-schema-org/JSON-Schema-Test-Suite).
## Copyright and License
Copyright © 2025-2026 François Perrad
This library is licensed under the terms of the MIT/X11 license, like Lua itself.
* * *
Copyright © 2025-2026 François Perrad
Documentation built with [MkDocs](https://www.mkdocs.org/).
#### Search
From here you can search these documents. Enter your search terms below.
#### Keyboard Shortcuts
Keys | Action  
---|---  
`?` | Open this help  
`n` | Next page  
`p` | Previous page  
`s` | Search
