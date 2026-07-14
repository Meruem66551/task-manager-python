import json
class Task:
    def __init__(self, title, deadline, priority, done=False):
        self.title = title
        self.deadline = deadline
        self.priority = priority
        self.done = done
    
    def show(self):
        print("Задача: ", self.title)
        print("Срок: ", self.deadline)
        print("Приоритет: ", self.priority)
        print("Статус: ","выполнено" if self.done else "не выполнено") 
    
    def to_dict(self):
        return {
        "title": self.title,
        "deadline": self.deadline,
        "priority": self.priority,
        "done": self.done
        }
class TaskManager: 
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Задача '{task.title}' Добавлена!")

    def show_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
            return
        
        for number, task in enumerate(self.tasks, start=1):
            print(f"Номер задачи: {number}")
            task.show()
            print()

    def save_tasks(self):
        data = []
        for task in self.tasks:
            data.append(task.to_dict())
        with open("tasks.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    
    def load_tasks(self):
        try:
            with open("tasks.json", "r", encoding="utf-8") as file:
                data = json.load(file)
            for item in data:
                task= Task(item["title"], item["deadline"], item["priority"], item["done"])
                self.tasks.append(task)
        except FileNotFoundError:
            pass

    def delete_task_by_number(self, number):
        index = number - 1

        if 0 <= index < len(self.tasks):
            deleted_task = self.tasks[index]
            del self.tasks[index]
            print(f"Задача '{deleted_task.title}' удалена")
        else:
            print("Неверный номер!")

    def complete_task_by_number(self, number):
        index = number - 1
        if 0 <= index < len(self.tasks):
            self.tasks[index].done = True 
            print(f"Задача '{self.tasks[index].title}' выполнена!")
        else:
            print("Неверный номер!")

    def show_active_tasks(self):
        found = False
        for number, task in enumerate(self.tasks, start=1):
            if not task.done:
                print(f"Номер задачи: {number}")
                task.show()
                print()
                found = True
        if not found:
            print("Нет невыполненных задач.")  
    
    def show_completed_tasks(self):
        found = False
        for number, task in enumerate(self.tasks, start=1):
            if task.done:
                print(f"Номер задачи: {number}")
                task.show()
                print()
                found = True
        if not found:
            print("Нет выполненных задач.")

    def edit_task(self, number):
        index = number - 1
        if 0 <= index < len(self.tasks):
            while True:
                print("Выберите пункт, который хотите изменить: ")
                print("\n1 - Имя задачи")
                print("2 - Срок задачи")
                print("3 - Приоритет задачи")
                print("4 - Вернуться")
                try:
                    x = int(input("Введите число для нужного действия: "))
                except ValueError:
                    print("Нужно ввести число!")
                    continue
                if x == 1:
                    new_title = input("Введите новое имя для задачи: ")
                    self.tasks[index].title = new_title
                    print("Задача обновлена!")
                    break
                    
                elif x == 2:
                    new_deadline = input("Введите новый срок для задачи: ")
                    self.tasks[index].deadline = new_deadline
                    print("Задача обновлена!")
                    break
                elif x == 3:
                    new_priority = input("Введите новый приоритет задачи: ")
                    self.tasks[index].priority = new_priority
                    print("Задача обновлена!")
                    break
                elif x == 4:
                    print("Возвращаемся в главное меню! ")
                    break
                else:
                    print("Такого пункта нет!")
        else:
            print("Неверный номер!")

def get_number(text):
    try:
        return int(input(text))
    except ValueError:
        print("Нужно ввести число!")
        return None
    

def show_menu(manager):
    while True:
        print("\n1 - Добавить задачу")
        print("2 - Показать все задачи")
        print("3 - Удалить задачу")
        print("4 - Отметить выполненной")
        print("5 - Редактировать задачу")
        print("6 - Показать список невыполненных задач")
        print("7 - Показать список выполненных задач")
        print("8 - Выйти")

        try:
            x = int(input("Введи число для нужного действия: "))
        except ValueError:
            print("Нужно ввести число!")
            continue

        if x == 8:
            manager.save_tasks()
            print("Задачи сохранены. Выход")
            break
        elif x == 1:
            title = input("Введите сюда название задачи: ")
            deadline = input("Введите сюда срок задачи: ")
            priority = input("Введите сюда приоритет задачи: ")
            task = Task(title, deadline, priority)
            manager.add_task(task)
            manager.save_tasks()
        elif x == 2:
            manager.show_tasks()
        elif x == 3:
            number = get_number("Введите номер задачи которую нужно удалить: ")
            if number is not None:
                manager.delete_task_by_number(number)
                manager.save_tasks()
        elif x == 4: 
            number = get_number("Введите номер выполненной задачи: ")
            if number is not None:
                manager.complete_task_by_number(number)
                manager.save_tasks()

        elif x == 5:
            number = get_number("Введите номер задачи которую нужно отредактировать: ")
            if number is not None:
                manager.edit_task(number)
                manager.save_tasks()
        elif x == 6:
            manager.show_active_tasks()
        elif x == 7:
            manager.show_completed_tasks()
        else:
            print("Такого пункта нет!")


manager = TaskManager()
manager.load_tasks()
show_menu(manager)
