# Data Structure

## Array
* An array is a collection of elements stored at **contiguous memory locations**, where each element is accessed by an index.
* Fast access using index: `O(1)` time
* Use cases
  * Storing a list of items
  * ***Efficient lookups*** and iteration

---

## LinkedList
* A linkedList is a **linear data structure** where each element(node) contains: 
  * The data
  * A pointer to the next node in the sequence
* Unlikely arrays, elements are not stored in contiguous memory
* Access time: `O(n)` time

--- 

## Tree
* A tree is a hierarchical data structure mad up of **nodes**, where:
  * The topmost node is called the **root**
  * Each node may point to one or more **child** nodes
  * Nodes with no children are called **leaves**
* Each child has only one parent (Except for root)
* Unlike arrays or linkedList, trees are non-linear - they don't go straight from left to right

### 🌳 Basic Tree Terminology
| Term     | Meaning                                             |
|----------|-----------------------------------------------------|
| Root     | The top node of the tree                            |
| Child    | A node connected below another node                 |
| Parent   | The node above a child                              |
| Sibling  | Nodes with the same parent                          |
| Leaf     | A node with no children                             |
| Depth    | Distance from root to the node                      |
| Height   | Longest path from node to a leaf                    |
| Subtree  | A tree formed from a node and its descendants       |


---
## Stack
* A stack is a linear data structure that follows the **Last In, First Out (LIFO)** principle
  * The last element added is the first one removed

### 📚 Basic Stack Operations
| Operation         | Description                                      |
| ----------------- | ------------------------------------------------ |
| `push(x)`         | Add element `x` to the top                        |
| `pop()`           | Remove and return the top element                 |
| `peek()` / `top()`| Return the top element without removing           |
| `is_empty()`      | Check if the stack is empty                       |


--- 
## Queue
* A queue is a linear data structure that follows the **First In, First Out (FIFO)** principle

### 📚 Basic Queue Operations
| Operation            | Description                              |
|----------------------|------------------------------------------|
| `enque(x)`           | Add element to the **back** of the queue |
| `deque`              | Remove element from the **front**        |
| `peek()` / `front()` | Get the front element without removing   |
| `is_empty()`         | Check if the queue is empty              |


---
## Heap
* A heap is a **special binary tree-based data structure** that satisfies the heap property
  * In a **Max Heap**, the parent is always greater than or equal to its children
  * In a **Min Heap**, the parent is always less than or equal to its children
* ✅ Heaps are **complete binary trees**
  * All levels are full except possibly the last, which is filled from left to right