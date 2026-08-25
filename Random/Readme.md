

# Python `random` Module Cheat Sheet

| Method | Description | Example |
|---|---|---|
| random() | Random float between 0.0 and 1.0 | `random.random()` |
| randint(a, b) | Random integer between `a` and `b` (inclusive) | `random.randint(1, 10)` |
| randrange(start, stop, step) | Random number from range | `random.randrange(0, 10, 2)` |
| uniform(a, b) | Random float between `a` and `b` | `random.uniform(1.5, 5.5)` |
| choice(seq) | Random item from sequence | `random.choice(colors)` |
| choices(seq, k=n) | Multiple random items (with replacement) | `random.choices(colors, k=3)` |
| sample(seq, k=n) | Unique random items | `random.sample(colors, k=3)` |
| shuffle(seq) | Shuffle list in place | `random.shuffle(cards)` |
| seed(x) | Set random seed | `random.seed(42)` |
| getrandbits(n) | Random integer with `n` bits | `random.getrandbits(8)` |
| triangular(low, high, mode) | Random float using triangular distribution | `random.triangular(1, 10, 5)` |
| betavariate(alpha, beta) | Beta distribution | `random.betavariate(2, 5)` |
| expovariate(lambda) | Exponential distribution | `random.expovariate(1.5)` |
| gammavariate(alpha, beta) | Gamma distribution | `random.gammavariate(2, 3)` |
| gauss(mu, sigma) | Gaussian distribution | `random.gauss(0, 1)` |
| lognormvariate(mu, sigma) | Log-normal distribution | `random.lognormvariate(0, 1)` |
| normalvariate(mu, sigma) | Normal distribution | `random.normalvariate(0, 1)` |
| vonmisesvariate(mu, kappa) | Circular data distribution | `random.vonmisesvariate(0, 4)` |
| paretovariate(alpha) | Pareto distribution | `random.paretovariate(2)` |
| weibullvariate(alpha, beta) | Weibull distribution | `random.weibullvariate(1, 2)` |
