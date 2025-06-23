
from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route("/canal_24_7")
def canal_24_7():
    with open("/home/tatiana2006/mysite/programacion.json", "r", encoding="utf-8") as f:
        videos = json.load(f)
        server_time = int(time.time())
    return render_template("index.html", videos=videos,server_time=server_time)



if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)


