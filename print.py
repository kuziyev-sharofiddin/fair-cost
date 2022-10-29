import asyncio
# from doctest import FAIL_FAST
from aiogram.dispatcher.filters import Text
import logging
from button import a_buttons, color_buttons, color_paper_buttons, order_back, per_term, head
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '5270351454:AAF1HRscpQ_PVBKnSdF-BabsiYvwoXwKiWM'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


initialConfig = {
    "paperType": "",
    "paperColor": "",
    "colorful": "",
    'pageCount': 0,
    'withTermoKley': False,
    'withPereplyot': False
}

prices = {
    "A5_sariq_oq-qora": 50,
    "A5_sariq_rangli": 100,
    "A5_oq_oq-qora": 70,
    "A5_oq_rangli": 120,

    "A4_sariq_oq-qora": 100,
    "A4_sariq_rangli": 150,
    "A4_oq_oq-qora": 120,
    "A4_oq_rangli": 180,
}

pereplyotPrices = {
    "A4": 8000,
    "A5": 6000
}

termoKleyPrices = {
    "A4": 9000,
    "A5": 7000
}


configs = []


@ dp.message_handler(commands=['start', 'help'])
async def start_qogoz(message: types.Message):
    await message.answer('Xush kelibsiz', reply_markup=head)


@ dp.message_handler(Text(equals='Buyurtma berish'))
async def get_order(message: types.Message):
    await message.answer('@Fair_print')


@ dp.message_handler(Text(equals='Boshiga o\'tish'))
async def get_head(message: types.Message):
    await message.answer('Boshqa formatda ko\'ring', reply_markup=head)


@ dp.message_handler(Text(equals='Boshlash'))
async def send_bosh(message: types.Message):
    index = findIndex(configs, message.from_id)
    if (index >= 0):
        configs[index] = {"user": message.from_id} | initialConfig
    else:
        configs.append({"user": message.from_id} | initialConfig)

    await message.answer('Kitobning necha sahifadan iborat ekanligini kiriting:')


@ dp.message_handler(Text(equals='⚫️A5'))
async def send_a5(message: types.Message):
    config = getUserConfig(message.from_id)
    config["paperType"] = "A5"
    await message.answer("Quyidagilardan birini tanlang", reply_markup=color_paper_buttons)


@ dp.message_handler(Text(equals='⚫️A4'))
async def send_a4(message: types.Message):
    config = getUserConfig(message.from_id)
    config["paperType"] = "A4"
    await message.answer("Quyidagilardan birini tanlang", reply_markup=color_paper_buttons)


@ dp.message_handler(Text(equals='Sariq qog\'oz'))
async def oq_qora_qogoz(message: types.Message):
    config = getUserConfig(message.from_id)
    config["paperColor"] = "sariq"
    await message.answer("Quyidagilardan birini tanlang", reply_markup=color_buttons)


@ dp.message_handler(Text(equals='Oq qog\'oz'))
async def rangli_qogoz(message: types.Message):
    config = getUserConfig(message.from_id)
    config["paperColor"] = "oq"
    await message.answer("Quyidagilardan birini tanlang", reply_markup=color_buttons)


@ dp.message_handler(Text(equals='Oq qora'))
async def oq_qora_qogoz_hisob(message: types.Message):
    config = getUserConfig(message.from_id)
    config["colorful"] = "oq-qora"
    await message.answer("Quyidagilardan birini tanlang", reply_markup=per_term)


@ dp.message_handler(Text(equals='Rangli'))
async def rangli_qogoz_hisob(message: types.Message):
    config = getUserConfig(message.from_id)
    config["colorful"] = "rangli"
    await message.answer("Quyidagilardan birini tanlang", reply_markup=per_term)


@ dp.message_handler(Text(equals='Pereplyot'))
async def perpl_price(message: types.Message):
    config = getUserConfig(message.from_id)
    config["withPereplyot"] = True
    await message.answer(f"Jami narx: {calculate(config)} so'm", reply_markup=order_back)


@ dp.message_handler(Text(equals='Termokley'))
async def term_price(message: types.Message):
    config = getUserConfig(message.from_id)
    config["withTermoKley"] = True
    await message.answer(f"Jami narx: {calculate(config)} so'm", reply_markup=order_back)


@dp.message_handler()
async def send_qogoz(message: types.Message):
    if message.text:
        config = getUserConfig(message.from_id)
        config["pageCount"] = int(message.text)

        await message.answer("Quyidagilardan birini tanlang", reply_markup=a_buttons)


def calculate(config):

    prop = config["paperType"] + "_" + \
        config["paperColor"] + "_" + config["colorful"]
    initialPrice = prices[prop] * (config["pageCount"])

    pereplyotPrice = pereplyotPrices[config["paperType"]]
    termoKleyPrice = termoKleyPrices[config["paperType"]]

    if config["withTermoKley"]:
        initialPrice += termoKleyPrice
        return initialPrice

    if config["withPereplyot"]:
        initialPrice += pereplyotPrice
        return initialPrice


def getUserConfig(userId):
    return next(config for config in configs if config["user"] == userId)


def hasConfigForUser(userId):
    return len(list(filter(lambda config: config["user"] == userId, configs))) > 0


def findIndex(configs, userId):
    index = -1
    for x in range(len(configs)):
        if (configs[x]["user"] == userId):
            index = x
            break

    return index


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    asyncio.run(bot.infinity_polling(skip_pending=True))
