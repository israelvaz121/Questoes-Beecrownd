a = int(input())
if a > 2 and a <= 100000 :
    b = list(map(int,input().split()))
    d = b.count(2)
    if len(b) % 2 == 0 :
        print("0")
        if d % 2 == 0 :
            print("0")
        elif d % 2 == 1 :
            print("1")
    elif len(b) % 2 >= 1 :
        print("1")
        if d % 2 == 0 :
            print("0")
        elif d % 2 == 1 :
            print("1")