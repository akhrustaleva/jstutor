def stats(nums):
    sums = 0
    cnt = 0
    min_num = None
    max_num = None
    for num in nums:
        if min_num is None or min_num > num:
            min_num = num
        if max_num is None or num > max_num:
            max_num = num

        sums = sums + num
        cnt += 1
    if cnt == 0:
        average = None
    else:
        average = sums / cnt

    return min_num, max_num, average



def main():
    print(str(stats([1, 4, 5, 0, 4, 3, 2, 9])) + ' == (0, 9, 3.5)')
    print(str(stats([1, 3])) + ' == (1, 3, 2)')
    print(str(stats([])) + ' == (None, None, None)')


if __name__ == '__main__':
    main()

