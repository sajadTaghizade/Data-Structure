input_str = input().strip()
a = input_str.split('], ')
nums_list = a[0][1:].split(',')
x = int(a[1].split('=')[1].strip())

pre_final = []

for i in range(0, len(nums_list), x):
    group = nums_list[i:i + x]
    if len(group) == x:
        pre_final.extend(reversed(group))
    else:
        pre_final.extend(group)

print('[' + ','.join(pre_final) + ']')
