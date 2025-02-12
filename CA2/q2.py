ts = int(input().strip())
for t in range(ts):
    asbs = []
    while True:
        n = int(input().strip())  
        if n == 0:
            break  
        elif n > 0:
            asbs.append(n)  
        elif n < 0:
            asbs.sort()
            if len(asbs) % 2 == 0:
                asb_vasati = (len(asbs) // 2) - 1
            else:
                asb_vasati = len(asbs) // 2

            vasati = asbs.pop(asb_vasati) 
            print(vasati)
