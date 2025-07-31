# task_tracker.py
tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f"Задача '{task}' добавлена.")

def view_tasks():
    if not tasks:
        print("Список задач пуст.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else " "
        print(f"{i}. [{status}] {task['task']}")

def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        print(f"Задача '{tasks[task_index - 1]['task']}' отмечена как выполненная.")
    else:
        print("Неверный индекс задачи.")

def delete_task(task_index):
    if 1 <= task_index <= len(tasks):
        task = tasks.pop(task_index - 1)
        print(f"Задача '{task['task']}' удалена.")
    else:
        print("Неверный индекс задачи.")

def main():
    while True:
        print("\nТрекер задач")
        print("1. Добавить задачу")
        print("2. Просмотреть задачи")
        print("3. Отметить задачу как выполненную")
        print("4. Удалить задачу")
        print("5. Выход")
        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            task = input("Введите задачу: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                task_index = int(input("Введите номер задачи для завершения: "))
                complete_task(task_index)
            except ValueError:
                print("Введите корректный номер.")
        elif choice == "4":
            view_tasks()
            try:
                task_index = int(input("Введите номер задачи для удаления: "))
                delete_task(task_index)
            except ValueError:
                print("Введите корректный номер.")
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()