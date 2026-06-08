import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# Ievades lauki un to etiķetes
tk.Label(root, text="Vārds:").grid(row=0, column=0, sticky="W", pady=10, padx=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Uzvārds:").grid(row=1, column=0, padx=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Poga apakšā
tk.Button(root, text="Iesniegt").grid(row=2, column=0, columnspan=2, sticky="W", padx=10, pady=10)

root.mainloop()