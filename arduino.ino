int photogatePin = 6; //create global variable for pin assignment to sensor
int photogatePin2 = 2;
int LEDpin = 13; //create global variable for pin assignment to LED
int photogateStatus; //create global variable for photogate status: LOW=blocked, HIGH=unblocked
int oldStatus = HIGH;
unsigned long timeus = 0; //Time in us
String gate1 = "0";
String gate2 = "0";


void setup() 
  {
   Serial.begin(9600);           // set up Serial library at 9600 bps
    pinMode(LEDpin, OUTPUT);
    //Serial.println("Vernier Format 1");
    //Serial.println("Photogate blocked times taken using Ardunio");
    //Serial.print("Time");
    //Serial.print("us");

   
    
  };// end of setup

void loop ()
{
//delay(100);
photogateStatus = digitalRead(photogatePin);//low when blocked
   if (photogateStatus == HIGH)
   { 
    
   digitalWrite(LEDpin, LOW);// turn off LED
   gate1 = "1";
   delay(500);
      
   }
   else 
   {
   digitalWrite(LEDpin, HIGH);// turn on LED
   gate1 = "0";
   
   }
    
   photogateStatus = digitalRead(photogatePin2);//low when blocked
   if (photogateStatus == HIGH)
   { 
    digitalWrite(LEDpin, LOW);// turn off LED
    gate2 = "1";
    delay(1000);
   }
   else 
   {
    
    digitalWrite(LEDpin, HIGH);// turn on LED
    gate2 = "0";
     
   }
   String gates = gate1 + gate2;
    Serial.println(gates);
   }
   
// end of loop
