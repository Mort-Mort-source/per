# Guia de uso

## 1. Ejecutar el *broker*
abre una terminal (*cmd*)
~~~bash
python broker.py
~~~

se mostrara como resultado:
~~~bash 
[BROKER] escuchando en 0.0.0.0:14000...
~~~

## 2. Ejecutar uno o mas suscriptores

abre una terminal y ejecuta un suscriptor
o mas
~~~bash 
python subscriber.py
~~~
cuando se te pida, escribe el tema (*topic*), por ejemplo:
~~~bash
Tema a suscribirse: deportes
~~~
El sistema mantendra la conexion abierta esperando mensajes del *broker*

## 3. Ejecutar uno o mas publicadores
En otra terminal: 
~~~bash
python publisher.py
~~~
Envia un mensaje con este formato:
~~~bash
deportes: !El America gano 15-0¡
~~~
todos los *suscriptores* suscritos a *deportes* recibiran:
~~~bash
[deportes] ¡El pumas gano 5-0!
~~~ 