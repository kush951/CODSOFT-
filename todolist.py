while True:
    user_prompt = input("Type 'add', 'show', 'edit', 'complete' or 'exit': ")
    user_prompt = user_prompt.strip()

    match user_prompt:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo.capitalize())

            file = open('todos.txt','w')
            file.writelines(todos)
            file.close()    

        case 'show':
            for index, item in enumerate(todos):
                row = f"{index + 1}.{item}"
                print(row)

        case 'edit':
            number = int(input("Number of todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

        case 'complete':
            number = int(input("Number of todo to complete: "))
            todos.pop(number - 1)

        case 'exit':
            break
