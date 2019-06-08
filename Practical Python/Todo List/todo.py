import json
import os

def getTodoList():

	with open("todos.json", "r") as file:
		return json.load(file)


def updateTodoList(task, add=True):

	todoList = getTodoList()

	if add:
		todoList.append(task.capitalize())
	else:
		del todoList[task-1]

	with open("todos.json", "w") as file:
		json.dump(todoList, file)


def main():

	exitCodes = ["q", "quit", "exit", "done", "stop", "end"]
	
	while True:

		os.system("cls")

		todoList = getTodoList()

		for index, todo in enumerate(todoList, start=1):
			print("{}) {}".format(index, todo))

		print("\nCommands:")
		print("add <task>")
		print("rm <#>\n")

		prompt = input("> ").strip().lower()

		if prompt in exitCodes:
			break

		elif prompt.startswith("add "):
			task = prompt[4:]
			updateTodoList(task)

		elif prompt.startswith("rm "):
			index = int(prompt[3:])
			updateTodoList(index, False)



main()