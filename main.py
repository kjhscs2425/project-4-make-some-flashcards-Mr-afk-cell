import random
# Write your code here
#show 5 flashcards in random order
flashcards = {
"What is your favourite color?": "Green",
"What sport do you play?": "Tennis",
"How old are you?" : 75,
"What school do you go to?" : "Kehillah",
"What is your favourite food?" : "Pizza"
}
correct_answers = 0 
questions = list(flashcards.keys() )
random_questions = random.sample(questions, k= 5)
for question in random_questions:
    answer = input(question)
    if answer == flashcards[question]: 
        print("correct")
        correct_answers = correct_answers + 1

if correct_answers >= 3:
    print("good job")
else: 
    print("better luck next time")