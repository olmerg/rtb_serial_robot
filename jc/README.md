# PROYECTO FINAL  JC25馃殌
![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/robot1.jpeg)

# Identificaci贸n del reto 馃

## 馃搩 Descripci贸n
Debido al covid 19, muchos hospitales y laboratorios tuvieron m煤ltiples
problemas para continuar trabajando en el an谩lisis de pruebas o muestras,
adem谩s con la llegada de la crisis aumentaron la cantidad de muestras,
debido a esto se desea probar robots colaborativos para optimizar los
procesos en los laboratorios.

el robot seleccionado para el proyecto final fue un robot de 6 grados de libertad Los prop贸sitos generales del desarrollo de este robot son la versatilidad y la adaptabilidad.con el fin de Acelerar la obtenci贸n de los an谩lisis de los laboratorios.

### 馃搩 Contenido



1. Objetivos

1. Hardware del robot 

1. Software de simulaci贸n y programaci贸n

1. Descripci贸n de la elaboraci贸n del modelo

1. simulaci贸n URDF


1. Cinematica directa en python


1. Cinematica inversa en python 


1. Trayectorias


1. Visualizaci贸n final


1. Aplicaci贸n serial arduino

1. Resultados


1. Conclusi贸nes



#### 1. Objetivos

##### objetivo general

Realizar la programaci贸n necesaria para que el robot colaborativo del laboratorio realice la tarea asignada. 

##### objetivos espec铆ficos


- A trav茅s del urdf y ros realizar la simulaci贸n de trayectoria y velocidad de la tarea asignada
- El robot debe ser capaz de recoger un tubo en posici贸n vertical y dejarlo en otro sitio en posici贸n horizontal.
- Hacer que el robot f铆sico por medio de arduino y python ejecute la labor programada


#### 2. Hardware del robot 

- Servomotor Tower Pro red.MG995

- Servomotor Futaba ref.S3003

- Microservo 9g ref.SG90

- Arduino UNO R3

- Cables Dupond Jumper 40 unidades 20 cm Macho Macho Arduino 

- Cables Dupond Jumper 40 unidades 20 cm Macho Hembra Arduino 

- Protoboard

- Shield pca9685

- Shield v5.0 sensor expansion board

- Modulo Hc-0.6 Bluetooth

- Cargador 5v-2.5A

- Modulo Driver L298

- MPU 6050


#### 3. Software de simulaci贸n y programaci贸n

- Inventor

- ROS 2

- Arduino

- python


#### 4. Descripci贸n de la elaboraci贸n del modelo

Inicialmente se elaboro el modelo de cada una de las piezas del robot en inventor manteniendo las dimenciones de robot fisico, con el fin de poder hacer los ensambles necesarios para simular posteriormente los URDF en ROS.  


![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/WhatsApp%20Image%202021-10-05%20at%2012.21.24%20AM.jpeg)


![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/WhatsApp%20Image%202021-10-05%20at%2012.14.21%20AM.jpeg)


![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/WhatsApp%20Image%202021-10-05%20at%2012.14.51%20AM.jpeg)

#### 5. simulaci贸n URDF ROS 馃悽 

A continuaci贸n se usan los ensambles simulados en formato stl para hacer el URDF del robot y la simulaci贸n de movimientos e identificar las limitaciones de movimiento


![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/WhatsApp%20Image%202021-11-04%20at%205.22.31%20PM.jpeg)

![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/WhatsApp%20Image%202021-11-04%20at%205.22.05%20PM.jpeg)

![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/WhatsApp%20Image%202021-11-04%20at%205.23.50%20PM.jpeg)

![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/WhatsApp%20Image%202021-11-04%20at%205.20.53%20PM.jpeg)

![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/WhatsApp%20Image%202021-11-04%20at%205.21.16%20PM.jpeg)


#### 6. Cinematica directa en python 馃悕

