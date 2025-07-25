sobrinhos = list(map(int, input().split()))
hugo = sobrinhos[0]
ze = sobrinhos[1]
luis = sobrinhos[2]

if hugo<ze and ze<luis:
    print('zezinho')
elif hugo > ze and ze < luis:
    print('luisinho')
else:
    if hugo <ze and ze >  luis:
        print('huguinho')