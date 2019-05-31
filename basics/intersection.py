def intersection(a1, a2):
    res = []
    for i in a1:
        if i in a2:
            res.append(i)
    return res


def main():
    print(intersection([1, 4, 9, 3, 5, 8], [2, 10, 5, 1]), ' == [1, 5]')
    print(intersection([1, 2, 9], [4, 5, 9]), ' == [9]')


if __name__ == '__main__':
    main()

