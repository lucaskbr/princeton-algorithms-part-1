import os

class UF:
  def __init__(self, n: int):
    self.n = n
    self.objects = [v for v in range(0, n)]
    self.components: list[set] = []

  def union(self, p: int, q: int):

    if p not in self.objects:
      return 
    if q not in self.objects:
      return

    p_component = None
    q_component = None

    for index, component in enumerate(self.components):
      if p in component:
        p_component = index
      if q in component:
        q_component = index
      
      if p_component != None and q_component != None:
        break
    
    if p_component != None and q_component != None:
      self.components[p_component] = self.components[p_component] | self.components[q_component]
      self.components.pop(q_component)
    elif p_component != None and q_component == None:
      self.components[p_component].add(q)
    elif p_component == None and q_component != None:
      self.components[q_component].add(p)
    else:
      self.components.append(set((p, q)))

  
  def connected(self, p: int, q: int):
    for component in self.components:
      if p in component and q in component:
        return True
    
    return False

n = int(input("Initialize the value of N: "))
uf = UF(n)

while True:
  print("c to check connection")
  print("u to perform an union")
  option = str(input("Press c or u: "))
  os.system("clear")
  
  p = int(input("Value of p: "))
  q = int(input("Value of q: "))

  match option:
    case "c":
      is_connected = uf.connected(p, q)
      print(f"{p} and {q} connection is: {is_connected}")
    case "u":
      uf.union(p, q)

  print(f"Current component: {uf.components}")
  print("\n")

