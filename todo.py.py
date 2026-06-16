todos = []
 
while True:
    print("\nWhat do you want to do?")
    print("1. See my tasks")
    print("2. Add a task")
    print("3. Done with a task")
    print("4. Exit")
 
    choice = input("\nPick a number: ")
 
    if choice == "1":
        print("\nHere's what you've got:" if todos else "\nNothing on your list yet!")
        for i, task in enumerate(todos, 1):
            print(f"  {i}. {task}")
 
    elif choice == "2":
        task = input("What do you need to do? ")
        todos.append(task)
        print(f"Got it! Added '{task}' to your list.")
 
    elif choice == "3":
        if not todos:
            print("Your list is already empty!")
        else:
            for i, task in enumerate(todos, 1):
                print(f"  {i}. {task}")
            num = input("Which one did you finish? ")
            done = todos.pop(int(num) - 1)
            print(f"Nice work finishing '{done}'!")
 
    elif choice == "4":
        print("See you later! Go get things done 💪")
        break