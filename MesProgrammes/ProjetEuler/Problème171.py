import math, itertools
def calcul():
  LENGTH = 20
  BASE = 10
  MOD = 10**9

  # Maximum possible somme des carrés (pour 99...99)
  MAX_SQR_DIGIT_SUM = (BASE - 1)**2 * LENGTH

 
  sqsum = []                  # sqsum[n][s] la somme des nombres à n caractèrs avec s pour somme de ses chiffres, mod MOD
  count = []                  # count[n][s] le nombre de nombres à n caractèrs avec s pour somme de ses chiffres, mod MOD

  for i in range(LENGTH + 1):
    sqsum.append([0] * (MAX_SQR_DIGIT_SUM + 1))
    count.append([0] * (MAX_SQR_DIGIT_SUM + 1))
    if i == 0:
      count[0][0] = 1
    else:
      for j in range(BASE):
        for k in itertools.count():
          index = k + j**2
          if index > MAX_SQR_DIGIT_SUM:
            break
          sqsum[i][index] = (sqsum[i][index] + sqsum[i - 1][k] + pow(BASE, i - 1, MOD) * j * count[i - 1][k]) % MOD
          count[i][index] = (count[i][index] + count[i - 1][k]) % MOD

  ans = sum(sqsum[LENGTH][i**2] for i in range(1, math.isqrt(MAX_SQR_DIGIT_SUM)))
  return f"{ans%MOD:09}"


if __name__ == "__main__":
  print(calcul())