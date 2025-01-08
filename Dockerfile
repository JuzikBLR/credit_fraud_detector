FROM python:3.9-slim-buster

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл requirements.txt из корневой директории проекта в контейнер
COPY requirements.txt /app/requirements.txt

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Устанавливаем psycopg2-binary отдельно, чтобы избежать проблем с зависимостями
RUN apt-get update && apt-get install -y libpq-dev && pip install --no-cache-dir psycopg2-binary && \
    apt-get remove -y libpq-dev && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

# Копируем весь проект в контейнер
COPY . /app/

# Указываем порт, который будет использовать приложение
EXPOSE 8000

# Команда для запуска Flask-приложения (исправляем путь к main.py)
CMD ["python", "main.py"]