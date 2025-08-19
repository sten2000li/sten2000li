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

def add_task(task, category="Без категории"):
    """Добавляет задачу с категорией / Adds a task with a category"""
    if not task.strip():
        print("Ошибка: задача не может быть пустой. / Error: task cannot be empty.")
        return
    tasks.append({"task": task, "completed": False, "category": category})
    print(f"Задача '{task}' (категория: {category}) добавлена. / Task '{task}' (category: {category}) added.")

def view_tasks():
    """Показывает все задачи / Shows all tasks"""
    if not tasks:
        print("Список задач пуст. / Task list is empty.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else " "
        print(f"{i}. [{status}] {task['task']} (категория: {task['category']})")

def view_incomplete_tasks():
    """Показывает только незавершённые задачи / Shows only incomplete tasks"""
    if not tasks:
        print("Список задач пуст. / Task list is empty.")
        return
    found = False
    for i, task in enumerate(tasks, 1):
        if not task["completed"]:
            print(f"{i}. [ ] {task['task']} (категория: {task['category']})")
            found = True
    if not found:
        print("Нет незавершённых задач. / No incomplete tasks.")

def view_completed_tasks():
    """Показывает только завершённые задачи / Shows only completed tasks"""
    if not tasks:
        print("Список задач пуст. / Task list is empty.")
        return
    found = False
    for i, task in enumerate(tasks, 1):
        if task["completed"]:
            print(f"{i}. [✓] {task['task']} (категория: {task['category']})")
            found = True
    if not found:
        print("Нет завершённых задач. / No completed tasks.")

def view_tasks_by_category():
    """Показывает задачи по категории / Shows tasks by category"""
    category = input("Введите категорию для фильтра: / Enter category to filter: ")
    if not tasks:
        print("Список задач пуст. / Task list is empty.")
        return
    found = False
    for i, task in enumerate(tasks, 1):
        if task["category"].lower() == category.lower() or (not category and task["category"] == "Без категории"):
            status = "✓" if task["completed"] else " "
            print(f"{i}. [{status}] {task['task']} (категория: {task['category']})")
            found = True
    if not found:
        print(f"Нет задач в категории '{category}'. / No tasks in category '{category}'.")

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
        print("5. Просмотреть незавершённые задачи / View incomplete tasks")
        print("6. Просмотреть завершённые задачи / View completed tasks")
        print("7. Просмотреть задачи по категории / View tasks by category")
        print("8. Выход / Exit")
        choice = input("Выберите действие (1-8): / Choose an action (1-8): ")

        if choice == "1":
            task = input("Введите задачу: / Enter task: ")
            category = input("Введите категорию (или Enter для 'Без категории'): / Enter category (or Enter for 'No category'): ")
            add_task(task, category if category else "Без категории")
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
            view_incomplete_tasks()
        elif choice == "6":
            view_completed_tasks()
        elif choice == "7":
            view_tasks_by_category()
        elif choice == "8":
            save_tasks()  # Сохраняем задачи перед выходом / Save tasks before exiting
            print("Выход из программы. / Exiting program.")
            break
        else:
            print("Неверный выбор. Попробуйте снова. / Invalid choice. Try again.")

if __name__ == "__main__":
    main()