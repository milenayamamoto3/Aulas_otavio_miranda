from typing import Deque, Any
from collections import deque

queue: Deque[Any] = deque()
queue.append("A")
queue.append("B")
queue.append("C")
print("Removido", queue.popleft())
print("Removido", queue.popleft())
print("Removido", queue.popleft())
print("Removido", queue.popleft())  # IndexError: pop from an empty deque

print("For inútil")
for item in queue:
    print(item)
