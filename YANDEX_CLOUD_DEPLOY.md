# 🚀 Деплой на Yandex Cloud

## Подготовка

1. **Создайте аккаунт на Yandex Cloud**
2. **Создайте платежный аккаунт**
3. **Создайте облако и каталог**

## Шаг 1: Создание Container Registry

1. **В консоли Yandex Cloud** перейдите в "Container Registry"
2. **Создайте реестр:**
   - Название: `schedule-bot-registry`
   - Тип: `Docker Hub`
3. **Запомните ID реестра** (например: `crp1234567890abcdef`)

## Шаг 2: Сборка и загрузка образа

**Скопируйте и выполните команды:**

```bash
# Авторизация в Container Registry
yc container registry configure-docker

# Сборка образа
docker build -t cr.yandex/crp1234567890abcdef/schedule-bot:latest .

# Загрузка образа
docker push cr.yandex/crp1234567890abcdef/schedule-bot:latest
```

## Шаг 3: Создание Container Instance

1. **В консоли Yandex Cloud** перейдите в "Container Instance"
2. **Создайте инстанс:**
   - Название: `schedule-bot`
   - Образ: `cr.yandex/crp1234567890abcdef/schedule-bot:latest`
   - Память: 1 GB
   - vCPU: 1
   - Порт: 8000

3. **Добавьте переменные окружения:**
   - `BOT_TOKEN=7613496891:AAG8Jb75aUPvy7Jh8v_Nk91QGBxrGeJIEKQ`
   - `DATABASE_URL=sqlite:///./schedule.db`
   - `DEBUG=False`
   - `WEBAPP_URL=https://ваш-домен.yandexcloud.net`

## Шаг 4: Настройка Load Balancer (опционально)

1. **Создайте Application Load Balancer**
2. **Настройте backend group** с вашим Container Instance
3. **Настройте HTTP router** на порт 8000
4. **Получите публичный IP**

## Шаг 5: Настройка бота

1. **В @BotFather** обновите Web App URL:
   - `/mybots` → выберите бота → `Bot Settings` → `Menu Button`
   - URL: `https://ваш-домен.yandexcloud.net`

## Локальное тестирование

**Для тестирования локально:**

```bash
# Создайте .env файл
echo "BOT_TOKEN=7613496891:AAG8Jb75aUPvy7Jh8v_Nk91QGBxrGeJIEKQ" > .env

# Запустите через Docker Compose
docker-compose up --build
```

## Мониторинг

- **Логи:** В консоли Container Instance
- **Метрики:** В разделе "Monitoring"
- **Масштабирование:** Автоматическое или ручное

## Стоимость

- **Container Instance:** ~300-500 руб/мес
- **Container Registry:** ~100 руб/мес
- **Load Balancer:** ~200 руб/мес
- **Трафик:** ~1-2 руб/GB

## Преимущества Yandex Cloud

- ✅ Российская платформа
- ✅ Оплата российскими картами
- ✅ Низкая задержка в России
- ✅ Интеграция с другими сервисами Яндекса
- ✅ Поддержка на русском языке 