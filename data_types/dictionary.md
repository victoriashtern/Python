
# Python Dictionary Methods and Operations

| Method / Operation | Description | Example |
|---|---|---|
| dict[key] | Access value by key | student["name"] |
| get(key) | Get value safely | student.get("name") |
| keys() | Return all keys | student.keys() |
| values() | Return all values | student.values() |
| items() | Return key-value pairs | student.items() |
| update() | Update dictionary values | student.update({"age": 26}) |
| pop(key) | Remove and return item | student.pop("age") |
| popitem() | Remove last inserted item | student.popitem() |
| clear() | Remove all items | student.clear() |
| copy() | Create shallow copy | student.copy() |
| setdefault() | Get or insert default value | student.setdefault("city", "Toronto") |
| del dict[key] | Delete key-value pair | del student["age"] |
| key in dict | Check if key exists | "name" in student` |
| len(dict) | Get number of items | len(student) |
| for key in dict | Loop through keys | for k in student: |
| for value in dict.values() | Loop through values | for v in student.values(): |
| for k, v in dict.items() | Loop through key-value pairs | for k, v in student.items(): |
| dict1 \| dict2 | Merge dictionaries (Python 3.9+) | d1 \| d2 |
| Dictionary comprehension | Create dictionary dynamically | {x: x*x for x in range(5)} |
| Nested dictionary access | Access nested values | students["s1"]["name"] |

---

## Example

```python
student = {
    "name": "Alice",
    "age": 25
}

# Access value
print(student["name"])

# Add new item
student["course"] = "Python"

# Update value
student["age"] = 26

# Remove item
student.pop("course")

# Loop through dictionary
for key, value in student.items():
    print(key, value)
