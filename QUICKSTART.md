# 🚀 Быстрый старт Schedule Bot

## Локальный запуск

1. **Установите Python 3.11**
2. **Создайте виртуальное окружение:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Создайте файл `.env`:**
   ```
   BOT_TOKEN=ваш_токен_бота
   ```

5. **Инициализируйте базу данных:**
   ```bash
   python init_db.py
   ```

6. **Запустите приложение:**
   ```bash
   python run_local.py
   ```

7. **Откройте в браузере:**
   - Веб-интерфейс: http://localhost:8000
   - API документация: http://localhost:8000/docs

## Деплой на Railway

1. **Создайте бота в Telegram** через @BotFather
2. **Загрузите код на GitHub**
3. **Подключитесь к Railway** и выберите репозиторий
4. **Добавьте переменные окружения:**
   - `BOT_TOKEN=ваш_токен_бота`
   - `WEBAPP_URL=https://ваш-домен.railway.app`
5. **Настройте бота** у @BotFather:
   - Web App URL: `https://ваш-домен.railway.app`
   - Menu Button: "Расписание"

## Команды бота

- `/start` - Запуск бота
- `/schedule` - Показать расписание
- `/help` - Справка

## Структура проекта

```
├── app/                 # Основной код
├── static/              # Веб-интерфейс
├── requirements.txt     # Зависимости
├── runtime.txt          # Python 3.11
├── Procfile            # Команда запуска
├── init_db.py          # Инициализация БД
└── run_local.py        # Локальный запуск
```

## Поддержка

При проблемах:
1. Проверьте версию Python (должна быть 3.11)
2. Убедитесь, что токен бота корректный
3. Проверьте логи в Railway
4. Убедитесь, что все зависимости установлены 