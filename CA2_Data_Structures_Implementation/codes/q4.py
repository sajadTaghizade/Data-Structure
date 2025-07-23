num_list = list(map(int, input().strip("[]").split(",")))
k = int(input().strip())

left_max = [0] * len(num_list)
right_max = [0] * len(num_list)

for i in range(len(num_list)):
    if i % k == 0:
        left_max[i] = num_list[i]  
    else:
        left_max[i] = max(left_max[i - 1], num_list[i])

for i in range(len(num_list) - 1, -1, -1):
    if i == len(num_list) - 1 or (i + 1) % k == 0:
        right_max[i] = num_list[i] 
    else:
        right_max[i] = max(right_max[i + 1], num_list[i])

max_all = []
for i in range(len(num_list) - k + 1):
    max_all.append(max(right_max[i], left_max[i + k - 1]))


print("[" + ",".join(map(str, max_all)) + "]")
