#!/usr/bin/python3

import sys
import requests
import json


sender="Alina"
if len(sys.argv)<2:
	print("Bad config:", sys.argv)
	sys.exit()
config = json.load(open(sys.argv[1],"r"))
print(config)

user_ID=config["uid"]  #"98b363da-781d-4507-a5ee-2965bf55a7e9"
user_token = config["token"]


def add_todo(args):
	task_types= ["habit", "daily", "todo"]
	difficulties = {"trivial":"0.1","leicht":"1","mittel":"1.5","schwer":"2"}
	difficulty  = "1"
	task_type = "todo"
	
	if len(args) == 0:
		print("Zu wenige Argumente. \nBeispiel: stefan bring bier\nstefan schwer daily 50 liegestütz\nDie Reihenfolge ist wichtig!")
		return
	if len(args) > 1:
		if args[0] in difficulties:
			difficulty = difficulties[args[0]]
			args = args[1:]
		if args[0] in task_types:
			task_type = args[0]
			args = args[1:]
		
	task_text = ""
	for s in args:
		task_text+=s+" "
	#print("D:",difficulty,"T:",task_type, "Text:",task_text)
	task = {
    "text": task_text,
    "type": task_type,
    "notes": "Von " + sender+" hinzugefügt",
    "priority": difficulty}
	headers = {
		"x-api-user":user_ID,
		"x-api-key":user_token
			  }
	r = requests.post("https://habitica.com/api/v3/tasks/user",data=task,headers=headers)
	if r.ok:
		print("Erstellt")
	else:
		print("Fehler:", r.text)

add_todo(sys.argv[2:])
