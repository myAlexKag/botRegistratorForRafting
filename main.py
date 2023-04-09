# Подключение внешних модулей
from aiogram import Bot, Dispatcher, executor, types

# Тут будут локальные импорты
from settings import API_TOKEN

print(API_TOKEN)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])  # Явно указываем в декораторе, на какую команду реагируем.
async def send_welcome(message: types.Message):
    # Так как код работает асинхронно, то обязательно пишем await.
    await message.reply(
        "Привет!\nЯ бот для записи на сплавы в группу Славные сапы!\n"
        "Отправь мне любое сообщение, а я тебе обязательно отвечу.")


@dp.message_handler()  # Создаём новое событие, которое запускается в ответ на любой текст, введённый пользователем.
async def echo(
        message: types.Message):  # Создаём функцию с простой задачей — отправить обратно тот же текст, что ввёл пользователь.
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
