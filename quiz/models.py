from django.db import models


class Question(models.Model):
    text = models.TextField()
    option_1 = models.CharField(max_length=200)
    option_2 = models.CharField(max_length=200)
    option_3 = models.CharField(max_length=200)
    answer = models.IntegerField(help_text="Введите 1, 2 или 3")

    def __str__(self):
        return self.text[:50]


class UserProfile(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    total_games = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} (@{self.username})"

    @property
    def average_score(self):
        if self.total_games == 0:
            return 0
        return round(self.total_score / self.total_games, 1)


class GameSession(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="sessions")
    score = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=0)
    played_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} — {self.score}/{self.total_questions} ({self.played_at.strftime('%d.%m.%Y')})"