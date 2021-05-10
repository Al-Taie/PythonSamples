"""
[builtin] Example-07 (~1000 lines)
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
    

    # block 12
    t = (a * 12 - b) ^ ((a + b + 12) & 7)
    if t % 5 == 0:
        acc += t // (12 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (12 % 4 + 1)
        elif acc % 3 == 0:
            acc += (12 * a) // ((b or 1))
        else:
            for j in range(2):
                if (j + a + b + 12) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(2):
            if (w + t) % 2 == 0:
                acc += (w * t) % (12+3)
            else:
                acc -= (w + 12) // 2
    else:
        r = 0
        m = 12 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 13
    t = (a * 13 - b) ^ ((a + b + 13) & 7)
    if t % 5 == 0:
        acc += t // (13 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (13 % 4 + 1)
        elif acc % 3 == 0:
            acc += (13 * a) // ((b or 1))
        else:
            for j in range(3):
                if (j + a + b + 13) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(3):
            if (w + t) % 2 == 0:
                acc += (w * t) % (13+3)
            else:
                acc -= (w + 13) // 2
    else:
        r = 0
        m = 13 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 14
    t = (a * 14 - b) ^ ((a + b + 14) & 7)
    if t % 5 == 0:
        acc += t // (14 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (14 % 4 + 1)
        elif acc % 3 == 0:
            acc += (14 * a) // ((b or 1))
        else:
            for j in range(4):
                if (j + a + b + 14) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(4):
            if (w + t) % 2 == 0:
                acc += (w * t) % (14+3)
            else:
                acc -= (w + 14) // 2
    else:
        r = 0
        m = 14 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 15
    t = (a * 15 - b) ^ ((a + b + 15) & 7)
    if t % 5 == 0:
        acc += t // (15 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (15 % 4 + 1)
        elif acc % 3 == 0:
            acc += (15 * a) // ((b or 1))
        else:
            for j in range(2):
                if (j + a + b + 15) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(5):
            if (w + t) % 2 == 0:
                acc += (w * t) % (15+3)
            else:
                acc -= (w + 15) // 2
    else:
        r = 0
        m = 15 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 16
    t = (a * 16 - b) ^ ((a + b + 16) & 7)
    if t % 5 == 0:
        acc += t // (16 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (16 % 4 + 1)
        elif acc % 3 == 0:
            acc += (16 * a) // ((b or 1))
        else:
            for j in range(3):
                if (j + a + b + 16) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(2):
            if (w + t) % 2 == 0:
                acc += (w * t) % (16+3)
            else:
                acc -= (w + 16) // 2
    else:
        r = 0
        m = 16 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 17
    t = (a * 17 - b) ^ ((a + b + 17) & 7)
    if t % 5 == 0:
        acc += t // (17 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (17 % 4 + 1)
        elif acc % 3 == 0:
            acc += (17 * a) // ((b or 1))
        else:
            for j in range(4):
                if (j + a + b + 17) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(3):
            if (w + t) % 2 == 0:
                acc += (w * t) % (17+3)
            else:
                acc -= (w + 17) // 2
    else:
        r = 0
        m = 17 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 18
    t = (a * 18 - b) ^ ((a + b + 18) & 7)
    if t % 5 == 0:
        acc += t // (18 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (18 % 4 + 1)
        elif acc % 3 == 0:
            acc += (18 * a) // ((b or 1))
        else:
            for j in range(2):
                if (j + a + b + 18) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(4):
            if (w + t) % 2 == 0:
                acc += (w * t) % (18+3)
            else:
                acc -= (w + 18) // 2
    else:
        r = 0
        m = 18 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 19
    t = (a * 19 - b) ^ ((a + b + 19) & 7)
    if t % 5 == 0:
        acc += t // (19 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (19 % 4 + 1)
        elif acc % 3 == 0:
            acc += (19 * a) // ((b or 1))
        else:
            for j in range(3):
                if (j + a + b + 19) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(5):
            if (w + t) % 2 == 0:
                acc += (w * t) % (19+3)
            else:
                acc -= (w + 19) // 2
    else:
        r = 0
        m = 19 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 20
    t = (a * 20 - b) ^ ((a + b + 20) & 7)
    if t % 5 == 0:
        acc += t // (20 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (20 % 4 + 1)
        elif acc % 3 == 0:
            acc += (20 * a) // ((b or 1))
        else:
            for j in range(4):
                if (j + a + b + 20) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(2):
            if (w + t) % 2 == 0:
                acc += (w * t) % (20+3)
            else:
                acc -= (w + 20) // 2
    else:
        r = 0
        m = 20 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 21
    t = (a * 21 - b) ^ ((a + b + 21) & 7)
    if t % 5 == 0:
        acc += t // (21 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (21 % 4 + 1)
        elif acc % 3 == 0:
            acc += (21 * a) // ((b or 1))
        else:
            for j in range(2):
                if (j + a + b + 21) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(3):
            if (w + t) % 2 == 0:
                acc += (w * t) % (21+3)
            else:
                acc -= (w + 21) // 2
    else:
        r = 0
        m = 21 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 22
    t = (a * 22 - b) ^ ((a + b + 22) & 7)
    if t % 5 == 0:
        acc += t // (22 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (22 % 4 + 1)
        elif acc % 3 == 0:
            acc += (22 * a) // ((b or 1))
        else:
            for j in range(3):
                if (j + a + b + 22) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(4):
            if (w + t) % 2 == 0:
                acc += (w * t) % (22+3)
            else:
                acc -= (w + 22) // 2
    else:
        r = 0
        m = 22 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 23
    t = (a * 23 - b) ^ ((a + b + 23) & 7)
    if t % 5 == 0:
        acc += t // (23 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (23 % 4 + 1)
        elif acc % 3 == 0:
            acc += (23 * a) // ((b or 1))
        else:
            for j in range(4):
                if (j + a + b + 23) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(5):
            if (w + t) % 2 == 0:
                acc += (w * t) % (23+3)
            else:
                acc -= (w + 23) // 2
    else:
        r = 0
        m = 23 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 24
    t = (a * 24 - b) ^ ((a + b + 24) & 7)
    if t % 5 == 0:
        acc += t // (24 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (24 % 4 + 1)
        elif acc % 3 == 0:
            acc += (24 * a) // ((b or 1))
        else:
            for j in range(2):
                if (j + a + b + 24) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(2):
            if (w + t) % 2 == 0:
                acc += (w * t) % (24+3)
            else:
                acc -= (w + 24) // 2
    else:
        r = 0
        m = 24 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 25
    t = (a * 25 - b) ^ ((a + b + 25) & 7)
    if t % 5 == 0:
        acc += t // (25 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (25 % 4 + 1)
        elif acc % 3 == 0:
            acc += (25 * a) // ((b or 1))
        else:
            for j in range(3):
                if (j + a + b + 25) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(3):
            if (w + t) % 2 == 0:
                acc += (w * t) % (25+3)
            else:
                acc -= (w + 25) // 2
    else:
        r = 0
        m = 25 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 26
    t = (a * 26 - b) ^ ((a + b + 26) & 7)
    if t % 5 == 0:
        acc += t // (26 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (26 % 4 + 1)
        elif acc % 3 == 0:
            acc += (26 * a) // ((b or 1))
        else:
            for j in range(4):
                if (j + a + b + 26) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(4):
            if (w + t) % 2 == 0:
                acc += (w * t) % (26+3)
            else:
                acc -= (w + 26) // 2
    else:
        r = 0
        m = 26 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 27
    t = (a * 27 - b) ^ ((a + b + 27) & 7)
    if t % 5 == 0:
        acc += t // (27 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (27 % 4 + 1)
        elif acc % 3 == 0:
            acc += (27 * a) // ((b or 1))
        else:
            for j in range(2):
                if (j + a + b + 27) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(5):
            if (w + t) % 2 == 0:
                acc += (w * t) % (27+3)
            else:
                acc -= (w + 27) // 2
    else:
        r = 0
        m = 27 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 28
    t = (a * 28 - b) ^ ((a + b + 28) & 7)
    if t % 5 == 0:
        acc += t // (28 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (28 % 4 + 1)
        elif acc % 3 == 0:
            acc += (28 * a) // ((b or 1))
        else:
            for j in range(3):
                if (j + a + b + 28) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(2):
            if (w + t) % 2 == 0:
                acc += (w * t) % (28+3)
            else:
                acc -= (w + 28) // 2
    else:
        r = 0
        m = 28 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 29
    t = (a * 29 - b) ^ ((a + b + 29) & 7)
    if t % 5 == 0:
        acc += t // (29 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (29 % 4 + 1)
        elif acc % 3 == 0:
            acc += (29 * a) // ((b or 1))
        else:
            for j in range(4):
                if (j + a + b + 29) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(3):
            if (w + t) % 2 == 0:
                acc += (w * t) % (29+3)
            else:
                acc -= (w + 29) // 2
    else:
        r = 0
        m = 29 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 30
    t = (a * 30 - b) ^ ((a + b + 30) & 7)
    if t % 5 == 0:
        acc += t // (30 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (30 % 4 + 1)
        elif acc % 3 == 0:
            acc += (30 * a) // ((b or 1))
        else:
            for j in range(2):
                if (j + a + b + 30) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(4):
            if (w + t) % 2 == 0:
                acc += (w * t) % (30+3)
            else:
                acc -= (w + 30) // 2
    else:
        r = 0
        m = 30 % 4 + 3
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
