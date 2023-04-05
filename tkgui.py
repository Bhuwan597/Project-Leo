import tkinter as tk
import tkinter.font as tkFont

def tkinter_input(title,label_title):
    global to
    root = tk.Tk()
    #setting title
    root.title(title)
    #setting window size
    width=484
    height=220
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)
    entry_value = tk.StringVar()
    GLineEdit_219=tk.Entry(root,textvariable=entry_value)
    GLineEdit_219["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    GLineEdit_219["font"] = ft
    GLineEdit_219["fg"] = "#333333"
    GLineEdit_219["justify"] = "center"
    GLineEdit_219.place(x=100,y=90,width=286,height=48)

    def command():
        global to
        to = entry_value.get()
        root.destroy()

    GButton_980=tk.Button(root)
    GButton_980["activebackground"] = "#5fb878"
    GButton_980["activeforeground"] = "#fbf5f5"
    GButton_980["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times',size=14)
    GButton_980["font"] = ft
    GButton_980["fg"] = "#000000"
    GButton_980["justify"] = "center"
    GButton_980["text"] = "Ok"
    GButton_980.place(x=200,y=160,width=107,height=33)
    GButton_980["command"] = command
    GLabel_269=tk.Label(root)
    GLabel_269["activeforeground"] = "#5fb878"
    ft = tkFont.Font(family='Times',size=16)
    GLabel_269["font"] = ft
    GLabel_269["fg"] = "#333333"
    GLabel_269["justify"] = "center"
    GLabel_269["text"] = label_title
    GLabel_269.place(x=40,y=30,width=409,height=58)


    root.mainloop()

