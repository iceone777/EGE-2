for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                f = ((a and b) <= c) and ((b and c) <= d)
                if f == 0:
                    print(d, b, a, c, '|', f * 1)