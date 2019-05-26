def list_users(users):
    i = 0
    for user in users:
        i += 1
        print(str(i) + '. ' + user)


def main():
    users = ['Vasya', 'Kirill']

    while True:
        try:
            com = input('Enter command: ')
            if com == 'list':
                list_users(users)
            elif com == 'exit':
                print('Goodbye!')
                return
            elif com.startswith('add '):
                add_user(users, com[4:])
                list_users(users)
            elif com.startswith('del '):
                del_user(users, int(com[4:]))
                list_users(users)
        except Exception:
            print('Oops... Try again!')


def add_user(users, user):
    users.append(user.title())


def del_user(users, n):
    if n <= 0 or n > len(users):
        print('Dolbaeb!')
        return
    del users[n - 1]


if __name__ == '__main__':
    main()

