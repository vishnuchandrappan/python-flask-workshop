import pickle


# prints available menu
def printOptions():
    print("\n\n\n*************************")
    print("1. Show TodoList\n2. Add New Todo\n3. Mark as DONE\n4. Delete todo\n5. Edit todo\n6. Exit")


# read choice input from user
def readChoice():
    printOptions()
    return input("Enter your choice... ")


# show all todoList
def showTodoList():
    storeTodoList()
    clearScreen()
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


# determine new todoId
def generateId():
    if len(todoList) > 0:
        return int(todoList[-1]['id']) + 1
    else:
        return 1


# read new todo and add to todoList
def addToTodoList(newTodo):
    newId = generateId()
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

    available_choices = ['1', '2', '3', '4', '5']

    while choice in available_choices:
        if choice == '1':
            showTodoList()
        elif choice == '2':
            addNewTodo()
        elif choice == '3':
            markTodoAsDone()
        elif choice == '4':
            deleteTodo()
        elif choice == '5':
            editTodo()

        choice = readChoice()

    print("See you later... Take care...")


# read user input for todo to be deleted
def deleteTodo():
    targetTodo = input("Enter todo Id...")
    deleteFromTodoList(targetTodo)
    showTodoList()


# delete todo dict from todoList
def deleteFromTodoList(targetTodo):
    for i in range(len(todoList) - 1):
        if(todoList[i]['id'] == targetTodo):
            del todoList[i]


# read user input for editing todo
def editTodo():
    targetTodo = input("Enter todo Id...")
    newValue = input("Enter new value...")
    updateTodo(targetTodo, newValue)
    showTodoList()


# update todo details
def updateTodo(targetTodo, newValue):
    for todo in todoList:
        if(todo['id'] == targetTodo):
            todo['todo'] = newValue


# clear console screen
def clearScreen():
    print('\x1bc')


# store todoList dictionary to filesystem
def storeTodoList():
    with open('appData.lol', 'wb') as fh:
        pickle.dump(todoList, fh)


# read todoList from filesystem
def fetchTodoList():
    temp = []
    try:
        pickle_off = open("appData.lol", "rb")
        temp = pickle.load(pickle_off)
    except:
        print("Welcome...")
        temp = []

    return temp


# app execution starts here.
todoList = fetchTodoList()
app()
