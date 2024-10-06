# from question_model import Question
# from main import question_bank
# from main import question_bank
#
# question_list = question_bank
# question_number = 0
# class QuizBrain():
#
#     def __init__(self , question_number , question_list):
#         self.question_number = question_number
#         self.question_list = question_list
#
#     def next_question(self):
#         print(input(question_list[question_number]))
#
#
#     next_question(1)

class QuizBuzz():
    def __init__(self , q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}:{current_question.text} 'True' or 'False':")
        self.check_answer(user_answer , current_question.answer)


    def check_answer(self , user_answer , correct_answer ):
        if user_answer.lower() == correct_answer.lower():
            print("your answer is correct")
            self.score += 1
            print(f"your score is {self.score}/{(self.question_number)}")
            return True
        else:
            print("your answer is wrong")
            print(f"your score is {self.score}/{(self.question_number)}")
            return False
        print(f"the correct answer is {correct_answer}")







