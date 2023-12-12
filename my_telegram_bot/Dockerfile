# Базовый образ
FROM python:3.9

# Установка ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Установка зависимостей Python
COPY req.txt /app/req.txt
COPY bot.py /app/bot.py
WORKDIR /app
RUN pip install -r req.txt

# Команда по умолчанию для запуска бота
CMD ["python", "bot.py"]
