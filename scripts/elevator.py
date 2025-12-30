floor = int(input('Enter the floor number: '))

NO_SUCH_FLOOR = 'No such floor'
FIRST_FLOOR = 'First floor'
UNDEGROUND_FLOOR = 'Undeground floor'
ODD_FLOOR = 'Living floor'
EVEN_FLOOR = 'Office floor'
TECH_FLOOR = 'Technical floor. No entry'

match floor:
    case 1:
        print(FIRST_FLOOR)
    case -1:
        print(UNDEGROUND_FLOOR)
    case 10:
        print(TECH_FLOOR)
    case _ if 2 <= floor <= 9:
        floor_type = EVEN_FLOOR if floor % 2 == 0 else ODD_FLOOR
        print(floor_type)
    case _:
        print(NO_SUCH_FLOOR)