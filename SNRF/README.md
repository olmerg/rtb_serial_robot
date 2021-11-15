# ENTREGA PROYECTO FINAL :trophy:

### Universidad Jorge Tadeo Lozano 
### Robotica Industrial 2021-2s
### Docente : Olmer Garcia - [@olmerg](https://github.com/olmerg)  
## Integrantes :writing_hand:
> - Sergio N. Rodríguez F.
> - Andres F. Patiño 
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

***NO OLVIDAR AGREGAR LA IMAGEN***
## Robot en ROS :computer:
Para hacer la comunicacion del robot con ROS, se plantea usar el archivo URDF (Unified Robot Description Format), pues este a traves de sus frames, joint, y links permite darle manipulación y comunicación al robot. 
