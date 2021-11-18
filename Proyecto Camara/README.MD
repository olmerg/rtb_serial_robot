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

1. Hardware y Software utilizado
2. Elaboración del modelo 3D
3. Simulación URDF en ROS
4. Corte láser del robot
5. Control de peso de los Links físicos
6. Cinematica directa en python
7. Cinematica inversa en python
8. Aplicación serial arduino
9. Trayectorias
10. Video promocional
11. Opciones de mejora
12. Conclusiones

#### 1. Hardware y Software utilizado -

## --> HARDWARE
    Arduino Uno (x1)
    Sensor Shield 5v (x1)
    Modulo bluetooth para arduino (x1)
    Convertidor 120v a 5v (x1)
    Servomotor MG995 (x4)
    Servomotor SG90 (x2)
    Cámara Web (x1)
## --> SOFTWARE
    Visual Studio Code
    Arduino IDE
    Autodesk Inventor
    Bluetooth Electronics
    ROS

#### 2. Elaboración del modelo 3D

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

Ya con todas con todas las piezas diseñadas, realizamos el ensamblaje del robot  y se modeló. Se realizaron uniones rotacionales para el conjunto de piezas que lo necesitaran.
![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/CapturaEnsambeCompleto.PNG)

Ensamble completo del robot

#### 3. Simulación URDF en ROS 

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

## --> https://github.com/olmerg/rtb_serial_robot/blob/a94f923dfe8814012ff47716d1299d0069b88605/Proyecto%20Camara/xacro/urdf/planar_3dof.urdf

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

#### 4.Corte láser del robot

Para el corte láser creamos estos 3 archivos PDF tamaño A4, los obtuvimos a partir de los archivos DWG
que creamos en Autodesk Inventor. 

![Click Aquí para ver PDF 1](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Plano%20de%20CORTE%201.pdf)

![Click Aquí para ver PDF 2](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Plano%20de%20CORTE%202.pdf)

![Click Aquí para ver PDF 3](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Plano%20de%20CORTE%203.pdf)

#### 5. Control de peso de los Links físicos

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

#### 6. Cinematica directa en python 🐍-

Consiste en determinar cual es la posición y orientación del extremo final del robot, con respecto a un sistema de 
coordenadas que se toma como referencia, conocidos los valores de las articulaciones y los parámetros geométricos de los elementos del robot

Este es el código que usamos
## --> https://github.com/olmerg/rtb_serial_robot/blob/a94f923dfe8814012ff47716d1299d0069b88605/Proyecto%20Camara/CinematicaDirecta

Esto es lo que se imprime en la consola

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/CapturaTerminalCinematicaDirecta.PNG)

Estos son los plot que generamos, el plot de la parte derecha viene con las barras deslizadoras que permiten 
cambiar el ángulo de cada una de las uniones.

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/CapturaPlotCinematicaDirecta.PNG)

#### 7. Cinematica inversa en python 🐍--

En Robótica, la Cinemática inversa (IK) es la técnica que permite determinar el movimiento de una cadena de 
articulaciones para lograr que un actuador final se ubique en una posición concreta. 
El cálculo de la cinemática inversa es un problema complejo que consiste en la resolución de una 
serie de ecuaciones cuya solución normalmente no es única.

Este es el código que usamos
## --> https://github.com/olmerg/rtb_serial_robot/blob/a94f923dfe8814012ff47716d1299d0069b88605/Proyecto%20Camara/CinemticaInversa

Esto es lo que se imprime en la consola

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/CapturaTerminalCinematicaInversa.PNG)

Estos es el plot que generamos

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/CapturaPlotCinematicaInversa.PNG)

Cabe aclarar que este código está relacionado unicamente a los primeros tres grados de libertad del robot, para hacer la cinemática inversa completa podemos acudir a algún método mumérico como lo son ikine o ikineLM, o también podemos acudir al uso del desacoplo cinemático del mismo.

#### 8. Aplicación serial arduino

Este es el código que usamos en el Arduino

En el Setup declaramos los pines para cada motor, declaramos el delay y la función de escritura.

```
void setup(){
  Serial.begin(115200);
  mySerial.begin(9600);
  delay(3000);
  //pines en el arduino para cada señal del servomotor
  Cadera.attach(2);
  HombroD.attach(3);
  //HombroI.attach(8);
  Codo.attach(9);
  Muneca.attach(11);
  Camara.attach(12);
  home();
  Cadera.write(anguloCadera);  
  HombroD.write(anguloHombroD);
  //HombroI.write(anguloHombroI);
  Codo.write(anguloCodo);
  Muneca.write(anguloMuneca);
  Camara.write(anguloCamara);
}
```

