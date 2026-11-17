# Python Quiz Game

Python 기초 문법을 학습하기 위해 제작한 콘솔 기반 객관식 퀴즈 게임입니다.

## 프로젝트 제작 목적
Python의 조건문, 반복문, 함수, 클래스, 파일 입출력 및 예외 처리를 직접 구현하고 Git/GitHub 협업 과정을 연습하기 위해 제작했습니다.

## 실행 환경
- Python 3.10 이상
- 외부 라이브러리 설치 불필요 (표준 라이브러리만 사용)

## 실행 방법
```bash
python main.py
```

## 주요 기능
1. 퀴즈 풀기: 기본 문제 5개, 정답 판별 및 점수 계산
2. 문제 추가: 문제와 보기 4개, 정답 번호 입력
3. 문제 목록: 등록된 모든 문제 확인
4. 최고 점수: 지금까지의 최고 점수 조회
5. 종료: 저장 후 프로그램 종료

## 기술 구현
- Quiz 클래스: 문제 관리, 목록 출력, 퀴즈 진행
- QuizGame 클래스: 메뉴 실행, 파일 저장 및 불러오기
- JSON 기반 데이터 영구 저장
- 입력값 검증 및 예외 처리
- UTF-8 인코딩 지원

## 프로젝트 구조
```text
python-quiz-game/
├── main.py
├── state.json
├── README.md
├── .gitignore
└── docs/
    └── screenshots/
```

## 데이터 저장 구조
state.json 파일에 문제와 최고 점수를 저장합니다.

```json
{
  "questions": [
    {
      "question": "Python에서 화면에 글자를 출력하는 함수는?",
      "options": ["input()", "print()", "open()", "len()"],
      "answer": 2
    }
  ],
  "high_score": 50
}
```

위 JSON은 데이터 형식 예시입니다. 실제 저장 파일에는 기본 문제 5개 이상이 포함됩니다.

## 예외 처리
- 메뉴 및 정답 입력 범위 검사
- 빈 문제 및 보기 입력 방지
- 저장 파일이 없을 때 기본 데이터 생성
- 손상된 JSON 파일에 대한 복구 처리
- 파일 읽기·쓰기 오류 안내
- Ctrl+C 및 EOF 입력 시 안전한 종료

## Git 및 GitHub 학습
git init, add, commit, push, pull, checkout, clone 명령어를 활용하고 브랜치 병합을 실습합니다.

## 실행 증빙
실행 화면은 docs/screenshots/ 폴더에 정리합니다.
