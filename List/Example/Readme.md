
### 🆕 Creating Lists
- **Empty list**
```python
numbers = []
````

* **List with values**

```python
fruits = ["apple", "banana", "orange"]
```

* **Mixed data types**

```python
mixed = [10, "hello", True, 3.14]
```

* **Nested list**

```python
matrix = [[1, 2], [3, 4]]
```

---

## 🔍 Accessing Elements

```python
fruits = ["apple", "banana", "orange"]

print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[-1])  # orange
```

---

## ✏️ Changing List Items

```python
fruits = ["apple", "banana", "orange"]
fruits[1] = "grape"
```

## ➕ Adding Items

### append()
```python
numbers = [1, 2, 3]
numbers.append(4)
````

### insert()

```python
fruits = ["apple", "banana"]
fruits.insert(1, "orange")
```

### extend()

```python
a = [1, 2]
b = [3, 4]
a.extend(b)
```

---

## ❌ Removing Items

### remove()

```python
fruits.remove("banana")
```

### pop()

```python
numbers.pop(1)
```

### del

```python
del numbers[0]
```

### clear()

```python
numbers.clear()
```

---

## 📏 List Length

```python
len(numbers)
```

## 🔄 Looping Through Lists

### for loop
```python
for fruit in fruits:
    print(fruit)
````

### while loop

```python
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
```

---

## ❓ Checking if Item Exists

```python
if "banana" in fruits:
    print("Found")
```

---

## ✂️ List Slicing

```python
numbers[1:4]
numbers[:3]
numbers[2:]
numbers[::2]
numbers[::-1]
```

---

## 🔃 Sorting Lists

```python
numbers.sort()
numbers.sort(reverse=True)

sorted(numbers)
```

---

## 🔄 Reversing Lists

```python
numbers.reverse()
```

---

## 📋 Copying Lists

```python
b = a.copy()
b = list(a)
```

---

## 🔗 Joining Lists

```python
c = a + b
```

---

## 🧩 Nested Lists

```python
matrix = [[1, 2], [3, 4]]
print(matrix[0][1])
```

---
## Useful List Functions
These are built-in Python functions commonly used with lists:

- len() – Returns the number of items in a list
- max() – Returns the largest item in a list
- min() – Returns the smallest item in a list
- sum() – Returns the sum of all items in a list
- sorted() – Returns a new sorted list from the elements of any iterable

## Common List Methods
These are methods available for Python list objects:

- append() – Adds an item to the end of the list
- insert() – Inserts an item at a specified index
- extend() – Adds all items from another iterable to the list
- remove() – Removes the first matching item from the list
- pop() – Removes and returns an item at a given index (last item by default)
- clear() – Removes all items from the list
- sort() – Sorts the list in place
- reverse() – Reverses the order of the list in place
- copy() – Returns a shallow copy of the list
- count() – Returns the number of occurrences of a value
- index() – Returns the index of the first occurrence of a value
```

```
## Lists vs Tuples

- **List → Mutable**
  - Can be changed after creation (add, remove, modify elements)

- **Tuple → Immutable**
  - Cannot be changed after creation

---

## Lists vs Dictionaries

- **List → Access by index**
  - Elements are accessed using numerical positions (e.g., `list[0]`)

- **Dictionary → Access by key**
  - Elements are accessed using keys (e.g., `dict["name"]`)

---

## Common Errors in Python

- **IndexError**
  - Occurs when trying to access an index that is out of range in a list or tuple

- **ValueError**
  - Occurs when a function receives an argument of the correct type but an inappropriate value
    
```

```
## Advantages of Lists
- Easy to use  
- Flexible  
- Dynamic (can grow or shrink as needed)  
- Powerful built-in methods for manipulation  

---

## Disadvantages of Lists
- Slower than tuples in performance  
- Uses more memory  
- Searching large lists can be slow
  
---
## When to Use Lists
Use lists when:

- Data changes frequently  
- You need ordered data  
- Duplicate values are allowed  
- You need to frequently add or remove items

