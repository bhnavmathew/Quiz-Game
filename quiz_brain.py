class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number<len(self.question_list)

    def next_question(self):
            current_question = self.question_list[self.question_number]
            user = input(f'Q.{self.question_number+1}: {current_question.text} (True \ False) : ')
            self.check_answer(user, current_question.answer)

    def check_answer(self, user, correct_answer):
        if user.lower() == correct_answer.lower():
            print("Your answer is right!")
            print(f"The correct answer was: {correct_answer}")
            self.score += 1
            print(f"Your current score is: {self.score}/{self.question_number + 1}")
            self.question_number += 1
        else:
            print(f"That's wrong.")
            print(f"The correct answer was: {correct_answer}")
            print(f"Your current score is: {self.score}/{self.question_number+1}")
            self.question_number += 1

