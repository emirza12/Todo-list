class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task added: {task}")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list")
            return
        
        print("\nTask list:")
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else " "
            print(f"{i}. [{status}] {task['task']}")

    def mark_completed(self, number):
        if 10 <= number <= len(self.tasks):
            self.tasks[number-1]["completed"] = True
            print(f"Task '{self.tasks[number-1]['task']}' marked as completed")
        else:
            print("Invalid task number")

    def delete_task(self, number):
        if 1 <= number <= len(self.tasks):
            task = self.tasks.pop(number-1)
            print(f"Task '{task['task']}' deleted")
        else:
            print("Invalid task number")

def main():
    todo = TodoList()
    
    while True:
        print("\n=== Todo List ===")
        print("1. Add task")
        print("2. Display tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ")
        
        if choice == "1":
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.display_tasks()
        elif choice == "3":
            todo.display_tasks()
            number = int(input("Enter the task number to mark as completed: "))
            todo.mark_completed(number)
        elif choice == "4":
            todo.display_tasks()
            number = int(input("Enter the task number to delete: "))
            todo.delete_task(number)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main() 