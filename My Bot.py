import requests
from bs4 import BeautifulSoup
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from fake_useragent import UserAgent
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN1

bot = Bot(token=TOKEN1)
dp = Dispatcher(bot)

def ParthInfoGI():
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    url = "https://genshin-info.ru/wiki/personazhi/"
    respounse = requests.get(url, headers)
    soup = BeautifulSoup(respounse.text, 'lxml')
    quests = soup.find_all('div', class_='card')


inline_btn_1 = InlineKeyboardButton('Персонаж', callback_data='button_chr')
inline_btn_2 = InlineKeyboardButton('Оружие', callback_data='button_wap')
inline_kb_chr_wap = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2)

inline_btn_3 = InlineKeyboardButton('Пять звёзд', callback_data='button_5st')
inline_btn_4 = InlineKeyboardButton('Четыре звезды', callback_data='button_4st')
inline_kb_5or4st = InlineKeyboardMarkup().add(inline_btn_3).add(inline_btn_4)

inline_btn_6 = InlineKeyboardButton('Пять звёзд', callback_data='button_5st_w')
inline_btn_7 = InlineKeyboardButton('Четыре звезды', callback_data='button_4st_w')
inline_kb_5or4st_w = InlineKeyboardMarkup().add(inline_btn_6).add(inline_btn_7)

@dp.message_handler(commands=['help1'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

@dp.message_handler(commands=['start1'])
async def process_start1_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет, похоже ты любишь поиграть в Genshin Imact.\n"
                        "Тогда здесь ты можешь найти актуальную информацию на тему ресурсов для улучшения персонажей и оружия. Выбирай скорее!\n", reply_markup=inline_kb_chr_wap)

@dp.callback_query_handler(lambda c: c.data == 'button_chr')
async def process_callback_button_chr(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Персонажи какой редкости тебя интересуют?", reply_markup=inline_kb_5or4st)

inline_btn_ELan = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_Ayato = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_YaeMiko = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_ShenHe = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_Itto = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_Kokomi = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_Raiden = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_Eloi = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_Yoimiya = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_ElectroGG = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_Ayaka = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_Kadzuha = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_Eola = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_HuTao = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_Xyao = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_GanYui = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_Albedo = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_DjunLi = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_Tartaliya = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_Klee = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_Venti = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_ChiChi = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_Mona = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_KeTsin = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_Dilyuk = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_Djin = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_GeoGG = InlineKeyboardButton('', callback_data='button_5st_w')
inline_btn_AnemoGG = InlineKeyboardButton('', callback_data='button_5st_w')

inline_kb_5str_chr = InlineKeyboardMarkup().add(inline_btn_ELan).add(inline_btn_Ayato).add(inline_btn_YaeMiko).add(inline_btn_ShenHe).add(inline_btn_Itto).add(inline_btn_Kokomi).add(inline_btn_Raiden).add(inline_btn_Eloi).add(inline_btn_Yoimiya).add(inline_btn_ElectroGG).add(inline_btn_Ayaka).add(inline_btn_Kadzuha).add(inline_btn_Eola).add(inline_btn_HuTao).add(inline_btn_Xyao).add(inline_btn_GanYui).add(inline_btn_Albedo).add(inline_btn_DjunLi).add(inline_btn_Tartaliya).add(inline_btn_Klee).add(inline_btn_Venti).add(inline_btn_ChiChi).add(inline_btn_Mona).add(inline_btn_KeTsin).add(inline_btn_Dilyuk).add(inline_btn_Djin).add(inline_btn_GeoGG).add(inline_btn_AnemoGG)


@dp.callback_query_handler(lambda c: c.data == 'button_5st')
async def process_callback_button_chr(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Выбирай легендарных персонажей!", reply_markup=inline_kb_5str_chr)


@dp.callback_query_handler(lambda c: c.data == 'button_wap')
async def process_callback_button_wap(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Оружия какой редкости ты хочешь посмотреть?", reply_markup=inline_kb_5or4st_w)

# @dp.message_handler()
# async def come_back_word(message: types.Message):
#     wrd = 0
#     ltr = 0
#     smbl = 0
#     for x in message.text:
#         if x == '!' or x == '.' or x == '?' or x == ',' or x == '/' or x == ':' or x == '"' or x == ".":
#             smbl += 1
#         elif x != ' ':
#            ltr += 1
#         elif x == ' ':
#            wrd += 1
#
#     wrd += 1
#     await message.answer(f"{wrd} Слов , {ltr} букв и {smbl} других символов")


if __name__ == '__main__':
    executor.start_polling(dp)
