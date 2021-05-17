# Readme brazo robotico

Integrantes: 

    - Miguel Angel Murcia Castellanos
    - Jorge Eliecer Rodriguez
    - Luis Carlos Escobar

![](attachment:image.png)

## Construccion del robot

* Se selecciono el material adecuado para la fabricacion del robot en este caso utilizamos mdf con un espesor de 3mm.

![](https://www.blogger.com/u/1/blog/post/edit/preview/7394514771347193319/2504004808712897670)

* Se parte de los planos que teniamos y se producen unos nuevos para construccion en formato DWG r14.

![image-5.png](attachment:image-5.png)

* Se Selecciona los procesos adecuados para darle forma a nuestro robot en este caso utilizamos corte laser partiendo de los archivos en autocad DWG r14.
* Se realiza el ensamble de las piezas utilizando tornilleria m3x30.
* Se instala para la rotacion un servo de referencia mg995
* Se instalan para el movimiento del hombro dos servos con referencia s3003
* Se instala para el movimiento del codo un servo de referencia mg995
* Se instala para el movimiento de la muñeca un servo de referencia mg995
* Se instala para el movimiento de la mano un servo de referencia sg90
* Se instala para el movimiento de los dedos un servo con referencia sg90
* Se procede a hacer la conexion a la placa sensor shield v5.0 a los pines 

Rotacion(2)
Hombro(3)   
Hombro(4)
Codo(8)
Muneca(9)
Mano(11)
Dedos(12)

* Se procede a instalar la placa shield a una placa Arduino uno.
* Se sube el programa a la placa
* Se realizan pruebas de funcionamiento inicialmente con el serial monitor de Arduino
* Se realiza la conexion del modulo bluetooth mediante la conexion 6 y 7 de nuestra placa shield
* Se realizan las pruebas con la aplicacion bluetooth electronics.
* Se realizan pruebas de funcionamiento de todo el mecanismo.
* Se procede a hacer las trayectorias utilizando los conceptos vistos en el curso buscando la calidad y solidez, esto se logra por el numero de pruebas realizadas: cuanto mayor sea el numero de test, mayor garantia  tendria la funcionalidad del robot.

![image-3.png](attachment:image-3.png)

## Pruebas segundo corte

En el segundo corte de Robotica Industrial desarrollamos 3 pruebas:
-------------------------------------------------------------------
1. Prueba fisica: prueba que se desarrollo durante y despues de la 
primera y segunda clase presencial donde diseñamos y construimos un 
brazo robotico, despues se realiza una prueba mediante la tarjeta arduino
y se prueba su funcionalidad
-------------------------------------------------------------------
2. prueba virtual: prueba realizada en el segundo corte mediante ROS 
simulando las trayectorias de un robot virtual, para ello se desarrollo un 
urdf y unas trayectorias mediante el programa ROS o en su defecto Visual
Studio Code, ademas de visualizar y simular el robot, despues de tener estos archivos anteriores
se ejecutaba el comando 
"roslaunch urdf_tutorial display.launch model:=`rospack find lesson_urdf`/urdf/" - para ejecuralo 
y por ultimo ejecutabamos el comando  "rosrun rqt_graph rqt_graph" - para ver su diagrama de nodos
-------------------------------------------------------------------
3. prueba bluetooth: Se realizo una prueba de funcionamiento del robot fisico mediante bluetooth utilizando una aplicacion movil y arduino, en arduino realizamos un codigo el cual nos permitia controlar el movimiento
de los servomotores desde el celular.

![](https://1.bp.blogspot.com/-kGzaiTT7Jf0/YKL-iOZHdaI/AAAAAAAAAME/KurcCEtbTfQUu7JcfzXyNqgCxkw1BzoogCLcBGAsYHQ/s881/este%2Bes%2Bel%2Bque%2Btoca%2Bhacer.png)


## Grados de libertad robot

Nuestro brazo robotico cuenta con 5 grados de libertad

- 1er grado de libertad "Base"
- 2do grado de libertad "Brazo"
- 3er grado de libertad "Codo"
- 4to grado de libertad "Muñeca"
- 5to grado de libertad "Gripper"

Cada articulacion cuenta con un servomotor el cual tiene 180° de rotacion, por lo cual cada articulacion cuenta con una rotacion de -90° hasta 90°, es importante mencionar que los servos no deben ser accionados
en su totalidad de rango de movimiento ya que puede generar problemas de choques entre las articulaciones

## El planeamiento de trayectorias 

Las trayectorias del brazo robotico que realizamos las hicimos en jupyter notebook.

1. Realizamos una trayectoria para la letra L utilizando SE3, ingresamos las trayectorias x,y,z requeridas para la trayectoria

![image.png](attachment:image.png) 

2. Utilizamos el metodo Ctraj y Jtraj para hallar la trayectoria de la articulacion
3. Visualizamos la trayectoria cartesiana

![image.png](attachment:image.png)

4. Ya teniendo las trayectorias calculamos la cinematica inversa con el metodo ikine_min

![image.png](attachment:image.png)

## Aplicación brazo robótico

![](https://i.ytimg.com/vi/wAy9u0frJ9c/maxresdefault.jpg)

Hay numerosas aplicaciones de los brazos robóticos uno de ellos es el paletizado automático de botellas pet. Ofrecen numerosas aplicaciones para el packaging en la industria el robot diseñado por nuestro grupo es un robot que se puede aplicar en este tipo de industria.

Aunque es un prototipo puede desempeñarse bien en este tipo de industria, pero con otro tipo de motores y montados sobre un bastidor rígido ya que estos no poseen el torque suficiente para mover este tipo de objetos ni los materiales adecuados para su aplicación.

como esta compuesto:

Está compuesto por un brazo mecánico que se encarga de depositar el material que sale de una cadena de suministros, mientras que un robot despaletizador es el encargado desmontar el material de un palet para introducirlo en una línea de montaje. Los brazos robóticos automatizan el proceso de apilar las piezas que históricamente se ha realizado a mano por una persona. Este proceso de automatización es llevado a cabo por uno o dos robots, dependiendo de la velocidad exigida por el ciclo del proceso.
Existen otros sistemas orientados al paletizado de mercancías. Hablamos de los robots cartesianos paletizadores destinados a desarrollar el mismo trabajo. Destacan por su velocidad, pero tienen la desventaja de que necesitan una mayor inversión, ofrecen menor movilidad que los brazos robóticos y abarcan un mayor espacio de trabajo complicando su incorporación en una fábrica.
El objetivo de los robots paletizadores de cajas es recogerlas y colocarlas de manera autónoma en una plataforma. Son muchos los materiales y sectores en donde pueden ser incorporados, ya sean en el sector de la alimentación, de las bebidas, electrónico o en el ecommerce. Debemos dejar claro que no existen limitaciones a la hora de poder automatizar el paletizado de cualquier material.

En el momento de integrar un robot para paletizado hay que identificar cuáles son las necesidades del trabajo. Los aspectos más destacables son la capacidad de carga necesaria y la longitud que requiere el robot industrial para poder realizar la tarea. Del mismo modo hay que valorar el material que debemos coger, la velocidad, el tiempo de ciclo o el sistema de visión artificial que requiere. 
Los robots paletizadores disponen de sistemas de control muy sencillos de usar para tareas de escasa complejidad. En caso de necesitarlo tienes la posibilidad de realizar simulaciones de movimientos de paletizado antes de transmitirle la configuración al robot. El software de simulación a su vez te permite programar mientras el robot sigue trabajando, por lo que eludes tener que interrumpir el ciclo de trabajo.
El fabricante Fanuc ha creado el software Pallet Pro con el que realizamos simulaciones con zonas en las que simular virtualmente la línea de producción, las estaciones de alimentación y hojas deslizantes. Esta recreación en 3D la puedes compartir con PalletTool. Los equipos incorporados en los finales de línea que disponen zonas 3D pueden detectar los materiales que se ubican fuera de la posición de referencia favoreciendo la calidad del producto.
Un sistema de paletizado automático de bloques de hormigón o de botellas pet es muy sencillo, y básicamente replica la forma con el que se hace manualmente. El material llega hasta el robot por medio de una cinta transportadora. El brazo robótico levanta el material gracias a unas servo pinzas y lo coloca en palet. Una vez completada la fila, si es necesario, coloca un separador de cartón e inicia el proceso hasta que termine las alturas que sean necesarias. El palet es retirado y una vez se coloca uno nuevo, el robot comienza el proceso desde el inicio. Debemos recordar que los palets pueden llegar a la célula de paletizado por medio de una alimentación automática.


```python

```
