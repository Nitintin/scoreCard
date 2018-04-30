from tkinter import *
windowGUI=Tk()
def addrec():
    fileAdd=open('opendb.txt','a')
    Fname=s1.get()
    Lname=s2.get()
    run=s3.get()
    match=s4.get()
    boundary=s5.get()
    strikeRate=s6.get()
    lines_of_text=[Fname.ljust(25),Lname.ljust(25),run.ljust(25),match.ljust(25),boundary.ljust(25),strikeRate.ljust(25),"\n"]
    fileAdd.writelines(lines_of_text)
    print("Congrats! player added succesfully")
    fileAdd.close()

def update():
    Fname=s1.get()
    Lname=s2.get()
    run=s3.get()
    match=s4.get()
    boundary=s5.get()
    strikeRate=s6.get()
    fileUpdate=open("opendb.txt","r")
    fileLine=fileUpdate.readlines()
    fileUpdate.close()
    fileUpdate=open("opendb.txt","w")
    for eachLine in fileLine:
        j=eachLine.split()
        if(j[0]==Fname and j[1]==Lname):
            fileUpdate.writelines(Fname.ljust(25)+Lname.ljust(25)+run.ljust(25)+match.ljust(25)+boundary.ljust(25)+strikeRate.ljust(25)+"\n")
            print("PLAYER UPDATED SUCCESFULLY")
        else :
            fileUpdate.writelines(j[0].ljust(25)+j[1].ljust(25)+j[2].ljust(25)+j[3].ljust(25)+j[4].ljust(25)+"\n")
    fileUpdate.close()

def delete():
    k=[s1.get(), s2.get()]
    fileDelete=open('opendb.txt','r')
    fileLines=fileDelete.readlines()
    fileDelete.close()
    fileDelete=open("opendb.txt","w")
    for eachLine in fileLines:
        j=eachLine.split()            
        if(j[0]==k[0] and j[1]==k[1]):
            print("Deletion success!!!")
        else:
            lines_of_text=[j[0].ljust(25),j[1].ljust(25),j[2].ljust(25),j[3].ljust(25),j[4].ljust(25),j[5].ljust(25),"\n"]
            fileDelete.writelines(lines_of_text)
    fileDelete.close()

def search():
    playerName=s1.get()
    fileSearch=open("opendb.txt","r")
    fileLine=fileSearch.readlines()
    for eachLine in fileLine:
        j=eachLine.split()
        if(j[0]==playerName):
            s1.set(j[0])
            s2.set(j[1])
            s3.set(j[2])
            s4.set(j[3])
            s5.set(j[4])
            s6.set(j[5])
            print("First name: ",j[0]," Last name: ",j[1]," run: ",j[2]," match:",j[3]," boundaries:",j[4]," strike rate:",j[5])
    print("--------------")
    fileSearch.close()

def lr():
    fileLast=open('opendb.txt','r')
    fileLine=fileLast.readlines();
    j=fileLine[-1].split()
    print("-------LAST RECORD----\n")
    print("First name: ",j[0]," Last name: ",j[1]," run: ",j[2]," match:",j[3]," boundaries:",j[4]," strike rate:",j[5])
    fileLast.close()

def fr():
    fileFirst=open('opendb.txt','r')
    fileLine=fileFirst.readline();
    j=fileLine.split()
    print("-------FIRST RECORD----\n")
    print("First name: ",j[0]," Last name: ",j[1]," run: ",j[2]," match:",j[3]," boundaries:",j[4]," strike rate:",j[5])
    fileFirst.close()

def viewAll():
    fileView=open('opendb.txt','r')
    fileLine=fileView.readlines()
    print("---ALL PLAYER RECORDS---")
    for eachLine in fileLine:
        j=eachLine.split()
        print("First name: ",j[0]," Last name:",j[1]," runs:",j[2]," matches:",j[3]," boundaries:",j[4]," strike rate:",j[5])
    fileView.close()

s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
s6=StringVar()
l0=Label(windowGUI,text="---------SCORE CARD SYSTEM--------")
l1=Label(windowGUI,text="First Name")
l2=Label(windowGUI,text="Last Name")
l3=Label(windowGUI,text="Runs scored")
l4=Label(windowGUI,text="Match Played")
l5=Label(windowGUI,text="Boundaries")
l6=Label(windowGUI,text="Strike Rate")
l7=Label(windowGUI,text="Developed by- Nitin Gupta || 15CSU140 || 9999915487")
t1=Entry(windowGUI,textvariable=s1)
t2=Entry(windowGUI,textvariable=s2)
t3=Entry(windowGUI,textvariable=s3)
t4=Entry(windowGUI,textvariable=s4)
t5=Entry(windowGUI,textvariable=s5)
t6=Entry(windowGUI,textvariable=s6)
l0.grid(row=1,column=2)
l1.grid(row=2,column=1)
l2.grid(row=3,column=1)
l3.grid(row=4,column=1)
l4.grid(row=5,column=1)
l5.grid(row=6,column=1)
l6.grid(row=7,column=1)
l7.grid(row=8,column=2)
t1.grid(row=2,column=2)
t2.grid(row=3,column=2)
t3.grid(row=4,column=2)
t4.grid(row=5,column=2)
t5.grid(row=6,column=2)
t6.grid(row=7,column=2)
b0=Button(windowGUI,text="View All Players",command=viewAll)
b1=Button(windowGUI,text="Add Player", command=addrec)
b2=Button(windowGUI,text="Delete Player", command=delete)
b3=Button(windowGUI,text="Search Player", command=search)
b4=Button(windowGUI,text="Update Player", command=update)
b5=Button(windowGUI,text="Last Record", command=lr)
b6=Button(windowGUI,text="First Record", command=fr)
b0.grid(row=2,column=3)
b1.grid(row=3,column=3)
b2.grid(row=4,column=3)
b3.grid(row=5,column=3)
b4.grid(row=6,column=3)
b5.grid(row=7,column=3)
b6.grid(row=1,column=3)
windowGUI.mainloop()
