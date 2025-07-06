# Schedule Bot - Telegram Mini App

Telegram бот для просмотра расписания с веб-интерфейсом, построенный на FastAPI и aiogram.

## 🚀 Быстрый деплой на Railway

### 1. Подготовка

1. Создайте бота в Telegram через [@BotFather](https://t.me/BotFather)
2. Получите токен бота
3. Создайте репозиторий на GitHub и загрузите код

### 2. Деплой на Railway

1. Перейдите на [Railway](https://railway.app)
2. Войдите через GitHub
3. Нажмите "New Project" → "Deploy from GitHub repo"
4. Выберите ваш репозиторий
5. Railway автоматически определит Python-приложение

### 3. Настройка переменных окружения

В настройках проекта Railway добавьте переменные:

```
BOT_TOKEN=ваш_токен_бота
WEBAPP_URL=https://ваш-домен.railway.app
```

### 4. Настройка бота

1. В настройках бота у @BotFather установите:
   - Web App URL: `https://ваш-домен.railway.app`
   - Menu Button: "Расписание"

## 📁 Структура проекта

```
├── app/
│   ├── bot/           # Логика Telegram бота
│   ├── core/          # Конфигурация и БД
│   ├── models/        # Модели SQLAlchemy
│   ├── schemas/       # Pydantic схемы
│   ├── services/      # Бизнес-логика
│   └── main.py        # Точка входа FastAPI
├── static/            # Веб-интерфейс
├── requirements.txt   # Зависимости Python
├── runtime.txt        # Версия Python (3.11)
└── Procfile          # Команда запуска для Railway
```

## 🛠 Технологии

- **Backend**: FastAPI, SQLAlchemy, aiogram 3.x
- **Frontend**: HTML, CSS, JavaScript, Telegram Web App API
- **База данных**: SQLite (автоматически на Railway)
- **Деплой**: Railway

## 📱 Функции

- Просмотр расписания по группам
- Веб-интерфейс в Telegram
- Команды бота: `/start`, `/schedule`, `/help`
- Адаптивный дизайн
- Поддержка тем Telegram

## 🔧 Локальная разработка

1. Установите Python 3.11
2. Создайте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Создайте файл `.env` с переменными окружения

5. Запустите приложение:
   ```bash
   uvicorn app.main:app --reload
   ```

## 📊 База данных

Приложение использует SQLite с автоматическими миграциями. Таблицы создаются при первом запуске.

### Модели:
- **Group**: Группы студентов
- **Schedule**: Расписание занятий

## 🌐 API Endpoints

- `GET /` - Веб-интерфейс
- `GET /api/schedule` - Все расписания
- `GET /api/schedule/{group}` - Расписание по группе
- `GET /health` - Проверка здоровья

## 🔒 Безопасность

- Все переменные окружения хранятся в Railway
- HTTPS автоматически настроен
- Валидация данных через Pydantic

## 📝 Логи

Логи доступны в панели Railway в разделе "Deployments".

## 🆘 Поддержка

При возникновении проблем:
1. Проверьте логи в Railway
2. Убедитесь, что токен бота корректный
3. Проверьте переменные окружения
4. Убедитесь, что используется Python 3.11

## 📄 Лицензия

MIT License 