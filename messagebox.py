from tkinter import *
from tkinter import messagebox
def Exit_Application():
    answer = messagebox.askyesno(title="Exit Application",
                              message="Are you sure exit the application?", icon="warning")
    if (answer == True):
        print("Yes, you will exit the application.")
    else:
        messagebox.showinfo(title="Return",message=" You will now return to the application screen")
window=Tk()
window.geometry("100x100")
r_button =Button(window,text =" Exit Application", command =Exit_Application, bg ="red",
                 fg="white")
canvas1 = Canvas(window, width = 100, height = 100)
canvas1.pack()
r_button.pack()
window.mainloop()






