# 🐍 Python List Data Structure

A **list** in Python is a collection of items stored in a specific order.

## 📌 What is a List?

A list is:
- ✔️ **Ordered** → items keep their position  
- ✔️ **Mutable** → items can be changed  
- ✔️ **Dynamic** → size can grow or shrink  
- ✔️ **Allows duplicates**  
- ✔️ **Can store different data types**
- ````markdown id="3q8kz1"
# 🧱 Creating and Working with Python Lists

## 🆕 Creating Lists

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

````markdown id="lq9x2a"
# ➕ Adding and Removing Items in Python Lists

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

````markdown id="7v9m2k"
# 🔁 Working with Python Lists

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

## ⚡ List Comprehension

```python
numbers = [x for x in range(5)]
evens = [x for x in range(10) if x % 2 == 0]
```

```markdown id="r8k3md"
# 🛠️ Python List Utilities and Comparisons

## 📌 Useful List Functions

- `len()` → returns the number of items in a list  
- `max()` → returns the largest value  
- `min()` → returns the smallest value  
- `sum()` → returns the sum of elements  
- `sorted()` → returns a sorted version of the list  

---

## 📚 Common List Methods

- `append()`  
- `insert()`  
- `extend()`  
- `remove()`  
- `pop()`  
- `clear()`  
- `sort()`  
- `reverse()`  
- `copy()`  
- `count()`  
- `index()`  

---
