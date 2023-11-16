# **MyList Implementation with Dynamic Array**

This Python code provides an implementation of a dynamic array-based list named `MyList`. It utilizes concepts from **Data Structures** and **Algorithms** to create a versatile and efficient list data structure. Below is an overview of the functionalities and the underlying concepts used in this implementation.

## **Features**

### 1. **Dynamic Array**
The list is implemented as a dynamic array, allowing it to resize automatically when the number of elements exceeds the current capacity. This helps in efficient memory usage and avoids the need to specify the size of the list in advance.

### 2. **Indexing**
The list supports both positive and negative indexing. Positive indexing starts from 0, while negative indexing allows accessing elements from the end of the list. The implementation ensures that index errors are handled gracefully.

### 3. **Basic Operations**
- **Append**: Adds an element to the end of the list. If the list is full, it dynamically resizes to accommodate more elements.
- **Pop**: Removes and returns the last element from the list.
- **Clear**: Empties the list by resetting the number of elements and size.
- **Find**: Searches for an element in the list and returns its index. If not found, an error is returned.
- **Insert**: Inserts an element at a specified position in the list, shifting other elements as necessary.
- **Delete**: Removes an element at a specified position in the list.
- **Min, Max, Sum**: Computes the minimum, maximum, and sum of the elements in the list, respectively.
- **Extend**: Appends elements from another list to the current list.
- **Remove**: Removes the first occurrence of a specified element in the list.
- **Sort**: Sorts the elements of the list in ascending order using the Bubble Sort algorithm.
- **Slicing**: Creates a new list containing elements from the original list within a specified range.

### 4. **Other Operations**
- **Negative Indexing**: Accesses elements using negative indices.
- **Resize**: Resizes the internal array to a new capacity.

## **Data Structures and Algorithms Concepts**

### 1. **Dynamic Array**
The implementation uses a dynamic array to achieve efficient resizing and memory management.

### 2. **Indexing and Searching**
Indexing operations are implemented with support for both positive and negative indices. Linear search is used to find elements in the list.

### 3. **Sorting**
The `sort` method uses the Bubble Sort algorithm to sort the elements in ascending order.

### 4. **Slicing**
The `slicing` method demonstrates the concept of slicing a list to create a new list with a subset of elements.

### 5. **Memory Management**
The `__makeArray` method utilizes the `ctypes` library to create a C-type array for efficient memory management.


**Note:** The code in this repository is provided as a learning resource and may not be suitable for production use without further modification and testing.