# a dictionary that stores questions and answer
# have a variable that tracks the score of the player 
# loop through dictionary using key value pairs  
# display each question to the user & allow them to answer
# tell them if thay are right or wrong
# show final result when quiz is completed

quiz={
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question4": {
        "question": "What is the capital of India?",
        "answer": "New Delhi"
    },
    "question5": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
}

score=0

for key, value in quiz.items():
    print(value["question"])
    answer=input("Answer- ")

    if answer.lower()== value['answer'].lower():
        print("Correct")
        score+=1
        print("Your score is: ", str(score))
        print("")
        print("")
    else:
        print("Wrong")
        print("The answer is: " + value["answer"])
        print("Your score is: " + str(score))
        print("")
        print("")


print("Your final score is " +str(score) + " out of 5.")
print("Congratulations.........")
print("Your percentage is "+ str(int(score/5 * 100)) + "%")