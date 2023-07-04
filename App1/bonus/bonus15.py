import json

with open("questions.json", "r") as file:
    content = file.read()

data = json.loads(content)

score = 0
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)

    user_choice = int(input("Enter your awnser: "))

    question["user_choice"] = user_choice

for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Correct answer"
    else:
        result = "Wrong answer"

    message = f"{result} {index + 1} - Your answer: {question['user_choice']}, " \
              f"Correct answer: {question['correct_answer']}"

    print(message)