Creamos una clase, llamada home, que cuando se llama, hace que el robot vaya a su posición inicial,
que en nuestro caso es que haga su extensión vertical máxima.

```
void home(){
  // las posiciones iniciales de los servos para home
      anguloCadera=90;
      anguloHombroD=81;
      //anguloHombroI=84;
      anguloCodo=110;
      anguloMuneca=100;
      anguloCamara=81;
  }
```

En el loop declaramos algunas variables tipo char, para que aumente o disminuya el ángulo del motor que queramos,
también hicimos las restricciones de los motores y dimos un pequeño delay, todo esto desde el monitor serial de arduino.

```
while(Serial.available()){//solo leeremos si hay un byte en el buffer
    comando=Serial.read();//leemos el byte
    if(comando=='A')anguloCadera+=1;//incrementamos 1
    else if(comando=='a')anguloCadera-=1;//decrementamos 1
    else if(comando=='B')anguloHombroD+=1;
    else if(comando=='b')anguloHombroD-=1;
    //else if(comando=='C')anguloHombroI+=1;
    //else if(comando=='c')anguloHombroI-=1;
    else if(comando=='D')anguloCodo+=1;
    else if(comando=='d')anguloCodo-=1;
    else if(comando=='E')anguloMuneca+=1;
    else if(comando=='e')anguloMuneca-=1;
    else if(comando=='G')anguloCamara=0;
    else if(comando=='g')anguloCamara=80;
    else if(comando=='h')home();
    anguloCadera=constrain(anguloCadera,0,180);//restringimos el valor de 0 a 180
    anguloHombroD=constrain(anguloHombroD,0,180);//restringimos el valor de 0 a 180
    //anguloHombroI=constrain(anguloHombroI,0,180);//restringimos el valor de 0 a 180
    anguloCodo=constrain(anguloCodo,0,180);//restringimos el valor de 0 a 180
    anguloMuneca=constrain(anguloMuneca,0,180);
    anguloCamara=constrain(anguloCamara,0,180);
    delayMicroseconds(10);
  }
  }
```

También en el loop declaramos algunas variables tipo char, que cumplen con la misma función anterior, pero estas se utilizan para controlar el robot desde un dispositivo externo conectado mediante bluetooth.

## --> https://github.com/olmerg/rtb_serial_robot/blob/a94f923dfe8814012ff47716d1299d0069b88605/Proyecto%20Camara/brazo5DOF.ino

Finalemente mediante la aplicacion Bluetooth Electronics de keuwlsoft, disponible en el App Store de Android, desarrollamos una sencilla aplicacion que nos permite controlar el robot desde el telefono mediante diversos botones.

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/WhatsApp%20Image%202021-11-15%20at%2011.52.53.jpeg)

Asi podemos controlar nuestro robot de cualquiera de las dos maneras, sea mediante el monitor serial o el bluetooth. Podemos ver su funcionamiento aqui:
## --> https://youtu.be/pAqLarWzQy8


#### 9. Trayectorias 📈-

Mediante el codigo en python planeamos diversas trayectorias que graban diferentes movimientos mediante la cámara ubicada en el gripper, puede ser una escena de acción como en las peliculas o tomas desde diversos angulos.

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/trayectoriasPython.PNG)

Mediante el comando Swift de python obtenemos una visualización del robot de manera virtual, basandonos en el URDF del mismo, aqui vemos las trayectorias que sigue el robot físico.

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Swift.png)

## --> https://youtu.be/YHawVIMIhZU

Podemos ver como el robot físico sigue la misma trayectoria que el robot virtual, ya que enviamos las trayectorias de python hasta el arduino mediante el codigo que cargamos anteriomente de comunicacion serial.

## --> https://youtu.be/jNTdWokAjWE

#### 10. Video Promocional 📷-

Con el fin de convertir este proyecto en algo más allá de la investigación, hemos desarrollado un concepto de marca alrededor de él y todo lo contenido en este documento, por eso desarrollamos un video pitch que contiene toda la información relevante del proyecto y que lo hace atractivo al público.

![2222](https://github.com/JuanSebastianReina/ImagenesProyectoRob/blob/main/Dise%C3%B1o%20sin%20t%C3%ADtulo.png)
## --> https://youtu.be/KYo8mj_5Os8

#### 11. Opciones de mejora-


#### 12. Conclusiones-


## Autores 🤵👩‍🎓🤵

_Las siguientes personas colaboraron con el desarrollo del proyecto_

* **Juan Sebastian Reina** - [JuanSebastianReina](https://github.com/JuanSebastianReina)// juanS.reinaa@utadeo.edu.co
* **Valentina Vega Mahecha** - [vale2012](https://github.com/vale2012)// valentina.vegam@utadeo.edu.co
* **Cristian Paez** - []()// cristian.paez@utadeo.edu.co
