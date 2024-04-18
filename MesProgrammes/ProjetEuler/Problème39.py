pythperims = [2 * i * (i+1) for i in range(2,25)]
div_c = []
for idx, perim in enumerate(pythperims):
    subcount = 1
    for subper in pythperims[:idx]:
        subcount += 1 if perim % subper == 0 else 0
    div_c.append(subcount)

perlist2 = [(pyth, div_c[idx]) for idx, pyth in enumerate(pythperims)]
print(sorted(perlist2, key = lambda x: x[1], reverse = True))       # Take the first one