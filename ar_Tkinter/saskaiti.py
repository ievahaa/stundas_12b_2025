import tkinter as tk

def aprekinat():
    try:
        sk1 = float(entry1.get())
        sk2 = float(entry2.get())
        rezultats.config(text=f"Rezultāts: {sk1 + sk2}")
    except ValueError:
        rezultats.config(text="Netika ievadīts skaitlis")

def dzest():
    entry1.delete(0, tk.END) 
    entry2.delete(0, tk.END)
    rezultats.config(text="Rezultāts:")

logs = tk.Tk()
logs.minsize(width=400, height=300)

tk.Label(logs, text="1. skaitlis:", font=("bold",18)).pack()
entry1 = tk.Entry(logs)
entry1.pack()

tk.Label(logs, text="2. skaitlis:", font=("bold",18)).pack()
entry2 = tk.Entry(logs)
entry2.pack()

tk.Button(logs, text="Saskaitīt", command=aprekinat, font=(18)).pack(pady=10)
tk.Button(logs, text="Nodzēst", command=dzest, font=(18)).pack(pady=10)

rezultats = tk.Label(logs, text="Rezultāts: ", font=(18))
rezultats.pack(side="left", padx=10)

logs.mainloop()
