# Quiz Game Test Checklist

- [x] Display five default questions
- [x] Show four options per question
- [x] Calculate 50 points for five correct answers
- [x] Add a new question
- [x] Exit through menu option 5
- [ ] Verify saved data after restarting
- [ ] Verify invalid input handling
- [ ] Verify corrupted JSON recovery

## Automated Test Results

Command: python -m unittest discover -p "test_quiz.py" -v

- [x] Default questions
- [x] Add question
- [x] Invalid input validation
- [x] JSON save
- [x] Corrupted JSON recovery
- [x] JSON reload after saving

Result: 6 tests passed (OK).
