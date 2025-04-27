import os

class UF:
  def __init__(self, n: int):
    self.n = n
    self.objects = [v for v in range(0, n)]

  def union(self, p: int, q: int) -> list[int]:
    length = len(self.objects)

    if p > length:
      return

    if q > length:
      return

    p_id = self.objects[p]
    q_id = self.objects[q]

    for i, id in enumerate(self.objects):
      if id == q_id:
        self.objects[i] = p_id

    return self.objects

  def connected(self, p: int, q: int) -> bool:
    return self.objects[p] == self.objects[q]
  
  def find(self, p: int) -> int:
    return self.objects[p]
  
  def count(self) -> int:
    components = set()

    for id in self.objects:
      components.add(id)

    return len(components)


n = int(input("Initialize the value of N: "))
uf = UF(n)

print(uf.objects)

while True:
  print(f"Current component: {uf.objects}")
  print("[connect] to check connection")
  print("[union] to perform an union")
  print("[find] to check id of number")
  print("[count] to check how many ids exists")
  
  option = str(input("[type...]: "))
  os.system("clear")

  match option:
    case "connect":
      p = int(input("Value of p: "))
      q = int(input("Value of q: "))

      is_connected = uf.connected(p, q)
      print(f"{p} and {q} connection is: {is_connected}")
    case "union":
      p = int(input("Value of p: "))
      q = int(input("Value of q: "))
      uf.union(p, q)
    case "find":
      p = int(input("Value of p: "))
      find = uf.find(p)
      print(f"[find] result is: {find}")
    case "count":
      count = uf.count()
      print(f"[count] result is: {count}")

  print("\n")

