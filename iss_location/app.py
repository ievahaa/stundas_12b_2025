import datetime
import requests
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

atbilde = requests.get(url="http://api.open-notify.org/iss-now.json")

atbilde.raise_for_status()
dati = atbilde.json()["iss_position"]
laiks = atbilde.json()["timestamp"]
platums = dati["latitude"]
garums = dati["longitude"]

dt = datetime.datetime.fromtimestamp(laiks)
datums = f"{dt.day:02d}.{dt.month:02d}.{dt.year:04d} {dt.hour:02d}:{dt.minute:02d}:{dt.second:02d}"


print(datums,platums,garums)

#mājaslapas forma
@app.route("/")
def home():
    return render_template("index.html")

#Datu saglabāšana
@app.route("/submit", methods=["get"])
def submit(laiks, platums, garums):
    if request.method == "get":
            conn = sqlite3.connect("./iss_location/database.db")
            conn.execute("INSERT INTO iss_loc (datums, platums, garums) VALUES (?, ?, ?)", (laiks, platums, garums))
            conn.commit()
            conn.close()
    return redirect("/") #pēc datu saglabāšanas atgriežas uz sākuma lapu

submit()

if __name__ == "__main__":
     app.run(debug=True)