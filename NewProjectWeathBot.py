# Импортируем нужные библиотеки:
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
import schedule
import time
bot = Bot(token=TOKEN2)
dp = Dispatcher(bot)

#   Создаём инлайн кнопки и инлайн клавиатуру
inline_btn_ToDay = InlineKeyboardButton('Погода на сегодня', callback_data='button_weath_tod')
inline_btn_7_days = InlineKeyboardButton('Погода на неделю', callback_data='button_weath_7d')
inline_kb_Weath = InlineKeyboardMarkup().add(inline_btn_ToDay).add(inline_btn_7_days)

#   Сайты для сбора информации
url1 = "https://primpogoda.ru/weather/yuzhno-sahalinsk.6days"
url3 = 'https://www.gismeteo.ru/weather-yuzhno-sakhalinsk-4894/10-days/'
#   Код парсинга
ua = UserAgent()
headers = {'User-Agent': ua.random}
respounse = requests.get(url1, headers=headers)
soup = BeautifulSoup(respounse.text, 'lxml')
respounse2 = requests.get(url3, headers=headers)
soupc = BeautifulSoup(respounse2.text, 'lxml')
#   Первая функция для получения погоды на сегодняшний день
def weath_ToD(tim, tim2):
    quest = soup.find('tr', class_='temperature tip-right')
    wet = []
    pres = []
    quast = quest.find_all('td', class_=tim)
    for dt in quast:
        wet.append(dt.text)
    windy = soup.find('tr', class_='wind advanced tip-right')
    dwind = windy.find('td', class_=tim)
    for dw in dwind:
        wet.append(dw.text)
    press = soup.find('tr', class_='pressure advanced divider tip-right')
    dpres = press.find('td', class_=tim)
    for pd in dpres:
        pres.append(pd.text)
    wet.append(pres[0])

    if wet[2] == "Штиль":
        wind = "Нет ветра"
    else:
        wind = "Скорость ветра"
    result = f"{tim2}\nТемпература от  {wet[0]}  до  {wet[1]}\n{wind}  -  {wet[2]}\nАтмосферное давление  -  {wet[3]} мм рт. ст."
    return result
#   Вторая функция для получения погоды на неделю
def weath_week():
    week_temp1 = soupc.find_all('div', class_='maxt')
    week_temp2 = soupc.find_all('div', class_='mint')
    temper_h = []
    #   Цикль находящий максимальную температуру по дням
    for wt1 in week_temp1:
        temp_h = wt1.find('span', class_='unit unit_temperature_c')
        try:
            a = temp_h.text
            temper_h.append(a)
        except:
            continue
    #   Цикль находящий минимальную температуру по дням
    temper_l = []
    for wt2 in week_temp2:
        temp_l = wt2.find('span', class_='unit unit_temperature_c')
        try:
            a = temp_l.text
            temper_l.append(a)
        except:
            continue
    #   Код который находит дни недели
    Week_days = soup.find_all('h3')
    week_days = []
    for da in Week_days:
        week_days.append(da.text)
    result = f"Погода на неделю.\n{week_days[0]}: от  {temper_l[0]}  до  {temper_h[0]}\n{week_days[1]}:  от  {temper_l[1]}  до  {temper_h[1]}\n{week_days[2]}:  от  {temper_l[2]}  до  {temper_h[2]}\n" \
             f"{week_days[3]}: от  {temper_l[3]}  до  {temper_h[3]}\n{week_days[4]}:  от  {temper_l[4]}  до  {temper_h[4]}\n{week_days[5]}:  от  {temper_l[5]}  до  {temper_h[5]}\n"
    return result

#   Хандлер ловящий команду "start"
@dp.message_handler(commands=['start'])
async def start_1(message: types.Message):
    await message.answer("Привет.\nЯ буду подсказывать тебе погоду в Южно-Сахалинске по твоему выбору. Также я буду присылать тебе каждое утро прогноз на весь день.\n"
                         "Выбирай, какую погоду ты хочешь узнать?:", reply_markup=inline_kb_Weath)
    schedule.every().day.at("07:00").do(job)
#   Хендлер реагирующий на кнопку "Погода на сегодня"
@dp.callback_query_handler(lambda c: c.data == 'button_weath_tod')
async def process_callback_button_ToDay(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, weath_ToD('morning',"Утро"))
    await bot.send_message(callback_query.from_user.id, weath_ToD('day', "День"))
    await bot.send_message(callback_query.from_user.id, weath_ToD('evening', "Вечер"))
    await bot.send_message(callback_query.from_user.id, weath_ToD('night', "Ночь"))
#   Хендлер реагирующий на кнопку "Погода на неделю"
@dp.callback_query_handler(lambda c: c.data == 'button_weath_7d')
async def process_callback_button_ToDay(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, weath_week())

#   Функция для отправки ботом сообщений каждое утро
def job(message):
    bot.send_message(weath_ToD('morning', 'Утро'))
    bot.send_message(weath_ToD('day', 'День'))
    bot.send_message(weath_ToD('evening', 'Вечер'))
    message.answer(weath_ToD('night', "Ночь"))


if __name__ == '__main__':
    executor.start_polling(dp)