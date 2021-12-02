import sys

file1 = open('task.txt', 'r')
tasks = file1.readlines()
for task in tasks:
    print(task)

def show_help():
  print("""Usage :-
    $ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
    $ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
    $ ./task del INDEX            # Delete the incomplete item with the given index
    $ ./task done INDEX           # Mark the incomplete item with the given index as complete
    $ ./task help                 # Show usage
    $ ./task report               # Statistics""")

def add_task(priority, text):
  print("Adding task : {} {}".format(priority, text))

def list_tasks():
  print("Listing tasks")

def del_task(index):
  print("Removing task")

def done_task(index):
  print("Completed task")

def report():
  print("Generating report")

try:
    if(sys.argv[1]=='add'):
        add_task(sys.argv[2], sys.argv[3])
    elif(sys.argv[1]=='ls'):
        list_tasks()
    elif(sys.argv[1]=='del'):
        del_task(sys.argv[2])
    elif(sys.argv[1]=='done'):
        done_task(sys.argv[2])
    elif(sys.argv[1]=='report'):
        report()
    else:
        show_help()
except:
  show_help()


