import json  # Импортируем модуль для работы с JSON / Import JSON module

tasks = []  # Список задач / Task list

def load_tasks():
    """Загружает задачи из tasks.json / Loads tasks from tasks.json"""
    global tasks
    try:
        with open("tasks.json", "r", encoding="utf-8") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []  # Если файл не существует, начинаем с пустого списка / Start with empty list if file doesn't exist

def add_task(task):
    """Добавляет задачу в список / Adds a task to the list"""
    if not task.strip():
        print("Ошибка: задача не может быть пустой. / Error: task cannot be empty.")
        return
    tasks.append({"task": task, "completed": False})
    print(f"Задача '{task}' добавлена. / Task '{task}' added.")

def view_tasks():
    """Показывает все задачи / Shows all tasks"""
    if not tasks:
        print("Список задач пуст. / Task list is empty.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else " "
        print(f"{i}. [{status}] {task['task']}")

def complete_task(task_index):
    """Переключает статус задачи / Toggles task completion status"""
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = not tasks[task_index - 1]["completed"]
        status = "выполнена" if tasks[task_index - 1]["completed"] else "не выполнена"
        print(f"Задача '{tasks[task_index - 1]['task']}' теперь {status}. / Task '{tasks[task_index - 1]['task']}' is now {status}.")
    else:
        print("Неверный индекс задачи. / Invalid task index.")

def delete_task(task_index):
    """Удаляет задачу по индексу / Deletes a task by index"""
    if 1 <= task_index <= len(tasks):
        task = tasks.pop(task_index - 1)
        print(f"Задача '{task['task']}' удалена. / Task '{task['task']}' deleted.")
    else:
        print("Неверный индекс задачи. / Invalid task index.")

def save_tasks():
    """Сохраняет задачи в tasks.json / Saves tasks to tasks.json"""
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def main():
    """Основная функция программы / Main program function"""
    load_tasks()  # Загружаем задачи при старте / Load tasks on start
    while True:
        print("\nТрекер задач / Task Tracker")
        print("1. Добавить задачу / Add task")
        print("2. Просмотреть задачи / View tasks")
        print("3. Отметить задачу / Toggle task")
        print("4. Удалить задачу / Delete task")
        print("5. Выход / Exit")
        choice = input("Выберите действие (1-5): / Choose an action (1-5): ")

        if choice == "1":
            task = input("Введите задачу: / Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                task_index = int(input("Введите номер задачи для переключения: / Enter task number to toggle: "))
                complete_task(task_index)
            except ValueError:
                print("Введите корректный номер. / Enter a valid number.")
        elif choice == "4":
            view_tasks()
            try:
                task_index = int(input("Введите номер задачи для удаления: / Enter task number to delete: "))
                delete_task(task_index)
            except ValueError:
                print("Введите корректный номер. / Enter a valid number.")
        elif choice == "5":
            save_tasks()  # Сохраняем задачи перед выходом / Save tasks before exiting
            print("Выход из программы. / Exiting program.")
            break
        else:
            print("Неверный выбор. Попробуйте снова. / Invalid choice. Try again.")

if __name__ == "__main__":
    main()