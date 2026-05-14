# Python List Methods and Operations

## List Methods

| Method | Description | Example |
|--------|-------------|---------|
| append(x) | Add item to the end of the list | nums.append(5) |
| extend(iterable) | Add multiple items to the list | nums.extend([6, 7]) |
| insert(i, x) | Insert item at a specific position | nums.insert(1, 10) |
| remove(x) | Remove first matching item | nums.remove(10) |
| pop([i]) | Remove and return item at index | nums.pop() |
| clear() | Remove all items from the list | nums.clear() |
| index(x) | Return index of first matching item | nums.index(5) |
| count(x) | Count occurrences of an item | nums.count(5) |
| sort() | Sort the list in ascending order | nums.sort() |
| reverse() | Reverse the list | nums.reverse() |
| copy() | Return a shallow copy of the list | new_nums = nums.copy() |

---

## Common List Operations

| Operation | Description | Example |
|-----------|-------------|---------|
| + | Concatenate lists | [1,2] + [3,4] |
| * | Repeat list items | [1] * 3 |
| in | Check membership | 2 in nums |
| not in | Check non-membership | 5 not in nums |
| len() | Get length of list | len(nums) |
| min() | Get smallest item | min(nums) |
| max() | Get largest item | max(nums) |
| sum() | Sum all items | sum(nums) |
| sorted() | Return sorted copy | sorted(nums) |
| del | Delete item or slice | del nums[1] |
| Slicing | Extract part of list | nums[1:4] |
| Indexing | Access item by index | nums[0] |
| Assignment | Modify list item | nums[0] = 99 |

---

## Example Usage

```python
nums = [3, 1, 4]

nums.append(5)
nums.insert(1, 10)
nums.remove(1)

print(nums)        # [3, 10, 4, 5]
print(nums[0])     # 3
print(nums[1:3])   # [10, 4]

nums.sort()
print(nums)        # [3, 4, 5, 10]
