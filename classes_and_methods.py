class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        print(f"Задача '{task}' добавлена!")

    def complete_task(self, task):
        if not self.tasks:
            print("В списке не существует такой задачи.")
            return

        for t in self.tasks:
            if t["task"] == task:
                if t["done"]:
                    print(f"Задача '{task}' уже выполнена!")
                    return
                t["done"] = True
                print(f"Задача '{task}' отмечена как выполненная.")

    def remove_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                self.tasks.remove(t)
                print(f"Задача '{task}' удалена.")
                return

        print(f"В списке не существует задачи '{task}'.")

    def list_tasks(self):
        print("\nТекущий список задач:")

        if not self.tasks:
            print("Список задач пуст.")
            return

        for index, t in enumerate(self.tasks, start=1):
            status = "Выполнено" if t["done"] else "Не выполнено"
            print(f"{index}. {t['task']} — {status}.")


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
