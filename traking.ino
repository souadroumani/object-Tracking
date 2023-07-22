#include<Servo.h>
Servo servoA1;
Servo servoB1;

int q=100;
int p=100;
int Z=0 ;
bool u=false ;
bool d=false ;
bool s1=false ;
bool l=false ;
bool r=false ;
bool s2=false ;

int down(int q){
   q--;
   servoA1.write(q);  
   delay(50);
   return q;
  }

int up(int q){
   q++;
   servoA1.write(q);  
   delay(50);
   return q;
  }

int Stop1(int q){
   servoA1.write(q);  
   return q;
  }

int right(int p){
   p--;
   servoB1.write(p);  
   delay(50);
   return p;
  }

int left(int p){
   p++;
   servoB1.write(p);  
   delay(50);
   return p;
  }

int Stop2(int p){
   servoB1.write(p);  
   return p;
  }

  
void setup() {
  Serial.begin(9600);
  servoA1.attach(10);
  servoB1.attach(11);
  
  servoA1.write(100);
  servoB1.write(100);

}

void loop() {
if(Serial.available()>0){

//  for(int i=0 ; i<50 ;i++ ){
  char Y = Serial.read();
    
    switch(Y){
      
      case 'r' :
        l = false ;
        r = true ;
        s2 = false ;
        break;

      case 'l' :
        l = true ;
        r = false ;
        s2 = false ;
        break;

     case 'x' :
        l = false ;
        r = false ;
        s2 = true ;
        break;
      

      
    
      case 'u' :
        u = true ;
        d = false ;
        s1 = false ; 
        break;
        
      case 'd' :
        u = false ;
        d = true ;
        s1 = false ;
        break;

      case 's' :
        u = false ;
        d = false ;
        s1 = true ;
        break;

    }
}


  if (l == true ){
        p = left(p);
        }

      else if (r == true){
        p = right(p);
        }

      else if (s2 == true){
        p = Stop2(p);
        }

        
      if (u == true ){
        q = down(q);
        
        }

      else if (d == true){
        q = up(q);
        
        }

      else if(s1 == true){
        q = Stop1(q);
        
        }
}



      

 
