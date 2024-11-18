class QuizBrain:

    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        no_of_questions = len(self.question_list)
        if self.question_number < no_of_questions:
            return True
        else:
            return False

    def next_question(self):
        question_asked = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question_asked.question}. (True/False): ").lower()
        self.check_answer(user_answer, question_asked.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("You got it right!!")
        else:
            print("That's wrong!!")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")

    def quiz_completed(self):
        print("You've completed the quiz!!")
        print(f"Your Final score is {self.score}/{self.question_number}")
