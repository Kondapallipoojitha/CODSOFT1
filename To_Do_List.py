import datetime

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date=None):
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'due_date': due_date,
            'completed': False
        }
        self.tasks.append(task)
        print(f'Task "{description}" added successfully!')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks found.')
        else:
            for task in self.tasks:
                status = 'Done' if task['completed'] else 'Not Done'
                due_date = task['due_date'] or 'No due date'
                print(f"{task['id']}. {task['description']} (Due: {due_date}, Status: {status})")

    def mark_as_done(self, task_id):
        task = self._get_task_by_id(task_id)
        if task:
            task['completed'] = True
            print(f'Task "{task["description"]}" marked as done!')
        else:
            print('Task not found.')

    def update_task(self, task_id, new_description, new_due_date=None):
        task = self._get_task_by_id(task_id)
        if task:
            task['description'] = new_description
            task['due_date'] = new_due_date
            print(f'Task updated successfully!')
        else:
            print('Task not found.')

    def delete_task(self, task_id):
        task = self._get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            print(f'Task "{task["description"]}" deleted successfully!')
        else:
            print('Task not found.')

    def _get_task_by_id(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None

def main():
    todo_list = ToDoList()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Update Task")
        print("5. Delete Task")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional, format: YYYY-MM-DD): ")
            if due_date:
                try:
                    due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
                except ValueError:
                    print("Invalid date format. Task will be added without a due date.")
                    due_date = None
            todo_list.add_task(description, due_date)

        elif choice == '2':
            todo_list.view_tasks()

        elif choice == '3':
            task_id = int(input("Enter task ID to mark as done: "))
            todo_list.mark_as_done(task_id)

        elif choice == '4':
            task_id = int(input("Enter task ID to update: "))
            new_description = input("Enter new task description: ")
            new_due_date = input("Enter new due date (optional, format: YYYY-MM-DD): ")
            if new_due_date:
                try:
                    new_due_date = datetime.datetime.strptime(new_due_date, "%Y-%m-%d").date()
                except ValueError:
                    print("Invalid date format. Task will be updated without a due date.")
                    new_due_date = None
            todo_list.update_task(task_id, new_description, new_due_date)

        elif choice == '5':
            task_id = int(input("Enter task ID to delete: "))
            todo_list.delete_task(task_id)

        elif choice == '0':
            print("Exiting To-Do List. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
