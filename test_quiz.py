import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
from main import Quiz, QuizGame, ask_number

class QuizTests(unittest.TestCase):
    def test_default_questions(self):
        self.assertEqual(len(Quiz().questions), 5)

    def test_add_question(self):
        quiz = Quiz()
        quiz.add("Git 명령어는?", ["add", "commit", "push", "pull"], 2)
        self.assertEqual(len(quiz.questions), 6)

    def test_invalid_input(self):
        with patch("builtins.input", side_effect=["", "abc", "9", "2"]):
            self.assertEqual(ask_number("번호: ", 1, 4), 2)

    def test_json_persistence(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "state.json"
            with patch.object(QuizGame, "load", return_value=None):
                game = QuizGame()
            game.path = path
            game.high_score = 50
            game.save()
            self.assertEqual(json.loads(path.read_text(encoding="utf-8"))["high_score"], 50)

    def test_corrupted_json(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "state.json"
            path.write_text("{invalid", encoding="utf-8")
            with patch.object(QuizGame, "load", return_value=None):
                game = QuizGame()
            game.path = path
            game.load()
            self.assertEqual(len(game.quiz.questions), 5)

if __name__ == "__main__":
    unittest.main()

class PersistenceTests(unittest.TestCase):
    def test_reload_saved_data(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / "state.json"
            with patch.object(QuizGame, "load", return_value=None):
                game = QuizGame()
            game.path = path
            game.high_score = 50
            game.quiz.add("Git 명령어는?", ["add", "commit", "push", "pull"], 2)
            game.save()

            with patch.object(QuizGame, "load", return_value=None):
                restored = QuizGame()
            restored.path = path
            restored.load()

            self.assertEqual(restored.high_score, 50)
            self.assertEqual(len(restored.quiz.questions), 6)
