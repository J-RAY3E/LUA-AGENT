# os.setlocale()

**Category**: Standard Libraries

### `os.setlocale (locale [, category])`

Sets the current locale of the program. `locale` is a system-dependent string specifying a locale; `category` is an optional string describing which category to change: `"all"`, `"collate"`, `"ctype"`, `"monetary"`, `"numeric"`, or `"time"`; the default category is `"all"`. The function returns the name of the new locale, or **fail** if the request cannot be honored.

If `locale` is the empty string, the current locale is set to an implementation-defined native locale. If `locale` is the string "`C`", the current locale is set to the standard C locale.

When called with **nil** as the first argument, this function only returns the name of the current locale for the given category.

This function may be not thread safe because of its reliance on C function `setlocale`.