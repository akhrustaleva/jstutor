def bs(arr, n,):
    lo = 0
    hi = len(arr) - 1

    while True:
        mid = lo + (hi - lo) // 2
        if arr[mid] < n:
            lo = mid + 1
        elif arr[mid] > n:
            hi = mid - 1
        else:
            return mid

        if hi < lo:
            return None


def main():
    # l = [1, 3, 50, 75, 80, 100, 120, 140]
    l = [100, 120, 140]
    print(bs(l, 5) is None)
    # print(bs(l, 50) == 2)
    # print(bs(l, 140))
    # print(bs(l, 120))


if __name__ == '__main__':
    main()
