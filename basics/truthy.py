def main():
    to_check = [
        True,
        False,
        1,
        0,
        "",
        "0",
        "Test",
        [],
        [0],
        [1],
        {},
        {'test': True},
        (),
        (1,),
    ]

    for val in to_check:
        print(val, ' is ', bool(val))


if __name__ == '__main__':
    main()

