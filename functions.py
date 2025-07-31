# program to make a To Do list

def get_todo(filename):
 """ get_todo reads the file and store in todos_local it can be accessed by help()"""
 with open(filename,"r") as file:                  
  todos_local=file.readlines()  
 return todos_local
# print(help(get_todo))

def write_todo(filename,todos):
     with open(filename,"w") as file: 
         file.writelines(todos)

if __name__=="__main__": # this is used when you don't want to print when importing the module
   
 print("Hello")
 print("Hello")

