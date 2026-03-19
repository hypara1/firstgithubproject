todo_list = []

running = True

while running == True:
  print("\n1. Add an item to list.")
  print("2. Remove an item from list.")
  print("3. Show all tasks in list.")
  print("4. Exit program.")
  choice = input("What would you like to do? ")

  if choice == "1":
    task = input("\nWrite a task to add to list. ").lower()
    if task in todo_list:
      print("Task already in list!")
    else:
      todo_list.append(task)
  elif choice == "2":
    if len(todo_list) >= 1:
      task = input("\nPick a task to remove. ")
      todo_list.remove(task)
    else:
      pass
  elif choice == "3":
    if todo_list:
      print("\nTodo list:\n")
      print(", ".join(todo_list) + ".")
    else:
      print("\nYour list is empty!")
  elif choice == "4":
    print("\nYou have exited the program!")
    running = False
  else:
    print("\nNot a valid syntax! Use the numbers 1-4!")
