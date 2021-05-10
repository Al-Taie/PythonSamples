"""
[builtin] Example-01 (~120 lines)
Auto-generated program with branching and loops to exercise CFG/path exploration.
Single large entry(a, b) function builds a rich CFG and many feasible paths.
"""

def helper1(a,b):
    return (a*a - b) if (a ^ b) & 1 else (a + b)

def helper2(a,b):
    return (a|b) - (a&b)
    
def entry(a, b):
    acc = 0

    # block 0
    t = (a * 0 - b) ^ ((a + b + 0) & 7)
    if t % 5 == 0:
        acc += t // (0 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (0 % 4 + 1)
        elif acc % 3 == 0:
            acc += (0 * a) // ((b or 1))
        else:
            for j in range(2):
                if (j + a + b + 0) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(2):
            if (w + t) % 2 == 0:
                acc += (w * t) % (0+3)
            else:
                acc -= (w + 0) // 2
    else:
        r = 0
        m = 0 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 1
    t = (a * 1 - b) ^ ((a + b + 1) & 7)
    if t % 5 == 0:
        acc += t // (1 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (1 % 4 + 1)
        elif acc % 3 == 0:
            acc += (1 * a) // ((b or 1))
        else:
            for j in range(3):
                if (j + a + b + 1) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(3):
            if (w + t) % 2 == 0:
                acc += (w * t) % (1+3)
            else:
                acc -= (w + 1) // 2
    else:
        r = 0
        m = 1 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 2
    t = (a * 2 - b) ^ ((a + b + 2) & 7)
    if t % 5 == 0:
        acc += t // (2 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (2 % 4 + 1)
        elif acc % 3 == 0:
            acc += (2 * a) // ((b or 1))
        else:
            for j in range(4):
                if (j + a + b + 2) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(4):
            if (w + t) % 2 == 0:
                acc += (w * t) % (2+3)
            else:
                acc -= (w + 2) // 2
    else:
        r = 0
        m = 2 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 3
    t = (a * 3 - b) ^ ((a + b + 3) & 7)
    if t % 5 == 0:
        acc += t // (3 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (3 % 4 + 1)
        elif acc % 3 == 0:
            acc += (3 * a) // ((b or 1))
        else:
            for j in range(2):
                if (j + a + b + 3) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(5):
            if (w + t) % 2 == 0:
                acc += (w * t) % (3+3)
            else:
                acc -= (w + 3) // 2
    else:
        r = 0
        m = 3 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # tail
    if acc > 0:
        return acc - (a % 5)
    elif acc < 0:
        return acc + (b % 7)
    return acc
