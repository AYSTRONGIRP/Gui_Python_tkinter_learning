import tkinter as tk
from tkinter import ttk


def button_functions():
    print('Button function')

window = tk.Tk()
window.title("widget_working")
window.geometry("600x600")

#ttk widget
label = ttk.Label(master= window , text = 'Label')
label.pack()

#create widget 
text1 = tk.Text(master = window , cursor= '')
text1.pack()

#ttk entry 
entry = ttk.Entry(master = window)
entry.pack()

# ttk button 
button = ttk.Button(master = window , text= 'Button' , command = button_functions)
button.pack()

# exercise label 
exercise_label = ttk.Label(master=window , text= 'Exercise')
#run
window.mainloop()

#only run after the window is closed