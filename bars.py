import json
import math


def load_data(filepath):
    bars_description = json.loads(open(filepath, 'r').read())
    return bars_description

def get_biggest_bar(data):
    bars_size = []
    for bar_list_id, bar in enumerate(bars_description): # Перебираем бары по одному.
        bars_size.append([bar['Cells']['SeatsCount'], bar_list_id])
    return max(bars_size)[1]


def get_smallest_bar(data):
    bars_size = []
    for bar_list_id, bar in enumerate(bars_description): # Перебираем бары по одному.
        bars_size.append([bar['Cells']['SeatsCount'], bar_list_id])
    return min(bars_size)[1]


def get_closest_bar(bars_description, latitude, longitude):
    bars_distance = [] # Первым элементом каждого вложенного массива будет дистанция, вторым - id.
    for bar_list_id, bar in enumerate(bars_description): # Перебираем бары по одному.
        distance_to_current_bar = \
        math.sqrt((bar['Cells']['geoData']['coordinates'][0] - float(latitude))**2 +
            (bar['Cells']['geoData']['coordinates'][1] - float(longitude))**2)
            # Используем теорему Пифагора, принимая, что в пределах Москвы можем считать, что работаем на плоскости, а не на эллипсоиде/геоиде.
        bars_distance.append([distance_to_current_bar, bar_list_id])
    return min(bars_distance)[1]
    


if __name__ == '__main__':
    
    json_file_path = input("Enter the path to the file: ")
    bars_description = load_data(json_file_path)

    latitude, longitude = input('Введите ваши GPS-координаты через пробел в формате \
                        \"55.754069 37.620543\"\n').split()
    nearest_bar_id = get_closest_bar(bars_description, latitude, longitude)
    print("\n\nБлижайший к тебе бар:\n%s\nID: %s\nКоординаты: %s\nКоличество мест: %s\n" %
       (bars_description[nearest_bar_id]['Cells']['Name'],
        bars_description[nearest_bar_id]['Id'],
        bars_description[nearest_bar_id]['Cells']['geoData']['coordinates'],
        bars_description[nearest_bar_id]['Cells']['SeatsCount']))

    biggest_bar_id = get_biggest_bar(bars_description)
    print("Самый большой бар:\n%s\nID: %s\nКоординаты: %s\nКоличество мест: %s\n" %
       (bars_description[biggest_bar_id]['Cells']['Name'],
        bars_description[biggest_bar_id]['Id'],
        bars_description[biggest_bar_id]['Cells']['geoData']['coordinates'],
        bars_description[biggest_bar_id]['Cells']['SeatsCount']))

    smallest_bar_id = get_smallest_bar(bars_description)
    print("Самый маленький бар:\n%s\nID: %s\nКоординаты: %s\nКоличество мест: %s\n" %
       (bars_description[smallest_bar_id]['Cells']['Name'],
        bars_description[smallest_bar_id]['Id'],
        bars_description[smallest_bar_id]['Cells']['geoData']['coordinates'],
        bars_description[smallest_bar_id]['Cells']['SeatsCount']))