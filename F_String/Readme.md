
## f-string?

An **f-string** (formatted string literal) is a Python feature that allows you to insert **variables and expressions directly inside a string** using `{}`.

### Example

```python
name = "John"
age = 25

print(f"My name is {name} and I am {age} years old.")
```

## Python f-String Formatting Options

| Option | Description | Example | Output |
|---|---|---|---| 
| {variable}| Insert a variable | name="John"; print("f"Hello {name}")| "Hello John" |
| {expression}` | Evaluate an expression | print(f"{10 + 5}") | 15 |
| :.2f | 2 decimal places | print(f"{3.14159:.2f}") | 3.14 |
| :.0f | No decimal places | print(f"{3.7:.0f}") | 4 |
| :,.2f | Thousands separator + 2 decimals | print(f"{1234567.89:,.2f}")| 1,234,567.89 |
| :d | Integer format | print(f"{100:d}") | 100 |
| :, | Thousands separator | print(f"{1234567}") | 1,234,567 |
| :e | Scientific notation | print(f"{12345:e}") | 1.234500e+04 |
| :.2e | Scientific notation with precision | print(f"{12345:.2e}")| 1.23e+04 |
| :% | Percentage | print(f"{0.75:%}") | 75.000000% |
| :.2% | Percentage with 2 decimals | print(f"{0.756:.2%}") | 75.60% |
| :s | String format | print(f"{'Hello':s}") | Hello |
| :>10 | Right-align in 10 characters | print(f"{'Hi':>10}") |         Hi |
| :<10 | Left-align in 10 characters | print(f"{'Hi':<10}") | Hi         |
| :^10 | Center-align in 10 characters | print(f"{'Hi':^10}"`) | "    Hi    " |
| :*^10 | Center with `*` padding | print(f"{'Hi':*^10}") | "****Hi****" |
| :0>5 | Zero-padding | print(f"{42:0>5}") | 00042 |
| :05d | Zero-pad integer | print(f"{42:05d}") | 00042 |
| :+d | Always show sign | print(f"{42:+d}") | "+42" |
| :+.2f | Sign + 2 decimals | print(f"{42.5:+.2f}") | "+42.50" |
| : d | Space for positive sign | print(f"{42: d}") | " 42" |
| :x | Hexadecimal | print(f"{255:x}") | ff |
| :X | Uppercase hexadecimal | print(f"{255:X}") | FF |
| :b | Binary | print(f"{10:b}") | 1010 |
| :o | Octal | print(f"{10:o}") | 12 |
| :#x | Hexadecimal with `0x` | print(f"{255:#x}") | 0xff |
| :#b | Binary with `0b` | print(f"{10:#b}") | 0b1010 |
| :#o | Octal with `0o` | print(f"{10:#o}") | 0o12 |
| :.3g | 3 significant digits | print(f"{1234.56:.3g}") | 1.23e+03 |
| :.2f | Fixed-point notation | f"{12.3456:.2f}"` | 12.35 |
| !s | Convert using `str()` | print(f"{value!s}") | value as string |
| !r | Convert using `repr()` | print(f"{value!r}") | repr(value) |
| !a | Convert using `ascii()` | print(f"{value!a}") | ASCII representation |
| = | Show expression and value | print(f"{x=}") | x=10 |
| :=` | Assignment expression | `f"{(x := 10)}"` | `10` |

