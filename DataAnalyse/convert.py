__author__ = 'Michyo'

import json

def run():
    django_data = []

    django_data.append(['time', 'Quantity'])

    print django_data

    file_name = "/Users/Michyo/PycharmProjects/TwitterData/DataAnalyse/output/TwQuantity.json"

    with open(file_name) as f:
        for line in f:
            line_data = json.loads(line)
            pair = []
            pair.append(line_data['time'])
            pair.append(line_data['Quantity'])
            django_data.append(pair)

    return django_data