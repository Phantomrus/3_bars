import json
import math


def load_data(filepath):
    with open(filepath, 'r') as file_with_inform:
        bars_description = json.loads(file_with_inform.read())
    return bars_description

def get_biggest_bar(data):
    biggest_bar = max(data, key=lambda x: x['Cells']['SeatsCount'])    
    return biggest_bar

def get_smallest_bar(data):
    smallest_bar = min(data, key=lambda x: x['Cells']['SeatsCount'])    
    return smallest_bar

def get_nearest_bar(data, latitude, longitude):

    nearest_bar = min(data, key=lambda bar: math.sqrt((bar['Cells']['geoData']['coordinates'][0] - float(latitude))**2 +
            (bar['Cells']['geoData']['coordinates'][1] - float(longitude))**2))
    return nearest_bar


if __name__ == '__main__':
    
    json_file_path = input("Enter the path to the file: ")
    bars_description = load_data(json_file_path)

    latitude, longitude = input('Введите ваши GPS-координаты через пробел в формате \
                        \"55.754069 37.620543\"\n').split()
    nearest_bar = get_nearest_bar(bars_description, latitude, longitude)
    print("\n\nБлижайший к тебе бар:\n%s\nID: %s\nКоординаты: %s\nКоличество мест: %s\n" %
       (nearest_bar['Cells']['Name'],
        nearest_bar['Id'],
        nearest_bar['Cells']['geoData']['coordinates'],
        nearest_bar['Cells']['SeatsCount']))

    biggest_bar = get_biggest_bar(bars_description)
    print("Самый большой бар:\n%s\nID: %s\nКоординаты: %s\nКоличество мест: %s\n" %
       (biggest_bar['Cells']['Name'],
        biggest_bar['Id'],
        biggest_bar['Cells']['geoData']['coordinates'],
        biggest_bar['Cells']['SeatsCount']))

    smallest_bar = get_smallest_bar(bars_description)
    print("Самый маленький бар:\n%s\nID: %s\nКоординаты: %s\nКоличество мест: %s\n" %
       (smallest_bar['Cells']['Name'],
        smallest_bar['Id'],
        smallest_bar['Cells']['geoData']['coordinates'],
        smallest_bar['Cells']['SeatsCount']))
