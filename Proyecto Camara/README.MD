Realizado por el curso de Robotica Industrial 2021-II de Ingeniería en automatización de Universidad Jorge Tadeo Lozano

Profesor: Olmer Garcia Bedoya (@olmerg)

Grupo 1: Juan Sebastian Reina-Valentina Vega-Cristian Paez

# PROYECTO FINAL ROBÓTICA INDUSTRIAL 

# Identificación del reto 🦾📷

## 📃 Descripción
Nuestro reto consiste en desarrollar un brazo robótico camarógrafo, es decir, un brazo robótico 
que cuenta con una cámara en la punta, la cual sigue determinadas trayectorias definidas previamente 
por un director de cámara y que dependen del propósito del video. Este robot lo que permite es realizar 
movimientos más precisos, concisos y uniformes comparados con un operador humano, además de realizar
tareas o poses más complejas con las cuales un ser humano tendría bastantes problemas en realizar por su 
propia morfología como podemos ver en el video de ejemplo.
## --> https://www.youtube.com/watch?v=UIwdCN4dV6w 
Esto es un hito en la utilización de brazos robóticos en entornos artísticos y no tan industriales, 
donde el robot tiene que trabajar junto al ser humano en tareas más humanas y que dependen de la creatividad, 
ya que eventualmente un robot puede aprender estas cosas y no limitarse solo a seguir trayectorias predefinidas. 
Esta es nuestra forma de acercarnos a la fusión arte y ciencia que se define como uno de los pilares, si no 
el más importante de la universidad Jorge Tadeo Lozano.


El robot seleccionado para el proyecto final fue un robot de 6 grados de libertad Los propósitos generales del 
desarrollo de este robot son la versatilidad y la adaptabilidad.con el fin de Acelerar la obtención de los 
análisis de los laboratorios.

### Contenido 📑

1. Elaboración del modelo 3D

1. Simulación URDF en ROS

1. Corte láser del robot

1. Control de peso de los Links físicos

1. Cinematica directa en python


1. Cinematica inversa


1. Trayectorias


1. Aplicación serial arduino



#### 1. Elaboración del modelo 3D

Inicialmente elaboramos el modelo de cada una de las piezas,(lista al final de este párrafo),del robot en Autodesk 
Inventor, manteniendo las dimensiones del robot fisico que pedimos prestado en la universidad, con el fin de poder 
hacer los ensambles necesarios para simular posteriormente los URDF en ROS.  


![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Listado%20Piezas%20del%20Cuerpo.PNG)

Listado de piezas del cuerpo del robot

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Listado%20Piezas%20de%20la%20Pinza.PNG)

Listado de piezas de la pinza del robot

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/CapturaPiezaCuerpoRobot1.PNG)

Soporte Base de Servomotores(Hombro)

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/CapturaPiezaCuerpoRobot2.PNG)

ServoMotor (MG995)

Ya con todas con todas las piezas diseñadas, realizamos el ensamblaje del robot  y se modeló. Se realizaron uniones rotacionales
 para el conjunto de piezas que lo necesitaran.
![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/CapturaEnsambeCompleto.PNG)

Ensamble completo del robot

#### 2. Simulación URDF en ROS 

Con el ensamblaje realizado procedimos a obtener los 6 archivos STL que necesitamos, para posteriormente recrear el robot en ROS

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Captura%20LINK%20BASE.PNG)

STL Link Cadera

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Captura%20LINK%201.PNG)

STL Link Hombro

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Captura%20LINK%202.PNG)

STL Link Brazos

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Captura%20LINK%203.PNG)

STL Link Antebrazo

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Captura%20LINK%204.PNG)

STL Link Muñeca

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Captura%20LINK%205.PNG)

STL Link Gripper

Luego cargamos estos archivos STL para recrear nuestro modelo mediante la herramienta RVIZ en ROS, lo que 
nos permitió aprender sobre las diversas formas de visualizar un robot y poder manipularlo mediante un 
nodo publisher, de manera que podamos ver algunos aspectos de la cinemática directa del mismo.
Fue importante para solucionar el reto, ya que a partir de modelos 3D creados en inventor pudimos evaluar 
las posibilidades del robot y ver si efectivamente a la hora de ensamblarlo iba a cumplir con nuestras 
expectativas, es una forma interesante de conocer un robot sin nisiquiera tener la parte física, el RVIZ 
nos permitió interactuar con él y ver como funcionan cada una de sus articulaciones y los límites que debemos 
tener en cuenta a la hora de programar en arduino.

Pero para visualizar el robot en RVIZ tuvimos que hacer el siguiente código en el que especifica para cada link,
su nombre, su origen, su ruta de acceso, el color, su padre, su hijo y el tipo de unión que queriamos.

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Captura%20c%C3%B3digo%20URDF%201.PNG)
![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Captura%20c%C3%B3digo%20URDF%202.PNG)
![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Captura%20c%C3%B3digo%20URDF%203.PNG)
![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Captura%20c%C3%B3digo%20URDF%204.PNG)
![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Captura%20c%C3%B3digo%20URDF%205.PNG)

