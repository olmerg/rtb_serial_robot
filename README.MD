[![Powered by the Robotics Toolbox](https://raw.githubusercontent.com/petercorke/robotics-toolbox-python/master/.github/svg/rtb_powered.min.svg)](https://github.com/petercorke/robotics-toolbox-python)

## Robots Utadeo Arduino

Esta libreria se conecta por serial a los robots basados en servos de aeromodelismo para lograr el movimiento del robot

- Instalación
```
    pip install pyserial
    pip install roboticstoolbox-python
```
- cargar el archivo Arduino_firmware.ino en el arduino uno

- Identificar el puerto serial con el que se identifica el arduino al conectarlo al pc

- modificar el metodo __main__ de example.py con el puerto requerido y el robot definido en robotics-toolbox 

- definir sus trayectorias

- ejecutar el script de ejemplo
```
    python example.py
```


Realizado por el curso de Robotica Industrial 2021-I de Ingeniería en automatización de Universidad Jorge Tadeo Lozano

Profesor: Olmer Garcia Bedoya (@olmerg)

Grupo 1: Jonathan Sechagua Guarnizo - Diego Carreño - Jorge Lemos - Alberto Roa



