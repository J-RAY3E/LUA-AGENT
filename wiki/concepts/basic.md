# Lua Programming — Syntax & Use Cases

> Reference guide for Lua 5.4. Features such as `//` (floor division), `goto`, and the integer subtype are available from Lua 5.3+.

---

## Table of Contents

1. [Comments](#comments)
2. [Data Types](#data-types)
3. [Variables](#variables)
4. [Operators](#operators)
5. [Strings](#strings)
6. [Tables](#tables)
7. [Conditionals](#conditionals)
8. [Loops](#loops)
9. [Functions](#functions)
10. [Scope & Closures](#scope--closures)
11. [Error Handling](#error-handling)
12. [Modules & Require](#modules--require)
13. [Metatables & OOP](#metatables--oop)
14. [Coroutines](#coroutines)
15. [Real-World Use Cases](#real-world-use-cases)

---

## Comments

Single-line comment

```lua
-- This is a single-line comment
```

Multi-line comment

```lua
--[[
  This is a
  multi-line comment
]]
```

---

## Data Types

Lua has 8 built-in data types: `nil`, `boolean`, `number`, `string`, `table`, `function`, `userdata`, and `thread`.

**nil**

```lua
local a = nil
```

**boolean**

```lua
local b = true
local c = false
```

**number — integer**

```lua
local i   = 42
local hex = 0xFF
```

**number — float**

```lua
local f = 3.14
```

**string — single and double quotes**

```lua
local s  = "Hello"
local s2 = 'World'
```

**string — multi-line literal**

```lua
local s3 = [[
  Multi-line
  string
]]
```

**table**

```lua
local t = {}
```

**function**

```lua
local fn = function() end
```

Checking the type of a value

```lua
print(type(42))      --> number
print(type("lua"))   --> string
print(type(nil))     --> nil
print(type({}))      --> table
print(type(print))   --> function
```

---

## Variables

Global variable

```lua
x = 10
```

Local variable (always preferred)

```lua
local name = "Lua"
local age  = 30
```

Multiple assignment

```lua
local a, b, c = 1, 2, 3
```

Swapping values

```lua
a, b = b, a
```

When there are fewer values than variables, the rest become `nil`

```lua
local p, q, r = 10, 20
print(p, q, r)   --> 10   20   nil
```

Constant (convention: all caps)

```lua
local MAX_SIZE = 100
```

---

## Operators

### Arithmetic

Addition

```lua
print(10 + 3)    --> 13
```

Subtraction

```lua
print(10 - 3)    --> 7
```

Multiplication

```lua
print(10 * 3)    --> 30
```

Division — always returns a float

```lua
print(10 / 3)    --> 3.3333...
```

Floor division

```lua
print(10 // 3)   --> 3
```

Modulo

```lua
print(10 % 3)    --> 1
```

Exponentiation

```lua
print(10 ^ 3)    --> 1000.0
```

Negation

```lua
print(-10)       --> -10
```

### Comparison

Equal and not equal — use `~=` instead of `!=`

```lua
print(5 == 5)   --> true
print(5 ~= 3)   --> true
```

Greater / less than

```lua
print(5 > 3)    --> true
print(5 < 3)    --> false
print(5 >= 5)   --> true
print(5 <= 4)   --> false
```

### Logical

```lua
print(true and false)   --> false
print(true or false)    --> true
print(not true)         --> false
```

Short-circuit — `or` returns the first truthy value

```lua
local x = nil
local y = x or "default"   --> "default"
```

Short-circuit — `and` returns the first falsy value or the last value

```lua
local z = true and "yes"   --> "yes"
```

### Concatenation & Length

String concatenation with `..`

```lua
local s = "Hello" .. " " .. "World"
print(s)    --> Hello World
print(#s)   --> 11
```

Length of a sequential table

```lua
local t = {1, 2, 3, 4}
print(#t)   --> 4
```

---

## Strings

Built-in string functions

```lua
local str = "hello, lua!"

print(string.upper(str))          --> HELLO, LUA!
print(string.lower("WORLD"))      --> world
print(string.len(str))            --> 11
print(string.sub(str, 1, 5))      --> hello
print(string.rep("ab", 3))        --> ababab
print(string.reverse(str))        --> !aul ,olleh
print(string.byte("A"))           --> 65
print(string.char(65))            --> A
```

Formatted string — works like `printf`

```lua
local result = string.format("Name: %s, Age: %d, Score: %.2f", "Budi", 20, 98.5)
print(result)   --> Name: Budi, Age: 20, Score: 98.50
```

Finding and replacing

```lua
local s = "learning lua is fun"
print(string.find(s, "lua"))              --> 10  12
print(string.gsub(s, "lua", "Python"))   --> learning Python is fun   1
```

OOP-style method syntax — shorthand using `:`

```lua
print(str:upper())
print(str:sub(1, 5))
print(str:find("lua"))
```

---

## Tables

Tables are the only data structure in Lua. They serve as arrays, dictionaries, objects, and more.

### Array — Index Starts at 1

Declaring and accessing

```lua
local fruits = {"apple", "mango", "orange"}

print(fruits[1])   --> apple
print(fruits[2])   --> mango
print(#fruits)     --> 3
```

Iterating an array

```lua
for i = 1, #fruits do
  print(i, fruits[i])
end
```

Appending an element

```lua
table.insert(fruits, "banana")
```

Inserting at a specific index

```lua
table.insert(fruits, 2, "durian")
```

Removing by index

```lua
table.remove(fruits, 1)
```

Removing the last element

```lua
table.remove(fruits)
```

Sorting

```lua
table.sort(fruits)
```

Joining into a string

```lua
print(table.concat(fruits, ", "))
```

### Dictionary (Hash Map)

Declaring and accessing

```lua
local person = {
  name = "Andi",
  age  = 25,
  city = "Jakarta",
}

print(person.name)      --> Andi
print(person["age"])    --> 25
```

Adding and updating a key

```lua
person.job = "Engineer"
person.age = 26
```

Deleting a key

```lua
person.city = nil
```

Iterating a dictionary

```lua
for key, value in pairs(person) do
  print(key, "=", value)
end
```

### Mixed & Nested Tables

```lua
local data = {
  id   = 1,
  tags = {"lua", "programming", "scripting"},
  meta = {
    created = "2024-01-01",
    active  = true,
  },
}

print(data.tags[1])        --> lua
print(data.meta.created)   --> 2024-01-01
```

---

## Conditionals

if / elseif / else

```lua
local score = 75

if score >= 90 then
  print("A")
elseif score >= 80 then
  print("B")
elseif score >= 70 then
  print("C")
else
  print("D")
end
```

Ternary-style using `and` / `or`

```lua
local status = score >= 60 and "Pass" or "Fail"
print(status)   --> Pass
```

Truthy / Falsy — only `nil` and `false` are falsy; `0` and `""` are truthy

```lua
if 0 then
  print("0 is truthy in Lua")
end
```

---

## Loops

### Numeric For

Counting up

```lua
for i = 1, 5 do
  print(i)
end
```

Counting down with a step

```lua
for i = 10, 1, -2 do
  print(i)
end
```

### Generic For

Iterating an array in order with `ipairs`

```lua
local arr = {"a", "b", "c"}

for index, value in ipairs(arr) do
  print(index, value)
end
```

Iterating all keys with `pairs` — order is not guaranteed

```lua
local dict = {x = 1, y = 2, z = 3}

for key, value in pairs(dict) do
  print(key, value)
end
```

### While

```lua
local i = 1
while i <= 5 do
  print(i)
  i = i + 1
end
```

### Repeat-Until — condition is checked at the end

```lua
local j = 1
repeat
  print(j)
  j = j + 1
until j > 5
```

### Break — exit a loop early

```lua
for i = 1, 10 do
  if i == 5 then break end
  print(i)
end
```

### Goto — skip an iteration (Lua's substitute for `continue`, available since 5.2)

```lua
for i = 1, 5 do
  if i == 3 then goto continue end
  print(i)
  ::continue::
end
```

---

## Functions

Basic function declaration

```lua
local function greet(name)
  return "Hello, " .. name .. "!"
end

print(greet("Budi"))   --> Hello, Budi!
```

Function as a value — first-class function

```lua
local add = function(a, b)
  return a + b
end

print(add(3, 4))   --> 7
```

Multiple return values

```lua
local function minmax(t)
  local min, max = t[1], t[1]
  for _, v in ipairs(t) do
    if v < min then min = v end
    if v > max then max = v end
  end
  return min, max
end

local lo, hi = minmax({5, 2, 9, 1, 7})
print(lo, hi)   --> 1   9
```

Variadic function — variable number of arguments

```lua
local function sum(...)
  local total = 0
  for _, v in ipairs({...}) do
    total = total + v
  end
  return total
end

print(sum(1, 2, 3, 4, 5))   --> 15
```

Default argument values using `or`

```lua
local function connect(host, port)
  host = host or "localhost"
  port = port or 3306
  print("Connecting to " .. host .. ":" .. port)
end

connect()                       --> Connecting to localhost:3306
connect("192.168.1.1", 5432)    --> Connecting to 192.168.1.1:5432
```

---

## Scope & Closures

Closure — a function that captures variables from its outer scope

```lua
local function makeCounter(start)
  local count = start or 0
  return {
    increment = function() count = count + 1 end,
    decrement = function() count = count - 1 end,
    get       = function() return count end,
  }
end

local counter = makeCounter(10)
counter.increment()
counter.increment()
counter.decrement()
print(counter.get())   --> 11
```

Upvalue — a local variable captured by a closure

```lua
local function multiplier(factor)
  return function(x)
    return x * factor
  end
end

local double = multiplier(2)
local triple = multiplier(3)
print(double(5))   --> 10
print(triple(5))   --> 15
```

---

## Error Handling

pcall  protected call, catches errors without propagating them

```lua
local ok, err = pcall(function()
  error("something went wrong!")
end)

print(ok)    --> false
print(err)   --> ...: something went wrong!
```

`xpcall` — protected call with a custom error handler

```lua
local function handler(err)
  return "ERROR: " .. tostring(err)
end

local ok, msg = xpcall(function()
  error({code = 404, message = "not found"})
end, handler)

print(ok)    --> false
print(msg)   --> ERROR: ...
```

Throwing an error object (table)

```lua
local function divide(a, b)
  if b == 0 then
    error({code = "DIV_ZERO", message = "division by zero"})
  end
  return a / b
end

local ok, result = pcall(divide, 10, 0)
if not ok then
  print("Error code:", result.code)
  print("Message:",   result.message)
end
```

`assert` — quick validation

```lua
local function sqrt(n)
  assert(n >= 0, "input must be a non-negative number")
  return math.sqrt(n)
end

print(sqrt(16))   --> 4.0
```

---


### Function Call API

```lua
local http = require("socket.http")
local ltn12 = require("ltn12")

function api_call(base_url, path, query, token)
    -- Construct the full URL
    local full_url = base_url .. path .. "?" .. query
    
    -- Add token if provided
    if token then
        full_url = full_url .. "&token=" .. token
    end
    
    -- Send GET request
    local response_body = {}
    local res, code, headers = http.request{
        url = full_url,
        method = "GET",
        sink = ltn12.sink.table(response_body)
    }
    
    if code == 200 then
        return table.concat(response_body)
    else
        return nil, "HTTP Error: " .. tostring(code)
    end
end
```

### Using a Module (`main.lua`)

Importing and calling module functions

```lua
local mymath = require("mymath")

print(mymath.add(3, 4))    --> 7
print(mymath.square(5))    --> 25
```

Creating a local alias for convenience

```lua
local add = mymath.add
print(add(10, 20))         --> 30
```

---

## Metatables & OOP

### Basic Metatable

Defining metamethods

```lua
local t  = {}
local mt = {
  __index    = function(tbl, key) return "default" end,
  __newindex = function(tbl, key, val) rawset(tbl, key, val * 2) end,
  __tostring = function(tbl) return "MyTable" end,
  __add      = function(a, b) return {value = a.value + b.value} end,
}

setmetatable(t, mt)
```

`__index` — called when a key is not found

```lua
print(t.x)         --> default
```

`__newindex` — intercepts assignment; here it doubles the value

```lua
t.y = 5
print(t.y)         --> 10
```

`__tostring` — called by `tostring()`

```lua
print(tostring(t)) --> MyTable
```

### OOP with Classes

Class definition

```lua
local Animal = {}
Animal.__index = Animal

function Animal.new(name, sound)
  local self = setmetatable({}, Animal)
  self.name  = name
  self.sound = sound
  return self
end

function Animal:speak()
  print(self.name .. " says: " .. self.sound)
end
```

Inheritance — `Dog` extends `Animal`

```lua
local Dog = setmetatable({}, {__index = Animal})
Dog.__index = Dog

function Dog.new(name)
  local self = Animal.new(name, "Woof!")
  return setmetatable(self, Dog)
end

function Dog:fetch(item)
  print(self.name .. " fetches the " .. item)
end
```

Usage

```lua
local cat = Animal.new("Cat", "Meow")
cat:speak()              --> Cat says: Meow

local dog = Dog.new("Rex")
dog:speak()              --> Rex says: Woof!
dog:fetch("ball")        --> Rex fetches the ball
```

---

## Coroutines

Creating and running a coroutine

```lua
local co = coroutine.create(function(a, b)
  print("start:", a, b)
  local c = coroutine.yield(a + b)
  print("resumed with:", c)
  return "done"
end)

local ok, val = coroutine.resume(co, 10, 20)
print("yielded:", val)     --> yielded: 30

local ok2, val2 = coroutine.resume(co, "hello")
print("returned:", val2)   --> returned: done

print(coroutine.status(co))   --> dead
```

Generator pattern using `coroutine.wrap`

```lua
local function range(from, to, step)
  step = step or 1
  return coroutine.wrap(function()
    for i = from, to, step do
      coroutine.yield(i)
    end
  end)
end

for v in range(1, 10, 2) do
  io.write(v .. " ")   --> 1 3 5 7 9
end
print()
```

---

## Real-World Use Cases

### 1. Configuration File (`config.lua`)

Defining the config

```lua
return {
  database = {
    host     = "localhost",
    port     = 5432,
    name     = "myapp_db",
    user     = "admin",
    password = "secret",
  },
  server = {
    host    = "0.0.0.0",
    port    = 8080,
    timeout = 30,
  },
  debug = false,
}
```

Loading and using the config

```lua
local config = require("config")
print(config.database.host)   --> localhost
print(config.server.port)     --> 8080
```

---

### 2. Data Processing Pipeline

Higher-order functions

```lua
local function map(t, fn)
  local result = {}
  for i, v in ipairs(t) do result[i] = fn(v) end
  return result
end

local function filter(t, fn)
  local result = {}
  for _, v in ipairs(t) do
    if fn(v) then result[#result + 1] = v end
  end
  return result
end

local function reduce(t, fn, init)
  local acc = init
  for _, v in ipairs(t) do acc = fn(acc, v) end
  return acc
end
```

Composing the pipeline — filter evens, square them, then sum

```lua
local numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

local result = reduce(
  map(
    filter(numbers, function(x) return x % 2 == 0 end),
    function(x) return x * x end
  ),
  function(a, b) return a + b end,
  0
)

print(result)   --> 220
```

---

### 3. Simple State Machine

State machine class

```lua
local StateMachine = {}
StateMachine.__index = StateMachine

function StateMachine.new(initial)
  return setmetatable({
    state       = initial,
    transitions = {},
  }, StateMachine)
end

function StateMachine:addTransition(from, event, to, action)
  if not self.transitions[from] then
    self.transitions[from] = {}
  end
  self.transitions[from][event] = {to = to, action = action}
end

function StateMachine:trigger(event)
  local t = self.transitions[self.state]
  if t and t[event] then
    local transition = t[event]
    if transition.action then transition.action() end
    self.state = transition.to
    return true
  end
  return false, "invalid transition from state: " .. self.state
end
```

Door example

```lua
local door = StateMachine.new("closed")
door:addTransition("closed", "open",   "opened", function() print("Door opened")   end)
door:addTransition("opened", "close",  "closed", function() print("Door closed")   end)
door:addTransition("opened", "lock",   "locked", function() print("Door locked")   end)
door:addTransition("locked", "unlock", "opened", function() print("Door unlocked") end)

door:trigger("open")     --> Door opened
door:trigger("lock")     --> Door locked
door:trigger("unlock")   --> Door unlocked
door:trigger("close")    --> Door closed
print(door.state)        --> closed
```

---

### 4. Simple Event Emitter

EventEmitter class

```lua
local EventEmitter = {}
EventEmitter.__index = EventEmitter

function EventEmitter.new()
  return setmetatable({listeners = {}}, EventEmitter)
end

function EventEmitter:on(event, callback)
  if not self.listeners[event] then
    self.listeners[event] = {}
  end
  table.insert(self.listeners[event], callback)
end

function EventEmitter:emit(event, ...)
  if self.listeners[event] then
    for _, cb in ipairs(self.listeners[event]) do
      cb(...)
    end
  end
end

function EventEmitter:off(event)
  self.listeners[event] = nil
end
```

Usage

```lua
local emitter = EventEmitter.new()

emitter:on("data", function(val)
  print("Listener 1 received:", val)
end)

emitter:on("data", function(val)
  print("Listener 2 received:", val * 2)
end)

emitter:on("error", function(msg)
  print("Error:", msg)
end)

emitter:emit("data", 42)
emitter:emit("error", "connection failed")
```

---

## Common Idioms

| Idiom | Example | Description |
|---|---|---|
| Default value | `x = x or 10` | Use `10` if `x` is `nil` or `false` |
| Ternary-style | `a and "yes" or "no"` | Equivalent to `a ? "yes" : "no"` |
| Method syntax | `function T:method()` | Sugar for `function T.method(self)` |
| Safe navigation | `t and t.x and t.x.y` | Avoids errors on missing keys |
| Length operator | `#t` | Accurate only for sequential arrays |
| Module pattern | `local M = {} ... return M` | Standard way to create a Lua module |
| Memoization | `cache[k] = cache[k] or compute(k)` | Cache expensive computation results |