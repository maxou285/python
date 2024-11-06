
S0, S1, S2, S3, S4, D0, D1, D2, D3, D4 = range(10)

cache = {}
def explore(max_steps, current_direction, positions, step_count=0):
    if step_count > max_steps:
        return 0
    k = tuple(positions) + (step_count, current_direction)
    try:
        return cache[k]
    except:
        tot = 0
        if step_count == max_steps:
            if (positions[S0] == positions[S1] == positions[S2] == positions[S3] == positions[S4] and
                positions[D0] == positions[D1] == positions[D2] == positions[D3] == positions[D4]):
                tot = 1
        else:
            if (max(positions[:5]) * 5 - sum(positions[:5]) +
                max(positions[5:]) * 5 - sum(positions[5:]) + step_count) <= max_steps:
                if current_direction > 4:
                    next2 = (current_direction - 4) % 5 + 5
                else:
                    next2 = (current_direction + 1) % 5
                for next in (9 - current_direction, next2):
                    positions[next] += 1
                    tot += explore(max_steps, next, positions, step_count + 1)
                    positions[next] -= 1
        cache[k] = tot
        return tot

print(explore(70, S4, [0]*10))