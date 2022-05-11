from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
from config import TOKEN2
import regex
import os
import datetime
import pyautogui
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
bot = Bot(token=TOKEN2)
dp = Dispatcher(bot)

inline_btn_ToDay = InlineKeyboardButton('Погода на сегодня', callback_data='button_weath_tod')
inline_btn_Tommor = InlineKeyboardButton('Погода на завтра', callback_data='button_weath_tom')
inline_btn_10_days = InlineKeyboardButton('Погода на 10 дней', callback_data='button_weath_10d')
inline_kb_Weath = InlineKeyboardMarkup().add(inline_btn_ToDay).add(inline_btn_Tommor).add(inline_btn_10_days)

@dp.message_handler(commands=['start'])
async def start_1(message: types.Message):
    await message.answer("Привет.\nЯ буду подсказывать тебе погоду в Южно-Сахалинске по твоему выбору. Также я буду присылать тебе каждое утро прогноз на весь день.\n"
                         "P.S. /help - помощь и список команд\n"
                         "Выбирай, какую погоду ты хочешь узнать?:", reply_markup=inline_kb_Weath)

@dp.message_handler(commands=['help'])
async def help_1(message: types.Message):
    await message.reply("")



@dp.callback_query_handler(lambda c: c.data == 'button_weath_tod')
async def process_callback_button_ToDay(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id)
@dp.callback_query_handler(lambda c: c.data == 'button_weath_tom')
async def process_callback_button_ToDay(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id)
@dp.callback_query_handler(lambda c: c.data == 'button_weath_10d')
async def process_callback_button_ToDay(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id)



dfgh = ''

# url = "https://www.gismeteo.ru/weather-yuzhno-sakhalinsk-4894/"
#
# ua = UserAgent()
# headers = {'User-Agent': ua.random}
# respounse = requests.get(url, headers)
# soup = BeautifulSoup(respounse.text, 'lxml')
# quest = soup.find_all('div', class_='w')
# for ni in quest:
#     ni.find('a')
#     print(ni.text)
#
#
# for it in quest:
#     links = it.get("href")
#
# print(links)
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp)