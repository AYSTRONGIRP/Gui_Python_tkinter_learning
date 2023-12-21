import tkinter as tk 
from tkinter import ttk
import ttkbootstrap as ttk
def convert():
    print("Converting") 
    mile_input = entryInt.get()
    km_output = mile_input*1.61
    print(entry.get())
    print(entryInt.get()) 
    output_string.set(km_output)

#windows platform
window = ttk.Window(themename='journal')
window.title("demo")
window.geometry("400x400")

title_label = ttk.Label(master = window ,text ="Miles to Kilometers" , font = 'Calibri 24 bold')
title_label.pack()

#create input field
input_frame = ttk.Frame(master = window) 
entryInt = tk.IntVar()  
entry = ttk.Entry(master = input_frame , textvariable=entryInt)
button = ttk.Button(master = input_frame, text = 'convert ' , command = convert)
entry.pack(side = 'left' ,padx = 10)
button.pack(side = 'right' , padx = 10)
input_frame.pack(pady = 10)

#output 
output_string = tk.StringVar()
output_label = ttk.Label(master=window , 
                         text=output_string , 
                         font = "Calibri 24",
                         textvariable=output_string )
output_label.pack(pady=10)

#run
window.mainloop()
