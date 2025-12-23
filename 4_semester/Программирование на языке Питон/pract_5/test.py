def main(x):
    conditions = {
        'HTTP': 8,
        'AMPL': {
            'TCL': 6,
            'EDN': 7,
            'MUPAD': {
                2005: {
                    1991: 0,
                    1988: 1,
                    2012: 2
                },
                2008: {
                    1991: 3,
                    1988: 4,
                    2012: 5
                }
            }
        },
        'ROFF': {
            1991: {
                'GO': {
                    'MUPAD': 9,
                    'TCL': 10,
                    'EDN': 11
                },
                'OX': 12,
                'QML': 13
            },
            1988: 14,
            2012: 15
        }
    }

    current = conditions.get(x[0])
    while isinstance(current, dict):
        if x[1] in current:
            current = current[x[1]]
        elif x[2] in current:
            current = current[x[2]]
        elif x[3] in current:
            current = current[x[3]]
        elif x[4] in current:
            current = current[x[4]]
        else:
            return None
    print(type(current))
    return current

main(['AMPL', 2005, 1991, 'MUPAD', 'GO'])