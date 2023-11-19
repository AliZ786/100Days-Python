class Brain:
    def __init__(self, question_list):
        self.question_num = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(
            f'Q{self.question_num}: {current_question.text} (True/False): ')
        self.check_answer(user_answer)

    def still_has_questions(self):
        return self.question_num < len(self.question_list)

    def check_answer(self, user_answer):
        # Get the current question
        current_question = self.question_list[self.question_num - 1]
        correct_answer = current_question.answer

        user_answer = user_answer.lower()
        if user_answer == str(correct_answer).lower():
            self.score += 1
            print('Correct!')
        else:
            print("Incorrect")
        print(f'The correct answer was {correct_answer}.')
        print(f'Your current score is  {self.score}/{self.question_num}')
        print("\n")
