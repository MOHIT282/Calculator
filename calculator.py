from tkinter import *
import pygame
import math as m
import customtkinter
from PIL import Image
window = customtkinter.CTk()
pygame.init()
equation =""
i=0
j=0

def modes():
    global j
    if j== 0:
        customtkinter.set_appearance_mode("light")
        pygame.mixer.music.load("click sound.mp3")
        pygame.mixer.music.play()
        entry.configure(fg_color="grey",text_color="black",border_color="#2e2d2d")
        button_mode.configure(text="Dark\nMode")
        j = j+1
        
    elif j == 1:
        customtkinter.set_appearance_mode("dark")
        pygame.mixer.music.load("click sound.mp3")
        pygame.mixer.music.play()
        entry.configure(fg_color="#292928",text_color="white",border_color="white")
        button_mode.configure(text="Light\nMode")
        j = j-1
        
def trigno(value):
    global equation
    global i
    pygame.mixer.music.load("click sound2.mp3")
    pygame.mixer.music.play()
    if value =="sin":
        value = "m.sin("
    if value == "cos":
        value = "m.cos("
    equation += value
    entry.insert(i,value)
    i=i+1
    for i in range(0,len(equation)+1):
        entry.insert(i,"")

def show(value):
    global i
    global equation
    pygame.mixer.music.load("click sound2.mp3")
    pygame.mixer.music.play()
    equation += value
    entry.insert(i,value)
    i=i+1
    for i in range(0,len(equation)+1):
            entry.insert(i,"")
    
def perc(value):
    global i
    global equation
    pygame.mixer.music.load("click sound.mp3")
    pygame.mixer.music.play()
    if value == "%":
        value = "/100"
    equation += value
    entry.insert(i,value)
    i=i+1
    enter()
    
def Clear():
    global equation
    pygame.mixer.music.load("click sound.mp3")
    pygame.mixer.music.play()
    entry.delete(0,END)
    equation=""

def enter():
    global equation
    global i
    try:
        results = ""
        results = eval(equation)
        Clear()
        equation = str(results)
        entry.insert(0,equation)
        for i in range(0,len(equation)+1):
            entry.insert(i,"")
            
    except:
        new_eq = "Invalid Entry"
        Clear()
        entry.insert(0,new_eq)
        for i in range(0,len(new_eq)+1):
            entry.insert(i,"")
    
def back():
    global equation
    new_eq = equation[:len(equation)-1]
    Clear()
    equation = new_eq
    for i in range(0,len(new_eq)):
        entry.insert(i,new_eq[i])
        
window.title("Calculator By Mohit Kumar")
window.wm_iconbitmap("icon.ico")
# window.geometry("350x470")
window.resizable(False,False)
main_frame = customtkinter.CTkFrame(window)
main_frame.pack(padx=10,pady=10,fill="both",expand="true")

entry = customtkinter.CTkEntry(main_frame,justify="right",height=80,text_color="white",fg_color="#292928",font=("Cascadia",36,"bold"),border_color="white",border_width=3)
entry.pack(side="top",padx=5,pady=0,fill="x",expand=True)

frame_0 = customtkinter.CTkFrame(main_frame,height=80)
frame_0.pack(side="top",padx=5,pady=0,fill="x",expand=True)

frame_5 = customtkinter.CTkFrame(main_frame,height=80)
frame_5.pack(side="top",padx=5,pady=0,fill="x",expand=True)

frame_1 = customtkinter.CTkFrame(main_frame,height=80)
frame_1.pack(side="top",padx=5,pady=0,fill="x",expand=True)

frame_2 = customtkinter.CTkFrame(main_frame,height=80)
frame_2.pack(side="top",padx=5,pady=0,fill="x",expand=True)

frame_3 = customtkinter.CTkFrame(main_frame,height=80)
frame_3.pack(side="top",padx=5,pady=0,fill="x",expand=True)

frame_4 = customtkinter.CTkFrame(main_frame,height=80)
frame_4.pack(side="top",padx=5,pady=(0,1),fill="x",expand=True)

#buttons for frame 5
button_sin = customtkinter.CTkButton(frame_5,command=lambda:trigno("sin"),height=70,width=85,fg_color="#4d4c4c",hover_color="#30302f",text="sin",font=("Cascadia",36,"bold"))
button_sin.pack(side="left",padx=2,pady=4)

button_cos = customtkinter.CTkButton(frame_5,command=lambda:trigno("cos"),height=70,width=85,fg_color="#4d4c4c",hover_color="#30302f",text="cos",font=("Cascadia",36,"bold"))
button_cos.pack(side="left",padx=2,pady=4)

button_lp = customtkinter.CTkButton(frame_5,height=70,width=85,command=lambda:show("("),fg_color="#4d4c4c",hover_color="#30302f",text="(",font=("Cascadia",36,"bold"))
button_lp.pack(side="left",padx=2,pady=4)

button_rp = customtkinter.CTkButton(frame_5,command=lambda:show(")"),height=70,width=85,fg_color="#2e2d2d",hover_color="#30302f",text=")",font=("Cascadia",36,"bold"))
button_rp.pack(side="left",padx=2,pady=4)

#buttons for frame 0
button_c = customtkinter.CTkButton(frame_0,command=Clear,height=70,width=85,fg_color="#ede215",text_color="#3b3a37",hover_color="#2e2d2d",text="C",font=("Cascadia",36,"bold"))
button_c.pack(side="left",padx=2,pady=4)

