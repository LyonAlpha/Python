import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.title("App Starter")
apps = []

if os.path.isfile("save.txt"):
    with open("save.txt", "r") as f:
        tempApps = f.read()
        tempapps = tempApps.split(",")
        apps = [x for x in tempapps if x.strip()]

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", 
                                        filetypes=(("Executables","*.exe"), ("All Files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

def deleteApps():
    os.startfile("save.txt")

# To Change Height And Width, Change The Variable Below

mainheight = 500
mainwidth = 800

canvas = tk.Canvas(root, height=mainheight, width=mainwidth, bg="#263D42") 
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File / Apps", padx=10, pady=5, fg="white", bg= "#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg= "#263D42", command=runApps)
runApps.pack()

deleteApps = tk.Button(root, text="Delete Apps", padx=10, pady=5, fg="white", bg= "#263D42", command=deleteApps)
deleteApps.pack()



def close_root(e):
   root.destroy()
# Add a label widget
label = ttk.Label(root, text="Press Esc To Quit", font=('Times New Roman italic', 18), background="gray", foreground="white")
label.pack()

# Bind the ESC key with the callback function
root.bind('<Escape>', lambda e: close_root(e))

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open("Save.txt", 'w') as f:
    for app in apps:
        f.write(app + ",")

    