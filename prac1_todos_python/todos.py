todos = []

def todo_add():
    task = input("Enter Task:")
    todos.append({"task":task,"Completed":False})
    print("Task added")

def  todo_view():
    c = 1
    for i in todos:
        print(c,".",i)
        c+=1
        
def  todo_update():
    n = int(input("Entry to update :"))-1
    #todos[n]["Completed"] =True
    if 0 <= n <len(todos):
        todos[n]["Completed"] = True
    else:
        print("Enter valid index")
        todo_view()
        todo_update()
    
def  todo_delete():
    n = int(input("Entry to delete:"))-1
    if 0 < n <len(todos):
        del(todos[n])
    else:
        print("Enter valid index")
        todo_view()
        todo_delete()
    
def main():
    while True:
        print("1.Add\n2.View\n3.Update\n4.Delete\n5.Exit\n")
        choice = input("Enter Choice:")
        if choice == '1':
            todo_add()
        elif choice == '2':
            todo_view()
        elif choice == '3':
            todo_update()
        elif choice == '4':
            todo_delete()
        elif choice == '5':
            break
        else:
            print("Invaid input\n")
        
main()