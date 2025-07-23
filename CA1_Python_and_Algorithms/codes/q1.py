def extract_number(S):
    S = S.lstrip()
    
    if len(S) == 0:
        return 0

    sign = 1
    start = 0
    
    if S[0] == '-':
        sign = -1
        start = 1
    elif S[0] == '+':
        start = 1

    num_str = ""
    
    for i in range(start, len(S)):
        if S[i].isdigit():
            num_str += S[i]
        else:
            break

    if num_str == "":
        return 0

    number = sign * int(num_str)
    min_num = -2**31
    max_num = 2**31 - 1
    if number < min_num:
        return min_num
    if number > max_num:
        return max_num

    return number

x=input()
x=x[1:len(x)-1]
print(extract_number(x))
