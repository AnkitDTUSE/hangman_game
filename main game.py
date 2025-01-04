from tkinter import*
import random

atmps = 10
answer= random.randint(1,99)

def first_fun():
    global atmps   
    global atmp
    atmps -=1
    guess =int(c.get())
    if answer==guess:
        st1.set("Hey congrats you win !! :)")
        
    elif atmps == 0:
        st1.set("better luck next time")

    elif atmps == -1:
        a.destroy()
       
    elif guess > answer:
        st1.set("enter a smaller number:" + str(atmps)+ "left")
        
    else:
        st1.set("enter larger number:" + str(atmps)+ "left")
        

def end():
    a.destroy()

def dis_ans():
    st1.set("the answer is "+ str(answer)+" (you cheat the game :( )" )
    f= Button(a,text="quit",command= end)
    f.pack()
    
a= Tk()
a.title ("Guess the number game")
a.geometry("700x400")

b= Label(text= "Guess a number between 1 to 99")
b.pack()

c= Entry(a,width=30,borderwidth=4)
c.pack()

d= Button(a,text="let's check",width=20,borderwidth=1,command=first_fun,fg="black",bg = "white")

d.pack()

e= Button(a,text="display the answer",command= dis_ans)
e.pack()

st1 = StringVar()
st1.set("YOU have only 10 attempts remaning!!")

g = Label(a, text="Computer Science project by Group A Names :(Ankit panchal,Bilal khan, Nikhil pandey,amar chahar,swayam )")
g.pack()

atmp = Label(a, textvariable= st1)
atmp.pack()

a.mainloop()
