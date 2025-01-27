Telegram Bot Project

Описание
Это приложение представляет собой Telegram-бота, разработанного на базе библиотеки Aiogram. Бот предоставляет интерактивный интерфейс для пользователей, поддерживает кнопки, обработку команд и управление состояниями.

---

Структура проекта
Основные файлы и папки:
- `app.py`: Главный файл для запуска бота. Содержит обработчики событий и настройку polling.
- `config.py`: Конфигурационный файл с основными настройками, такими как токен бота и ID администратора.
- `loader.py`: Загружает основные компоненты, такие как бот, диспетчер, базовые настройки.
- `handlers/`: Модуль с обработчиками команд и сообщений.
- `keybord_s/`: Логика кнопок и клавиатур.
- `data/`: Данные, используемые ботом.
- `database.db`: SQLite-база данных для хранения информации о пользователях.
- `requirements.txt`: Список зависимостей, необходимых для работы приложения.
