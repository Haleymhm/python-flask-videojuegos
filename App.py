from flask import Flask, render_template, request, redirect, flash
import gameController

app = Flask(__name__)

# settings SESSION
app.secret_key = "mysecretkey"

@app.route("/")
@app.route("/games")
def getGames():
    juegos = gameController.obtener_juegos()
    return render_template("juegos.html", juegos=juegos)