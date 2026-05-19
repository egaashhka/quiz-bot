import requests
import random
import html


class TriviaQuizService:

    def __init__(self):
        self.url = "https://opentdb.com/api.php?amount=1&type=multiple"

    def get_random_question(self):
        try:
            response = requests.get(self.url, timeout=5)
            response.raise_for_status()
            data = response.json()['results'][0]

            question_text = html.unescape(data['question'])
            correct_answer = html.unescape(data['correct_answer'])
            incorrect_answers = [html.unescape(ans) for ans in data['incorrect_answers']]

            options = incorrect_answers[:2] + [correct_answer]
            random.shuffle(options)

            return {
                'text': question_text,
                'option_1': options[0],
                'option_2': options[1],
                'option_3': options[2],
                'answer': options.index(correct_answer) + 1
            }
        except requests.exceptions.ConnectionError:
            print("Ошибка: нет подключения к интернету")
        except requests.exceptions.Timeout:
            print("Ошибка: сервер не ответил вовремя")
        except requests.exceptions.HTTPError as e:
            print(f"Ошибка HTTP: {e}")
        except (KeyError, IndexError) as e:
            print(f"Ошибка при разборе ответа API: {e}")
        except Exception as e:
            print(f"Неизвестная ошибка при запросе к Trivia API: {e}")
        return None