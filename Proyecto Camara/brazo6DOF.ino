#include <Servo.h>

/*
 * 5 servomotor program to communicate with robotics-toolbox-python
 * @olmerg
 */
Servo Cadera;
Servo HombroD;
Servo HombroI;
Servo Codo;
Servo Muneca;
Servo Camara;

int anguloCadera=0;
int anguloHombroD=0;
int anguloHombroI=0;
int anguloCodo=0;
int anguloMuneca=0;
int anguloCamara=0;
int i=1;

void setup(){
  Serial.begin(115200);
  delay(3000);
  //pines en el arduino para cada señal del servomotor
  Cadera.attach(2);
  HombroD.attach(3);
  HombroI.attach(8);
  Codo.attach(9);
  Muneca.attach(11);
  Camara.attach(12);
  home();
  Cadera.write(anguloCadera);  
  HombroD.write(anguloHombroD);
  HombroI.write(anguloHombroI);
  Codo.write(anguloCodo);
  Muneca.write(anguloMuneca);
  Camara.write(anguloCamara);
  
}

void home(){
  // las posiciones iniciales de los servos para home
      anguloCadera=90;
      anguloHombroD=81;
      anguloHombroI=84;
      anguloCodo=110;
      anguloMuneca=100;
      anguloCamara=81;
  }
  void horizontal(){
  // las posiciones iniciales de los servos para home
      anguloCadera=90;
      anguloHombroD=143;
      anguloHombroI=84;
      anguloCodo=110;
      anguloMuneca=100;
      anguloCamara=81;
  }
void loop(){
  unsigned char comando=0;
  while(Serial.available()){//solo leeremos si hay un byte en el buffer
    comando=Serial.read();//leemos el byte
    if(comando=='A')anguloCadera+=1;//incrementamos 1
    else if(comando=='a')anguloCadera-=1;//decrementamos 1
    else if(comando=='B'){anguloHombroD+=1;
    anguloHombroI-=1;}
    else if(comando=='b'){anguloHombroD-=1;
    anguloHombroI+=1;}
    else if(comando=='D')anguloCodo+=1;
    else if(comando=='d')anguloCodo-=1;
    else if(comando=='E')anguloMuneca+=1;
    else if(comando=='e')anguloMuneca-=1;
    else if(comando=='G')anguloCamara+=1;
    else if(comando=='g')anguloCamara-=1;
    else if(comando=='h')home();
    else if(comando=='H')horizontal();
    anguloCadera=constrain(anguloCadera,0,180);//restringimos el valor de 0 a 180
    anguloHombroD=constrain(anguloHombroD,0,180);//restringimos el valor de 0 a 180
    //anguloHombroI=constrain(anguloHombroI,0,180);//restringimos el valor de 0 a 180
    anguloCodo=constrain(anguloCodo,0,180);//restringimos el valor de 0 a 180
    anguloMuneca=constrain(anguloMuneca,0,180);
    anguloCamara=constrain(anguloCamara,0,180);
    delayMicroseconds(10);
  }
  Cadera.write(anguloCadera);  
  HombroD.write(anguloHombroD);
  HombroI.write(anguloHombroI);
  Codo.write(anguloCodo);
  Muneca.write(anguloMuneca);
  Camara.write(anguloCamara);

  Serial.print("*");
  Serial.print(anguloCadera);
  Serial.print(',');
  Serial.print(anguloHombroD);
  Serial.print(',');
  Serial.print(anguloHombroI);
  Serial.print(',');
  Serial.print(anguloCodo);
  Serial.print(',');
  Serial.print(anguloMuneca);
  Serial.print(',');
  Serial.print(anguloCamara);
  Serial.println('*');

  delay(5);
}//End loop
