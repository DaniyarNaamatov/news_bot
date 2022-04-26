# import sqlite3
# from conf import bot
# import random
#
#
#
# def sql_create():
#     global db, cursor
#     db = sqlite3.connect("news12_db.sqlite3")
#     cursor = db.cursor()
#     if db:
#         print("База данных подключена!")
#     db.execute("CREATE TABLE IF NOT EXISTS news"
#                "(title TEXT, url TEXT, chat_id TEXT )")
#     db.commit()
#
#
#
# async def sql_command_insert(state):
#     async with state.proxy() as data:
#         cursor.execute("INSERT INTO users VALUES (?, ?, ?)", tuple(data.values()))
#         db.commit()
#
# async def sql_command_random(message):
#     result = cursor.execute("SELECT * FROM news").fetchall()
#     r_d = random.randint(0, len(result) - 1)
#     await bot.send_photo(message.chat.id, result[r_d][0])
#     await bot.send_message(message.from_user.id,
#                            f"news: {result[r_d][1]}\n"
#                            f"URL: {result[r_d][2]}\n"
#                            f"chat_id: {result[r_d][3]}\n")
#
#
# async def sql_command_all(message):
#     return cursor.execute("SELECT * FROM news").fetchall()
#
#
# async def sql_command_delete(id):
#     cursor.execute("DELETE FROM news WHERE news == ?", (id,))
#     db.commit()
