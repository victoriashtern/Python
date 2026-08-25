

# Python String Methods & Operations

## Complete Table

| Method / Operation | Description | Example |
|------------------|-------------|---------|
| + | Concatenates strings | "a" + "b" → "ab" |
| * | Repeats string | "ha" * 3 → "hahaha" |
| s[i] | Gets character at index | "hello"[0] → "h" |
| s[i:j] | Slices string | "hello"[1:4] → "ell" |
| in | Checks substring | "h" in "hello" → True |
| ==, <, > | Compares strings | "abc" < "bcd" → True |
| for char in s | Iterates characters | for c in "hi": ... |
| capitalize() | First letter uppercase | "hello".capitalize() → "Hello" |
| casefold() | Aggressive lowercase | "HELLO".casefold() → "hello"`|
| center() | Centers string | "hi".center(5) → " hi  " |
| count() | Counts substring | "hello".count("l") → 2 |
| encode() | Converts to bytes | "hi".encode() → b'hi' |
| endswith() | Checks suffix | "hello".endswith("lo") → True |
| expandtabs() | Replaces tabs with spaces | "a\tb".expandtabs() |
| find() | Finds first index | "hello".find("l") → 2 |
| format() | Formats string | "{}!".format("hi") → "hi!" |
| format_map() | Dict formatting | "{x}".format_map({'x':1}) |
| index() | Like find (error if not found) | "hello".index("e") → 1 |
| isalnum() | Letters + digits check | "a1".isalnum() → True |
| isalpha() | Letters only | "abc".isalpha() → True |
| isascii() | ASCII check | "a".isascii() → True |
| isdecimal() | Decimal digits | "123".isdecimal() → True |
| isdigit() | Digit check | "123".isdigit() → True |
| isidentifier() | Valid variable name | "var".isidentifier() → True |
| islower() | All lowercase | "hi".islower() → True |
| isnumeric() | Numeric check | "123".isnumeric() → True |
| isprintable() | Printable check | "hi".isprintable() → True |
| isspace() | Whitespace only | `"   ".isspace() → True |
| istitle() | Title case check | "Hello World".istitle() → True |
| isupper() | All uppercase | "HI".isupper() → True |
| join() | Joins iterable | ",".join(["a","b"]) → "a,b" |
| ljust() | Left-align | "hi".ljust(5) → "hi   " |
| lower() | Lowercase | "HI".lower() → `"hi" |
| lstrip() | Remove left spaces | " hi".lstrip() → "hi" |
| maketrans() | Translation map | str.maketrans("a","b") |
| partition() | Split into 3 parts | "a-b".partition("-") |
| removeprefix() | Remove prefix | "test".removeprefix("te") → "st" |
| removesuffix() | Remove suffix | "test".removesuffix("st") → "te" |
| replace() | Replace substring | "hi".replace("i","o") → "ho" |
| rfind() | Last occurrence index | "hello".rfind("l") → 3 |
| rindex() | Last index (error if missing) | "hello".rindex("l") → 3 |
| rjust() | Right-align | "hi".rjust(5) → "   hi" |
| rpartition() | Split from right | "a-b-c".rpartition("-") |
| rsplit() | Split from right | "a,b,c".rsplit(",",1) |
| rstrip() | Remove right spaces | "hi ".rstrip() → "hi" |
| split() | Split string | "a,b".split(",") → ["a","b"] |
| splitlines() | Split by lines | "a\nb".splitlines() → ["a","b"] |
| startswith() | Checks prefix | "hi".startswith("h") → True |
| strip() | Remove both sides spaces | " hi ".strip() → "hi" |
| swapcase() | Swap case | "Hi".swapcase() → "hI" |
| title() | Title case | "hello world".title() → "Hello World" |
| translate() | Apply translation | "a".translate(table) |
| upper() | Uppercase | "hi".upper() → "HI" |
| zfill() | Pad with zeros | "42".zfill(5) → "00042" |

---

## Notes

- Python strings are **immutable**
- Most string methods return a **new string**
- Indexing starts at `0`
- Negative indexing starts from the end

Example:

```python
s = "hello"

print(s[0])   # h
print(s[-1])  # o
