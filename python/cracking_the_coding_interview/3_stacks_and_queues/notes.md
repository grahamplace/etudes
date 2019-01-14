# Stacks and Queues

## Implementing a Stack

- Stacks are LIFO (last in first out)
  - Think "tennis ball can", the last one you put in the can is the first one you pull out
- Standard stack operations:
  - `pop()`: Remove (and return) the top item from the stack
  - `push(item)`: Add an item to the top of the stack
  - `peek()`: Return (but don't remove) the top item of the stack
  - `isEmpty()`: Return true if and only if the stack is empty (useful for while loop until stack is empty, e.g. in Dijkstra's)
- Performance considerations
  - Stacks can't offer constant-time access to `ith` item like an array can
  - Stacks *do* offer constant time adds/removes, since it doesn't require shifting elements around
- Implementation
  - Stacks are often implemented as Linked Lists (adding/removing from the same side)
- Use Cases
  - Recursive algorithms
    - Push temporary data onto a stack as you recurse, then remove that data as you backtrack
    - Stacks can also be used to implement a recursive algorithm iteratively
