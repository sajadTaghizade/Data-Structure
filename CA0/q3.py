
x = input()
x = eval(x)

def move_ross(x):
    result = []
    
    top, bottom, left, right = 0, len(x) - 1, 0, len(x[0]) - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(x[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(x[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(x[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(x[i][left])
            left += 1

    return result

print(move_ross(x))