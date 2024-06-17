def get_todos(filename='todos.txt'):
    with open(filename,'r') as file:
        todos_local=file.readlines()
    return todos_local
def write_todos(new_list,filename='todos.txt'):
    with open(filename,'w') as file:
        file.writelines(new_list)

if __name__=="__main__":
    print("Hello")
    print(get_todos())