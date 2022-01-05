from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def lista_api():
    lista = requests.get("https://api.adviceslip.com/advice")
    lista = lista.json()

    return render_template("index.html", id = lista['slip']['id'], advice = lista['slip']['advice'] )

if __name__ == '__main__':   
    #lista_api()
    app.run(use_reloader = True, debug = True)