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
* A stack is a linear data structure that follows the **Last In, First Out (LIFO) principle
  * The last element added is the first one removed

### 📚 Basic Stack Operations
| Operation         | Description                                      |
| ----------------- | ------------------------------------------------ |
| `push(x)`         | Add element `x` to the top                        |
| `pop()`           | Remove and return the top element                 |
| `peek()` / `top()`| Return the top element without removing           |
| `is_empty()`      | Check if the stack is empty                       |