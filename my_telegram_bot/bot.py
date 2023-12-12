import logging
import os

import aiohttp
from aiogram import Bot, Dispatcher, types
import asyncio

API_TOKEN = '1711154445:AAFtvTCVtvNY21MfutTGvvEgwNun-lZHYSw'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message()
async def process_voice_message(message: types.Message):
    if message.voice:
        file_id = message.voice.file_id
    else:
        file_id = message.document.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    audio_filename = f"{file_id}.wav"
    await bot.download_file(file_path, audio_filename)

    # Создайте объект FormData и добавьте туда файл
    form = aiohttp.FormData()
    form.add_field('file', open(audio_filename, 'rb'), content_type='audio/x-wav')

    # URL, на который нужно отправить запрос
    url = 'http://localhost:8000/predict'

    # Отправка POST-запроса
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=form) as response:
            # Проверяем успешность запроса
            if response.status == 200:
                # Получаем данные ответа
                data = await response.json()
                emotion = data.get('emotion', 'Не удалось определить эмоцию')
                await message.reply(f"Обнаружена эмоция в голосе: {emotion}")
            else:
                await message.reply("Произошла ошибка при обработке аудио")

    # Удаление локального файла
    os.remove(audio_filename)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
