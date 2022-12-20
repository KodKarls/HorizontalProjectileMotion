from math import sqrt

import constants


def run_app() -> None:
    print('----------[ wczytujemy dane ]----------')
    start_height = read_data('Podaj wysokość początkową (w m): ', 10)
    start_velocity = read_data('Podaj prędkość początkową (w m/s): ', 2)
    print(f'{start_height}, {start_velocity}')

    print('OK, dane początkowe wczytane, działamy dalej.')

    total_time = calculate_time_to_get_ground(start_height)
    max_range = calculate_range(start_velocity, total_time)


def read_data(user_prompt: str, min_value: int) -> float:
    while True:
        try:
            result = float(input(user_prompt))
        except ValueError:
            print('To nie jest liczba zmiennoprzecinkowa (np. 3.14).')
        else:
            if result < min_value:
                print(f'Minimalna wartość powinna wynosić: {min_value}')
                continue
            break

    return result


def calculate_time_to_get_ground(height: float) -> float:
    return sqrt((constants.NUMBER_TWO * height) / constants.G)


def calculate_range(velocity: float, time: float) -> float:
    return velocity * time
