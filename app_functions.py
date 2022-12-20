def run_app() -> None:
    initial_values = read_data()
    print(initial_values)

    print('OK, dane początkowe wczytane, działamy dalej.')


def read_data() -> tuple[float, float]:
    start_height = get_correct_data('Podaj wysokość początkową (w m): ', 10)
    start_velocity = get_correct_data('Podaj prędkość początkową (w m/s): ', 2)

    return start_height, start_velocity


def get_correct_data(user_prompt: str, min_value: int) -> float:
    print('---[ wczytujemy dane ]----------')
    while True:
        try:
            result = float(input(user_prompt))
        except ValueError:
            print('To nie jest liczba zmiennoprzecinkowa (np. 3.14).')
        else:
            if result < min_value:
                continue
            break

    return result
