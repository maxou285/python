# FICHIERS TEXTE EXERICE
# "Ecrire des nombres"

# nombres.txt
# 1
# 2
# 3
# 4
# for
# 10 lignes

f = open("nombres.txt", "w")

for i in range(1,11):
    f.write(str(i)+"\n")


f.close()