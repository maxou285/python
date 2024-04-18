nbr_max = 200
manners = [1] + [0]*nbr_max
coins = [1,2,5,10,20,50,100,200]

for coin in coins:
    for i in range(coin,len(manners)):
        manners[i] += manners[i-coin]

print(manners[-1])