Consiste en determinar cual es la posici贸n y orientaci贸n del extremo final del robot, con respecto a un sistema de coordenadas que se toma como referencia, conocidos los valores de las articulaciones y los par谩metros geom茅tricos de los elementos del robot.

ejecutando el siguiente codigo:

https://github.com/olmerg/rtb_serial_robot/blob/main/jc/codigos/CinematicaDirecta.py

obtuvimos los siguientes resultados

![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20directa/Captura%20de%20pantalla%202021-11-06%20001741.png)


![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20directa/Captura%20de%20pantalla%202021-11-06%20001831.png)


![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20directa/Captura%20de%20pantalla%202021-11-06%20001948.png)


#### 7. Cinematica inversa en python 馃悕

la Cinem谩tica inversa (IK) es la t茅cnica que permite determinar el movimiento de una cadena de articulaciones para lograr que un actuador final se ubique en una posici贸n concreta. El c谩lculo de la cinem谩tica inversa es un problema complejo que consiste en la resoluci贸n de una serie de ecuaciones cuya soluci贸n normalmente no es 煤nica.

ejecutando el siguiente codigo:

https://github.com/olmerg/rtb_serial_robot/blob/main/jc/codigos/CinematicaInversa.py

obtuvimos los siguientes resultados 


![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20inversa/Captura%20de%20pantalla%202021-11-06%20232454.png)

![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20inversa/Captura%20de%20pantalla%202021-11-06%20232528.png)

![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20inversa/Captura%20de%20pantalla%202021-11-06%20232556.png)

![Alt Text](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/cinematica%20inversa/Mi%20video1%20(1).gif)

#### 8. Trayectorias 馃搱

con el siguiente codigo 

https://github.com/olmerg/rtb_serial_robot/blob/main/jc/codigos/Trayectorias.py

Aplicamos las siguientes trayectorias:


![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/trayectorias/Captura%20de%20pantalla%202021-11-06%20233332.png)

![2222](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/trayectorias/Captura%20de%20pantalla%202021-11-06%20233404.png)

#### 9. Visualizaci贸n final  馃弫 

![Alt Text](https://github.com/cristianchernandezs/Parcial_2_robotica/blob/main/imagenes%20github/imagenes/serial/Robot%20(2).gif)

#### 10. Aplicaci贸n serial arduino-

para la aplicacion serial con arduino se usaron los siguientes parametros para marcar cada una de la trayectorias deseadas

https://github.com/olmerg/rtb_serial_robot/blob/main/Arduino_firmware/Arduino_firmware.ino

#### 11. Resultados

Despu茅s de haber realizado m煤ltiples pruebas tanto software como de hardware  con el fin de programar, simular e implementar f铆sicamente , las trayectorias y movivientos deseados 

En los resultados finales podemos observar que el robot f铆sico realiza una serie de  movimientos de forma sincr贸nica  iguales a los propuestos  con la simulaci贸n que nos entrega python

Comprobando que efectivamente representa con exactitud las 贸rdenes y la secuencias que deb铆a seguir para todo el proceso.

##### video final: https://youtu.be/4HT8Srp_R5g

#### 12. Conclusi贸nes

- Gracias a las herramientas adquiridas durante el semestre fue posible comprender de manera 贸ptima la metodolog铆a de cinem谩tica inversa y cinem谩tica directa 

- las herramientas de python y Arduino son un m茅todo pr谩ctico para programar los distintos movimientos que requiere el brazo rob贸tico, ya que adem谩s de ser un software libre de c贸digo abierto fue sencillo comprender como se utilizan sus funciones




## Autores 鉁掞笍


_Las siguientes personas colaboraron con el desarrollo del proyecto_

* **Juan Felipe Ca帽as Bustos** - [JuanCa帽as](https://github.com/jcscorpion)
* **Cristian Hernandez Salazar** - [CristianHernandez](https://github.com/cristianchernandezs)
