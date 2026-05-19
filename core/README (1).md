# 🧠 Quiz Bot — Telegram Intelligence Quiz

A Telegram chatbot built with Python and Django. The bot asks multiple-choice questions, saves player statistics, and loads new questions from an open API.

---

## 📸 Screenshots

**Welcome screen**
![Start command]([screenshots/start.png](https://github.com/egaashhka/quiz-bot/blob/main/core/screenshots/start.png))

**Quiz question with answer buttons**
![Quiz question](screenshots/quiz.png)

**Correct / incorrect answer**
![Answer result](screenshots/answer1.png)
![Answer result](screenshots/answer2.png)

**Player statistics**
![Score](screenshots/score.png)

**Top players leaderboard**
![Top players](screenshots/top.png)

**Game history**
![History](screenshots/history.png)

---

## 🛠 Technologies

| Technology | Purpose |
|---|---|
| Python 3.10+ | Main language |
| Django 4.2 | ORM and data models |
| SQLite | Database |
| python-telegram-bot 20+ | Telegram Bot API |
| Open Trivia Database API | Question source |
| requests | HTTP requests |
| asgiref | Async/sync compatibility |

---

## 📁 Project Structure

```
PythonProject/
├── bot.py                  # Main bot file
├── requirements.txt        # Dependencies
├── README.md               # Documentation
├── screenshots/            # Bot screenshots
├── core/
│   └── core/
│       ├── settings.py     # Django settings
│       ├── urls.py
│       └── wsgi.py
└── quiz/
    ├── models.py           # Models: Question, UserProfile, GameSession
    └── services.py         # Trivia API service
```

---

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/quiz-bot.git
cd quiz-bot
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🚀 Running the Bot

1. Open `bot.py` and insert your Telegram bot token:
```python
TOKEN = "YOUR_TOKEN_HERE"
```

2. Start the bot:
```bash
python bot.py
```

3. Open Telegram, find your bot and send `/start`

---

## 💬 Bot Commands

| Command | Description |
|---|---|
| `/start` | Register and get welcome message |
| `/quiz` | Start a quiz game |
| `/score` | My statistics |
| `/top` | Top 5 players leaderboard |
| `/history` | Last 5 games |
| `/add_random` | Add a random question from the internet |
| `/cancel` | Cancel current game |
| `/about` | About the bot |
| `/help` | List of all commands |

The bot also understands basic phrases like *"hi"*, *"how are you"*, *"thanks"*, *"bye"*.

---

## 📊 Data Models

- **Question** — question with three answer options and correct answer index
- **UserProfile** — player profile (telegram_id, name, total score, games played)
- **GameSession** — record of each completed game (score, total questions, date)

---

## 🔒 Error Handling

- Empty user input
- Unknown commands and messages
- Trivia API connection errors (timeout, HTTP errors)
- Duplicate questions when adding
- Database read/write errors

---

## 📝 Example Interaction

```
User: /start

Bot: 👋 Hello, Alex!
     🧠 Welcome to the intelligence quiz!
     /quiz — Start game
     /help — All commands

User: /quiz

Bot: ❓ Question 1/5:
     What is the capital of France?
     1. Berlin
     2. Madrid
     3. Paris

User: [clicks 3. Paris]

Bot: ✅ Correct!

[After all questions]

Bot: 🏆 Quiz finished!
     Result: 5 out of 5 (100%)
```

---

## 👨‍💻 Author

Developed as a final project for the discipline **"Python Programming"** 🎓
