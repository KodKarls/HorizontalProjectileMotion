from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

import constants


def run_app() -> None:
    print(constants.READING_DATA_PROMPT.center(constants.PROMPT_WIDTH, constants.SIGN_TO_FILL_WIDTH))
    start_height = read_data(constants.READ_HEIGHT_PROMPT, constants.HEIGHT_RANGE)
    start_velocity = read_data(constants.READ_VELOCITY_PROMPT, constants.VELOCITY_RANGE)
    print(constants.FINISH_READING_DATA_PROMPT.center(constants.PROMPT_WIDTH, constants.SIGN_TO_FILL_WIDTH))

    total_time = calculate_time_to_get_ground(start_height)
    max_range = calculate_range(start_velocity, total_time)

    x_points = get_x_points(max_range)
    y_points = get_y_points(start_height, start_velocity, x_points)

    title = f'''Wykres rzutu poziomego z Vo = {start_velocity} m/s (g = {constants.G} m/s^2)
            Czas lotu = {round(total_time, constants.NUMBER_FOUR)} s'''

    draw_figure(start_height, max_range, x_points, y_points, title)


def read_data(user_prompt: str, min_value: int) -> float:
    while True:
        try:
            result = float(input(user_prompt))
        except ValueError:
            print(constants.VALUE_ERROR_MESSAGE)
        else:
            if result < min_value:
                print(constants.RANGE_ERROR_MESSAGE + str(min_value))
                continue
            break

    return result


def calculate_time_to_get_ground(height: float) -> float:
    return sqrt((constants.NUMBER_TWO * height) / constants.G)


def calculate_range(velocity: float, time: float) -> float:
    return velocity * time


def get_x_points(max_range: float) -> np.ndarray:
    return np.arange(constants.START_RANGE, max_range, max_range / constants.AMOUNT_OF_SAMPLES)


def get_y_points(height: float, velocity: float, x_points: np.ndarray) -> np.ndarray:
    return height - ((constants.G / constants.NUMBER_TWO) * (x_points / velocity) ** constants.NUMBER_TWO)


def draw_figure(start_height: float, max_range: float, x_points: np.ndarray, y_points: np.ndarray, title: str) -> None:
    height_label = f'Początkowa wysokość = {start_height} m'
    max_range_label = f'Maksymalny zasięg = {round(max_range, constants.NUMBER_THREE)} m'
    plt.scatter(constants.NUMBER_ZERO, start_height, label=height_label)
    plt.scatter(max_range, constants.NUMBER_ZERO, label=max_range_label)
    plt.plot(x_points, y_points, marker=constants.PLOT_MARKER, color=constants.PLOT_COLOR, label=constants.PLOT_LABEL)
    plt.grid()
    plt.title(title)
    plt.xlabel(constants.X_LABEL)
    plt.ylabel(constants.Y_LABEL)
    plt.legend()
    plt.show()
