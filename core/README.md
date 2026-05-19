# 🧠 Quiz Bot — Интеллектуальная викторина

Telegram-бот викторина, разработанный на Python + Django. Бот задаёт вопросы с вариантами ответов, сохраняет статистику игроков и подгружает новые вопросы из открытого API.

---

## 🛠 Используемые технологии

| Технология | Назначение |
|---|---|
| Python 3.10+ | Основной язык |
| Django 4.2 | ORM и модели данных |
| SQLite | База данных |
| python-telegram-bot 20+ | Telegram Bot API |
| Open Trivia Database API | Источник вопросов |
| requests | HTTP-запросы |
| asgiref | Async/sync совместимость |

---

## 📁 Структура проекта

```
core/
├── bot.py                  # Основной файл бота
├── requirements.txt        # Зависимости
├── README.md               # Документация
├── core/
│   ├── settings.py         # Настройки Django
│   ├── urls.py
│   └── wsgi.py
└── quiz/
    ├── models.py           # Модели: Question, UserProfile, GameSession
    └── services.py         # Сервис работы с Trivia API
```

---

## ⚙️ Установка

1. Клонируй репозиторий:
```bash
git clone https://github.com/your-username/quiz-bot.git
cd quiz-bot
```

2. Создай и активируй виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

3. Установи зависимости:
```bash
pip install -r requirements.txt
```

4. Примени миграции базы данных:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🚀 Запуск

1. Открой файл `bot.py` и замени токен:
```python
TOKEN = "ВАШ_ТОКЕН_ЗДЕСЬ"
```

2. Запусти бота:
```bash
python bot.py
```

---

## 💬 Команды бота

| Команда | Описание |
|---|---|
| `/start` | Регистрация и приветствие |
| `/quiz` | Начать викторину |
| `/score` | Моя статистика |
| `/top` | Топ-5 игроков |
| `/history` | Последние 5 игр |
| `/add_random` | Добавить вопрос из интернета |
| `/cancel` | Отменить текущую игру |
| `/about` | Информация о боте |
| `/help` | Список всех команд |

---

## 📊 Модели данных

- **Question** — вопрос с тремя вариантами ответа
- **UserProfile** — профиль игрока (telegram_id, имя, общий счёт)
- **GameSession** — запись каждой сыгранной игры (счёт, дата)

---

## 🔒 Обработка ошибок

- Пустой ввод от пользователя
- Неизвестные команды и сообщения
- Ошибки подключения к Trivia API (timeout, HTTP-ошибки)
- Дублирующиеся вопросы при добавлении
- Ошибки чтения/записи в базу данных

---

## 📸 Примеры работы

**Начало игры `/quiz`:**
```
❓ Вопрос 1/5:
What is the capital of France?

1. Berlin
2. Madrid
3. Paris        ← правильный ответ
```

**После ответа:**
```
✅ Правильно!
```

**Итог:**
```
🏆 Викторина окончена!
Результат: 5 из 5 (100%)
```
