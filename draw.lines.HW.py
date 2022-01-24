def drawLine ( length, direction ):
    if direction == 'h':
        print('-' * length)
    elif direction == 'v':
        print('|\n' * length)
    else:
        print('ERROR! Incorrect data was introduced!')

drawLine ( 5, 'h' )
drawLine ( 3, 'v' )
