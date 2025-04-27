class Stack:
  def __init__(self) -> None:
    self.items = []
    pass

  def push(self, value) -> None:
    self.items.append(value)

  def pop(self) -> None:
    self.items.pop()
