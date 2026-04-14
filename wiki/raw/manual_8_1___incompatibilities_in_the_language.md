# 8.1 – Incompatibilities in the Language

**Category**: Manual

## 8.1 – Incompatibilities in the Language

* The word **global** is a reserved word. Do not use it as a regular name.
* The control variable in **for** loops is read only. If you need to change it, declare a local variable with the same name in the loop body.
* A chain of `__call` metamethods can have at most 15 objects.
* In an error, a **nil** as the error object is replaced by a string message.