#https://opentdb.com/api_config.php

#pip install requests
import requests
import random


parameters = {"amount" : "1",
"difficulty" : "easy",
"type" : "multiple"}

trivia_request = requests.get('https://opentdb.com/api.php?', parameters)

#explain 200 and 404
#print(trivia_request.status_code)


#see as text and learn what to replace
#print(trivia_request.text)

#make into json
trivia_json  = trivia_request.json()
#see json and realize that we only want 'results'
#print(trivia_json)

trivia_json = trivia_json['results'][0]
#see again
#print(trivia_json)

print(trivia_json['question'])

answers = trivia_json['incorrect_answers'] + [trivia_json['correct_answer']]
#look to see
#print(answers)

random.shuffle(answers)

for x in range(1,5):
  print(str(x) + ". " + answers[x-1])

answer = input("Enter the correct number: ")
if answers[(int(answer)-1)] == trivia_json["correct_answer"]:
  print("Correct")
else:
  print("Incorrect")

