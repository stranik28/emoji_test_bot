import logging
import os
from aiogram import Bot, Dispatcher, types
import asyncio
from main import predict

API_TOKEN = '1711154445:AAFtvTCVtvNY21MfutTGvvEgwNun-lZHYSw'  # Замените на свой API токен

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


def convert_audio(audio_file):
    import subprocess
    subprocess.call(['ffmpeg', '-i', f'{audio_file}', f'{audio_file[:-4]}.wav'])
    return f'{audio_file[:-4]}.wav'


@dp.message()
async def handle_audio_message(message: types.Message):
    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    audio_filename = f"{file_id}.mp3"
    await bot.download_file(file_path, audio_filename)

    wav_file = convert_audio(audio_filename)
    emotion = await predict(wav_file)

    os.remove(audio_filename)
    os.remove(wav_file)

    await message.reply(f"Обнаружена эмоция в голосе: {emotion}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

