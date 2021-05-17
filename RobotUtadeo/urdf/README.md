# Proyecto Robot Utadeo 
**Integrantes**:

	- Jonathan Alexander Sechagua Guarnizo
	
	- Diego Carreño Bustacara
	
	- Jorge Lemos
	
	- Alberto Roa
	
Curso de Robotica Industrial 2021-I de Ingeniería en automatización de Universidad Jorge Tadeo Lozano

**Profesor**: Olmer Garcia Bedoya (@olmerg)



[========]
##Diseño y construcción del robot
El proceso de diseño y construcción del robot se desarrolló en varias etapas.
1. En primera instancia se tomaron medidas de las piezas de los robots que se encuentran en la universidad esto con el fin de tener una base para desarrollar nuestros propios planos, pues los motores son los mismos, estos planos fueron desarrollados en **Inventor** a continuación se presenta una imagen de los planos del robot.
![](https://1.bp.blogspot.com/-s6t6qwnHBo4/YKAqUocKcuI/AAAAAAAAALs/UqH3s3Znt9MiKztJL-CNOzT8xV4nnQvigCNcBGAsYHQ/s16000/PLANOS.PNG)
*Nota: Los planos en pdf y dwg se encuentran en la carpeta llamada Inventor y dentro hay otra que se llama planos, ahí se encuentran estos archivos por si se desea modificarlos, revisarlos o replicarlo.*

1. El proceso de construcción de las piezas en 3D se realizó con los planos anteriormente mencionados, en primera instancia se realizó la construcción de cada una de las piezas por separado, las piezas fueron las bases, los eslabones y el gripper, adicional a ello también se diseñaron los tornillos y servomotores, pero pues estos solo con el fin de la visualización del robot en el CAD y URDF, a continuación se presenta una tabla de imágenes de las piezas pero estas también se encuentran en la carpeta inventor y dentro de esta carpeta hay otra que se llama piezas allí se encuentran cada una de las piezas en extensión .ipt que es la extensión de piezas de inventor, por si se desea implementar o hacer alguna modificación a estas.

![](https://1.bp.blogspot.com/-qTpQKYGFvsg/YKA_NUPomQI/AAAAAAAAAMU/-52LvwP-Vg0uzaEz9mMlKXZ9F92EuxhNgCNcBGAsYHQ/s16000/Piezas_Robot.PNG)

1. Posterior a la realización de las piezas individuales se realizó la unión de estas en ensambles,  para importar las piezas al URDF y unirlas allí era mucho más complejo que hacerlo en el inventor, estos ensambles se realizaron teniendo en cuenta en que puntos se encontraban las articulaciones o grados de libertad esto con el fin que a la hora de importarlos a URDF se pudiera hacer la animación de estos mismos, estos ensambles se encuentran también dentro de la carpeta inventor y allí se encuentra otra carpeta que se denomina ensambles allí se encuentran los ensambles en extensión .iam por si se desea hacer alguna modificación o los ensambles en .stl que es la extensión que nos permite importar en el URDf. A continuación, como en la parte anterior se presenta una tabla con los respectivos ensambles.
![](https://1.bp.blogspot.com/-NuY3oVMiDaA/YKBBJLse3aI/AAAAAAAAAMk/cwimXunCVlULmXdeJieFtQCjV7C6VtKfwCNcBGAsYHQ/s16000/Ensambles.PNG)
Como se mencionó anteriormente estos ensambles fueron con los que se realizó el URDF, por último, se presenta una imagen del robot ensamblado en inventor, este ensamble se realizó con los ensambles valga la redundancia anteriormente mencionados y presentados.

![](https://1.bp.blogspot.com/-I_E_1XU1BW4/YKBB4KGDf9I/AAAAAAAAAMs/Zb7Mij70cP41zUXxP_432zXiZ3V8ey0xQCNcBGAsYHQ/w640-h438/Solido.PNG)

1. Posteriormente realizar corte láser, el material escogido fue acrílico, pues es un material resistente y no muy pesado.

![](https://1.bp.blogspot.com/-iXkMXQ_NM5I/YKAsrZDNEzI/AAAAAAAAAL0/N8tbkSOLtugoHY9OoZVSIzNRhisuxqUfgCNcBGAsYHQ/w640-h430/corte_laser.PNG)

1. Construcción del robot

![](https://1.bp.blogspot.com/-yEGr8z6nn7w/YKAwFQkqPyI/AAAAAAAAAL8/efsItCRcM_IvtjUwD-B1FI61CesIgJfzACNcBGAsYHQ/s16000/Construccion.PNG)
*Nota: Los tornillos que se usaron para la base tienen 7.5 cm de largo y 0.5 cm de ancho.*

## Robot virtual en ROS
Para tener un robot es ROS es necesario describrir sus frames, joint y links, lo cual es realizado a traves de un archivo xml llamado Unified Robot Description Format (URDF).
1. Realizar el archivo urdf del robot(puede ser con piezas stl ,a través de cylinder o por archivos .dae (recomendado porque incluye texturas)) [RobotUtadeo(Urdf)](https://robotutadeo.blogspot.com/2021/05/urdf-del-robot-utadeo.html "RobotUtadeo(Urdf)")
en los siguientes links [XML Robot Description Format (URDF)](http://wiki.ros.org/urdf/XML/model "XML Robot Description Format (URDF)") , [Examples](http://wiki.ros.org/action/fullsearch/urdf/Tutorials/Building%20a%20Visual%20Robot%20Model%20with%20URDF%20from%20Scratch?action=fullsearch&context=180&value=linkto%3A%22urdf%2FTutorials%2FBuilding+a+Visual+Robot+Model+with+URDF+from+Scratch%22 "Examples") encontrarás información necesaria para realizar el urdf.
*Nota: Al final de este capitulo encontrarás un video donde hablaremos con más detalle sobre el diseño de los planos y el urdf del Robot Utadeo.*
1. Generar el grafico de la cadena cinematica
abrir una consola desde la carpeta donde está el urdf y ejecutar
*urdf_to_graphiz planar_3dof.urdf*
![](https://1.bp.blogspot.com/-R_Jk9p67xYE/YKA6s1O391I/AAAAAAAAAME/XUs8RDI09BgNM05FtJccfPHH7Xkl7ePZwCNcBGAsYHQ/w141-h640/Cadena_cinem%25C3%25A1tica.PNG)
1. Ver el diagrama de nodos con sus topicos por medio de:
*rosrun rqt_graph rqt_graph*
![](https://1.bp.blogspot.com/-igMa8Ow_kc4/YKA7pAu4YGI/AAAAAAAAAMM/BctowQvvwfQhJxUSkLdnTecpRltRRM4CQCNcBGAsYHQ/w640-h230/Diagrama_Nodos.PNG)
En el siguente video se explica con más detalle el diseño de los planos y el urdf del robot [Planos&URDF](https://robotutadeo.blogspot.com/2021/05/diseno-planos-y-urdf-del-robot-utadeo.html "Planos&URDF")

[========]
## Planeamiento de trayectoria
1. Importar el robot de la clase RobotUtadeo
	![](https://lh3.googleusercontent.com/-AUCIVXdZjXY/YKAIdB9mD2I/AAAAAAAAAJk/s1eg40ZbowgZUA03E0ZUsVBFJ2McX4qGQCNcBGAsYHQ/w320-h43/Importar.PNG)
	en dicha clase se encuentra la ruta de la carpeta URDF del robot, además se establecen  diferentes valores articulares.
	![](https://1.bp.blogspot.com/-xVFdcngGShM/YKAN97gXG1I/AAAAAAAAAKE/etbAjLI5DXAse9gYETxqTmYqD_28kjmwwCNcBGAsYHQ/w400-h155/Clase.PNG)
1. Caracteristicas del Robot Utadeo
	![](https://lh3.googleusercontent.com/-OlIB1XKusNg/YKAPuBUzuDI/AAAAAAAAAKM/e9KGSqLYFn8-7dRK73pTjK_13xg9JzSNgCNcBGAsYHQ/w353-h400/Robot.PNG)
	El Robot Utadeo tiene 5GDL cada grado de libertad tiene un rango de (-90° , 90°).
	- Los tres primeros GDL (cadera, hombro, codo) tienen servomotores** Tower Pro MG995** que tienen las siguientes especificaciones:
	• Peso: 55 g
	• Dimensión: 40.7 x 19.7 x 42.9 mm aprox.
	• 8.5 kgf·cm (4.8 V ), 10 kgf·cm (6 V)
	• Velocidad de trabajo: 0.2 s/60º (4.8 V), 0.16 s/60º (6 V)
	• Voltaje de operación: 4.8 V a 7.2 V
	• Ancho de banda: 5 µs
	• Rango de temperatura: 0 ºC – 55 ºC
	- El cuarto GDL (Muñeca) tiene un servomotor** Futaba S3003** que tiene las siguientes 		especificaciones:
	• Voltaje de operación 4.8-6 Volts.
	• Peso 38 gr.
	• Velocidad de trabajo
	• 0.23 seg/60 grados (4.8Volts)
	• 0.19 seg/60 grados (6 Volts)
	• Torque
	• 3.2 kg/cm (4.8 volts)
	• 4.1 kg/cm (6 Volts)
	• Frecuencia de funcionamiento 50Hz
	- El quinto GDL (Mano) tiene un **Micro Servo SG90** que tiene las siguientes 		especificaciones:
	• Peso: 9 g
	• Dimensión: 22.2 x 11.8 x 31 mm aprox.
	• 1.8 kgf·cm
	• Velocidad de trabajo: 0.1 s/60 degree
	• Voltaje de operación: 4.8 V (~5V)
	• Ancho de banda: 10 μs
	• Rango de temperatura: 0 ºC – 55 ºC
	### Espacio de trabajo 
	#### 	Vista Lateral
	![](https://1.bp.blogspot.com/-s9vUGvSHtL8/YKAUIp6PqtI/AAAAAAAAAKc/C0v6MVAp_fEEGGy0zdEVXM7PN7Vv6x9fwCNcBGAsYHQ/w320-h307/VistaLateral.PNG)
	#### 	Vista Superior
	![](https://1.bp.blogspot.com/-MoX6yk7piMQ/YKAVEfPUEXI/AAAAAAAAAKs/BtMtVV-AHaUrJn9oH7jriWbEeDZgcRSvQCNcBGAsYHQ/w320-h308/VistaSuperior.PNG)

1. Trayectoria deseada del gripper para que el realice la letra **M**
	**Letra M**: Utilizamos SE3, e ingresamos las coordenas (x,y,z) en mm, asi con cada **P#** hasta realizar la letra **M**.
	Donde **P **es un punto en el plano cartesiano, es un punto donde quiero que mi efector final llegue.
	> Nota: Las coordenas (x,y,z) deben estar dentro del espacio de trabajo.

	 Estas son las coordenadas cartesianas para realizar la letra **M**
	![](https://1.bp.blogspot.com/-DbJDHcreLWk/YKAW49yAcEI/AAAAAAAAAK0/QhiZeusDL18N26iW2gisESOYbtRDQTlFgCNcBGAsYHQ/s16000/TrayectoriaCartesiana.PNG)
1. Se usa ctraj(T0, T1, n), ctraj es una trayectoria cartesiana desde la pose SE3 T0 hasta T1 con n puntos que siguen un perfil de velocidad trapezoidal a lo largo de la trayectoria. La trayectoria cartesiana es una instancia SE3 que contiene n valores.
	También usamos jtraj(q0, qf, N), jtraj es una trayectoria del espacio de la articulación 		donde las coordenadas de la articulación varían de q0(M) a qf(M), en N pasos.
	![](https://1.bp.blogspot.com/-pHkB92tovu4/YKAZjGOW3nI/AAAAAAAAAK8/7uFOoNS_2Eca3jQKTznJU9Q91qXAq_mWQCNcBGAsYHQ/s16000/ctraj.PNG)

1. Visualizar las trayectorias Cartesianas
![](https://1.bp.blogspot.com/-kA1DcBoW0os/YKAaVWUYmAI/AAAAAAAAALE/43W_D6vPiiAb6sgnXhVjOBwNv_zNGIlzACNcBGAsYHQ/s16000/plot.PNG)

1. Animación del robot haciendo las trayectorias
	Debemos pasar nuestras coordenadas de mm a cm, y usar nuevamente el método ctraj, para calcular las trayectorias cartesianas.
	![](https://1.bp.blogspot.com/-kT7gXuNJ2nA/YKAboE6V5OI/AAAAAAAAALM/gicEahPJ4Kw5Bcf2BZZOu5T1u-acPiyfwCNcBGAsYHQ/s16000/Ctraj2.PNG)

1. Ya teniendo las trayectorias cartesianas, calculamos la cinemática inversa, esto con el fin de obtener los valores que debe tomar cada articulación.
	![](https://1.bp.blogspot.com/-Y3-hrUeaGqU/YKAc83CaNeI/AAAAAAAAALU/xYHa4tFxosgjR8saN1SAoHOpr7bHfgvoQCNcBGAsYHQ/s16000/ikine.PNG)

1. Con los valores articulares obtenidos anteriormente, usamos el método jtraj, el cual calcula un polinomio de grado 5 para cada articulación que lleva de P_inicial a P_final, en un intervalo n.
	![](https://1.bp.blogspot.com/-3BDPa43vu7A/YKAd8_o9RcI/AAAAAAAAALc/eMlUS8BAlg8q_DJx801grB5s5oLw0EoGwCNcBGAsYHQ/s16000/jtraj.PNG)

1. Animación del robot
	![](https://1.bp.blogspot.com/-knuzAw2E_N8/YKAe9mxp6cI/AAAAAAAAALk/pwwMR4e1K-Q8RlLBVloflZu2kf0aLriUACNcBGAsYHQ/s16000/Animacion.PNG)

En el siguiente video [Trayectorias](https://robotutadeo.blogspot.com/2021/05/planeamiento-de-trayectorias.html "Trayectorias") se explica con más detalle el planeamiento de trayectorias del Robot Utadeo

[========]
## Pruebas con el Bluetooth
1. Cargar el archivo Arduino_firmware.ino en el arduino uno
1. Identificar el puerto serial con el que se identifica el arduino al conectarlo al pc
1. Descargar la app [Bluetooth_Electronics](https://play.google.com/store/apps/details?id=com.keuwl.arduinobluetooth&hl=es_CO&gl=US "Bluetooth_Electronics")
En el siguente video se explica con más detalle las [Pruebas_Bluetooth](https://robotutadeo.blogspot.com/2021/05/bluetooth.html "Pruebas_Bluetooth")
	> Nota: Antes de cargar el código al Arduino se recomienda desconectar el Bluetooth, en ocasiones genera errores.

[========]
## Aplicación de este robot
El objetivo con este robot es simular la automatización de un proceso químico
es cierto que se requiere de otras máquinas y sensores a parte del brazo robótico, sin embargo trataremos de simular un proceso químico con la intervención del Robot Utadeo.
![](https://lh3.googleusercontent.com/proxy/5YTCUzNqvajsRA9GcnwrR1Iye_LVDgwa6rl0y_m7BsL-DPH503zEEHoNxsT6rVmftXoTy_hTdKkWzVgQlgD1G3gMoCJgrkIH04POUqM4w9jPvKvpN59boZnUhK3id1Su-C-jQzO1EUon6JI5UX8oljwqJlc3lTfWLrcZq8No8RrFtFlsFWwQBg)
> *"En este tipo de aplicaciones **la automatización no es opcional.** Es una necesidad. 	Debido a que, si no se hace, el personal que tenga contacto con la materia prima o el proceso puede sufrir **daños graves e incluso la muerte**". *

Una vez identificado el proceso, el siguiente paso es hacer el planeamiento de trayectorias, para ello es necesario saber las caracteristicas del robot, si has leído con detalle habrás notado que anteriormente mostramos el espacio de trabajo del Robot Utadeo, por lo tanto solo nos queda explicar sus grados de libertad.

[========]
## Grados de libertad
![](https://1.bp.blogspot.com/-YWXys-gXbP4/YKBsYzye7cI/AAAAAAAAANA/bH1TJGrZdMcc-4Td8NLyj2KuztSyO1_9ACNcBGAsYHQ/s16000/GradosLibertad.PNG)
dado que todos los servomotores son de 180º, se decide ubicar todo los servos en 0º cuando el robot está totalmente estirado por lo tanto se tendrá un rango de (-90º , 90º). lo cual nos permite planear las trayectorias con un mejor rango de movimiento.
	*Nota: Esto se hace en el URDF, para el robot en físico se aconseja ubicar todos los servomotores en 90º cuando el robot está totalmente estirado.*

## Usando la clase swif_serial y el urdf del robot para visualizarlo en swift y poder mover el robot
![](https://1.bp.blogspot.com/-rd1bBvtRfwo/YKB7vLtfNkI/AAAAAAAAANY/LmeOH8QALFIF1wdEw2Cuzv8ayw1djy0RACNcBGAsYHQ/w640-h346/Diagrama.PNG)
Con la información del espacio de trabajo, los grados de libertad y el proceso que se realizará, procedemos a diseñar las trayectorias.
La trayectorias se diseñan con el objetivo de recoger un envase, y luego pasar por diferentes etapas donde se vierten componentes químicos y finalmente vaciar estos componentes químicos en otra etapa del proceso automatizado.
![](https://1.bp.blogspot.com/-7JFY_beJpow/YKBxMswqhxI/AAAAAAAAANI/6aHH49UdIHs21Bnphjf2QTr8tYQyVLligCNcBGAsYHQ/w640-h566/Trayect.PNG)
![](https://1.bp.blogspot.com/-ogXLrkYNtIc/YKB2QfUyktI/AAAAAAAAANQ/aK0f70mFAeQ8o6J6Lyxn6miiqj9aHJDawCNcBGAsYHQ/s749/Trayec2.PNG)
En el siguiente video [Trayectorias](https://robotutadeo.blogspot.com/2021/05/trayectorias-con-robot.html "Trayectorias") se explica la última etapa de este proyecto.











