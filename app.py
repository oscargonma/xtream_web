
from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

USERNAME = "zuly77rtvuy"
PASSWORD = "FZAUN"
BASE_URL = "http://maxcuentas.lat:8080"

def obtener_canales_desde_xtream():
    url = f"{BASE_URL}/player_api.php?username={USERNAME}&password={PASSWORD}&action=get_live_streams"
    respuesta = requests.get(url)
    datos = respuesta.json()
    
    canales = []
    for canal in datos:
        canales.append({
            "name": canal["name"],
            "url": f"{BASE_URL}/live/{USERNAME}/{PASSWORD}/{canal['stream_id']}.m3u8"
        })
    return canales


@app.route('/')
def index():
    return render_template("index.html")



@app.route("/load_channels")
def load_channels():
    try:
        canales = obtener_canales_desde_xtream()
        return jsonify(canales)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

