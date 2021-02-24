from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# creating the list of questions
question_bank = []
for x in range(0, len(question_data)):
    question = Question(question_data[x]['question'], question_data[x]['correct_answer'])
    question_bank.append(question)

# running the quiz using the quiz brain
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

# ending statements
print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
