# Resolución de la Actividad 2
### 1 HTTP: Fundamentos y herramientas
#### 1.1 Reporte de salida stdout de la aplicación Flask

```shell
(venv) ~/Documents/UNI/Desarrollo_software/CC3S2/Actividades/Actividad2-CC3S2
↳ fernando@Nitro-5$ PORT=8080 MESSAGE="Hola CC3S2" RELEASE="v1" python3 miapp/app.py
{"ts": "2025-09-12T15:47:40-0500", "level": "INFO", "event": "startup", "port": 8080}
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080
 * Running on http://192.168.1.38:8080
Press CTRL+C to quit
{"ts": "2025-09-12T15:47:53-0500", "level": "INFO", "event": "request", "method": "GET", "path": "/", "remote": "127.0.0.1", "proto": "http"}
127.0.0.1 - - [12/Sep/2025 15:47:53] "GET / HTTP/1.1" 200 -
{"ts": "2025-09-12T15:47:53-0500", "level": "INFO", "event": "request", "method": "GET", "path": "/favicon.ico", "remote": "127.0.0.1", "proto": "http"}
127.0.0.1 - - [12/Sep/2025 15:47:53] "GET /favicon.ico HTTP/1.1" 404 -
{"ts": "2025-09-12T15:48:45-0500", "level": "INFO", "event": "request", "method": "GET", "path": "/notfound", "remote": "127.0.0.1", "proto": "http"}
127.0.0.1 - - [12/Sep/2025 15:48:45] "GET /notfound HTTP/1.1" 404 -
```

#### 1.2 Inspección con curl

- `curl -v http://127.0.0.1:8080/` (cabeceras, código de estado, cuerpo JSON)

```shell
*   Trying 127.0.0.1:8080...
* Connected to 127.0.0.1 (127.0.0.1) port 8080
> GET / HTTP/1.1
> Host: 127.0.0.1:8080
> User-Agent: curl/8.5.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Server: Werkzeug/3.1.3 Python/3.12.3
< Date: Fri, 12 Sep 2025 20:52:37 GMT
< Content-Type: application/json
< Content-Length: 124
< Connection: close
< 
{"headers":{"X-Forwarded-For":null,"X-Forwarded-Host":null,"X-Forwarded-Proto":null},"message":"Hola CC3S2","release":"v1"}
* Closing connection
```

> Podemos apreciar las cabeceras HTTP: Server, Date, Content-Type, Content-Length, el código de estado 200 OK y el cuerpo JSON con el mensaje, release y headers.

- `curl -i -X POST http://127.0.0.1:8080`

```shell
HTTP/1.1 405 METHOD NOT ALLOWED
Server: Werkzeug/3.1.3 Python/3.12.3
Date: Fri, 12 Sep 2025 21:00:16 GMT
Content-Type: text/html; charset=utf-8
Allow: OPTIONS, GET, HEAD
Content-Length: 153
Connection: close

<!doctype html>
<html lang=en>
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>
```
> Aquí podemos observar el código de estado 405 METHOD NOT ALLOWED, indicando que el método POST no está permitido en la ruta `/`.

- Pregunta guía: ¿Qué campos de respuesta cambian si actualizas MESSAGE/RELEASE sin reiniciar el proceso? Explica por qué.

> Al actualizar las variables de entorno MESSAGE y RELEASE sin reiniciar el proceso, los campos en la respuesta JSON no cambian. Esto se debe a que las variables de entorno son leídas por la aplicación Flask al momento de su ejecución.

#### 1.3 Puertos abiertos con `ss`

- `ss -ltnp | grep :8080`

```shell
↳ fernando@Nitro-5$ ss -ltnp | grep :8080
LISTEN 0      128          0.0.0.0:8080       0.0.0.0:*    users:(("python3",pid=35514,fd=3))
```

> Se aprecia como el proceso `python3` está escuchando en el puerto 8080 en todas las interfaces del sistema.

#### 1.4 Logs como flujo: Demuestra que los logs salen por stdout (pega 2–3 líneas). Explica por qué no se escriben en archivo (12-Factor).

> En la siguiente captura de pantalla se observa la salida de logs en la terminal donde se ejecuta la aplicación Flask:

![Captura de logs en terminal](images/logs_stdout.png)

Estos mensajes se imprimen en **stdout** (flujo de salida estándar).  
Por defecto, `stdout` está asociado a la terminal, por lo que los logs aparecen directamente allí.  
La aplicación no escribe en archivos locales, sino que delega al entorno (Docker, systemd, Kubernetes, etc.) la captura y persistencia de los logs, siguiendo el principio de 12-Factor App.

### 2 DNS: nombres, registros y caché

#### 2.1 Hosts local
> Use el target hosts-setup del Makefile para añadir las entradas necesarias en /etc/hosts.

![ejecucion make hosts-setup](images/make_host.png)

#### 2.2 Comprueba resolución
![resolucion de miapp.local](images/dig.png)


#### 2.3 TTL/caché
> El TTL indica cuánto tiempo los resolutores pueden cachear esa respuesta antes de volver a preguntarle a un servidor autoritativo.