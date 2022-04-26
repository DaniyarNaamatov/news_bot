# from aiogram.types import ParseMode
# from aiogram import utils
# from peewee import *
#
#
# db = SqliteDatabase('news_db.sqlite3')
#
#
# class BaseModel(Model):
#     class Meta:
#         database = db
#
#
# class NewsCard(BaseModel):
#     title = CharField()
#     url = TextField()
#
#
# class SearchNews(BaseModel):
#     title = CharField()
#     chatid = CharField()
#
#
#
# def find_all_cards():
#     return NewsCard.select()
#
#
# def find_id_search(chat_id):
#     return SearchNews.select().where(SearchNews.chatid == chat_id)
#
#
#
# def find_all_search():
#     return SearchNews.select()
#
#
# async def process_search_news(message):
#     search_exist = True
#     try:
#         search = SearchNews.select().where(SearchNews.title == message.text).get()
#         search.delete_instance()
#         await message.answer('Строка поиска {} удалена'.format(message.text))
#         return search_exist
#     except DoesNotExist as de:
#         search_exist = False
#
#     if not search_exist:
#         rec = SearchNews(title=message.text, chatid=message.chat.id)
#         rec.save()
#         await message.answer('Строка поиска {} добавлена'.format(message.text))
#     else:
#         await message.answer('Строка поиска {} уже есть'.format(message.text))
#     return search_exist
#
#
#
# async def process_news_card(title, url, chat_id, bot):
#     _exist = True
#     try:
#         card = NewsCard.select().where(NewsCard.title == title).get()
#
#     except DoesNotExist as de:
#         card = False
#
#     if not card:
#         rec = NewsCard(title=title, url=url)
#         rec.save()
#         message_text = utils.markdown.hlink(title, url)
#         await bot.send_message(chat_id=chat_id, text=message_text, parse_mode=ParseMode.HTML)
#     return card
#
#
# def init_db():
#     db.create_tables([NewsCard, SearchNews])
#
#
#
#
#
#
#
#
#
