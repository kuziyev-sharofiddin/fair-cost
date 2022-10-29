from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

ad = [KeyboardButton(text='https://t.me/@Fair_print')]

admin = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(*ad)


bt = [KeyboardButton('Boshlash')]
head = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(*bt)

btns = [KeyboardButton('⚫️A5'),
        KeyboardButton('⚫️A4')

        ]

a_buttons = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(*btns)


btn = [
    KeyboardButton('Sariq qog\'oz'),
    KeyboardButton('Oq qog\'oz')

]


color_paper_buttons = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(*btn)

butn = [KeyboardButton('Oq qora'),
        KeyboardButton('Rangli')

        ]

color_buttons = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(*butn)

butns = [
    KeyboardButton('Buyurtma berish'),
    KeyboardButton('Boshiga o\'tish')

]

order_back = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(*butns)


buttns = [
    KeyboardButton('Pereplyot'),
    KeyboardButton('Termokley')

]

per_term = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(*buttns)
