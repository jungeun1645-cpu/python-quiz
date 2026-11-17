import json
from pathlib import Path

DEFAULT_QUESTIONS = [
    {"question": "Python에서 화면에 글자를 출력하는 함수는?", "options": ["input()", "print()", "open()", "len()"], "answer": 2},
    {"question": "Python에서 사용자 입력을 받는 함수는?", "options": ["print()", "len()", "input()", "type()"], "answer": 3},
    {"question": "Python에서 리스트를 만드는 기호는?", "options": ["[]", "{}", "()", "<>"], "answer": 1},
    {"question": "반복문을 나타내는 키워드는?", "options": ["if", "for", "def", "class"], "answer": 2},
    {"question": "함수를 정의하는 키워드는?", "options": ["return", "import", "def", "break"], "answer": 3},
]


def valid_question(item):
    return (isinstance(item, dict) and isinstance(item.get("question"), str)
            and bool(item["question"].strip())
            and isinstance(item.get("options"), list)
            and len(item["options"]) == 4
            and all(isinstance(v, str) and bool(v.strip()) for v in item["options"])
            and type(item.get("answer")) is int and 1 <= item["answer"] <= 4)


class Quiz:
    def __init__(self, questions=None):
        self.questions = questions if questions is not None else [q.copy() for q in DEFAULT_QUESTIONS]

    def add(self, question, options, answer):
        self.questions.append({"question": question, "options": options, "answer": answer})

    def show(self):
        for index, item in enumerate(self.questions, 1):
            print(f"{index}. {item['question']}")
            for number, option in enumerate(item["options"], 1):
                print(f"   {number}) {option}")

    def play(self):
        score = 0
        for index, item in enumerate(self.questions, 1):
            print(f"\n문제 {index}/{len(self.questions)}: {item['question']}")
            for number, option in enumerate(item["options"], 1):
                print(f"{number}. {option}")
            answer = ask_number("정답 (1~4): ", 1, 4)
            if answer == item["answer"]:
                score += 10
                print("정답! +10점")
            else:
                print(f"오답! 정답은 {item['answer']}번입니다.")
        print(f"\n최종 점수: {score}점 / {len(self.questions) * 10}점")
        return score


def ask_number(prompt, minimum, maximum):
    while True:
        value = input(prompt).strip()
        if value.isdecimal() and minimum <= int(value) <= maximum:
            return int(value)
        print(f"{minimum}~{maximum} 사이의 숫자를 입력하세요.")


class QuizGame:
    def __init__(self):
        self.path = Path(__file__).with_name("state.json")
        self.quiz = Quiz()
        self.high_score = 0
        self.load()

    def load(self):
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                raise ValueError("잘못된 데이터 형식")
            questions = data.get("questions")
            high_score = data.get("high_score")
            if (not isinstance(questions, list) or len(questions) < 5
                    or not all(valid_question(q) for q in questions)
                    or type(high_score) is not int or high_score < 0):
                raise ValueError("저장 데이터 검증 실패")
            self.quiz = Quiz(questions)
            self.high_score = high_score
        except FileNotFoundError:
            self.save()
        except (OSError, UnicodeError, ValueError, TypeError) as error:
            print(f"저장 파일을 읽지 못해 기본 문제로 시작합니다: {error}")

    def save(self):
        try:
            data = {"questions": self.quiz.questions, "high_score": self.high_score}
            self.path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        except (OSError, UnicodeError, TypeError) as error:
            print(f"저장 실패: {error}")

    def add_question(self):
        question = input("새 문제: ").strip()
        while not question:
            print("문제를 비워둘 수 없습니다.")
            question = input("새 문제: ").strip()
        options = []
        for number in range(1, 5):
            option = input(f"보기 {number}: ").strip()
            while not option:
                print("보기를 비워둘 수 없습니다.")
                option = input(f"보기 {number}: ").strip()
            options.append(option)
        answer = ask_number("정답 번호 (1~4): ", 1, 4)
        self.quiz.add(question, options, answer)
        self.save()
        print("문제가 추가됐습니다.")

    def run(self):
        try:
            while True:
                print("\n=== Python 퀴즈 게임 ===")
                print("1. 퀴즈 풀기  2. 문제 추가  3. 문제 목록  4. 최고 점수  5. 종료")
                choice = ask_number("메뉴 선택 (1~5): ", 1, 5)
                if choice == 1:
                    score = self.quiz.play()
                    if score > self.high_score:
                        self.high_score = score
                        print("새로운 최고 점수입니다!")
                    self.save()
                elif choice == 2:
                    self.add_question()
                elif choice == 3:
                    self.quiz.show()
                elif choice == 4:
                    print(f"최고 점수: {self.high_score}점")
                else:
                    self.save()
                    print("게임을 종료합니다.")
                    break
        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되어 게임을 종료합니다.")
            self.save()


if __name__ == "__main__":
    QuizGame().run()
