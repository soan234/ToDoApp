from task_storage import FileStorage
from task_repo import TaskRepo
from todoapp import ToDoApp

def main():
    storage = FileStorage()
    repo = TaskRepo()
    app = ToDoApp(repo, storage)


    while True:
        print("1. Visa uppgifter")
        print("2. Lägg till uppgift")
        print("3. Färdigmarkera uppgift")
        print("4. Ta bort uppgift")
        print("5. Avsluta.")

        val = input("Välj i menyn: ")

        if val =="1":
            for i, task in enumerate(app.get_tasks()):
                status = "KLAR" if task.done else "EJ KLAR"
                print(i + 1, task.title, status)
                
        elif val == "2":
            text = input("Vilken uppgift vill du lägga till: ")
            app.add_task(text)

        elif val == "3":
            try:
                index = int(input("Vilken uppgift är klar? "))
                app.mark_done(index - 1)
            except ValueError:
                print("Skriv ett nummer.")

        elif val == "4":
            try:
                index = int(input("Vilken uppgift vill du ta bort? "))
                app.delete_task(index - 1)
            except ValueError:
                print("Skriv ett nummer.")

        elif val == "5":
            break

        else:
            print("Fel val")
