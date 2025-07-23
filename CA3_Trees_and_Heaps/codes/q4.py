n = int(input()) 
text = input().split() 

def kmp(s):
    n = len(s)
    f = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = f[j - 1]
        if s[i] == s[j]:
            j += 1
        f[i] = j
    return f

def merge(text):
    ans = text[0]
    for i in range(1, len(text)):
        curr = text[i]
        mix = curr + "#" + ans[-len(curr):]
        f = kmp(mix)
        length = f[-1]
        ans += curr[length:]
    return ans

ans = merge(text)
print(ans)