Ya luego de este código y de algunos códigos en la consola, pudimos llegar a esta visualización.

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/urdf0.PNG)

Cuando ejecutamos el código, podemos abrir la siguiente ventana, que nos permite cambiar los grados de cada Join
y de esta manera llegar a la posición que queramos, siempre y cuando sea posible espacialmente.

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Captura%20URDF.jpeg)

Algunos ejemplos de otras posiciones que logramos son las siguientes:

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/urdf1.PNG)

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/urdf4.PNG)

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/urdf6.PNG)

Toda esta parte de la programación y visualización en ROS está más detallado en este video
## --> https://www.youtube.com/watch?v=fcq3hT-I8CQ

#### 3.Corte láser del robot

Para el corte láser creamos estos 3 archivos PDF tamaño A4, los obtuvimos a partir de los archivos DWG
que creamos en Autodesk Inventor. 

![Click Aquí para ver PDF 1](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Plano%20de%20CORTE%201.pdf)

![Click Aquí para ver PDF 2](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Plano%20de%20CORTE%202.pdf)

![Click Aquí para ver PDF 3](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Plano%20de%20CORTE%203.pdf)

#### 4. Control de peso de los Links físicos

Con los motores y cables brindados por la Universidad, junto a las las piezas que cortamos y con los tornillos,tuercas y la 
cámara que compramos, empezamos con la construcción o ensamblaje del robot físico

Pero antes de armarlo completamente, armamos cada Link del robot

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Robot%20separado.jpg)

Luego pesamos cada uno de los Links

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Pesaje%20Base.jpg)

Pesaje de la base

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Pesaje%20Brazos.jpg)

Pesaje de los brazos

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Pesaje%20Antebrazos.jpg)

Pesaje de los antebrazos

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Pesaje%20mu%C3%B1eca.jpg)

Pesaje de la muñeca

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Pesaje%20Camara.jpg)

Pesaje del "gripper" o cámara en nuestro caso

Luego, terminamos de armar nuestro robot, y verificamos su alcance vertical y horizontal con respecto
al modelo que hicimos en el URDF, estos 2 modelos no variaban en distancias.

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/AlcanceHorizontal.png)

Robot posicionado en su alcance horizontal máximo

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/AlcanceVertical.png)

Robot posicionado en su alcance vertical máximo


#### 5. Cinematica directa en python 🐍-

Consiste en determinar cual es la posición y orientación del extremo final del robot, con respecto a un sistema de 
coordenadas que se toma como referencia, conocidos los valores de las articulaciones y los parámetros geométricos de los elementos del robot

Este es el código que usamos

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/CapturaCodigoCinematicaDirecta.PNG)

Esto es lo que se imprime en la consola

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/CapturaTerminalCinematicaDirecta.PNG)

Estos son los plot que generamos, el plot de la parte derecha viene con las barras deslizadoras que permiten 
cambiar el ángulo de cada una de las uniones.

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/CapturaPlotCinematicaDirecta.PNG)

#### 6. Cinematica inversa en python 🐍--

En Robótica, la Cinemática inversa (IK) es la técnica que permite determinar el movimiento de una cadena de articulaciones para lograr que un actuador final se ubique en una posición concreta. El cálculo de la cinemática inversa es un problema complejo que consiste en la resolución de una serie de ecuaciones cuya solución normalmente no es única.


![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20inversa/Captura%20de%20pantalla%202021-11-06%20232157.png)
![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20inversa/Captura%20de%20pantalla%202021-11-06%20232229.png)
![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20inversa/Captura%20de%20pantalla%202021-11-06%20232314.png)
![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20inversa/Captura%20de%20pantalla%202021-11-06%20232340.png)
![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20inversa/Captura%20de%20pantalla%202021-11-06%20232454.png)
![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20inversa/Captura%20de%20pantalla%202021-11-06%20232528.png)
![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20inversa/Captura%20de%20pantalla%202021-11-06%20232556.png)


#### 7. Trayectorias 📈-

![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/trayectorias/Captura%20de%20pantalla%202021-11-06%20233159.png)
![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/trayectorias/Captura%20de%20pantalla%202021-11-06%20233332.png)
![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/trayectorias/Captura%20de%20pantalla%202021-11-06%20233404.png)

#### 8. Aplicación serial arduino-

## Autores 🤵👩‍🎓🤵


_Las siguientes personas colaboraron con el desarrollo del proyecto_

* **Juan Sebastian Reina** - [JuanSebastianReina](https://github.com/JuanSebastianReina)
* **Valentina Vega Mahecha** - [vale2012](https://github.com/vale2012)
* **Cristian Paez** - []()