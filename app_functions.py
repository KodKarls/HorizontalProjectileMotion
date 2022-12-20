from math import sqrt

import constants


def run_app() -> None:
    print(constants.READING_DATA_PROMPT.center(constants.PROMPT_WIDTH, constants.SIGN_TO_FILL_WIDTH))
    start_height = read_data(constants.READ_HEIGHT_PROMPT, constants.HEIGHT_RANGE)
    start_velocity = read_data(constants.READ_VELOCITY_PROMPT, constants.VELOCITY_RANGE)
    print(constants.FINISH_READING_DATA_PROMPT.center(constants.PROMPT_WIDTH, constants.SIGN_TO_FILL_WIDTH))

    total_time = calculate_time_to_get_ground(start_height)
    max_range = calculate_range(start_velocity, total_time)


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
