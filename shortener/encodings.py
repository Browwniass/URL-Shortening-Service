import random
import string


NUMBER_BASE = 62 


def id_to_short_url(number):
    map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    result = ""
    while number:
        result += map[number % NUMBER_BASE]
        number //= NUMBER_BASE
    return result[::-1]


def generate_short_url(id, encoding='base62'):
    match encoding:
        case 'base62':
            return id_to_short_url(id)
        case _:
            raise ValueError(f'Error: Encoding {encoding} is not supported.')
    