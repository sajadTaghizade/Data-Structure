
x = []
for i in range(9):
    a = input().replace('[', '').replace(']', '').replace('"', '').split(',')
    x.append(a)
for i in range(1,9):
    x[i]=x[i][1:]
    
def is_valid_group(group):
    check_list = []
    for i in group:
        if i != ".":
            if i in check_list:
                return False
            check_list.append(i)
    return True

def c_row(x): 
    for line in x:
        if not is_valid_group(line):
            return False
    return True

def c_col(x):
    for i in range(len(x[0])):
        col = [x[j][i] for j in range(len(x))] 
        if not is_valid_group(col):
            return False
    return True

def c_subgrid(x):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [x[m][n] for m in range(i, i + 3) for n in range(j, j + 3)]
            if not is_valid_group(subgrid):
                return False
    return True

def is_sudoku_valid(x):
    if c_row(x) and c_col(x) and c_subgrid(x):
        return "true"
    return "false"
print(is_sudoku_valid(x))
