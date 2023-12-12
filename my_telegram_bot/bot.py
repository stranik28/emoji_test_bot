import logging
import os

import requests
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

    emotion = await requests.post()

    os.remove(audio_filename)

    await message.reply(f"Обнаружена эмоция в голосе: {emotion}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
