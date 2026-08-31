
## 🧮 Python `math` Module Methods

| Method | Description | Example | Result |
|---|---|---|---:|
| `math.ceil(x)` | Rounds up to the nearest integer | `math.ceil(4.2)` | `5` |
| `math.comb(n, k)` | Number of combinations | `math.comb(5, 2)` | `10` |
| `math.copysign(x, y)` | Gives `x` the sign of `y` | `math.copysign(5, -1)` | `-5.0` |
| `math.fabs(x)` | Absolute value as a float | `math.fabs(-5)` | `5.0` |
| `math.factorial(x)` | Factorial of a number | `math.factorial(5)` | `120` |
| `math.floor(x)` | Rounds down to the nearest integer | `math.floor(4.8)` | `4` |
| `math.fmod(x, y)` | Floating-point remainder | `math.fmod(7, 3)` | `1.0` |
| `math.gcd(a, b)` | Greatest common divisor | `math.gcd(12, 8)` | `4` |
| `math.isclose(a, b)` | Checks if two values are approximately equal | `math.isclose(0.1 + 0.2, 0.3)` | `True` |
| `math.isfinite(x)` | Checks if value is finite | `math.isfinite(10)` | `True` |
| `math.isinf(x)` | Checks if value is infinity | `math.isinf(math.inf)` | `True` |
| `math.isnan(x)` | Checks if value is NaN | `math.isnan(math.nan)` | `True` |
| `math.isqrt(x)` | Integer square root | `math.isqrt(20)` | `4` |
| `math.lcm(a, b)` | Least common multiple | `math.lcm(4, 6)` | `12` |
| `math.log(x)` | Natural logarithm | `math.log(10)` | `2.302...` |
| `math.log10(x)` | Base-10 logarithm | `math.log10(100)` | `2.0` |
| `math.log2(x)` | Base-2 logarithm | `math.log2(8)` | `3.0` |
| `math.pow(x, y)` | Raises `x` to the power `y` | `math.pow(2, 3)` | `8.0` |
| `math.prod(iterable)` | Multiplies all values | `math.prod([2, 3, 4])` | `24` |
| `math.sqrt(x)` | Square root | `math.sqrt(25)` | `5.0` |
| `math.trunc(x)` | Removes decimal portion | `math.trunc(4.8)` | `4` |
| `math.exp(x)` | Calculates `eˣ` | `math.exp(1)` | `2.718...` |
| `math.expm1(x)` | Calculates `eˣ - 1` accurately | `math.expm1(1)` | `1.718...` |
| `math.degrees(x)` | Converts radians to degrees | `math.degrees(math.pi)` | `180.0` |
| `math.radians(x)` | Converts degrees to radians | `math.radians(180)` | `3.14159...` |
| `math.sin(x)` | Sine of an angle | `math.sin(math.pi / 2)` | `1.0` |
| `math.cos(x)` | Cosine of an angle | `math.cos(0)` | `1.0` |
| `math.tan(x)` | Tangent of an angle | `math.tan(0)` | `0.0` |
| `math.asin(x)` | Inverse sine | `math.asin(1)` | `1.5708...` |
| `math.acos(x)` | Inverse cosine | `math.acos(1)` | `0.0` |
| `math.atan(x)` | Inverse tangent | `math.atan(1)` | `0.7854...` |
| `math.atan2(y, x)` | Angle from coordinates | `math.atan2(1, 1)` | `0.7854...` |
| `math.sinh(x)` | Hyperbolic sine | `math.sinh(1)` | `1.175...` |
| `math.cosh(x)` | Hyperbolic cosine | `math.cosh(1)` | `1.543...` |
| `math.tanh(x)` | Hyperbolic tangent | `math.tanh(1)` | `0.761...` |
| `math.asinh(x)` | Inverse hyperbolic sine | `math.asinh(1)` | `0.881...` |
| `math.acosh(x)` | Inverse hyperbolic cosine | `math.acosh(2)` | `1.316...` |
| `math.atanh(x)` | Inverse hyperbolic tangent | `math.atanh(0.5)` | `0.549...` |
| `math.hypot(x, y)` | Euclidean distance / hypotenuse | `math.hypot(3, 4)` | `5.0` |
| `math.dist(p, q)` | Distance between two points | `math.dist((0,0), (3,4))` | `5.0` |
| `math.gamma(x)` | Gamma function | `math.gamma(5)` | `24.0` |
| `math.lgamma(x)` | Natural log of absolute gamma | `math.lgamma(5)` | `3.178...` |
| `math.erf(x)` | Error function | `math.erf(1)` | `0.842...` |
| `math.erfc(x)` | Complementary error function | `math.erfc(1)` | `0.157...` |
| `math.fsum(iterable)` | Accurate floating-point sum | `math.fsum([0.1, 0.2])` | `0.300...` |
| `math.remainder(x, y)` | IEEE remainder | `math.remainder(7, 3)` | `1.0` |
| `math.modf(x)` | Separates fractional and integer parts | `math.modf(4.5)` | `(0.5, 4.0)` |
| `math.frexp(x)` | Separates mantissa and exponent | `math.frexp(8)` | `(0.5, 4)` |
| `math.ldexp(x, i)` | Calculates `x × 2ⁱ` | `math.ldexp(0.5, 4)` | `8.0` |
| `math.nextafter(x, y)` | Next floating-point value toward `y` | `math.nextafter(1.0, 2.0)` | `1.000...` |
| `math.ulp(x)` | Value of the least significant bit | `math.ulp(1.0)` | `2.22e-16` |
