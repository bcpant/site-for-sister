import sys
import os

# Указываем путь к директории с приложением
# Не забудьте указать путь к проекту
sys.path.insert(0, '/home/easy-chinese/public_html')

# Импортируем приложение
from app import app as application  # Замените "app" на имя вашего файла с приложением без .py, если оно отличается.