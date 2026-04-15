# ToDoApp
En enkel todo-applikation som är skriven i Python. Projektet innehåller funktioner som är grundläggande för att kunna lägga till uppgift, ta bort uppgift och markera uppgifter som klara. 
Data sparas i en enkel textfil via en enkel filhanteringslösning.


#Funktioner.
-Lägga till uppgift
-Ta bort uppgift
- Markera uppgift som klar eller ej klar
- Spara och läsa uppgifter från fil
- Enhetstester för alla delar av applikationen


#Projektstruktur
- main.py - startar applikation med meny
- todoapp.py - logiken för appen
- task.py - Task-modellen
- task_repo.py - hanterar listan av tasks
- task_storage.py - sparar/läser från fil
- tests/ - enhetstester


#GitHub-workflow
Detta projekt använder Issues och Pull Requests i GitHub för att kunna hantera detta:
- branches
- user storys
- tasks
- bugs
Ändringar görs i separat branch som sedan till en issues med Fixat #(issues/bugs nummer)


#Krav för denna applikation.
- Python 3


#Klona projektet
git clone https://github.com/soan234/ToDoApp.git
cd ToDoApp


#Kör projektet.
python main.py


#Kör tester.
python -m unittest
