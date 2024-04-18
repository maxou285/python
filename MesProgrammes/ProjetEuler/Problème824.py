### Calcul du nombre total de placements des sliders sans forcément respecter les conditions
#N = 10**9
#K = 10**15

#print((K/2*N)**(N**2))

from tqdm import *              # Progress bar 
from functools import cache
from tqdm import trange         # Progress bar


def product(arr, md=None):
    res = 1
    for r in arr:
        res = res * r
        if md:
            res = res % md
    return res

@cache
def naive_fact(n, p, q):
    # computes n! % p^q
    if n == 0:
        return 1
    return n * naive_fact(n - 1, p, q) % p ** q


@cache
def naive_fact_p(n, p, q):
    # special case of fact_p
    # computes (n!)_p % p^q
    # print("[2] Size:", n)
    if n == 0:
        return 1
    if n % p == 0:
        return naive_fact_p(n - 1, p, q)
    return n * naive_fact_p(n - 1, p, q) % p ** q

# Page d'Andrew Granville
# https://ericrowland.github.io/papers/Lucas%27_theorem_modulo_p%5E2.pdf
def special_fact_p(n, p, q):
    # computes (np!)_p % p^q, Theorem 2
    md = p ** q
    r = q // 2
    
    res = 1
    for j in range(1, r + 1):
        beta_j = n * product([n ** 2 - i ** 2 for i in range(1, r + 1) if i != j])
        beta_j = beta_j // (j * product([j ** 2 - i ** 2 for i in range(1, r + 1) if i != j]))
        res = res * pow(naive_fact_p(j * p, p, q), beta_j, md) % md
    return res


def naive_special_binom(u, v, p, q):
    # special case of special_binom for when u is small
    # computes fact_p(up + v) / fact_p(up) / fact_p(v) % p^q
    md = p ** q
    res = naive_fact_p(u * p + v, p, q)
    res = res * pow(naive_fact_p(v, p, q), -1, md) % md
    res = res * pow(naive_fact_p(u * p, p, q), -1, md) % md
    return res


def special_binom(u, v, p, q):
    # computes fact_p(up + v) / fact_p(up) / fact_p(v) % p^q, Theorem 3
    assert 0 <= v < p
    md = p ** q
    _md = md // p
    res = 1
    for j in range(1, q):
        # naive
        alpha_j = u * product([u - i for i in range(1, q) if i != j])
        alpha_j = alpha_j // (j * product([j - i for i in range(1, q) if i != j]))
        res = res * pow(naive_special_binom(j, v, p, q), alpha_j, md) % md
    return res


def fact_p(n, p, q):
    # computes product of x <= n not divisible by p
    md = p ** q
    u, v = divmod(n, p)
    res = naive_fact(v, p, q) % md
    res = res * special_fact_p(u, p, q) % md
    res = res * special_binom(u, v, p, q) % md
    # res = res * naive_special_binom(u, v, p, q) % md
    return res


def compute_binom(n, m, p, q):
    # binomial(n, m) % p^q
    if m == 0:
        return 1
    
    r = n - m
    md = p ** q
    d = 0
    while p ** (d + 1) < n:
        d += 1
    
    Nj = [(n // p ** j) % md for j in range(d + 1)]
    Mj = [(m // p ** j) % md for j in range(d + 1)]
    Rj = [(r // p ** j) % md for j in range(d + 1)]
    nj = [(n // p ** j) % p for j in range(d + 1)]
    mj = [(m // p ** j) % p for j in range(d + 1)]
    rj = [(r // p ** j) % p for j in range(d + 1)]
    
    if m > r:
        ej = [int(nj[j] < mj[j]) for j in range(d + 1)]
    else:
        ej = [int(nj[j] < rj[j]) for j in range(d + 1)]

    for j in range(d - 1, -1, -1):
        ej[j] += ej[j + 1]

    res = 1
    for j in range(d + 1):
        res = res * fact_p(Nj[j], p, q) % md
        res = res * pow(fact_p(Mj[j], p, q), -1, md) % md
        res = res * pow(fact_p(Rj[j], p, q), -1, md) % md

    if len(ej) >= q and ej[q - 1] % 2 == 1:
        res = -res % md

    res = res * pow(p, ej[0], md) % md

    return res

p = 10 ** 7 + 19
q = 2
md = p ** q
n = 10 ** 9
k = 10 ** 15

# precompute cache
for i in trange(2 * p):
    tmp = naive_fact(i, p, q)
    tmp = naive_fact_p(i, p, q)

# https://www.kotesovec.cz/books/kotesovec_non_attacking_chess_pieces_2013_6ed.pdf p.408
s = 0
special_cases = []
for c in trange(k // n + 1):
    # shouldn't happen anyways
    if (n ** 2 - c * n - k) % p == 0:
        print("non-invertible... n = {n}, c = {c}, k = {k}")
        special_cases.append(c)
        continue

    r1 = (-1) ** (c * n)
    r2 = (n ** 2 - 2 * c * n) % md
    r3 = pow(n ** 2 - c * n - k, -1, md)
    r4 = compute_binom(n, c, p, q)
    r5 = compute_binom(n ** 2 - c * n - k, k - c * n, p, q)
    r = r1 * r2 * r3 * r4 * r5 % md
    s = (s + r) % md
print(s)


"""
def f(n, k): 
    factorials = [1]
    harmonics = [0]
    for i in range(1, p): 
        factorials.append(factorials[-1]*i%mod)
        harmonics.append((harmonics[-1]+pow(i, -1, p))%p)
    def factorialmod(n): 
        if(n==0): 
            return 1
        return (factorialmod(n//p)*(factorials[n%p]+factorials[n%p]*p*harmonics[n%p]*(n//p))*pow(factorials[p-1], n//p, mod))%mod
    def vp(n): 
        if(n<p): 
            return 0
        return n//p+vp(n//p)
    counter = 0
    nci = 1
    for i in range(k//n+1): 
        e = vp((n*n-i*n-k))-vp(k-i*n)-vp(n*n-2*k)
        if(e<=1): 
            counter+=nci*pow(p, e, mod)*factorialmod(n*n-i*n-k)*pow(factorialmod(k-i*n)*factorialmod(n*n-2*k), -1, mod)*(1+(k-i*n)*pow(n*n-i*n-k, -1, mod))
            counter%=mod
        nci = (nci*(n-i)*pow(i+1, -1, mod))%mod
    return counter
print(f(10**9, 10**15))"""