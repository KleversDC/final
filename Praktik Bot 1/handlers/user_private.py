from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram import F, Router
import common.functions as fun
import os
user_private_router = Router()

@user_private_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привіт {message.from_user.full_name} цей бот уміє все що находиця в меню також у цого бота можа спитати його улюблений колір для цого потрібно написати\n"який твій улюблений колір"\nтакож у бота можна спитати як прошов його день для цого потрібно написати \n "як в тебе прошов день"\nз цікавого тут можна перейти на ютуб тік ток подивитися погодо міский транспорт новини також карту повітряних тривог')
 
@user_private_router.message(Command("duck"))
async def cmd_duck(message: Message):
    await message.answer_photo(fun.get_random_duck())


@user_private_router.message(Command("youtube"))
async def cmd_you(message: Message):
    await message.answer("https://www.youtube.com/")


@user_private_router.message(Command("tiktok"))
async def cmd_tiktok(message: Message):
    await message.answer("https://www.tiktok.com/tiktokstudio/upload?lang=uk-UA")


@user_private_router.message(Command("news"))
async def cmd_you(message: Message):
    await message.answer("https://www.ukr.net/news/rivne.html")


@user_private_router.message(Command("weather"))
async def cmd_you(message: Message):
    await message.answer("https://meteofor.com.ua/weather-rivne-4940/")


@user_private_router.message(Command("dozop"))
async def cmd_you(message: Message):
    await message.answer("https://www.city.dozor.tech/ua/rivne/city")


@user_private_router.message(Command("anxietymap"))
async def cmd_you(message: Message):
    await message.answer("https://map.ukrainealarm.com/")
 

@user_private_router.message(F.text =='який твій улюблений колір')
async def cmd_color(message:Message):
   await message.reply('мій улюблений колір чорний⬛')

@user_private_router.message(F.text =='як в тебе прошов день')
async def cmd_day(message:Message):
   await message.reply('у мене день прошов добря\nдякую що спитали 😁 \nа як у вас прошов ден ? \n"напишіть добре або погано" ')

@user_private_router.message(F.text =='добре')
async def cmd_das(message:Message):
    await message.reply('це чудово хай у вас завжди будуть такі дні ')

@user_private_router.message(F.text =='погано')
async def cmd_daa(message:Message):
    await message.reply('це пагано я хотілаб вам порадити подивитися на милих качок цоб підняти настрій \n через команду що находиця в меню або подивиця Youtube теж через команду в меню не сумуйте все буде добре')