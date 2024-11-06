
from time import perf_counter
import sys
import itertools as it
from collections import Counter

def p892_v3(N=10**7, mod=1234567891):
    facts = [1]*(N+1)
    for n in range(2, N+1):
        facts[n] = facts[n-1]*n%mod
    invfacts = [1]*(N+1)
    invfacts[N] = pow(facts[N], -1, mod)
    for n in range(N-1, 0, -1):
        invfacts[n] = invfacts[n+1]*(n+1)%mod
    answer = 0
    for n in range(2, N+1):
        D = 2*facts[n-1]*facts[n-1]%mod \
                * invfacts[(n+1)//2]%mod \
                * invfacts[n//2]%mod \
                * invfacts[(n-1)//2]%mod \
                * invfacts[(n-2)//2]%mod
        answer = (answer+D)%mod
        if Verbose: print(n, D, answer)
    return answer

#------------------------------------------------------------------------------

def p892_v2(N=10**7, mod=1234567891):
    invs = [1]*(N+1)
    for n in range(2, N+1):
        q, r = divmod(mod, n)
        invs[n] = (-q*invs[r])%mod
    answer = Dprev = 2
    for n in range(3, N+1):
        half = n>>1
        if n&1:
            D = 2*Dprev*(n-1)%mod*invs[half+1]%mod
        else:
            t = (n-1)*(n-1)%mod
            u = invs[half]*invs[half-1]%mod
            D = Dprev*t%mod*u%mod
        answer = (answer+D)%mod
        Dprev = D
        if Verbose: print(n, D, answer)
    return answer

#------------------------------------------------------------------------------

def p892(N=10**7, mod=1234567891):
    facts = [1]*(N+1)
    for n in range(2, N+1):
        facts[n] = facts[n-1]*n%mod
    invfacts = [1]*(N+1)
    invfacts[N] = pow(facts[N], -1, mod)
    for n in range(N-1, 0, -1):
        invfacts[n] = invfacts[n+1]*(n+1)%mod
    answer = 0
    for n in range(2, N+1):
        half = n>>1 #n/2**1 shoft right binary places by 2
        t = invfacts[half]
        tsq = t*t%mod
        if n&1:
            D = 2*facts[n-1]**2%mod*tsq%mod*invfacts[half-1]%mod*invfacts[half+1]%mod
        else:
            D = facts[n]*facts[n-1]%mod*tsq%mod*invfacts[half-1]%mod*t%mod
        answer = (answer+D)%mod
        if Verbose: print(n, D, answer)
    return answer

#------------------------------------------------------------------------------

def p892_bruteforce(N=100, mod=1234567891):
    dps = [{(1,0):1}]
    answer = 0
    for n in range(1, N+1):
        dp = Counter()
        for k in range(n):
            for (e1,o1), c1 in dps[k].items():
                for (e2,o2), c2 in dps[n-k-1].items():
                    dp[o1+e2,e1+o2] += c1*c2%mod
        dps.append(dp)
        D = 0
        for (e,o), count in dp.items():
            D += abs(e-o)*count%mod
        D %= mod
        answer = (answer+D)%mod
        if Verbose: print(f"{n} {len(dp)}: {D} {answer}")
        if Verbose > 1: print(sorted(dp.items()))
    return D, answer

#------------------------------------------------------------------------------

Verbose = 0
Extensions = set()
DoCounts = False
Counts = [0] * 100

if __name__ == "__main__":
    def main():
        global Verbose, Extensions, DoCounts, start_time
        entrypoint = p892
        while len(sys.argv) > 1 and sys.argv[1][0] == '-':
            opt = sys.argv[1].lower()
            if opt in ('-v', '-vv', '-vvv', '-vvvv'):
                Verbose += len(opt)-1
            elif opt in ('-x', '-x1'):
                Extensions.add(1)
            elif opt in ('-c', '-count', '-counts'):
                DoCounts = True
            elif opt in ('-b', '-brute', '-bruteforce'):
                entrypoint = p892_bruteforce
            elif opt in ('-v1',):
                entrypoint = p892
            elif opt in ('-v2',):
                entrypoint = p892_v2
            elif opt in ('-v3',):
                entrypoint = p892_v3
            elif opt in ('--',):
                sys.argv.pop(1)
                break
            else:
                print(f"Unknown option {sys.argv[1]}")
                sys.exit(1)
            sys.argv.pop(1)
        start_time = perf_counter()
        try:
            result = entrypoint(*map(int, sys.argv[1:]))
        except KeyboardInterrupt:
            result = None
            print("\nInterrupted")
        end_time = perf_counter()
        if DoCounts:
            while Counts and not Counts[-1]: Counts.pop()
            if Counts: print(Counts)
        if result is not None: print(result)
        print(f"Time: {end_time-start_time} secs")

    if len(sys.argv) > 1 and sys.argv[1] in ('-profile', '-prof'):
        import cProfile
        sys.argv.pop(1)
        cProfile.run('main()', sort='cumtime')
    else:
        main()