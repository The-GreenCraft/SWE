import tkinter as tk
root = tk.Tk()

label1 = tk.Label(root, text="Hello World")
button = tk.Button(root, text="Button")
bild = tk.PhotoImage(file="../../pictures/json.png")
eingabefeld = tk.StringVar()
label2 = tk.Label(root, image=bild).pack()
eingabe=tk.Entry(root, textvariable=eingabefeld)
button.pack()
label1.pack()
eingabe.pack()
root.mainloop()