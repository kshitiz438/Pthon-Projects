from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question_text = data["question"]
    question_answer = data["correct_answer"]
    new_question = QuestionModel(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.quiz_completed()

