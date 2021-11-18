# ENTREGA PROYECTO FINAL :trophy:

### Universidad Jorge Tadeo Lozano 
### Robotica Industrial 2021-2s
### Docente : Olmer Garcia - [@olmerg](https://github.com/olmerg)  
## Integrantes :writing_hand:
> - Sergio N. Rodríguez F.
> - Andres F. Patiño M.
## Identificación del problema :mag_right:
Dado la alta demanda que se esta presentando en el campo del reciclaje, pero la falta de eficacia al momento de separar algunos metales de otros materiales se crea un problema ya que todos estos materiales tienen procesos diferentes al momento de reciclarlos. Cuando los materiales se mezclan en estos procesos puede que dañen algunas maquinas implicadas o lastimen a alguien, es primordial separar has te mas pequeño pedazo, hacerlo de manera manual puede resultar peligroso y el esquipo especializado puede ser muy costoso.
## Solución planteada :bulb:
Con este proyecto se plantea poder separar los metales de las grandes cantidades de reciclaje que lleguen a un punto de separaciín, separar los materiales de manera manual es muy dificil y a veces peligroso, en las grandes empresas se implementan imanes que logran separar la gran mayoria de metales, nosotros queremos presentar una solucion más economica, un brazo robotico equipado con un electroiman, este brazo no solo separa os metales sino que tambien facilitara su transporte a otro contenedor o banda transportadora para que se le haga su respectivo proceso. 
## Diseño del Robot :robot:
Para este proyecto, se planteo reutilizar el [Robot Utadeo](https://github.com/olmerg/rtb_serial_robot/tree/main/RobotUtadeo/urdf) desarrollado el semeste pasado por otros compañeros, pero acomodandolo para darle solución a nuestro problema planteado, es decir, que haremos una modificación en su gripper para que de esta manera podamos incluir un electroimán, y este será encargado de realizar el proceso descrito anteriormente. 

*Imagen de referencia del electroiman* 
![This is an image](https://www.hwlibre.com/wp-content/uploads/2020/01/electroiman.jpg) 

Adicional a esto, deseamos anclarlo a una tabla de madera que le genere un contra peso, pues al momento de generar algunas trayectorias o levantar algunos elementos, el robot tendia a ladearse o irse de frente. Incluso en el momento que se comenzaron a hacer las pruebas, esto sucedio y genero que el robot se cayera y se quebraran algunas piezas, lo que nos llevo a tener que generar nuevos cortes en laser y reemplazar dichas piezas.

*Imagen de referencia de la nueva version del robot* 
![This is an image](https://github.com/olmerg/rtb_serial_robot/blob/f7fb55173bb7c4d279c81e9bced54d27c8a48d06/RobotUTadeo_V2/Imagenes/IMG_20211117_225023.jpg)
![This is an image](https://github.com/olmerg/rtb_serial_robot/blob/b04b90a4ea845541ae16c695681eb9d0f284da3a/RobotUTadeo_V2/Imagenes/IMG_20211117_225037.jpg)
![This is an image](https://github.com/olmerg/rtb_serial_robot/blob/b04b90a4ea845541ae16c695681eb9d0f284da3a/RobotUTadeo_V2/Imagenes/IMG_20211117_225047.jpg)
![This is an image](https://github.com/olmerg/rtb_serial_robot/blob/b04b90a4ea845541ae16c695681eb9d0f284da3a/RobotUTadeo_V2/Imagenes/IMG_20211117_225104.jpg)
## Hadware y Software empleados :video_game: :desktop_computer:
***Hadware***
> - Arduino uno (x1)
> - Arduino sensor shield 5.0 (x1)
> - Modulo bluetooth para arduino (x1)
> - Convertidor 120v a 5v (x1)
> - Servo motor MG995 (x4)
> - Servo motor SG90 (x2)

***Software***
> - Visual Studio Code
> - Arduino
> - Inventor
> - Bluetooth electronics
## Robot en ROS :computer:
Para hacer la comunicacion del robot con ROS, se plantea usar el archivo [URDF](https://github.com/olmerg/rtb_serial_robot/tree/main/SNRF/URDF)  (Unified Robot Description Format), pues este a traves de sus frames, joint, y links permite poder simular y visualizar el robot y cu comportamiento.

## Comando por Bluetooth :iphone:
Para hacer los comando desde Bluetooth, nos ayudamos de una aplicación llamada Bluetooth electronics, con ella podremos crear el diseño que nosotros dispongamos, incluyendo los datos que van a enviar desde ella hacía el arduino, y de esta forma poder controlar nuestro brazo. 
Teniendo en cuenta el codigo realizado en arduino y las letras que se van a emplear para enviar los comandos, procedemos a diseñar la interfaz la cual visualizamos de la siguiente manera:

*Interfaz en Bluetooth Electronics* 
![This is an image](https://github.com/olmerg/rtb_serial_robot/blob/4afb454277e984d69e93cb750831d621d27ca72c/RobotUTadeo_V2/Imagenes/InterfazBluetooth.jpg)

Con estas flechas y botones, podremos manipular el brazo e inlcuso si queremos que este regrese a su posición inicial, podemos presionar el boton azul que dice "HOME" y el debería volver a dicha posición. El codigo utilizado para este proyecto se podrá encontrar [AQUÍ](https://github.com/olmerg/rtb_serial_robot/blob/d37b6842aa998b607cc1221b3aeb89b6a9b29748/RobotUTadeo_V2/CodigoArduino/CodigoArduino.ino)  
## Modelado y visualización :eyes:
Luego de haber modelado y ensamblado todas las piezas, podremos ver nuestro brazo con diferentes grados de libertad :
![This is an image](https://github.com/olmerg/rtb_serial_robot/blob/d3cee1eb60260a47448045f965aace5d251b18c5/RobotUTadeo_V2/Imagenes/IMG-20211114-WA0035.jpg) 
![This is an image](https://github.com/olmerg/rtb_serial_robot/blob/d3cee1eb60260a47448045f965aace5d251b18c5/RobotUTadeo_V2/Imagenes/IMG-20211114-WA0036.jpg)
![This is an image](https://github.com/olmerg/rtb_serial_robot/blob/d3cee1eb60260a47448045f965aace5d251b18c5/RobotUTadeo_V2/Imagenes/IMG-20211114-WA0037.jpg)
![This is an image](https://github.com/olmerg/rtb_serial_robot/blob/d3cee1eb60260a47448045f965aace5d251b18c5/RobotUTadeo_V2/Imagenes/IMG-20211114-WA0038.jpg)
![This is an image](https://github.com/olmerg/rtb_serial_robot/blob/d3cee1eb60260a47448045f965aace5d251b18c5/RobotUTadeo_V2/Imagenes/IMG-20211114-WA0039.jpg)
## Planteamiento de las trayectorias :chart_with_upwards_trend:
Para estas trayectorias vamos a implementar los pasos usados en el parcial de segundo corte, de tal forma que trabajariamos con el siguiente codigo: 

![This is an image](https://github.com/olmerg/rtb_serial_robot/blob/4888e2ee4398ec5dc13c4ea8633e09993e3fe042/RobotUTadeo_V2/Imagenes/Cod1.png)
![This is an image](https://github.com/olmerg/rtb_serial_robot/blob/4888e2ee4398ec5dc13c4ea8633e09993e3fe042/RobotUTadeo_V2/Imagenes/Cod2.png)
![This is an image](https://github.com/olmerg/rtb_serial_robot/blob/4888e2ee4398ec5dc13c4ea8633e09993e3fe042/RobotUTadeo_V2/Imagenes/Cod3.png)
![This is an image](https://github.com/olmerg/rtb_serial_robot/blob/4888e2ee4398ec5dc13c4ea8633e09993e3fe042/RobotUTadeo_V2/Imagenes/Cod4.png)
![This is an image](https://github.com/olmerg/rtb_serial_robot/blob/4888e2ee4398ec5dc13c4ea8633e09993e3fe042/RobotUTadeo_V2/Imagenes/Cod5.png)
![This is an image](https://github.com/olmerg/rtb_serial_robot/blob/4888e2ee4398ec5dc13c4ea8633e09993e3fe042/RobotUTadeo_V2/Imagenes/Cod6.png)
![This is an image](https://github.com/olmerg/rtb_serial_robot/blob/4888e2ee4398ec5dc13c4ea8633e09993e3fe042/RobotUTadeo_V2/Imagenes/Cod7.png)
![This is an image](https://github.com/olmerg/rtb_serial_robot/blob/4888e2ee4398ec5dc13c4ea8633e09993e3fe042/RobotUTadeo_V2/Imagenes/Cod8.png)
![This is an image](https://github.com/olmerg/rtb_serial_robot/blob/4888e2ee4398ec5dc13c4ea8633e09993e3fe042/RobotUTadeo_V2/Imagenes/Cod9.png)

## Conclusiones :white_check_mark:
Pudimos evidenciar que la implementación del electroiman, es una buena solución para el problema planteado, más sin embargo se podría mejorar la optimización de este proceso al implementar un transistor que le suba la corriente al electroiman, de esta forma obtendría más corriente para generar un campo magnetico mayor y atraer los elementos con más definición.

Al ponerle una base, evita que el brazo se incline o se vaya hacia adelante al momento de estar haciendo las trayectorias o algun movimiento, pues como se menciono en el cuerpo de este trabajo, era un problema que poseia este robot por el peso que tiene del codo hacia el electroiman. 

Se pudieron aplicar los conocimientos adquiridos a lo largo del semestre en la asigntura de Robotica industrial, haciendo la implementacion de diferentes librerias y del hadware y software arduino para poder manipular controladamente este brazo. 