tasks = []
completed_tasks = []

print("THE TO DO LIST")
print()
print("1. ADD TASK\n2. UPDATE TASK\n3. TRACK TRASKS")
   

while True:
   task = int(input("Choose a number from the menu above: "))
   if task == 1:
      add = input("Enter task: ")
      if add in tasks:
         print(f"{add} already exists")
      else:
         tasks.append(add)
         print(f"{add} added successfully")
      print("Current Tasks")
      print(tasks)
      exit_choice = input("Press 'q' to quit or any other key to continue: ")
      if exit_choice.lower() == 'q':
        break
   

   elif task == 2:
      print("ACTION MENU")
      menu = print("1. Delete\n2. Mark as Completed\n3. Replace task")
      action = int(input("Choose a number from the Action menu above: "))
      if action == 1:
         delete_task = input("Enter Task you'd like to delete: ")
         if delete_task in tasks:
            tasks.remove(delete_task)
         else:
            print(f"{delete_task} does not exist")
         print("Current Tasks:")
         print(tasks)
         continue
      
      elif action == 2:
         print("Tasks:")
         for index, t in enumerate(tasks, start=1):
            print(f"{index}. {t}")
         mark = int(input("Enter the number of the task to mark as complete: "))
         if 1 <= mark <= len(tasks):
            completed_task = tasks.pop(mark - 1)
            completed_tasks.append(completed_task)
            print(f"Task '{completed_task}' marked as complete.")
         else:
            print("Invalid task number.")
         exit_choice = input("Press 'q' to quit or any other key to continue: ")
         if exit_choice.lower() == 'q':
            break
         
      elif action == 3:
         task_replace = input("Enter a task you'd like to replace: ")
         if task_replace in tasks:
            replace_index = tasks.index(task_replace)
            new_task = input("Enter the new task: ")
            tasks[replace_index] = new_task
            print(f"Task '{task_replace}' replaced with '{new_task}' successfully.")
         else:
            print(f"{task_replace} does not exist in the list.")
            
            
   elif task == 3:
     print("Your Current List")
     print(tasks)
     print()
     print("Complete Tasks")
     print(completed_tasks)
     

   else:
      break
