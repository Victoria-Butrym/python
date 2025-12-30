teams = {
    2025: {
        'mclaren':{
            'drivers': [
                    {
                    'first_name': 'Lando',
                    'last_name': 'Norris',
                    'car_number': 4,
                    'world_champion': True,
                    'title': 'lead driver',
                    'country': 'Great Britain',
                    'points': 423,
                    'wins': 9,
                    'poles': 8
                },
                {
                    'first_name': 'Oscar',
                    'last_name': 'Piastri',
                    'car_number': 81,
                    'world_champion': False,
                    'title': 'second driver',
                    'country': 'Australia',
                    'points': 410,
                    'wins': 8,
                    'poles': 7
                }
            ],
            'drivers_count': 2,
            'principal': 'Andrea Stella',
            'constructor_champoinship': True
        },

        'red_bull': {
            'drivers': [
                    {
                    'first_name': 'Max',
                    'last_name': 'Verstappen',
                    'car_number': 1,
                    'world_champion': False,
                    'title': 'lead driver',
                    'country': 'Netherlands',
                    'points': 421,
                    'wins': 11,
                    'poles': 9
                },
                {
                    'first_name': 'Yuki',
                    'last_name': 'Tsunida',
                    'car_number': 22,
                    'world_champion': False,
                    'title': 'second driver',
                    'country': 'Japan',
                    'points': 33,
                    'wins': 0,
                    'poles': 0
                }
            ],
            'drivers_count': 2,
            'principal': 'Laurent Mekies',
            'constructor_champoinship': False
        },
    }
}

teams_2025 = {
    'mclaren':
        {
            'drivers': [
                    {
                    'first_name': 'Lando',
                    'last_name': 'Norris',
                    'car_number': 4,
                    'world_champion': True,
                    'title': 'lead driver',
                    'country': 'Great Britain',
                    'points': 423,
                    'wins': 9,
                    'poles': 8
                },
                {
                    'first_name': 'Oscar',
                    'last_name': 'Piastri',
                    'car_number': 81,
                    'world_champion': False,
                    'title': 'second driver',
                    'country': 'Australia',
                    'points': 410,
                    'wins': 8,
                    'poles': 7
                }
            ],
            'drivers_count': 2,
            'principal': 'Andrea Stella',
            'constructor_champoinship': True
        },

    'red_bull': {
            'drivers': [
                    {
                    'first_name': 'Max',
                    'last_name': 'Verstappen',
                    'car_number': 1,
                    'world_champion': False,
                    'title': 'lead driver',
                    'country': 'Netherlands',
                    'points': 421,
                    'wins': 11,
                    'poles': 9
                },
                {
                    'first_name': 'Yuki',
                    'last_name': 'Tsunida',
                    'car_number': 22,
                    'world_champion': False,
                    'title': 'second driver',
                    'country': 'Japan',
                    'points': 33,
                    'wins': 0,
                    'poles': 0
                }
            ],
            'drivers_count': 2,
            'principal': 'Laurent Mekies',
            'constructor_champoinship': False
        },
}

# print(teams)

for key, value in teams[2025].items():
    print(key, value, '\n')

# print(teams[2025]['mclaren']['drivers'][0]['first_name'])

# teams.popitem()
# print(teams)

# teams.clear()
# print(teams)