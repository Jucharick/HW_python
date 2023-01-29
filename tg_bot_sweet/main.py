# python -m venv venv

from aiogram import executor
from handlers import dp
async def on_start(_):
    print('Бот запущен')

# async - библиотека aiogram работает асинхронно

executor.start_polling(dp, skip_updates=True, on_startup = on_start) # команда, начинающая слушать; принимать сообщения
# skip_updates=True пока наш бот не активен все команды (сообщения) проходят мимо (игнорируются)
# skip_updates=False  все сообщения складируются в стек - как только мы включим бота сообщения начнут приходить по очереди из стека



