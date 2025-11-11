class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        if task in self.tasks:
            print(f"Задача '{task}' уже существует!")
        else:
            self.tasks[task] = False
            print(f"Задача '{task}' добавлена!")

    def complete_task(self, task):
        if task not in self.tasks:
            print("В списке не существует такой задачи.")
            return

        if self.tasks[task]:
            print(f"Задача '{task}' уже выполнена!")
        else:
            self.tasks[task] = True
            print(f"Задача '{task}' отмечена как выполненная.")

    def remove_task(self, task):
        if task not in self.tasks:
            print(f"В списке не существует задачи '{task}'.")
            return

        del self.tasks[task]
        print(f"Задача '{task}' удалена.")

    def list_tasks(self):
        print("\nТекущий список задач:")

        if not self.tasks:
            print("Список задач пуст.")
            return

        for index, (task, done) in enumerate(self.tasks.items(), start=1):
            status = "✅Выполнено" if done else "❌Не выполнено"
            print(f"{index}. {task} — {status}.")
        print()


def menu(todo_list):
    menu_actions = {
        "1": ("Показать все задачи", todo_list.list_tasks),
        "2": ("Добавить задачу", todo_list.add_task),
        "3": ("Отметить задачу как выполненную", todo_list.complete_task),
        "4": ("Удалить задачу из списка", todo_list.remove_task),
        "0": ("Выход", None)
    }

    while True:
        print("\nМеню:")

        for key, (desc, _) in menu_actions.items():
            print(f"{key}. {desc}.")

        choice = input("\nВыберите пункт меню: ")

        if choice == "0":
            print("Выход из программы.")
            break

        if choice not in menu_actions:
            print("Некорректный выбор, попробуйте выбрать заново пункт из предложенных.")
            continue

        description, action = menu_actions[choice]

        if action in (todo_list.add_task, todo_list.complete_task, todo_list.remove_task):
            task = input("Введите название задачи: ")
            action(task)
        else:
            action()


if __name__ == "__main__":
    todo = ToDoList()
    menu(todo)
