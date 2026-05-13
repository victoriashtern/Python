
| Method | Description |
|---|---|
| append(x) | Adds an item `x` to the end of the list. |
| extend(iterable) | Adds all elements from another iterable to the list. |
| insert(i, x) | Inserts item `x` at position `i`. |
| remove(x) | Removes the first occurrence of item `x`. |
| pop([i]) | Removes and returns the item at index `i` (last item if index not given). |
| clear() | Removes all items from the list. |
| index(x[, start[, end]]) | Returns the index of the first occurrence of `x`. |
| count(x) | Returns the number of times `x` appears in the list. |
| sort(key=None, reverse=False) | Sorts the list in ascending order by default. |
| reverse() | Reverses the elements of the list in place. |
| copy() | Returns a shallow copy of the list. |

---

## Example

```python
numbers = [3, 1, 2]

numbers.append(4)
print(numbers)   # [3, 1, 2, 4]

numbers.sort()
print(numbers)   # [1, 2, 3, 4]

numbers.pop()
print(numbers)   # [1, 2, 3]
