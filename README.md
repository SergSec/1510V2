Captura de Cabeceras HTTP (User-Agent)

Este proyecto demuestra cómo **capturar y registrar cabeceras HTTP**, especialmente el campo **`User-Agent`**, usando un **servidor Flask local** y **RequestBin (webhook.site)** para visualizar la información.

---

## Descripción

El servidor Flask recibe peticiones HTTP desde el navegador y:
- Obtiene las cabeceras de la petición (por ejemplo, `User-Agent`, `Host`, `Accept`, etc.).
- Guarda la información en un archivo local (`capturas_local.txt`).
- Envía una copia de los datos al servicio **[webhook.site](https://webhook.site)** para poder verlos en la web.

---

## Estructura del proyecto

proyecto_captura_user_agent/
│
├── app.py                # Servidor Flask principal
├── demo.html             # Página de demostración HTML
└── capturas_local.txt    # Archivo donde se guardan las capturas (se genera al ejecutar)

---

## ⚙️ Requisitos

- Python 3.x instalado  
- Librerías necesarias:
  pip install flask requests
- Una cuenta o enlace en [https://webhook.site](https://webhook.site) 

---

## Ejecución del proyecto

###  Configurar la URL de Webhook.site
1. Abre https://webhook.site  
2. Copia la URL única que te aparece (por ejemplo):
   https://webhook.site/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
3. En el archivo `app.py`, reemplaza la línea:
   REQUEST_BIN_URL = "https://webhook.site/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
   por tu propia URL.

---

### 2️⃣ Iniciar el servidor Flask
En la carpeta del proyecto, ejecuta:

python app.py

verás un mensaje:
Servidor iniciado en http://127.0.0.1:5000

---

### Probar en el navegador

Abre en tu navegador:
http://127.0.0.1:5000

Haz clic en el botón **"Enviar petición"**.

El servidor:
- Capturará tu cabecera `User-Agent`
- La guardará en `capturas_local.txt`
- Enviará los datos a tu URL de Webhook.site

---

###Ver resultados

### En local:
Abre el archivo:
capturas_local.txt

---

### Ver registros desde el navegador

También puedes ver las capturas guardadas localmente accediendo a:

http://127.0.0.1:5000/ver

---

