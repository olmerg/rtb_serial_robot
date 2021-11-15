#include <Servo.h>
#include <SoftwareSerial.h>
/*
 * 5 servomotor program to communicate with robotics-toolbox-python
 * @olmerg
 */
Servo Cadera;
Servo HombroD;
//Servo HombroI;
Servo Codo;
Servo Muneca;
Servo Camara;

int anguloCadera=0;
int anguloHombroD=0;
//int anguloHombroI=0;
int anguloCodo=0;
int anguloMuneca=0;
int anguloCamara=0;
int i=1;

SoftwareSerial mySerial(6, 7); //pin rx y pin tx bluetooth modem

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

void home(){
  // las posiciones iniciales de los servos para home
      anguloCadera=90;
      anguloHombroD=81;
      //anguloHombroI=84;
      anguloCodo=110;
      anguloMuneca=100;
      anguloCamara=81;
  }
void loop(){
  unsigned char comando=0;
  if (mySerial.available()){ //bluetooth commands
    comando=mySerial.read();//leemos el byte
    if(comando=='K')anguloCadera+=10;//incrementamos 10
    else if(comando=='k')anguloCadera-=10;//decrementamos 10
    else if(comando=='L')anguloHombroD+=10;
    else if(comando=='l')anguloHombroD-=10;
    //else if(comando=='M')anguloHombroI+=10;
    //else if(comando=='m')anguloHombroI-=10;
    else if(comando=='N')anguloCodo+=10;
    else if(comando=='n')anguloCodo-=10;
    else if(comando=='O')anguloMuneca+=10;
    else if(comando=='o')anguloMuneca-=10;
    else if(comando=='P')anguloCamara=0;
    else if(comando=='p')anguloCamara=80;
    else if(comando=='h')home();
    anguloCadera=constrain(anguloCadera,0,180);//restringimos el valor de 0 a 180
    anguloHombroD=constrain(anguloHombroD,0,180);//restringimos el valor de 0 a 180
    //anguloHombroI=constrain(anguloHombroI,0,180);//restringimos el valor de 0 a 180
    anguloCodo=constrain(anguloCodo,0,180);//restringimos el valor de 0 a 180
    anguloMuneca=constrain(anguloMuneca,0,180);
    anguloCamara=constrain(anguloCamara,0,180);

  }

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
  
  Cadera.write(anguloCadera);  
  HombroD.write(anguloHombroD);
  //HombroI.write(anguloHombroI);
  Codo.write(anguloCodo);
  Muneca.write(anguloMuneca);
  Camara.write(anguloCamara);

if(i==20){
  i=0;
  Serial.print("*");
  Serial.print(anguloCadera-90);
  Serial.print(',');
  Serial.print(anguloHombroD-81);
  Serial.print(',');
  Serial.print(anguloCodo-110);
  Serial.print(',');
  Serial.print(anguloMuneca-100);
  Serial.print(',');
  Serial.print(anguloCamara-81);
  Serial.println('*');
  }
else{i++;}

  delay(5);
}//End loop