if __name__ == "__main__":
    t = int(input())
    r = 0
    while t>0:
        P, V, T = map(int, input().split())
        if (P and V) or (P and T) or (V and T):
            r += 1
        t -= 1
    print(r)