## Decimal Rules

1. **`Decimal` is useful for money** because it provides precise decimal calculations.

2. **When creating a `Decimal`, use a string** to avoid inheriting floating-point approximation.

   ```python
   Decimal("0.1")  # Recommended
   
 
### Simple Rule to Remember

- `float` = fast and approximate
- `Decimal` = slower but precise for decimal values
 


## Python `Decimal` Methods


| Method / Usage | Description | Example |Output|
|---|---|---|--|
| Decimal() | Creates a Decimal value | x = Decimal("10.50") |10.50 |
| Decimal("...") | Creates a Decimal from a string | x = Decimal("3.14") |3.14 |
| Decimal(int)` | Creates a Decimal from an integer |x = Decimal(10) | 10 |
| Decimal(float) | Creates a Decimal from a float | x = Decimal(3.14) |3.14 |
| Decimal + Decimal | Adds two Decimal values | x = Decimal("10.5") + Decimal("2.5") | 13.0 |
| Decimal - Decimal | Subtracts two Decimal values | x = Decimal("10.5") - Decimal("2.5") | 8.0 |
| Decimal * Decimal | Multiplies two Decimal values | x = Decimal("10.5") * Decimal("2") | 21.0 |
| Decimal / Decimal | Divides two Decimal values | x = Decimal("10.5") / Decimal("2") | 5.25 |
| .quantize() | Rounds to a specified decimal precision | x.quantize(Decimal("0.01")) |
| .sqrt() | Calculates the square root | x = Decimal(25); x.sqrt() | 5|
| .copy_abs() | Returns the absolute value | x = Decimal(-25) ;x.copy_abs() |25|
| .copy_negate() | Returns the negated value | x = Decimal(25) ; x.copy_negate() |-25|
| .compare() | Compares two Decimal values, if numbers equal return 0, otherwise return 1 |  x = Decimal(25);  y = Decimal(4); x.compare(y) | 1 |
| .normalize() | Removes trailing zeros | x = Decimal(25.0001); x.normalize() |25.00009999999999976694198267 |
| .to_integral_value() | Rounds to an integer value | x = Decimal(25.0001); x.to_integral_value() |25 |
| .as_tuple() | Returns the Decimal's internal representation | x = Decimal(25); x.as_tuple() |DecimalTuple(sign=0, digits=(2, 5, 0), exponent=0) |
| .is_finite() | Checks whether the value is finite | `x.is_finite()` |
| .is_nan() | Checks whether the value is NaN |  x = Decimal(25); x.is_nan() | False |
| .is_zero() | Checks whether the value is zero | `x.is_zero()` |
| .is_signed() | Checks whether the value is negative/signed | `x.is_signed()` | False |


### Example

```python
from decimal import Decimal

price = Decimal("19.99")
tax = Decimal("1.50")

total = price + tax

print(total)

Output 21.49

```

## Float vs Decimal

| | `float` | `Decimal` |
|---|---|---|
| Purpose | General numerical calculations | Exact decimal calculations |
| Precision | Approximate | Exact decimal representation |
| Speed | Faster | Slower |
| Memory | Less | More |
| Best for | Science, engineering, graphics | Money, prices, financial calculations |
| Example | `0.1 + 0.2` | `Decimal("0.1") + Decimal("0.2")` |
| Result | `0.30000000000000004` | `0.3` |

### The classic example

#### Using `float`

```python
a = 0.1
b = 0.2

print(a + b)

0.30000000000000004

```

#### Using `Decimal`

```

from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.2")

print(a + b)

Output 0.3
```

## Limitations of `Decimal`

| Limitation | Explanation | Example |
|---|---|---|
| 🐌 Slower | `Decimal` is generally slower than `float` | `Decimal("1.5") + Decimal("2.5") |
| 💾 More memory | Uses more memory than `float` | Decimal("123.45") |
| 🔢 Precision is not unlimited | Precision is controlled by the decimal context | getcontext().prec = 10 |
| 🔄 Type mixing | You generally cannot directly mix `Decimal` and `float` in arithmetic | Decimal("1.5") + 2.5 → TypeError |
| 🧮 Not ideal for scientific computing | Many scientific/NumPy operations are designed around `float` | numpy typically uses float64 |
| 📐 Limited transcendental operations | Some advanced mathematical operations are less convenient than with `float` | sin(), cos(), etc. |
| ⚙️ Context-dependent | Rounding and precision depend on the active `Decimal` context | getcontext().prec = 5 |
| 📝 Requires care when creating values | Creating from a `float` can carry the float's approximation | Decimal(0.1) ⚠️ |
| 🌐 Serialization can require extra handling | Some systems/APIs expect regular JSON numbers rather than Decimal objects | json.dumps(Decimal("10.50")) |



```
