def convert_n_to_m(n, m):
    days = 0
    while m > n:
        if m % 2 == 0:  
            m //= 2
        else:  
            m += 1
        days += 1
    days += n - m
    return days

x=input().split()
n = int(x[0])
m = int(x[1])
result = convert_n_to_m(n, m)
print(result)
