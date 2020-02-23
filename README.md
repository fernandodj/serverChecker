# serverChecker

Servicio dedicado a recolectar datos relevantes de un servidor y enviarlos hacia otro servicio centralizado que guarda estos datos.

El servicio consta de un sólo script donde se realiza la recolección de datos, para ejecutarlo es necesario tener instalado Python (deseable Python 2) e instalar vía pip la librería "requests" necesaria para realizar la request hacia el servicio que guarda los datos.

Instalamos librería requests:

`pip install requests` 

Ejemplo de comando para ejecutar el servicio:

` serverChecker/app$ python agent.py `  
