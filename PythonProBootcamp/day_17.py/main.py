from question_model import Question
from data import question_data
from quiz_brain import Brain
question_bank = []
for i in question_data:
    q = Question(i["text"],i["answer"])
    question_bank.append(q)

quiz = Brain(question_bank)
while quiz.still_has_q():
    quiz.next_question()
print("Quiz completed!")
print(f"Your final score was {quiz.guees_right}/{len(question_bank)}.")