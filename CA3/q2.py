from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def directed_build_adjacency_list(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  
    return graph

def dfs(graph, node, parent, in_, out, sub, timer):
    in_[node] = timer[0]
    sub.append(node)
    timer[0] += 1
    for i in graph[node]:
        if i != parent:
            dfs(graph, i, node, in_, out, sub, timer)
    out[node] = timer[0]

x = input().split()
n = int(x[0])
m = int(x[1])
edges = []
for _ in range(n - 1):
    xx = input().split()
    u = int(xx[0])
    v = int(xx[1])
    edges.append((u, v))

money = []
for _ in range(m):
    xxx = input().split()
    a = int(xxx[0])
    b = int(xxx[1])
    money.append((a, b))

graph = directed_build_adjacency_list(edges)

in_ = [-1] * (n + 1)
out = [-1] * (n + 1)
sub = []
timer = [0]
dfs(graph, 1, -1, in_, out, sub, timer)

diff = [0] * (n + 1)

for a, b in money:
    diff[in_[a]] += b
    if out[a] < n:
        diff[out[a]] -= b

final = [0] * n
current = 0
for i in range(n):
    current += diff[i]
    final[sub[i] - 1] = current
print(" ".join(str(i) for i in final))