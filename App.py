import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

# Size
canvas = tk.Canvas(root, height=700, width=700, bg='#263D42')
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relheight=0.8, relwidth=0.8, relx=0.1, rely=0.1)

apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.split()]


# Open Apps function
def addApps():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir='/', title='Select Files',
                                          filetypes=(('executables', '*.exe'), ('all files', '*.*')))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg='gray')
        label.pack()


openApps = tk.Button(root, text="Open Apps", padx=10, pady=5, fg='white', bg='#263D42', command=addApps)
openApps.pack()


# Run apps function
def runApps():
    for app in apps:
        os.startfile(app)


runApps = tk.Button(root, text="Run files", padx=10, pady=5, fg='white', bg='#263D42', command=runApps)
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app, bg='gray')
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
