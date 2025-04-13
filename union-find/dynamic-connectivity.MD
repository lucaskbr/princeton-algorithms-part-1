Union-find data type (API)

Goal: Design efficient data structure for union-find.

• Number of objects N can be huge. • Number of operations M can be huge. • Find queries and union commands may be intermixed.

public class UF

- UF(int N) - initialize union-find data structure with N objects (0 to N-1)
- void union(int p, int q) - add connection between p and q
- boolean connected(int p, int q) - are p and q in the same component?
- int find(int p) - component identifier for p (0 to N-1)
- int count() - number of components