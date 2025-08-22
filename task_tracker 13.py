import json  # Импортируем модуль для работы с JSON / Import JSON module
from datetime import datetime  # Импортируем модуль для работы с датой / Import module for date handling

tasks = []  # Список задач / Task list

def load_tasks():
    """Загружает задачи из tasks.json / Loads tasks from tasks.json"""
    global tasks
    try:
        with open("tasks.json", "r", encoding="utf-8") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []  # Если файл не существует, начинаем с пустого списка / Start with empty list if file doesn't exist

def add_task(task, category="Без категории", priority="Средний"):
    """Добавляет задачу с категорией, приоритетом и датой создания / Adds a task with a category, priority, and creation date"""
    if not task.strip():
        print("Ошибка: задача не может быть пустой. / Error: task cannot be empty.")
        return
    priorities = ["Низкий", "Средний", "Высокий"]
    if priority not in priorities:
        priority = "Средний"
    tasks.append({
        "task": task,
        "completed": False,
        "category": category,
        "priority": priority,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    print(f"Задача '{task}' (категория: {category}, приоритет: {priority}) добавлена. / Task '{task}' (category: {category}, priority: {priority}) added.")

def view_tasks():
    """Показывает все задачи, отсортированные по приоритету / Shows all tasks sorted by priority"""
    if not tasks:
        print("Список задач пуст. / Task list is empty.")
        return
    priority_order = {"Высокий": 1, "Средний": 2, "Низкий": 3}
    sorted_tasks = sorted(tasks, key=lambda x: priority_order.get(x["priority"], 2))
    for i, task in enumerate(sorted_tasks, 1):
        status = "✓" if task["completed"] else " "
        print(f"{i}. [{status}] {task['task']} (категория: {task['category']}, приоритет: {task['priority']}, создано: {task['created_at']})")

def view_incomplete_tasks():
    """Показывает только незавершённые задачи, отсортированные по приоритету / Shows only incomplete tasks sorted by priority"""
    if not tasks:
        print("Список задач пуст. / Task list is empty.")
        return
    priority_order = {"Высокий": 1, "Средний": 2, "Низкий": 3}
    sorted_tasks = sorted([task for task in tasks if not task["completed"]], key=lambda x: priority_order.get(x["priority"], 2))
    if not sorted_tasks:
        print("Нет незавершённых задач. / No incomplete tasks.")
        return
    for i, task in enumerate(sorted_tasks, 1):
        print(f"{i}. [ ] {task['task']} (категория: {task['category']}, приоритет: {task['priority']}, создано: {task['created_at']})")

def view_completed_tasks():
    """Показывает только завершённые задачи, отсортированные по приоритету / Shows only completed tasks sorted by priority"""
    if not tasks:
        print("Список задач пуст. / Task list is empty.")
        return
    priority_order = {"Высокий": 1, "Средний": 2, "Низкий": 3}
    sorted_tasks = sorted([task for task in tasks if task["completed"]], key=lambda x: priority_order.get(x["priority"], 2))
    if not sorted_tasks:
        print("Нет завершённых задач. / No completed tasks.")
        return
    for i, task in enumerate(sorted_tasks, 1):
        print(f"{i}. [✓] {task['task']} (категория: {task['category']}, приоритет: {task['priority']}, создано: {task['created_at']})")

def view_tasks_by_category():
    """Показывает задачи по категории, отсортированные по приоритету / Shows tasks by category sorted by priority"""
    category = input("Введите категорию для фильтра: / Enter category to filter: ")
    if not tasks:
        print("Список задач пуст. / Task list is empty.")
        return
    priority_order = {"Высокий": 1, "Средний": 2, "Низкий": 3}
    sorted_tasks = sorted(
        [task for task in tasks if task["category"].lower() == category.lower() or (not category and task["category"] == "Без категории")],
        key=lambda x: priority_order.get(x["priority"], 2)
    )
    if not sorted_tasks:
        print(f"Нет задач в категории '{category}'. / No tasks in category '{category}'.")
        return
    for i, task in enumerate(sorted_tasks, 1):
        status = "✓" if task["completed"] else " "
        print(f"{i}. [{status}] {task['task']} (категория: {task['category']}, приоритет: {task['priority']}, создано: {task['created_at']})")

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
            priority = input("Введите приоритет (Низкий, Средний, Высокий или Enter для 'Средний'): / Enter priority (Low, Medium, High, or Enter for 'Medium'): ")
            add_task(task, category if category else "Без категории", priority)
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