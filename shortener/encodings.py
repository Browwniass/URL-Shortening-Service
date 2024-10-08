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


def generate_short_url(id):
    return id_to_short_url(id)