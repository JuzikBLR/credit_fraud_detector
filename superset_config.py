import os
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Задаем безопасный SECRET_KEY из переменной окружения
# Если переменная окружения не установлена, используем фиксированное значение
SECRET_KEY = os.getenv('SECRET_KEY', 'jQx2eM7yE+Rdo8nO2fNZpzzjQYPdz+3TdOflEUX0b5B7+BaS7OgdYtfd')

# Выводим значение SECRET_KEY в логи (только для отладки)
logger.info(f"Using SECRET_KEY: {SECRET_KEY}")

# База данных Superset (PostgreSQL)
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql+psycopg2://postgres:postgres@db:5432/superset')

# База данных примеров Superset (тоже PostgreSQL)
SQLALCHEMY_EXAMPLES_URI = os.getenv('SQLALCHEMY_EXAMPLES_URI', 'postgresql+psycopg2://postgres:postgres@db:5432/superset')

# Другие настройки Superset (если необходимо)
# Например, можно добавить настройки для кэширования, безопасности и т.д.