#include <Servo.h>
#include <SoftwareSerial.h>

/*
 * 5 servomotor program to communicate with robotics-toolbox-python
 * @olmerg
 */
Servo Rotacion;
Servo Hombro;
Servo Codo;
Servo Muneca;
Servo Mano;
Servo Dedos;

int angulorotacion=0;
int angulohombro=0;
int angulocodo=0;
int angulomuneca=0;
int angulomano=0;
int angulodedos=0;
int i=1;

SoftwareSerial mySerial(6, 7); //pin rx y pin tx bluetooth modem

void setup(){
  Serial.begin(115200);
  mySerial.begin(9600);
  delay(3000);
  //pines en el arduino para cada señal del servomotor
  Rotacion.attach(2);
  Hombro.attach(3);
  Codo.attach(8);
  Muneca.attach(9);
  Mano.attach(11);
  Dedos.attach(12);
  home();
  Rotacion.write(angulorotacion);  
  Hombro.write(angulohombro);
  Codo.write(angulocodo);
  Muneca.write(angulomuneca);
  Mano.write(angulomano);
  Dedos.write(angulodedos);
  
}

void home(){
  // las posiciones iniciales de los servos para home
      angulorotacion=90;
      angulohombro=75;
      angulocodo=130;
      angulomuneca=120;
      angulomano=90;
      angulodedos=80;
  }
void loop(){
  unsigned char comando=0;
  if (mySerial.available()){ //bluetooth commands
    comando=mySerial.read();//leemos el byte
    if(comando=='K')angulorotacion+=10;//incrementamos 10
    else if(comando=='k')angulorotacion-=10;//decrementamos 10
    else if(comando=='L')angulohombro+=10;
    else if(comando=='l')angulohombro-=10;
    else if(comando=='M')angulocodo+=10;
    else if(comando=='m')angulocodo-=10;
    else if(comando=='N')angulomuneca+=10;
    else if(comando=='n')angulomuneca-=10;
    else if(comando=='O')angulomano+=10;
    else if(comando=='o')angulomano-=10;
    else if(comando=='P')angulodedos=0;
    else if(comando=='p')angulodedos=80;
    else if(comando=='h')home();
    angulorotacion=constrain(angulorotacion,0,180);//restringimos el valor de 0 a 180
    angulocodo=constrain(angulocodo,0,180);//restringimos el valor de 0 a 180
    angulomuneca=constrain(angulomuneca,0,180);//restringimos el valor de 0 a 180
    angulomano=constrain(angulomano,0,180);//restringimos el valor de 0 a 180
    angulohombro=constrain(angulohombro,0,180);
  }
  while(Serial.available()){//solo leeremos si hay un byte en el buffer
    comando=Serial.read();//leemos el byte
    if(comando=='A')angulorotacion+=1;//incrementamos 1
    else if(comando=='a')angulorotacion-=1;//decrementamos 1
    else if(comando=='B')angulohombro+=1;
    else if(comando=='b')angulohombro-=1;
    else if(comando=='C')angulocodo+=1;
    else if(comando=='c')angulocodo-=1;
    else if(comando=='D')angulomuneca+=1;
    else if(comando=='d')angulomuneca-=1;
    else if(comando=='E')angulomano+=1;
    else if(comando=='e')angulomano-=1;
    else if(comando=='G')angulodedos=0;
    else if(comando=='g')angulodedos=80;
    else if(comando=='h')home();
    angulorotacion=constrain(angulorotacion,0,180);//restringimos el valor de 0 a 180
    angulocodo=constrain(angulocodo,0,180);//restringimos el valor de 0 a 180
    angulomuneca=constrain(angulomuneca,0,180);//restringimos el valor de 0 a 180
    angulomano=constrain(angulomano,0,180);//restringimos el valor de 0 a 180
    angulohombro=constrain(angulohombro,0,180);
    
  }
  Rotacion.write(angulorotacion);  
  Hombro.write(angulohombro);
  Codo.write(angulocodo);
  Muneca.write(angulomuneca);
  Mano.write(angulomano);
  Dedos.write(angulodedos);

  
  if(i==20){
  i=0;
  Serial.print("*");
  Serial.print(angulorotacion-90);
  Serial.print(',');
  Serial.print(angulohombro-75);
  Serial.print(',');
  Serial.print(angulocodo-20);
  Serial.print(',');
  Serial.print(angulomuneca-90);
  Serial.print(',');
  Serial.print(angulomano-90);
  Serial.print(',');
  Serial.print(angulodedos);
  Serial.println('*');
  }else{i++;}
  
  delay(5);
}//End loop
