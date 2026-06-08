import tkinter

def paradi_tekstu():
    rezult.config(text=f"Ievadīji: {entry.get()}")

window = tkinter.Tk()

window.title("Pirmā GLS programma")
window.minsize(width=500, height=300)

#uzraksti
virsraksts = tkinter.Label(text="Ievadi kaut ko un nospied pogu!", font=("Arial", 24, "italic"))
virsraksts.pack(pady=10)

#datu ievade
entry = tkinter.Entry(window)
entry.pack(pady=10)

#pogas izveide
poga = tkinter.Button(window, text="Nospied!", command=paradi_tekstu, fg="green", bg="yellow")
poga.pack(pady=10)

#rezultāts
rezult = tkinter.Label()
rezult.pack(pady=10)

tkinter.Label(window, text="Augšā", bg="red").pack(fill="x")
tkinter.Label(window, text="Kreisajā pusē", bg="blue").pack(side="left", fill="y")
tkinter.Label(window, text="Labajā pusē", bg="green").pack(side="right", fill="y")
tkinter.Label(window, text="Apakšā", bg="yellow").pack(side="bottom", fill="x")


window.mainloop()