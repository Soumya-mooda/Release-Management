class Stack:
      """A simple stack implementation using a Python list (LIFO)."""

    def __init__(self):
              """Initialize an empty stack."""
              self._data = []

    def push(self, item):
              """Push an item onto the top of the stack.

                      Args:
                                  item: The item to push.
                                          """
              self._data.append(item)

    def pop(self):
              """Remove and return the top item.

                      Returns:
                                  The item on top of the stack.

                                          Raises:
                                                      IndexError: If the stack is empty.
                                                              """
              if self.is_empty():
                            raise IndexError("Pop from an empty stack.")
                        return self._data.pop()

    def peek(self):
              """Return the top item without removing it.

                      Returns:
                                  The item on top of the stack.

                                          Raises:
                                                      IndexError: If the stack is empty.
                                                              """
        if self.is_empty():
                      raise IndexError("Peek at an empty stack.")
                  return self._data[-1]

    def is_empty(self):
              """Return True if the stack is empty."""
        return len(self._data) == 0

    def size(self):
              """Return the number of items in the stack."""
        return len(self._data)

    def __repr__(self):
              return f"Stack({self._data})"


if __name__ == "__main__":
      s = Stack()
    items = input("Enter items to push (space-separated): ").split()
    for item in items:
              s.push(item)
        print(f"Pushed '{item}' -> {s}")
    print(f"Peek: {s.peek()}")
    print(f"Pop: {s.pop()} -> {s}")
    print(f"Size: {s.size()}")
