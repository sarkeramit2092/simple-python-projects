# enumerate() in Python is super useful when you need both the index and the value while iterating over a sequence like a list, tuple, or string.

x = ("Masala", "lemon", "ginger")


y = enumerate(x)

print (y)

print(list(y))



- Why use enumerate()?

Without enumerate():

python

fruits = ['apple', 'banana', 'cherry']
index = 0
for fruit in fruits:
    print(index, fruit)
    index += 1

- With enumerate():

python

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)

✅ Advantages of using enumerate():
- Cleaner and more Pythonic
- Less prone to errors (no need to manually manage an index)
- Supports optional start parameter (enumerate(list, start=1))

📌 Example with start:
python
for i, item in enumerate(['a', 'b', 'c'], start=1):
    print(f"{i}: {item}")

# Output:

1: a
2: b
3: c