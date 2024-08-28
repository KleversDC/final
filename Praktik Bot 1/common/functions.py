from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
import requests


def get_random_duck():
    endpoint = "https://random-d.uk/api/random"
    response = requests.get(endpoint)
    data = response.json()
    return data['url']
