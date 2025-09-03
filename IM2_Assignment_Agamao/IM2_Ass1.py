while True:
    rows = int(input('Enter Row: '))
    col = int(input('Enter Col: '))

    # check if valid first
    if rows <= 0 or col <= 0:
        print('Invalid Input. Loop is stopped.')
        break

    search = int(input('Search a number: '))

    # print matrix with highlighted search
    for x in range(1, rows + 1):
        for y in range(1, col + 1):
            value = x * y
            if search == value:
                print(f'[{value}]', end=" ")
            else:
                print(value, end=" ")
        print()
