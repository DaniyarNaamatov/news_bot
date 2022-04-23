import datetime
import json
import io
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from config import token
from main import check_news_update
from aiogram.dispatcher.filters import Text
from aiogram import executor
import logging

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_button = ["Все новости", "Последние 5 новостей", "Свежие новости"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_button)

    await message.answer("Лента новостей", reply_markup=keyboard)




@dp.message_handler(Text(equals="Все новости"))
async def get_all_news(message: types.Message):
    with io.open("news_dict.json", encoding='utf-8') as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items()):
    #     news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
    #            f"{hunderline(v['article_title'])}\n" \
    #            f"{hcode(v['article_desc'])}\n" \
    #            f"{hlink(v['article_title'], v['article_url'])}"
          news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
                 f"{hlink(v['article_title'], v['article_url'])}"

          await message.answer(news)


@dp.message_handler(Text(equals="Последние 5 новостей"))
async def get_last_five_news(message: types.Message):
    with io.open("news_dict.json", encoding='utf-8') as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items())[-5:]:
        news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
               f"{hlink(v['article_title'], v['article_url'])}"

        await message.answer(news)


@dp.message_handler(Text(equals="Свежие новости"))
async def get_fresh_news(message: types.Message):
    fresh_news = check_news_update()

    if len(fresh_news) >= 1:

        for k, v in sorted(fresh_news.items())[-5:]:
            news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
                   f"{hlink(v['article_title'], v['article_url'])}"

            await message.answer(news)
    else:

        await message.answer("Пока нету свежих новостей")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)