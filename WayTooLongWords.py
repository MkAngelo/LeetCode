if __name__ == "__main__":
    t = int(input())
    while t>0:
        w = input()
        if len(w) <= 10: 
            print(w)
        else: 
            first = 0
            last = len(w) - 1
            between = len(w) - 2
            print(f'{w[first]}{between}{w[last]}')
        t -= 1 
