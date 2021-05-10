"""
[builtin] Example-04 (~400 lines)
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
    

    # block 4
    t = (a * 4 - b) ^ ((a + b + 4) & 7)
    if t % 5 == 0:
        acc += t // (4 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (4 % 4 + 1)
        elif acc % 3 == 0:
            acc += (4 * a) // ((b or 1))
        else:
            for j in range(3):
                if (j + a + b + 4) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(2):
            if (w + t) % 2 == 0:
                acc += (w * t) % (4+3)
            else:
                acc -= (w + 4) // 2
    else:
        r = 0
        m = 4 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 5
    t = (a * 5 - b) ^ ((a + b + 5) & 7)
    if t % 5 == 0:
        acc += t // (5 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (5 % 4 + 1)
        elif acc % 3 == 0:
            acc += (5 * a) // ((b or 1))
        else:
            for j in range(4):
                if (j + a + b + 5) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(3):
            if (w + t) % 2 == 0:
                acc += (w * t) % (5+3)
            else:
                acc -= (w + 5) // 2
    else:
        r = 0
        m = 5 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 6
    t = (a * 6 - b) ^ ((a + b + 6) & 7)
    if t % 5 == 0:
        acc += t // (6 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (6 % 4 + 1)
        elif acc % 3 == 0:
            acc += (6 * a) // ((b or 1))
        else:
            for j in range(2):
                if (j + a + b + 6) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(4):
            if (w + t) % 2 == 0:
                acc += (w * t) % (6+3)
            else:
                acc -= (w + 6) // 2
    else:
        r = 0
        m = 6 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 7
    t = (a * 7 - b) ^ ((a + b + 7) & 7)
    if t % 5 == 0:
        acc += t // (7 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (7 % 4 + 1)
        elif acc % 3 == 0:
            acc += (7 * a) // ((b or 1))
        else:
            for j in range(3):
                if (j + a + b + 7) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(5):
            if (w + t) % 2 == 0:
                acc += (w * t) % (7+3)
            else:
                acc -= (w + 7) // 2
    else:
        r = 0
        m = 7 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 8
    t = (a * 8 - b) ^ ((a + b + 8) & 7)
    if t % 5 == 0:
        acc += t // (8 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (8 % 4 + 1)
        elif acc % 3 == 0:
            acc += (8 * a) // ((b or 1))
        else:
            for j in range(4):
                if (j + a + b + 8) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(2):
            if (w + t) % 2 == 0:
                acc += (w * t) % (8+3)
            else:
                acc -= (w + 8) // 2
    else:
        r = 0
        m = 8 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 9
    t = (a * 9 - b) ^ ((a + b + 9) & 7)
    if t % 5 == 0:
        acc += t // (9 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (9 % 4 + 1)
        elif acc % 3 == 0:
            acc += (9 * a) // ((b or 1))
        else:
            for j in range(2):
                if (j + a + b + 9) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(3):
            if (w + t) % 2 == 0:
                acc += (w * t) % (9+3)
            else:
                acc -= (w + 9) // 2
    else:
        r = 0
        m = 9 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 10
    t = (a * 10 - b) ^ ((a + b + 10) & 7)
    if t % 5 == 0:
        acc += t // (10 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (10 % 4 + 1)
        elif acc % 3 == 0:
            acc += (10 * a) // ((b or 1))
        else:
            for j in range(3):
                if (j + a + b + 10) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(4):
            if (w + t) % 2 == 0:
                acc += (w * t) % (10+3)
            else:
                acc -= (w + 10) // 2
    else:
        r = 0
        m = 10 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 11
    t = (a * 11 - b) ^ ((a + b + 11) & 7)
    if t % 5 == 0:
        acc += t // (11 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (11 % 4 + 1)
        elif acc % 3 == 0:
            acc += (11 * a) // ((b or 1))
        else:
            for j in range(4):
                if (j + a + b + 11) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(5):
            if (w + t) % 2 == 0:
                acc += (w * t) % (11+3)
            else:
                acc -= (w + 11) // 2
    else:
        r = 0
        m = 11 % 4 + 3
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
