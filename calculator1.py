from tkinter import *
import math
equation =""
i=0
def show(value):
    global i
    global equation
    if value == "%":
        value = "/100"
    equation += value
    entry.insert(i,value)
    i=i+1
    
def perc(value):
    global i
    global equation
    if value == "%":
        value = "/100"
    equation += value
    entry.insert(i,value)
    i=i+1
    enter()
    
def Clear():
    global equation
    entry.delete(0,END)
    equation=""

def enter():
    try:
        global equation
        results = ""
        results = eval(equation)
        Clear()
        equation = str(results)
        entry.insert(0,results)
    except:
        new_eq = "Invalid Entry"
        Clear()
        for i in range(0,len(new_eq)):
            entry.insert(i,new_eq[i])
    
def back():
    global equation
    new_eq = equation[:len(equation)-1]
    Clear()
    equation = new_eq
    for i in range(0,len(new_eq)):
        entry.insert(i,new_eq[i])
        
window = Tk()
window.title("Calculator")
window.wm_iconbitmap("icon.ico")
window.geometry("450x570")
window.resizable(False,False)
main_frame = Frame(window,background="#f0e9e9")
main_frame.pack(padx=10,pady=10,fill="both",expand="true")

entry =Entry(main_frame,justify="right",font="Cascadia 40 bold",background="#c9c6c5")
entry.pack(side="top",padx=5,pady=5,fill="x",expand=True,ipady=7)

frame_0 = Frame(main_frame,height=80,width=450,background="#f0e9e9")
frame_0.pack(side="top",padx=5,fill="x",expand=True)

frame_1 = Frame(main_frame,height=80,width=440,background="#f0e9e9")
frame_1.pack(side="top",padx=5,fill="x",expand=True)

frame_2 = Frame(main_frame,height=80,width=440,background="#f0e9e9")
frame_2.pack(side="top",padx=5,fill="x",expand=True)

frame_3 = Frame(main_frame,height=80,width=440,background="#f0e9e9")
frame_3.pack(side="top",padx=5,fill="x",expand=True)

frame_4 = Frame(main_frame,height=80,width=440,background="#f0e9e9")
frame_4.pack(side="top",padx=5,fill="x",expand=True)

# buttons for frame 0
button_c = Button(frame_0,width=4,command=Clear,bg="#c2bcbc",highlightbackground="#9c9a9a",text="C",font=("Cascadia",28,"bold"))
button_c.pack(side="left",padx=(4,2))

button_perc = Button(frame_0,width=4,command=lambda:perc("%"),bg="#c2bcbc",text="%",font=("Cascadia",28,"bold"))
button_perc.pack(side="left",padx=2)

button_back = Button(frame_0,width=4,command=back,bg="#c2bcbc",text="<",font=("Cascadia",28,"bold"))
button_back.pack(side="left",padx=2)

button_divide = Button(frame_0,width=4,command=lambda:show("/"),bg="#353638",fg="white",text="/",font=("Cascadia",28,"bold"))
button_divide.pack(side="left",padx=(2,4))

# #buttons for frame 1
button_7 = Button(frame_1,command=lambda:show("7"),width=4,bg="#c2bcbc",text="7",font=("Cascadia",28,"bold"))
button_7.pack(side="left",padx=2)

button_8 = Button(frame_1,command=lambda:show("8"),width=4,bg="#c2bcbc",text="8",font=("Cascadia",28,"bold"))
button_8.pack(side="left",padx=2)

button_9 = Button(frame_1,command=lambda:show("9"),width=4,bg="#c2bcbc",text="9",font=("Cascadia",28,"bold"))
button_9.pack(side="left",padx=2)

button_x = Button(frame_1,command=lambda:show("*"),width=4,bg="#353638",fg="white",text="x",font=("Cascadia",28,"bold"))
button_x.pack(side="left",padx=2)

# #buttons for frame 2
button_4 = Button(frame_2,command=lambda:show("4"),width=4,bg="#c2bcbc",text="4",font=("Cascadia",28,"bold"))
button_4.pack(side="left",padx=2)

button_5 = Button(frame_2,command=lambda:show("5"),width=4,bg="#c2bcbc",text="5",font=("Cascadia",28,"bold"))
button_5.pack(side="left",padx=2)

button_6 = Button(frame_2,command=lambda:show("6"),width=4,bg="#c2bcbc",text="6",font=("Cascadia",28,"bold"))
button_6.pack(side="left",padx=2)

button_minus = Button(frame_2,command=lambda:show("-"),width=4,bg="#353638",fg="white",text="-",font=("Cascadia",28,"bold"))
button_minus.pack(side="left",padx=2)

# #buttons for frame 3
button_1 = Button(frame_3,command=lambda:show("1"),width=4,bg="#c2bcbc",text="1",font=("Cascadia",28,"bold"))
button_1.pack(side="left",padx=2)

button_2 = Button(frame_3,command=lambda:show("2"),width=4,bg="#c2bcbc",text="2",font=("Cascadia",28,"bold"))
button_2.pack(side="left",padx=2)

button_3 = Button(frame_3,command=lambda:show("3"),width=4,bg="#c2bcbc",text="3",font=("Cascadia",28,"bold"))
button_3.pack(side="left",padx=2)

button_plus = Button(frame_3,command=lambda:show("+"),width=4,bg="#353638",fg="white",text="+",font=("Cascadia",28,"bold"))
button_plus.pack(side="left",padx=2)

# #buttons for frame 4
button_0 = Button(frame_4,command=lambda:show("0"),width=4,bg="#c2bcbc",text="0",font=("Cascadia",28,"bold"))
button_0.pack(side="left",padx=2) 

button_dot = Button(frame_4,command=lambda:show("."),width=4,bg="#c2bcbc",text=".",font=("Cascadia",28,"bold"))
button_dot.pack(side="left",padx=2)

button_equals = Button(frame_4,command=enter,width=9,bg="#ecfc05",text="=",font=("Cascadia",28,"bold"))
button_equals.pack(side="left",padx=2)

window.mainloop()