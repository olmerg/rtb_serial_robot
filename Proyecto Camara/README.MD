Realizado por el curso de Robotica Industrial 2021-II de Ingeniería en automatización de Universidad Jorge Tadeo Lozano

Profesor: Olmer Garcia Bedoya (@olmerg)

Grupo 1: Juan Sebastian Reina-Valentina Vega-Cristian Paez

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Tarjetas.png)


# PROYECTO FINAL ROBÓTICA INDUSTRIAL 

# Identificación del reto 🤖📷

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


el robot seleccionado para el proyecto final fue un robot de 6 grados de libertad Los propósitos generales del desarrollo de este robot son la versatilidad y la adaptabilidad.con el fin de Acelerar la obtención de los análisis de los laboratorios.

### 📃 Contenido

1. Descripción de la elaboración del modelo

1. simulación URDF


1. Cinematica directa en python


1. Cinematica inversa


1. Trayectorias


1. Visualización final


1. Aplicación serial arduino



#### 1. Descripción de la elaboración del modelo-

Inicialmente se elaboro el modelo de cada una de las piezas del robot en inventor manteniendo las dimenciones de robot fisico, con el fin de poder hacer los ensambles necesarios para simular posteriormente los URDF en ROS.  


![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/WhatsApp%20Image%202021-10-05%20at%2012.21.24%20AM.jpeg)


![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/WhatsApp%20Image%202021-10-05%20at%2012.14.21%20AM.jpeg)


![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/WhatsApp%20Image%202021-10-05%20at%2012.14.51%20AM.jpeg)

#### 2. simulación URDF ROS 🐢 -

A continuación se usan los ensambles simulados en formato stl para hacer el URDF del robot y la simulación de movimientos e identificar las limitaciones de movimiento


![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/WhatsApp%20Image%202021-11-04%20at%205.22.31%20PM.jpeg)

![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/WhatsApp%20Image%202021-11-04%20at%205.22.05%20PM.jpeg)

![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/WhatsApp%20Image%202021-11-04%20at%205.23.50%20PM.jpeg)

![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/WhatsApp%20Image%202021-11-04%20at%205.20.53%20PM.jpeg)

![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/WhatsApp%20Image%202021-11-04%20at%205.21.16%20PM.jpeg)


#### 3. Cinematica directa en python 🐍-

Consiste en determinar cual es la posición y orientación del extremo final del robot, con respecto a un sistema de coordenadas que se toma como referencia, conocidos los valores de las articulaciones y los parámetros geométricos de los elementos del robot

1.  inicialmente se importan las librerias que requiere python para ejecutar el codigo satisfactoriamente.

![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20directa/Captura%20de%20pantalla%202021-11-06%20001356.png)


![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20directa/Captura%20de%20pantalla%202021-11-06%20001556.png)


![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20directa/Captura%20de%20pantalla%202021-11-06%20001647.png)


![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20directa/Captura%20de%20pantalla%202021-11-06%20001741.png)


![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20directa/Captura%20de%20pantalla%202021-11-06%20001831.png)


![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20directa/Captura%20de%20pantalla%202021-11-06%20001948.png)


#### 4. Cinematica inversa en python 🐍--

En Robótica, la Cinemática inversa (IK) es la técnica que permite determinar el movimiento de una cadena de articulaciones para lograr que un actuador final se ubique en una posición concreta. El cálculo de la cinemática inversa es un problema complejo que consiste en la resolución de una serie de ecuaciones cuya solución normalmente no es única.


![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20inversa/Captura%20de%20pantalla%202021-11-06%20232157.png)
![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20inversa/Captura%20de%20pantalla%202021-11-06%20232229.png)
![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20inversa/Captura%20de%20pantalla%202021-11-06%20232314.png)
![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20inversa/Captura%20de%20pantalla%202021-11-06%20232340.png)
![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20inversa/Captura%20de%20pantalla%202021-11-06%20232454.png)
![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20inversa/Captura%20de%20pantalla%202021-11-06%20232528.png)
![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20inversa/Captura%20de%20pantalla%202021-11-06%20232556.png)


#### 5. Trayectorias 📈-

![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/trayectorias/Captura%20de%20pantalla%202021-11-06%20233159.png)
![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/trayectorias/Captura%20de%20pantalla%202021-11-06%20233332.png)
![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/trayectorias/Captura%20de%20pantalla%202021-11-06%20233404.png)

#### 6. Visualización final  🏁 -

#### 7. Aplicación serial arduino-



## Autores ✒️


_Las siguientes personas colaboraron con el desarrollo del proyecto_

* **Juan Felipe Cañas Bustos** - [JuanCañas](https://github.com/jcscorpion)
* **Cristian Hernandez Salazar** - [CristianHernandez](https://github.com/cristianchernandezs)