button_perc = customtkinter.CTkButton(frame_0,command=lambda:perc("%"),height=70,width=85,fg_color="#4d4c4c",hover_color="#30302f",text="%",font=("Cascadia",36,"bold"))
button_perc.pack(side="left",padx=2,pady=4)

back_image = customtkinter.CTkImage(light_image=Image.open("back.png"),size=(40,40))
button_back = customtkinter.CTkButton(frame_0,height=70,width=85,command=back,fg_color="#4d4c4c",hover_color="#30302f",text="",image=back_image,font=("Cascadia",36,"bold"))
button_back.pack(side="left",padx=2,pady=4)

button_divide = customtkinter.CTkButton(frame_0,command=lambda:show("/"),height=70,width=85,fg_color="#2e2d2d",hover_color="#30302f",text="/",font=("Cascadia",36,"bold"))
button_divide.pack(side="left",padx=2,pady=4)

#buttons for frame 1
button_7 = customtkinter.CTkButton(frame_1,command=lambda:show("7"),height=70,width=85,fg_color="#4d4c4c",hover_color="#30302f",text="7",font=("Cascadia",36,"bold"))
button_7.pack(side="left",padx=2,pady=4)

button_8 = customtkinter.CTkButton(frame_1,command=lambda:show("8"),height=70,width=85,fg_color="#4d4c4c",hover_color="#30302f",text="8",font=("Cascadia",36,"bold"))
button_8.pack(side="left",padx=2,pady=4)

button_9 = customtkinter.CTkButton(frame_1,command=lambda:show("9"),height=70,width=85,fg_color="#4d4c4c",hover_color="#30302f",text="9",font=("Cascadia",36,"bold"))
button_9.pack(side="left",padx=2,pady=4)

button_x = customtkinter.CTkButton(frame_1,command=lambda:show("*"),height=70,width=85,fg_color="#2e2d2d",hover_color="#30302f",text="x",font=("Cascadia",36,"bold"))
button_x.pack(side="left",padx=2,pady=4)

#buttons for frame 2
button_4 = customtkinter.CTkButton(frame_2,command=lambda:show("4"),height=70,width=85,fg_color="#4d4c4c",hover_color="#30302f",text="4",font=("Cascadia",36,"bold"))
button_4.pack(side="left",padx=2,pady=4)

button_5 = customtkinter.CTkButton(frame_2,command=lambda:show("5"),height=70,width=85,fg_color="#4d4c4c",hover_color="#30302f",text="5",font=("Cascadia",36,"bold"))
button_5.pack(side="left",padx=2,pady=4)

button_6 = customtkinter.CTkButton(frame_2,command=lambda:show("6"),height=70,width=85,fg_color="#4d4c4c",hover_color="#30302f",text="6",font=("Cascadia",36,"bold"))
button_6.pack(side="left",padx=2,pady=4)

button_minus = customtkinter.CTkButton(frame_2,command=lambda:show("-"),height=70,width=85,fg_color="#2e2d2d",hover_color="#30302f",text="-",font=("Cascadia",36,"bold"))
button_minus.pack(side="left",padx=2,pady=4)

#buttons for frame 3
button_1 = customtkinter.CTkButton(frame_3,command=lambda:show("1"),height=70,width=85,fg_color="#4d4c4c",hover_color="#30302f",text="1",font=("Cascadia",36,"bold"))
button_1.pack(side="left",padx=2,pady=4)

button_2 = customtkinter.CTkButton(frame_3,command=lambda:show("2"),height=70,width=85,fg_color="#4d4c4c",hover_color="#30302f",text="2",font=("Cascadia",36,"bold"))
button_2.pack(side="left",padx=2,pady=4)

button_3 = customtkinter.CTkButton(frame_3,command=lambda:show("3"),height=70,width=85,fg_color="#4d4c4c",hover_color="#30302f",text="3",font=("Cascadia",36,"bold"))
button_3.pack(side="left",padx=2,pady=4)

button_plus = customtkinter.CTkButton(frame_3,command=lambda:show("+"),height=70,width=85,fg_color="#2e2d2d",hover_color="#30302f",text="+",font=("Cascadia",36,"bold"))
button_plus.pack(side="left",padx=2,pady=4)

#buttons for frame 4
button_mode = customtkinter.CTkButton(frame_4,command=modes,height=70,width=85,fg_color="#2e2d2d",hover_color="#30302f",text="Light\nMode",font=("Cascadia",20,"bold"))
button_mode.pack(side="left",padx=2,pady=4) 

button_0 = customtkinter.CTkButton(frame_4,command=lambda:show("0"),height=70,width=85,fg_color="#4d4c4c",hover_color="#30302f",text="0",font=("Cascadia",36,"bold"))
button_0.pack(side="left",padx=2,pady=4) 

button_dot = customtkinter.CTkButton(frame_4,command=lambda:show("."),height=70,width=85,fg_color="#4d4c4c",hover_color="#30302f",text=".",font=("Cascadia",36,"bold"))
button_dot.pack(side="left",padx=2,pady=4)

button_equals = customtkinter.CTkButton(frame_4,command=enter,height=70,width=85,fg_color="#ede215",text_color="#3b3a37",hover_color="#2e2d2d",text="=",font=("Cascadia",36,"bold"))
button_equals.pack(side="left",padx=2,pady=4)

window.mainloop()