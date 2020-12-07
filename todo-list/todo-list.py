# prints available menu
def printOptions():
    print("\n\n\n*************************")
    print("1. Show TodoList\n2. Add New Todo\n3. Change Status\n4. Exit")


# read choice input from user
def readChoice():
    printOptions()
    return input("Enter your choice... ")


# show all todoList
def showTodoList():
    if not len(todoList):
        print("+-----------------------+\n|     No todo found!    |\n+-----------------------+")
        return
    else:
        print(f"+{'-'*69}+")
        print(f"| SL. NO. ||{' '*16}TODO{' '*16}||{' '*7}STATUS{' '*7}|")
        print(f"+{'-'*69}+")

    for todo in todoList:
        if todo['completed'] is True:
            status = 'Done'
        else:
            status = "X"

        print(
            f"| {todo['id'].center(7)} || {todo['todo'].center(34)} || {status.center(18)} |")
        print(f"+{'-'*69}+")


# read new todo and add to todoList
def addToTodoList(newTodo):
    try:
        newId = int(todoList[-1]['id']) + 1
    except:
        newId = 1
    newTodoDictionary = {"id": str(newId), "todo": newTodo, "completed": False}
    todoList.append(newTodoDictionary)


# appends new todo to todoList
def addNewTodo():
    newTodo = input("Todo content... ")
    addToTodoList(newTodo)
    showTodoList()


# Update todo status
def markTodoAsDone():
    targetTodo = input("Enter todo Id...")
    toggleStatus(targetTodo)
    showTodoList()


# changes todo completion status from True to False and vice-versa
def toggleStatus(targetTodo):
    for todo in todoList:
        if(todo['id'] == targetTodo):
            todo['completed'] = not todo['completed']


# main app logic
def app():
    choice = readChoice()

    while choice != '4':
        if choice == '1':
            showTodoList()
        elif choice == '2':
            addNewTodo()
        elif choice == '3':
            markTodoAsDone()

        choice = readChoice()

    print("See you later... Take care...")


# app execution starts here.
todoList = []
app()
