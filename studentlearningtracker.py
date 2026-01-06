name=""
topic=[]
progress={}
def details():
    global name
    name=input("please enter your name")
    course=int(input("please enter how many course you are learning curruntly"))
    global topic
    for i in range(0,course):
        c=input(f"Enter {i+1} course name")
        topic.append(c)
    print(topic)
def trackprogress():
    global progress
    if (progress):
        print(progress)
    else:
        print("till now you did not mention your progress")
def updateprogress():
    global progress
    global topic
    a=open("progress.txt","w")
    if (topic):
        for i in topic:
            progress[i]=input(f"Enter progress for {i}")
        a.write(str(progress))
    else:
        print("please enter topic first")
def checkdata():
    global name
    global topic
    print("your name is ",name)
    print("your topics are ",topic)
details()

while True:
    print("press 1 for update your progress")
    print("press 2 for track your progress")
    print("press 3 to check your details")
    print("press 4 for close the app")
    choice=int(input("enter your choice"))
    if (choice==1):
        updateprogress()
    elif (choice==2):
        trackprogress()
    elif(choice==3):
        checkdata()
    elif(choice==4):
        break
    else:
        print("please enter valid choice")





