class Node:
  def __init__(self, value, next) -> None:
    self.value = value
    self.next = next

  def __str__(self) -> str:
    obj = {
      "value": self.value,
      "next": self.next
    }
    return str(obj)

class Stack:

  def __init__(self) -> None:
    self.head = None
    pass

  def push(self, value):

    if self.head == None:
      node = Node(value=value, next=None)
      self.head = node
    else:
      node = Node(value=value, next=self.head)
      self.head = node

  def pop(self):
    if self.head == None:
      return
    else:
      self.head = self.head.next
