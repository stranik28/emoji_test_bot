# Базовый образ
FROM python:3.9

# Установка ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Установка зависимостей Python
COPY req.txt /app/req.txt
WORKDIR /app
RUN pip install -r req.txt

# Копирование файлов приложения
COPY bot.py /app/bot.py
COPY main.py /app/main.py

# Команда по умолчанию для запуска бота
CMD ["python", "bot.py"]
