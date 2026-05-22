
# Python Dictionary Methods and Operations

## Python Dictionary Methods Cheat Sheet

| Operation | Description | Example |
|---|---|---|
| add | add elemt to the dictionary | dic[new_key]=new_value |
| Dictionary comprehension | Create dictionary dynamically | `{x: x*x for x in range(5)}` |
| Nested dictionary access | Access nested values | `students["s1"]["name"]` |
| clear() | Remove all items | `student.clear()` |
| copy() | Create shallow copy | `student.copy()` |
| del dict[key] | Delete key-value pair | `del student["age"]` |
| dict1 \| dict2 | Merge dictionaries (Python 3.9+) | `d1 \| d2` |
| dict[key] | Access value by key | `student["name"]` |
| for k, v in dict.items() | Loop through key-value pairs | `for k, v in student.items():` |
| for key in dict | Loop through keys | `for k in student:` |
| for value in dict.values() | Loop through values | `for v in student.values():` |
| get(key) | Get value safely | `student.get("name")` |
| key in dict | Check if key exists | `"name" in student` |
| items() | Return key-value pairs | `student.items()` |
| keys() | Return all keys | `student.keys()` |
| len(dict) | Get number of items | `len(student)` |
| pop(key) | Remove and return value that assosiated with key | `student.pop("age")` |
| popitem() | Remove last inserted item | `student.popitem()` |
| setdefault() | Get or insert default value | `student.setdefault("city", "Toronto")` |
| update() | Update dictionary values | `student.update({"age": 26})` |
| values() | Return all values | `student.values()` |
| dict[key] = value | Add new key-value pair | `student["age"] = 25` |
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
