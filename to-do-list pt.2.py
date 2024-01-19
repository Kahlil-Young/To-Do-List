# Kahlil Young
# 3rd Period
# 1/10/24
# Initialize
todolist=[]

#function
def toDoList():
        x=0
        print("""Welcome to To-Do List. Would you like to:
1. Add a task to the to-do list 
2. View the current to-do list 
3. Mark a task as completed 
4. Remove a task from the to-do list
5. Edit a task in the to-do list
6. Clear the to-do list
7. Sort the to-do list alphabetically
8. View the number of items in the list
9. Exit the program""")
        while x==0:
            option=input("(1-9)")
            if option=="1":
                  item=input("What do you want to add?")
                  m=input("Do you want to add a due date?(Y/N)")
                  if m=="Y":
                        date=input("What is the due date?")
                        todolist.append("("+date+") "+item)
                  else:
                        todolist.append(item)
            elif option=="2":
                  print(todolist)
            elif option=="3":
                  ans=input("What did you complete?")
                  m=input("Is there a due date?(Y/N)")
                  if m=="Y":
                        h=input("What was the due date?")
                        i= todolist.index("("+h+") "+ans)
                        todolist[i] = "("+h+") "+ans+ "(✔)"
                  else:
                        i= todolist.index(ans)
                        todolist[i] = ans+ "(✔)"
            elif option=="4":
                  d=input("What do you want to remove?")
                  m=input("Is there a due date?(Y/N)")
                  if m=="Y":
                        g=input("What was the due date?")
                        todolist.remove("("+g+") "+d)
                  else:
                        todolist.remove(d)
                  
            elif option=="5":
                  ans1=input("What do you want to edit?")
                  ans2=input("What do you want to replace it with?")
                  m=input("Is there a due date?(Y/N)")
                  if m=="Y":
                        j=input("What was the due date?")
                        e= todolist.index("("+j+") "+ans1)
                        todolist[e] ="("+j+") "+ans2
                  else:
                        e= todolist.index(ans1)
                        todolist[e] =ans2
            elif option=="6":
                  todolist.clear()
            elif option=="7":
                  todolist.sort()
            elif option=="8":
                  todolist.len()
            elif option=="9":
                  print(todolist)
                  print("Goodbye")
                  x=1
            else:
                  print("Try Again")
            
            
            

                  
#Main
toDoList()
