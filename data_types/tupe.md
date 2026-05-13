# Python Tuple and Set Methods

## Tuple Methods

| Method | Description |
|---|---|
| `count(x)` | Returns the number of times `x` appears in the tuple. |
| `index(x[, start[, end]])` | Returns the index of the first occurrence of `x`. |

---

# Common Tuple Operations

| Operation | Example | Result |
|---|---|---|
| Length | `len(t)` | `5` |
| Concatenation | `t1 + t2` | `(1, 2, 3, 4)` |
| Repetition | `t * 2` | `(1, 2, 1, 2)` |
| Membership | `3 in t` | `True` |
| Slicing | `t[1:3]` | `(2, 3)` |
| Iteration | `for x in t` | `1 2 3` |

---

# Set Methods

| Method | Description |
|---|---|
| `add(x)` | Adds an element to the set. |
| `clear()` | Removes all elements from the set. |
| `copy()` | Returns a shallow copy of the set. |
| `difference(set2)` | Returns elements present only in the first set. |
| `difference_update(set2)` | Removes common elements from the set. |
| `discard(x)` | Removes an element if it exists. |
| `intersection(set2)` | Returns common elements between sets. |
| `intersection_update(set2)` | Keeps only common elements. |
| `isdisjoint(set2)` | Returns `True` if sets have no common elements. |
| `issubset(set2)` | Returns `True` if set is a subset of another. |
| `issuperset(set2)` | Returns `True` if set is a superset of another. |
| `pop()` | Removes and returns a random element. |
| `remove(x)` | Removes an element; raises error if missing. |
| `symmetric_difference(set2)` | Returns elements not common in both sets. |
| `symmetric_difference_update(set2)` | Updates set with symmetric difference. |
| `union(set2)` | Combines elements from both sets. |
| `update(set2)` | Adds elements from another iterable or set. |

