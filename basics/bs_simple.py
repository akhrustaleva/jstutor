def bs(arr, n):
    num = 0
    for v in arr:
        if n == v:
            return num
        num += 1


def main():
    l = [1, 3, 50, 75, 80, 100, 120, 140]
    print(bs(l, 5) is None)
    print(bs(l, 50) == 2)
    print(bs(l, 140) == 7)
    print(bs(l, 24))


if __name__ == '__main__':
    main()
