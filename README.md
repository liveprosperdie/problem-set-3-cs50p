# CS50P – Problem Set 3: Exceptions

My solutions to **Problem Set 3** of [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python).

---

## Problems

### 1. ⛽ Fuel Gauge — `fuel.py`
**Problem:** [cs50.harvard.edu/python/psets/3/fuel](https://cs50.harvard.edu/python/psets/3/fuel/)

Prompts the user for a fraction (e.g. `3/4`) and outputs the fuel level as a percentage. Shows `E` if at or below 1%, `F` if at or above 99%. Raises `ValueError` for invalid input and `ZeroDivisionError` for zero denominator.

**Run:**
```bash
python fuel.py
```
**Example:**
```
Fraction: 3/4
75%
```
```
Fraction: 1/100
E
```
```
Fraction: 99/100
F
```
```
Fraction: 1/0
# ZeroDivisionError raised
```

---

### 2. 🌮 Felipe's Taqueria — `taqueria.py`
**Problem:** [cs50.harvard.edu/python/psets/3/taqueria](https://cs50.harvard.edu/python/psets/3/taqueria/)

Simulates a taqueria order system. Accepts menu items one at a time (case-insensitive), adds their price to a running total, and prints the updated total after each entry. Stops on EOF. Ignores invalid items.

**Menu:** Baja Taco ($4.25), Burrito ($7.50), Bowl ($8.50), Nachos ($11.00), Quesadilla ($8.50), Super Burrito ($8.50), Super Quesadilla ($9.50), Taco ($3.00), Tortilla Salad ($8.00)

**Run:**
```bash
python taqueria.py
```
**Example:**
```
Item: Taco
Total: $3.00
Item: Burrito
Total: $10.50
Item: invalid item
Item: Bowl
Total: $19.00
```

---

### 3. 🛒 Grocery List — `grocery.py`
**Problem:** [cs50.harvard.edu/python/psets/3/grocery](https://cs50.harvard.edu/python/psets/3/grocery/)

Collects grocery items from the user one at a time (until EOF), counts duplicates, then prints the sorted list in uppercase with quantities.

**Run:**
```bash
python grocery.py
```
**Example:**
```
mango
mango
apple
banana
apple
# ctrl+D (EOF)
2 APPLE
1 BANANA
2 MANGO
```

---

### 4. 📅 Outdated — `outdated.py`
**Problem:** [cs50.harvard.edu/python/psets/3/outdated](https://cs50.harvard.edu/python/psets/3/outdated/)

Converts dates from two formats into ISO 8601 (`YYYY-MM-DD`). Accepts `MM/DD/YYYY` or `Month DD, YYYY` format. Re-prompts on invalid input.

**Run:**
```bash
python outdated.py
```
**Example:**
```
Date: 9/8/1636
1636-09-08
```
```
Date: September 8, 1636
1636-09-08
```
```
Date: 23/200/1636
Date: 9/8/1636
1636-09-08
```

---

## What I Learned
- `try` / `except` for exception handling
- Catching specific exceptions — `ValueError`, `ZeroDivisionError`, `KeyError`, `EOFError`
- `raise` to manually raise exceptions
- Dictionaries for menu/price lookups
- `sorted()` on dictionaries
- String methods — `.title()`, `.strip()`, `.split()`, `.index()`
- f-string formatting — `{m:02}` for zero-padded numbers
- Re-prompting with `while True` + `pass` on invalid input

---

## Course
**CS50's Introduction to Programming with Python**
Harvard University — [cs50.harvard.edu/python](https://cs50.harvard.edu/python)
