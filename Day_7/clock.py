import tkinter as tk                        # this will import tikinter as tk.
from time import strftime                   # this will import date and time from time module.

root = tk.Tk()  # here we created root window using tkinter
root.title(" Digital Clock ")

# Created Label window where time will display. 
label = tk.Label(root,font=("calibri",30,'bold'),background="black",foreground="white")
label.pack(anchor="center")  

# function that will display time.
def time():
    string = strftime('%H:%M:%S %p \n%D')
    label.config(text=string)
    label.after(1000,time)
    
    
# invoked the main function.
time()
root.mainloop()    

 