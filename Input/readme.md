
## Python `input()` Methods

| Method / Usage | Description | Example |
|---|---|---|
| input() | Gets input from the user | name = input() |
| input("...") | Gets input with a prompt | name = input("Enter name: ") |
| int(input()) | Gets an integer | age = int(input("Age: ")) |
| float(input()) | Gets a decimal number | price = float(input("Price: ")) |
| input().strip() | Removes surrounding whitespace | name = input().strip() |
| input().lower() | Converts input to lowercase | answer = input().lower() |
| input().upper() | Converts input to uppercase | code = input().upper() |
| input().split() | Splits input into a list | items = input().split() |
| input().split(",") | Splits input using commas | items = input().split(",") |
| input().strip().lower() | Removes spaces and converts to lowercase | answer = input().strip().lower() |

### Example

If the user enters:

```text
Apple Banana Orange

items = input().split()
print(items)

Output 
['Apple', 'Banana', 'Orange']

