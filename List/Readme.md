## 📌 What is a List?

A list is:
- ✔️ **Ordered** → items keep their position  
- ✔️ **Mutable** → items can be changed  
- ✔️ **Dynamic** → size can grow or shrink  
- ✔️ **Allows duplicates**  
- ✔️ **Can store different data types**

# Python List Methods and Operations



| Method / Operation | Description | Example | Result |
|---|---|---|---|
| append() | Add one item to the end | nums = [1, 2] nums.append(3) | [1, 2, 3] |
| clear() | Remove all items | nums = [1, 2] nums.clear() | [] |
| copy() | Create shallow copy | nums = [1, 2] new_nums = nums.copy() | [1, 2] |
| count() | Count occurrences of value | nums = [1, 2, 2, 3] nums.count(2) | 2 |
| del | Delete item or slice | nums = [1, 2, 3] del nums[1] | [1, 3] |
| enumerate() | Get index and value together | list(enumerate(['a', 'b'])) | [(0, 'a'), (1, 'b')] |
| extend() | Add multiple items | nums = [1, 2] nums.extend([3, 4]) | [1, 2, 3, 4] |
| Indexing [] | Access item by index | nums = [10, 20, 30] nums[1] | 20 |
| index() | Find position of value | nums = [10, 20, 30] nums.index(20) | 1 |
| insert() | Insert item at specific index | nums = [1, 3] nums.insert(1, 2) | [1, 2, 3] |
| len() | Get number of items | nums = [1, 2, 3] len(nums) | 3 |
| List Comprehension | Create lists concisely | squares = [x*x for x in range(5)] | [0, 1, 4, 9, 16] |
| List with Values | Create a list with items | nums = [1, 2, 3] | [1, 2, 3] |
| list() | Create an empty list using constructor | nums = list() | [] |
| max() | Largest value | max([3, 1, 2]) | 3 |
| Membership in | Check if item exists | 2 in [1, 2, 3] | True |
| Membership not in | Check if item does not exist | 5 not in [1, 2, 3] | True |
| min() | Smallest value | min([3, 1, 2]) | 1 |
| Negative Indexing | Access from end | nums = [10, 20, 30] nums[-1] | 30 |
| Empty List Creation | Create an empty list | nums = [] | [] |
| pop() | Remove item by index and return it | nums = [1, 2, 3] nums.pop() | returns 3, list becomes [1, 2] |
| Repetition * | Repeat list items | [1, 2] * 2 | [1, 2, 1, 2] |
| remove() | Remove first matching value | nums = [1, 2, 3] nums.remove(2) | [1, 3] |
| reverse() | Reverse current order | nums = [1, 2, 3] nums.reverse() | [3, 2, 1] |
| Slicing | Get part of list | nums = [1, 2, 3, 4] nums[1:3] | [2, 3] |
| sort() | Sort list in ascending order | nums = [3, 1, 2] nums.sort() | [1, 2, 3] |
| sort(reverse=True) | Sort in descending order | nums = [3, 1, 2] nums.sort(reverse=True) | [3, 2, 1] |
| sorted() | Return new sorted list | sorted([3, 1, 2]) | [1, 2, 3] |
| `sum()` | Sum of numeric items | `sum([1, 2, 3])` | `6` |
| Concatenation `+` | Combine lists | `[1, 2] + [3, 4]` | `[1, 2, 3, 4]` |
| `zip()` | Combine multiple lists | `list(zip([1,2], ['a','b']))` | `[(1, 'a'), (2, 'b')]` |
