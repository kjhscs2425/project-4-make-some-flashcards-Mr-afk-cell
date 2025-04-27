import random
import json
with open("data.json", "r") as f:
    data = json.load(f)
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
incorrect_answers = 0
questions = list(flashcards.keys() )
random_questions = random.sample(questions, k= 5)
for question in random_questions:
    answer = input(question)
    if answer == flashcards[question]: 
        print("correct")
        correct_answers = correct_answers + 1
    else: 
        print("that's wrong")
        incorrect_answers = incorrect_answers + 1
data["correct"].append(correct_answers)
data["incorrect"].append(incorrect_answers)
if correct_answers >= 3:
    print("good job")
else:
    print("better luck next time")
print("you got " + str(correct_answers) + "/5")
print("total correct:" + str(sum(data["correct"])))
print("total incorrect:" + str(sum(data["incorrect"])))
with open("data.json", "w") as f:
     json.dump(data, f)