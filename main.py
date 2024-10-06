from data import question_data
from question_model import Question
from quiz_brain import QuizBuzz

question_bank = []


for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text , question_answer)
    question_bank.append(new_question)

print(question_bank)


quiz = QuizBuzz(question_bank)

while quiz.still_has_questions() is True:
    quiz.next_question()
if  quiz.still_has_questions() is False:
    print("you have completed all the quizes")
    