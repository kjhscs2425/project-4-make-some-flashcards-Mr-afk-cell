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
"What is your favourite food?" : "Pizza", 
"What state were you born in?" : "California" ,
"Where is the Grand Canyon?" : "Arizona" , 
"What do you want to be when you grow up": "Firefighter" ,
"What is your least favourite subject" : "Math" ,
"How many siblings do you have?" : "1" ,
"When did Abe Lincoln become president?" : "1861" ,
"Who was the only president born on the 4th of July?" : "Calvin Collidge",
"How many presidents died on the 50th anniversary of the 4th of July?" : "2",
"What is the largest mammal?" : "Blue whale",
"What is the top speed of a cheetah?" : "75 MPH",
"What are the only living dinosaurs?" : "Birds",
"What is the largest shark?" : "Whale shark" ,
"What are the largest trees?" : "Giant sequoia" ,
"What is the fastest bird?" : "Peregrine falcon" ,
"How many questions are in this quiz?" : "20"
}
num_questions = int(input("how many questions would you like to be asked?:"))
num_questions = min(20, max(1, num_questions))
correct_answers = 0 
incorrect_answers = 0
questions = list(flashcards.keys() )
random_questions = random.sample(questions, k= num_questions)
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
if correct_answers >= num_questions * 3/5:
    print("good job")
else:
    print("better luck next time")
print("you got " + str(correct_answers) + "/" + str(num_questions))
print("total correct:" + str(sum(data["correct"])))
print("total incorrect:" + str(sum(data["incorrect"])))
with open("data.json", "w") as f:
     json.dump(data, f)