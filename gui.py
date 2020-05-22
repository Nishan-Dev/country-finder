import tkinter as tk
from tkinter import filedialog, Text
import os
from text import namespace as name

root = tk.Tk()
apps = []

x = name()
y = x.addApps()


def runApps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=.8, relheight=.8, relx=.1, rely=.1)

openFile = tk.Button(root, text="open File", padx=10, pady=5, fg="white", bg="#263D42", command=y)
openFile.pack()

runApps = tk.Button(root, text="run apps", padx=10, pady=5, fg="white", command=runApps())

runApps.pack()

root.mainloop()

with open(' save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
