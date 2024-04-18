# On check à chaque fois si la condition est satisfaite ( pour chaque carré )
import itertools

l1 = [0,1,2,3,4,5,6,7,8,9]
c1 = itertools.combinations(l1, 6)

square_cubes = 0
for a in c1:
    c2 = itertools.combinations(l1, 6)
    for b in c2:
        # 01
        if (0 in a and 1 in b) or (0 in b and 1 in a):
            # 04
            if (0 in a and 4 in b) or (0 in b and 4 in a):
                # 09
                if (0 in a and (6 in b or 9 in b)) or (0 in b and (6 in a or 9 in a)):
                    # 16
                    if (1 in a and (6 in b or 9 in b)) or (1 in b and (6 in a or 9 in a)):
                        # 25
                        if (2 in a and 5 in b) or (2 in b and 5 in a):
                            # 36
                            if (3 in a and (6 in b or 9 in b)) or (3 in b and (6 in a or 9 in a)):
                                # 49 and 64
                                if (4 in a and (6 in b or 9 in b)) or (4 in b and (6 in a or 9 in a)):
                                    # 81
                                    if (8 in a and 1 in b) or (8 in b and 1 in a):
                                        square_cubes += 1
    

print(square_cubes / 2)         # Le double comptage