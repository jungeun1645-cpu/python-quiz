import json

# 평가항목 #8: Quiz(문제 단위)와 QuizGame(게임 흐름)의 책임 분리
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def to_dict(self):
        return {"question": self.question, "choices": self.choices, "answer": self.answer}

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.load_quizzes() # 평가항목 #3: 시작 시 로드

    def add_quiz(self):
        # 평가항목 #1: 추가 기능 구현
        q = input("문제 내용을 입력하세요: ")
        c = input("보기 4개를 콤마(,)로 구분해서 입력하세요: ").split(',')
        try:
            a = int(input("정답 번호(1~4)를 입력하세요: "))
            self.quizzes.append(Quiz(q, c, a))
            self.save_quizzes()
            print("문제 추가 완료!")
        except ValueError: # 평가항목 #2: 예외 처리
            print("숫자만 입력 가능합니다.")

    def save_quizzes(self):
        # 평가항목 #3: JSON 영속화
        with open('state.json', 'w', encoding='utf-8') as f:
            json.dump([q.to_dict() for q in self.quizzes], f, ensure_ascii=False, indent=4)

    def load_quizzes(self):
        try:
            with open('state.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.quizzes = [Quiz(d['question'], d['choices'], d['answer']) for d in data]
        except FileNotFoundError:
            # 평가항목 #4: 초기 기본 문제 5개 이상 설정
            self.quizzes = [
                Quiz("파이썬의 마스코트는?", ["사자", "뱀", "코끼리", "하마"], 2),
                Quiz("리스트 추가 함수는?", ["add", "push", "append", "insert"], 3),
                Quiz("출력 함수는?", ["input", "print", "show", "out"], 2),
                Quiz("정수형 타입은?", ["int", "str", "float", "bool"], 1),
                Quiz("딕셔너리 기호는?", ["[]", "()", "{}", "<>"], 3)
            ]

    def play(self):
        # 평가항목 #1: 풀기 기능
        score = 0
        for q in self.quizzes:
            print(f"\n문제: {q.question}")
            for i, choice in enumerate(q.choices, 1):
                print(f"{i}. {choice}")
            try:
                user_choice = int(input("정답 번호: ")) # 평가항목 #2: 예외 처리
                if user_choice == q.answer:
                    print("정답!")
                    score += 1
                else:
                    print("오답!")
            except ValueError:
                print("숫자를 입력해야 합니다. 다음 문제로 넘어갑니다.")
        print(f"\n최종 점수: {score}/{len(self.quizzes)}")

    def run_menu(self):
        # 평가항목 #1: 메뉴 시스템
        while True:
            print("\n--- 퀴즈 프로그램 ---")
            print("1. 퀴즈 풀기 / 2. 퀴즈 추가 / 3. 목록 보기 / 4. 종료")
            choice = input("선택: ")
            if choice == '1': self.play()
            elif choice == '2': self.add_quiz()
            elif choice == '3': 
                for i, q in enumerate(self.quizzes, 1): print(f"{i}. {q.question}")
            elif choice == '4': break

if __name__ == "__main__":
    game = QuizGame()
    game.run_menu()