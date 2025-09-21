# DSA_Data-Structures-Implementation-Lab

# Stack (LIFO) - Data Structures Implementation Lab

## Overview

This project implements a **Stack** data structure (Last-In-First-Out) in Python from scratch. The stack is built using a Python list internally, but exposes clear stack semantics. It is fully tested using Python's `unittest` framework.

## Features

* Push, pop, peek, size, clear, is\_empty
* Iteration in LIFO order
* Conversion to list
* Simple string representation

## Real-World Applications

* **Browser history navigation**: Back/forward actions
* **Function calls**: Call stack frames
* **Undo/redo systems**: Tracking operations

## Complexity Analysis

| Operation | Time Complexity |
| --------- | --------------- |
| Push      | O(1) amortized  |
| Pop       | O(1)            |
| Peek      | O(1)            |
| is\_empty | O(1)            |
| size      | O(1)            |
| to\_list  | O(n)            |

Space Complexity: **O(n)** for storing n elements.

## How to Run

1. Clone the repository
2. Run the tests:

   ```bash
   python stack_lab.py
