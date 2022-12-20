def run_app() -> None:
    print('----------[ wczytujemy dane ]----------')
    start_height = read_data('Podaj wysokość początkową (w m): ', 10)
    start_velocity = read_data('Podaj prędkość początkową (w m/s): ', 2)
    print(f'{start_height}, {start_velocity}')

    print('OK, dane początkowe wczytane, działamy dalej.')


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
