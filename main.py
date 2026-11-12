# 퀴즈 하나하나의 정보를 담는 '양식'이에요.
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question  # 문제 내용
        self.choices = choices    # 보기 (리스트)
        self.answer = answer      # 정답 번호

    # 문제를 화면에 보여주는 기능
    def display_quiz(self):
        print(f"\n[문제] {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")

    # 사용자가 입력한 답이 맞는지 확인하는 기능
    def check_answer(self, user_answer):
        return str(self.answer) == str(user_answer)

# 프로그램이 잘 돌아가는지 확인해봅시다!
if __name__ == "__main__":
    # 1. 문제 만들기
    q1 = Quiz("파이썬의 마스코트 동물은?", ["사자", "뱀", "코끼리", "하마"], 2)
    
    # 2. 문제 보여주기
    q1.display_quiz()
    
    # 3. 정답 체크 (2번을 입력했다고 가정)
    print(f"결과: {q1.check_answer(2)}") 


# 1. 퀴즈 객체 생성
q1 = Quiz(
    "파이썬에서 리스트에 요소를 추가하는 메서드는?",
    ["add()", "append()", "insert()", "push()"],
    2 # 정답은 2번 append()
)

# 2. 문제 보여주기
q1.display_quiz()

# 3. 사용자로부터 답 입력받기
# input()은 사용자의 입력을 '문자열'로 받기 때문에 int()로 숫자로 바꿔줍니다.
user_choice = int(input("정답 번호를 입력하세요: "))

# 4. 정답 확인 및 결과 출력
if q1.check_answer(user_choice):
    print("✅ 정답입니다! 정말 잘하시네요!")
else:
    print("❌ 아쉽네요, 오답입니다. 다시 한번 생각해보세요!")
