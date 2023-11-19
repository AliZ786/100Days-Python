# Quiz Game

# 1. Import section
from data import question_data
from question import Question
from brain import Brain
import random  # Import the random module for shuffling questions

# 2. Declare variables
logo = """
 ██████╗ ██╗   ██╗██╗███████╗
██╔═══██╗██║   ██║██║╚══███╔╝
██║   ██║██║   ██║██║  ███╔╝ 
██║▄▄ ██║██║   ██║██║ ███╔╝  
╚██████╔╝╚██████╔╝██║███████╗
 ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝
                             
"""

print(logo)
print("WELCOME TO THE QUICK QUIZ GAME!")

EASY = 5
HARD = 10

# Mode selection
print("Select a mode:")
print("1. Easy")
print("2. Hard")
print("3. Endless")

mode = input("Enter the mode number (1, 2, or 3): ")

if mode == "1":
    num_questions = EASY
elif mode == "2":
    num_questions = HARD
else:
    num_questions = len(question_data)

# Shuffle the questions for variety
random.shuffle(question_data)

question_bank = []
for question in question_data[:num_questions]:
    question_text = question["text"]
    question_answer = question["answer"]
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

quiz = Brain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

percentage = float((quiz.score)/quiz.question_num)*100
print("You have completed the quiz!")
print(f'Your final score is: {quiz.score}/{quiz.question_num} - {percentage}%')
