from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def dfs(node, adj, vis, nodes, values, node_vals, group):
    stack = [node]
    vis[node] = True
    while stack:
        cur = stack.pop()
        nodes.append((cur, group))
        values.append((node_vals[cur], group))
        for nei in adj[cur]:
            if not vis[nei]:
                vis[nei] = True
                stack.append(nei)


x = input().split()
n = int(x[0])
m = int(x[1])
vals = [0] + list(map(int, input().split()))  

adj = defaultdict(list)
vis = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

isolated = 0
group = 0
nodes, values = [], []

for i in range(1, n + 1):
    if vals[i] == i and not adj[i]:
        isolated += 1
    if not vis[i] and adj[i]:
        group += 1
        dfs(i, adj, vis, nodes, values, vals, group)

node_count, val_count, node_group, val_group = defaultdict(int), defaultdict(int), {}, {}

for node, g in nodes:
    node_count[node] += 1
    node_group[node] = g
for val, g in values:
    val_count[val] += 1
    val_group[val] = g

M = sum(1 for i in range(1, n + 1) if node_count[i] == val_count[i] and node_count[i] and node_group.get(i) == val_group.get(i))

print(M + isolated)
