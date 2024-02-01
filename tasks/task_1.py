
from typing import Union


def get_first_unique_char(processed_string: str) -> Union[str, None]:
    char_count = {}

    for char in processed_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in processed_string:
        if char_count[char] == 1:
            return char

    return None
