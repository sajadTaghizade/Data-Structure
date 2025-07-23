inputs = []
while True:
    user_input = input()
    if user_input == "6":
        break
    inputs.append(user_input.strip())

listt = []

def one_inp():
    global listt
    listt = []

def two_inp():
    global listt
    listt = None

def three_inp(m):
    global listt
    try:
        if listt is not None:
            listt.append(int(m))
        else:
            print("nulle")
    except ValueError:
        print("nulle")

def four_inp(n):
    global listt
    try:
        if listt is not None:
            print(listt[int(n)])
        else:
            print("nulle")
    except IndexError:
        print("oute")
    except ValueError:
        print("nulle")

def five_inp(m, n):
    try:
        print(int(m) // int(n))
    except ZeroDivisionError:
        print("sefre")
    except ValueError:
        print("nulle")

for inp in inputs:
    if inp.startswith("1"):
        one_inp()
    elif inp.startswith("2"):
        two_inp()
    elif inp.startswith("3"):
        three_inp(inp[2:].strip())
    elif inp.startswith("4"):
        four_inp(inp[2:].strip())
    elif inp.startswith("5"):
        m, n = inp[2:].split()
        five_inp(m.strip(), n.strip())
    elif inp.startswith("6"):
        break
