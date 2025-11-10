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


todo = ToDoList()

todo.list_tasks()

todo.add_task("Дочитать книгу")
todo.add_task("Связать новую игрушку")
todo.add_task("Провести тренировку")
todo.add_task("Приготовить вишнёвый пирог")

todo.list_tasks()

todo.complete_task("Дочитать книгу")
todo.complete_task("Связать новую игрушку")

todo.list_tasks()

todo.add_task("Купить фрукты и мороженое")
todo.add_task("На выходных съездить к своим грэнпэрэнтс")
todo.add_task("Поиграть в Red Dead Redemption")

todo.list_tasks()

todo.remove_task("Дочитать книгу")
todo.remove_task("Связать новую игрушку")

todo.list_tasks()

todo.remove_task("Поиграть на гитаре")
