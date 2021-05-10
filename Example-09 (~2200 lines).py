"""
[builtin] Example-09 (~2200 lines)
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
    

    # block 31
    t = (a * 31 - b) ^ ((a + b + 31) & 7)
    if t % 5 == 0:
        acc += t // (31 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (31 % 4 + 1)
        elif acc % 3 == 0:
            acc += (31 * a) // ((b or 1))
        else:
            for j in range(3):
                if (j + a + b + 31) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(5):
            if (w + t) % 2 == 0:
                acc += (w * t) % (31+3)
            else:
                acc -= (w + 31) // 2
    else:
        r = 0
        m = 31 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 32
    t = (a * 32 - b) ^ ((a + b + 32) & 7)
    if t % 5 == 0:
        acc += t // (32 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (32 % 4 + 1)
        elif acc % 3 == 0:
            acc += (32 * a) // ((b or 1))
        else:
            for j in range(4):
                if (j + a + b + 32) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(2):
            if (w + t) % 2 == 0:
                acc += (w * t) % (32+3)
            else:
                acc -= (w + 32) // 2
    else:
        r = 0
        m = 32 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 33
    t = (a * 33 - b) ^ ((a + b + 33) & 7)
    if t % 5 == 0:
        acc += t // (33 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (33 % 4 + 1)
        elif acc % 3 == 0:
            acc += (33 * a) // ((b or 1))
        else:
            for j in range(2):
                if (j + a + b + 33) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(3):
            if (w + t) % 2 == 0:
                acc += (w * t) % (33+3)
            else:
                acc -= (w + 33) // 2
    else:
        r = 0
        m = 33 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 34
    t = (a * 34 - b) ^ ((a + b + 34) & 7)
    if t % 5 == 0:
        acc += t // (34 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (34 % 4 + 1)
        elif acc % 3 == 0:
            acc += (34 * a) // ((b or 1))
        else:
            for j in range(3):
                if (j + a + b + 34) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(4):
            if (w + t) % 2 == 0:
                acc += (w * t) % (34+3)
            else:
                acc -= (w + 34) // 2
    else:
        r = 0
        m = 34 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 35
    t = (a * 35 - b) ^ ((a + b + 35) & 7)
    if t % 5 == 0:
        acc += t // (35 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (35 % 4 + 1)
        elif acc % 3 == 0:
            acc += (35 * a) // ((b or 1))
        else:
            for j in range(4):
                if (j + a + b + 35) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(5):
            if (w + t) % 2 == 0:
                acc += (w * t) % (35+3)
            else:
                acc -= (w + 35) // 2
    else:
        r = 0
        m = 35 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 36
    t = (a * 36 - b) ^ ((a + b + 36) & 7)
    if t % 5 == 0:
        acc += t // (36 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (36 % 4 + 1)
        elif acc % 3 == 0:
            acc += (36 * a) // ((b or 1))
        else:
            for j in range(2):
                if (j + a + b + 36) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(2):
            if (w + t) % 2 == 0:
                acc += (w * t) % (36+3)
            else:
                acc -= (w + 36) // 2
    else:
        r = 0
        m = 36 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 37
    t = (a * 37 - b) ^ ((a + b + 37) & 7)
    if t % 5 == 0:
        acc += t // (37 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (37 % 4 + 1)
        elif acc % 3 == 0:
            acc += (37 * a) // ((b or 1))
        else:
            for j in range(3):
                if (j + a + b + 37) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(3):
            if (w + t) % 2 == 0:
                acc += (w * t) % (37+3)
            else:
                acc -= (w + 37) // 2
    else:
        r = 0
        m = 37 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 38
    t = (a * 38 - b) ^ ((a + b + 38) & 7)
    if t % 5 == 0:
        acc += t // (38 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (38 % 4 + 1)
        elif acc % 3 == 0:
            acc += (38 * a) // ((b or 1))
        else:
            for j in range(4):
                if (j + a + b + 38) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(4):
            if (w + t) % 2 == 0:
                acc += (w * t) % (38+3)
            else:
                acc -= (w + 38) // 2
    else:
        r = 0
        m = 38 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 39
    t = (a * 39 - b) ^ ((a + b + 39) & 7)
    if t % 5 == 0:
        acc += t // (39 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (39 % 4 + 1)
        elif acc % 3 == 0:
            acc += (39 * a) // ((b or 1))
        else:
            for j in range(2):
                if (j + a + b + 39) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(5):
            if (w + t) % 2 == 0:
                acc += (w * t) % (39+3)
            else:
                acc -= (w + 39) // 2
    else:
        r = 0
        m = 39 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 40
    t = (a * 40 - b) ^ ((a + b + 40) & 7)
    if t % 5 == 0:
        acc += t // (40 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (40 % 4 + 1)
        elif acc % 3 == 0:
            acc += (40 * a) // ((b or 1))
        else:
            for j in range(3):
                if (j + a + b + 40) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(2):
            if (w + t) % 2 == 0:
                acc += (w * t) % (40+3)
            else:
                acc -= (w + 40) // 2
    else:
        r = 0
        m = 40 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 41
    t = (a * 41 - b) ^ ((a + b + 41) & 7)
    if t % 5 == 0:
        acc += t // (41 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (41 % 4 + 1)
        elif acc % 3 == 0:
            acc += (41 * a) // ((b or 1))
        else:
            for j in range(4):
                if (j + a + b + 41) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(3):
            if (w + t) % 2 == 0:
                acc += (w * t) % (41+3)
            else:
                acc -= (w + 41) // 2
    else:
        r = 0
        m = 41 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 42
    t = (a * 42 - b) ^ ((a + b + 42) & 7)
    if t % 5 == 0:
        acc += t // (42 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (42 % 4 + 1)
        elif acc % 3 == 0:
            acc += (42 * a) // ((b or 1))
        else:
            for j in range(2):
                if (j + a + b + 42) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(4):
            if (w + t) % 2 == 0:
                acc += (w * t) % (42+3)
            else:
                acc -= (w + 42) // 2
    else:
        r = 0
        m = 42 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 43
    t = (a * 43 - b) ^ ((a + b + 43) & 7)
    if t % 5 == 0:
        acc += t // (43 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (43 % 4 + 1)
        elif acc % 3 == 0:
            acc += (43 * a) // ((b or 1))
        else:
            for j in range(3):
                if (j + a + b + 43) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(5):
            if (w + t) % 2 == 0:
                acc += (w * t) % (43+3)
            else:
                acc -= (w + 43) // 2
    else:
        r = 0
        m = 43 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 44
    t = (a * 44 - b) ^ ((a + b + 44) & 7)
    if t % 5 == 0:
        acc += t // (44 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (44 % 4 + 1)
        elif acc % 3 == 0:
            acc += (44 * a) // ((b or 1))
        else:
            for j in range(4):
                if (j + a + b + 44) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(2):
            if (w + t) % 2 == 0:
                acc += (w * t) % (44+3)
            else:
                acc -= (w + 44) // 2
    else:
        r = 0
        m = 44 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 45
    t = (a * 45 - b) ^ ((a + b + 45) & 7)
    if t % 5 == 0:
        acc += t // (45 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (45 % 4 + 1)
        elif acc % 3 == 0:
            acc += (45 * a) // ((b or 1))
        else:
            for j in range(2):
                if (j + a + b + 45) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(3):
            if (w + t) % 2 == 0:
                acc += (w * t) % (45+3)
            else:
                acc -= (w + 45) // 2
    else:
        r = 0
        m = 45 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 46
    t = (a * 46 - b) ^ ((a + b + 46) & 7)
    if t % 5 == 0:
        acc += t // (46 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (46 % 4 + 1)
        elif acc % 3 == 0:
            acc += (46 * a) // ((b or 1))
        else:
            for j in range(3):
                if (j + a + b + 46) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(4):
            if (w + t) % 2 == 0:
                acc += (w * t) % (46+3)
            else:
                acc -= (w + 46) // 2
    else:
        r = 0
        m = 46 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 47
    t = (a * 47 - b) ^ ((a + b + 47) & 7)
    if t % 5 == 0:
        acc += t // (47 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (47 % 4 + 1)
        elif acc % 3 == 0:
            acc += (47 * a) // ((b or 1))
        else:
            for j in range(4):
                if (j + a + b + 47) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(5):
            if (w + t) % 2 == 0:
                acc += (w * t) % (47+3)
            else:
                acc -= (w + 47) // 2
    else:
        r = 0
        m = 47 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 48
    t = (a * 48 - b) ^ ((a + b + 48) & 7)
    if t % 5 == 0:
        acc += t // (48 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (48 % 4 + 1)
        elif acc % 3 == 0:
            acc += (48 * a) // ((b or 1))
        else:
            for j in range(2):
                if (j + a + b + 48) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(2):
            if (w + t) % 2 == 0:
                acc += (w * t) % (48+3)
            else:
                acc -= (w + 48) // 2
    else:
        r = 0
        m = 48 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 49
    t = (a * 49 - b) ^ ((a + b + 49) & 7)
    if t % 5 == 0:
        acc += t // (49 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (49 % 4 + 1)
        elif acc % 3 == 0:
            acc += (49 * a) // ((b or 1))
        else:
            for j in range(3):
                if (j + a + b + 49) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(3):
            if (w + t) % 2 == 0:
                acc += (w * t) % (49+3)
            else:
                acc -= (w + 49) // 2
    else:
        r = 0
        m = 49 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 50
    t = (a * 50 - b) ^ ((a + b + 50) & 7)
    if t % 5 == 0:
        acc += t // (50 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (50 % 4 + 1)
        elif acc % 3 == 0:
            acc += (50 * a) // ((b or 1))
        else:
            for j in range(4):
                if (j + a + b + 50) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(4):
            if (w + t) % 2 == 0:
                acc += (w * t) % (50+3)
            else:
                acc -= (w + 50) // 2
    else:
        r = 0
        m = 50 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 51
    t = (a * 51 - b) ^ ((a + b + 51) & 7)
    if t % 5 == 0:
        acc += t // (51 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (51 % 4 + 1)
        elif acc % 3 == 0:
            acc += (51 * a) // ((b or 1))
        else:
            for j in range(2):
                if (j + a + b + 51) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(5):
            if (w + t) % 2 == 0:
                acc += (w * t) % (51+3)
            else:
                acc -= (w + 51) // 2
    else:
        r = 0
        m = 51 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 52
    t = (a * 52 - b) ^ ((a + b + 52) & 7)
    if t % 5 == 0:
        acc += t // (52 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (52 % 4 + 1)
        elif acc % 3 == 0:
            acc += (52 * a) // ((b or 1))
        else:
            for j in range(3):
                if (j + a + b + 52) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(2):
            if (w + t) % 2 == 0:
                acc += (w * t) % (52+3)
            else:
                acc -= (w + 52) // 2
    else:
        r = 0
        m = 52 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 53
    t = (a * 53 - b) ^ ((a + b + 53) & 7)
    if t % 5 == 0:
        acc += t // (53 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (53 % 4 + 1)
        elif acc % 3 == 0:
            acc += (53 * a) // ((b or 1))
        else:
            for j in range(4):
                if (j + a + b + 53) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(3):
            if (w + t) % 2 == 0:
                acc += (w * t) % (53+3)
            else:
                acc -= (w + 53) // 2
    else:
        r = 0
        m = 53 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 54
    t = (a * 54 - b) ^ ((a + b + 54) & 7)
    if t % 5 == 0:
        acc += t // (54 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (54 % 4 + 1)
        elif acc % 3 == 0:
            acc += (54 * a) // ((b or 1))
        else:
            for j in range(2):
                if (j + a + b + 54) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(4):
            if (w + t) % 2 == 0:
                acc += (w * t) % (54+3)
            else:
                acc -= (w + 54) // 2
    else:
        r = 0
        m = 54 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 55
    t = (a * 55 - b) ^ ((a + b + 55) & 7)
    if t % 5 == 0:
        acc += t // (55 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (55 % 4 + 1)
        elif acc % 3 == 0:
            acc += (55 * a) // ((b or 1))
        else:
            for j in range(3):
                if (j + a + b + 55) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(5):
            if (w + t) % 2 == 0:
                acc += (w * t) % (55+3)
            else:
                acc -= (w + 55) // 2
    else:
        r = 0
        m = 55 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 56
    t = (a * 56 - b) ^ ((a + b + 56) & 7)
    if t % 5 == 0:
        acc += t // (56 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (56 % 4 + 1)
        elif acc % 3 == 0:
            acc += (56 * a) // ((b or 1))
        else:
            for j in range(4):
                if (j + a + b + 56) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(2):
            if (w + t) % 2 == 0:
                acc += (w * t) % (56+3)
            else:
                acc -= (w + 56) // 2
    else:
        r = 0
        m = 56 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 57
    t = (a * 57 - b) ^ ((a + b + 57) & 7)
    if t % 5 == 0:
        acc += t // (57 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (57 % 4 + 1)
        elif acc % 3 == 0:
            acc += (57 * a) // ((b or 1))
        else:
            for j in range(2):
                if (j + a + b + 57) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(3):
            if (w + t) % 2 == 0:
                acc += (w * t) % (57+3)
            else:
                acc -= (w + 57) // 2
    else:
        r = 0
        m = 57 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 58
    t = (a * 58 - b) ^ ((a + b + 58) & 7)
    if t % 5 == 0:
        acc += t // (58 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (58 % 4 + 1)
        elif acc % 3 == 0:
            acc += (58 * a) // ((b or 1))
        else:
            for j in range(3):
                if (j + a + b + 58) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(4):
            if (w + t) % 2 == 0:
                acc += (w * t) % (58+3)
            else:
                acc -= (w + 58) // 2
    else:
        r = 0
        m = 58 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 59
    t = (a * 59 - b) ^ ((a + b + 59) & 7)
    if t % 5 == 0:
        acc += t // (59 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (59 % 4 + 1)
        elif acc % 3 == 0:
            acc += (59 * a) // ((b or 1))
        else:
            for j in range(4):
                if (j + a + b + 59) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(5):
            if (w + t) % 2 == 0:
                acc += (w * t) % (59+3)
            else:
                acc -= (w + 59) // 2
    else:
        r = 0
        m = 59 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 60
    t = (a * 60 - b) ^ ((a + b + 60) & 7)
    if t % 5 == 0:
        acc += t // (60 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (60 % 4 + 1)
        elif acc % 3 == 0:
            acc += (60 * a) // ((b or 1))
        else:
            for j in range(2):
                if (j + a + b + 60) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(2):
            if (w + t) % 2 == 0:
                acc += (w * t) % (60+3)
            else:
                acc -= (w + 60) // 2
    else:
        r = 0
        m = 60 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 61
    t = (a * 61 - b) ^ ((a + b + 61) & 7)
    if t % 5 == 0:
        acc += t // (61 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (61 % 4 + 1)
        elif acc % 3 == 0:
            acc += (61 * a) // ((b or 1))
        else:
            for j in range(3):
                if (j + a + b + 61) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(3):
            if (w + t) % 2 == 0:
                acc += (w * t) % (61+3)
            else:
                acc -= (w + 61) // 2
    else:
        r = 0
        m = 61 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 62
    t = (a * 62 - b) ^ ((a + b + 62) & 7)
    if t % 5 == 0:
        acc += t // (62 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (62 % 4 + 1)
        elif acc % 3 == 0:
            acc += (62 * a) // ((b or 1))
        else:
            for j in range(4):
                if (j + a + b + 62) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(4):
            if (w + t) % 2 == 0:
                acc += (w * t) % (62+3)
            else:
                acc -= (w + 62) // 2
    else:
        r = 0
        m = 62 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 63
    t = (a * 63 - b) ^ ((a + b + 63) & 7)
    if t % 5 == 0:
        acc += t // (63 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (63 % 4 + 1)
        elif acc % 3 == 0:
            acc += (63 * a) // ((b or 1))
        else:
            for j in range(2):
                if (j + a + b + 63) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(5):
            if (w + t) % 2 == 0:
                acc += (w * t) % (63+3)
            else:
                acc -= (w + 63) // 2
    else:
        r = 0
        m = 63 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 64
    t = (a * 64 - b) ^ ((a + b + 64) & 7)
    if t % 5 == 0:
        acc += t // (64 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (64 % 4 + 1)
        elif acc % 3 == 0:
            acc += (64 * a) // ((b or 1))
        else:
            for j in range(3):
                if (j + a + b + 64) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(2):
            if (w + t) % 2 == 0:
                acc += (w * t) % (64+3)
            else:
                acc -= (w + 64) // 2
    else:
        r = 0
        m = 64 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 65
    t = (a * 65 - b) ^ ((a + b + 65) & 7)
    if t % 5 == 0:
        acc += t // (65 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (65 % 4 + 1)
        elif acc % 3 == 0:
            acc += (65 * a) // ((b or 1))
        else:
            for j in range(4):
                if (j + a + b + 65) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(3):
            if (w + t) % 2 == 0:
                acc += (w * t) % (65+3)
            else:
                acc -= (w + 65) // 2
    else:
        r = 0
        m = 65 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 66
    t = (a * 66 - b) ^ ((a + b + 66) & 7)
    if t % 5 == 0:
        acc += t // (66 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (66 % 4 + 1)
        elif acc % 3 == 0:
            acc += (66 * a) // ((b or 1))
        else:
            for j in range(2):
                if (j + a + b + 66) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(4):
            if (w + t) % 2 == 0:
                acc += (w * t) % (66+3)
            else:
                acc -= (w + 66) // 2
    else:
        r = 0
        m = 66 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 67
    t = (a * 67 - b) ^ ((a + b + 67) & 7)
    if t % 5 == 0:
        acc += t // (67 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (67 % 4 + 1)
        elif acc % 3 == 0:
            acc += (67 * a) // ((b or 1))
        else:
            for j in range(3):
                if (j + a + b + 67) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(5):
            if (w + t) % 2 == 0:
                acc += (w * t) % (67+3)
            else:
                acc -= (w + 67) // 2
    else:
        r = 0
        m = 67 % 4 + 3
        while m > 0:
            if (r + a + b + m) % 4 == 0:
                r += (a ^ b) & m
            else:
                r -= (a | b) % (m or 1)
            m -= 1
        acc += r
    

    # block 68
    t = (a * 68 - b) ^ ((a + b + 68) & 7)
    if t % 5 == 0:
        acc += t // (68 % 3 + 1)
        if (acc + a - b) & 1:
            acc -= (a - b) * (68 % 4 + 1)
        elif acc % 3 == 0:
            acc += (68 * a) // ((b or 1))
        else:
            for j in range(4):
                if (j + a + b + 68) % 3 == 0:
                    acc += j * (a - b)
                else:
                    acc -= j + (b - a)
    elif t % 7 == 0:
        for w in range(2):
            if (w + t) % 2 == 0:
                acc += (w * t) % (68+3)
            else:
                acc -= (w + 68) // 2
    else:
        r = 0
        m = 68 % 4 + 3
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
