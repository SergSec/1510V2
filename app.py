from flask import Flask, request, jsonify, render_template_string
import datetime, json, os, requests

app = Flask(__name__)

LOG_FILE = "capturas_local.txt"

REQUEST_BIN_URL = "https://webhook.site/tutoken"

def guardar_local(entry):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

@app.route("/")
def index():
    return render_template_string("""
    <html>
    <head><meta charset="utf-8"><title>Captura User-Agent</title></head>
    <body style="font-family: system-ui; margin: 2em;">
      <h2>Captura de cabeceras (User-Agent)</h2>
      <p>El navegador enviará una petición al servidor local y otra al RequestBin.</p>
      <p>Haz clic en el botón para probar:</p>
      <button onclick="enviar()">Enviar petición</button>
      <pre id="out"></pre>
      <script>
        async function enviar() {
          document.getElementById('out').textContent = "Enviando...";
          const res = await fetch('/capturar');
          const data = await res.json();
          document.getElementById('out').textContent = JSON.stringify(data, null, 2);
        }
      </script>
    </body>
    </html>
    """)

@app.route("/capturar")
def capturar():
    now = datetime.datetime.utcnow().isoformat() + "Z"
    ua = request.headers.get("User-Agent", "")
    ip = request.remote_addr

    datos = {
        "timestamp": now,
        "ip": ip,
        "user_agent": ua,
        "headers": dict(request.headers)
    }

    guardar_local(datos)

    try:
        requests.post(REQUEST_BIN_URL, json=datos, timeout=5)
    except Exception as e:
        print(f"[!] No se pudo enviar a RequestBin: {e}")

    return jsonify({"status": "ok", "user_agent": ua})

@app.route("/ver")
def ver():
    if not os.path.exists(LOG_FILE):
        return "No hay capturas aún.\n"
    with open(LOG_FILE, encoding="utf-8") as f:
        contenido = f.read()
    return f"<pre>{contenido}</pre>"

if __name__ == "__main__":
    print("Servidor iniciado en http://127.0.0.1:5000")
    print("Abrir en el navegador.")
    app.run(host="127.0.0.1", port=5000, debug=False)
