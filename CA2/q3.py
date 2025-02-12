def counter(n, arr):
    move = []
    for s, e in arr:
        move += [(s, 1), (e + 1, -1)]
    move = sorted(move)
    result = [0] * (n + 1)
    prev = 0
    curr = 0
    for i in range(len(move)):
        x, y = move[i]
        if curr > 0 and i > 0:
            result[curr] += x - prev
        curr += y
        prev = x
    print(*result[1:n + 1])



n = int(input())
myset = []

i = 0
while i < n:
    line = input().split()
    start = int(line[0])
    end = int(line[1])
    myset.append((start, end))
    i += 1

counter(n, myset)