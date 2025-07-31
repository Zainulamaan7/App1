import functions
import time
now=time.strftime("%b %d, %Y %H:%M:%S")
print(" It is",now)
while True: 

     user_action=input("Type add or show or edit or complete or exit:")

     user_action=user_action.strip().lower()
      
     if user_action.startswith("add"):
            
            todo=user_action[4:] +"\n"

            todos=functions.get_todo("demo.txt")
            todos.append(todo)
            functions.write_todo("demo.txt",todos)

     elif user_action.startswith("show"):
          todos=functions.get_todo("demo.txt")

          for index,items in enumerate(todos):

            items=items.strip("\n")    # strip is used to remove the extra\n

            print(f"{index+1}.{items}")    #print statement  produces anothe \n
       
     elif user_action.startswith("edit"):
            try:
               todos=functions.get_todo("demo.txt")
               number=int(user_action[5:])

               number=number-1

               new_todo=input("new_todo:") +"\n"

               todos[number]=new_todo
               functions.write_todo("demo.txt",todos)
            except ValueError:
                print("command is invalid !!!")
                continue

     elif user_action.startswith("complete"):
         try:
          
            todos=functions.get_todo("demo.txt")
            number=int(user_action[9:])

            index=number-1

            todo_to_remove=todos[index].strip("\n")
            
            todos.pop(index)
            functions.write_todo("demo.txt",todos)

            print(f"todo {todo_to_remove} was removed from the list.")
         except IndexError:
             print("Index is out of range!")
             continue
         except ValueError:
             print("command is invalid !!!")
             continue
     elif user_action.startswith("exit"):
         
         break
          
     else:

            print("Hey you have entered a unknown command!") 

print("Saved todos to demo.txt")

print("Bye!")


