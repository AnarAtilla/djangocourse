# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY . .

# Открываем порт 8000 для доступа к серверу
EXPOSE 8000

# Устанавливаем переменную окружения (опционально)
ENV NAME World

# Запускаем Django сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]