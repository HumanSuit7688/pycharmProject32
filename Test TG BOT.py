from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
from config import TOKEN
import regex
import os
import datetime
import pyautogui
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

inline_btn_usd = InlineKeyboardButton('American Dollar', callback_data='button_usd')
inline_btn_eur = InlineKeyboardButton('European Euro', callback_data='button_eur')
inline_btn_jpy = InlineKeyboardButton('Japanese Yen', callback_data='button_jpy')
inline_btn_cny = InlineKeyboardButton('Chinese Yuan', callback_data='button_cny')
inline_btn_kzt = InlineKeyboardButton('Kazakhstani Tenge', callback_data='button_kzt')
inline_btn_byn = InlineKeyboardButton('Belarusian Ruble', callback_data='button_byn')
inline_kb_exch_mon = InlineKeyboardMarkup().add(inline_btn_usd).add(inline_btn_eur).add(inline_btn_jpy).add(inline_btn_cny).add(inline_btn_kzt).add(inline_btn_byn)

def exchenge_mon(url):
    quotes = ''
    ua = UserAgent()
    Url = url
    headers = {'User-Agent': ua.random}
    response = requests.get(Url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    quests = soup.find_all('p', class_='result__BigRate-sc-1bsijpp-1 iGrAod')
    for quote in quests:
        quotes += quote.text
    return quotes

@dp.message_handler(commands='exch_money')
async def exch_money(message: types.Message):
    await message.reply("Курс валют.\n Выбирай скорее!", reply_markup=inline_kb_exch_mon)

@dp.callback_query_handler(lambda c: c.data == 'button_usd')
async def process_callback_button_chr(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, f' 1 American Dollar = {exchenge_mon("https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=RUB")}')

@dp.callback_query_handler(lambda c: c.data == 'button_eur')
async def process_callback_button_chr(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, f' 1 European Euro = {exchenge_mon("https://www.xe.com/currencyconverter/convert/?Amount=1&From=EUR&To=RUB")}')

@dp.callback_query_handler(lambda c: c.data == 'button_jpy')
async def process_callback_button_chr(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, f' 1 Japanese Yen = {exchenge_mon("https://www.xe.com/currencyconverter/convert/?Amount=1&From=JPY&To=RUB")}')

@dp.callback_query_handler(lambda c: c.data == 'button_cny')
async def process_callback_button_chr(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, f' 1 Chinese Yuan = {exchenge_mon("https://www.xe.com/currencyconverter/convert/?Amount=1&From=CNY&To=RUB")}')

@dp.callback_query_handler(lambda c: c.data == 'button_kzt')
async def process_callback_button_chr(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, f' 1 Kazakhstani Tenge = {exchenge_mon("https://www.xe.com/currencyconverter/convert/?Amount=1&From=KZT&To=RUB")}')

@dp.callback_query_handler(lambda c: c.data == 'button_byn')
async def process_callback_button_chr(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, f' 1 Belarusian Ruble = {exchenge_mon("https://www.xe.com/currencyconverter/convert/?Amount=1&From=BYN&To=RUB")}')

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply("Всё работает !\n Команд: \n"
                        "/crypta - Курс основных криптовалют\n"
                        "/exch_money - Курс основных валют\n"
                        "/crypto - Курс всех криптовалют(вводишь эту команду и через пробел название криптовалюты на англ. яз. с маленькой буквы.)\nПример: ('/crypto bitcoin') ")


def crypta1(id):
    crypto = cg.get_price(ids= id , vs_currencies= 'usd')
    x = crypto[id]['usd']
    return x

@dp.message_handler(commands=['crypto'])
async def crypto(message: types.Message):
    crp = message.text[8:]
    await message.reply(f'1 {crp} = {crypta1(crp)} Dollars')

inline_btn_1 = InlineKeyboardButton('Bitcoin', callback_data='button_btc')
inline_btn_2 = InlineKeyboardButton('Ethereum', callback_data='button_eth')
inline_btn_3 = InlineKeyboardButton('Tether', callback_data='button_tht')
inline_kb_crypta = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3)


@dp.callback_query_handler(lambda c: c.data == 'button_btc')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, f'1 Bitcoin = {crypta1("bitcoin")} Dollars')

@dp.callback_query_handler(lambda c: c.data == 'button_eth')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, f'1 Ethereum = {crypta1("ethereum")} Dollars')

@dp.callback_query_handler(lambda c: c.data == 'button_tht')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, f'1 Tether = {crypta1("tether")} Dollars')

@dp.message_handler(commands=['crypta'])
async def crypta(message: types.Message):
    await message.answer("Криптовалюта? Выбирай из трёх вариантов.", reply_markup=inline_kb_crypta)

@dp.message_handler(commands=['screen'])
async def screenshot(message: types.Message):
    dt_now = datetime.datetime.now().strftime("%H.%M %Y-%m-%d")
    screen = pyautogui.screenshot(f'screenshot {dt_now}.png')
    path =  r'E:\Python\pycharmProject'
    dir_list = [os.path.join(path, x) for x in os.listdir(path)]
    if dir_list:
        date_list = [[x, os.path.getctime(x)] for x in dir_list]
        sort_date_list = sorted(date_list, key=lambda x: x[1], reverse=True)
        photo = open(sort_date_list[0][0], 'rb')

    await bot.send_photo(chat_id=message.chat.id, photo=photo)


if __name__ == '__main__':
    executor.start_polling(dp)