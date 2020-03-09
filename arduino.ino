int photogatePin = 6; //create global variable for pin assignment to sensor
int photogatePin2 = 2;
int LEDpin = 13; //create global variable for pin assignment to LED
int photogateStatus; //create global variable for photogate status: LOW=blocked, HIGH=unblocked
int oldStatus = HIGH;
unsigned long timeus = 0; //Time in us

void setup() 
  {
   Serial.begin(9600);           // set up Serial library at 9600 bps
    pinMode(LEDpin, OUTPUT);
    Serial.println("Vernier Format 1");
    Serial.println("Photogate blocked times taken using Ardunio");
    Serial.print("Time");
    Serial.print("us");

   
    
  };// end of setup

void loop ()
{
//time.sleep(.1);
photogateStatus = digitalRead(photogatePin);//low when blocked
   if (photogateStatus == HIGH)
   { 
    digitalWrite(LEDpin, HIGH);// turn on LED
    Serial.println("Sensor1:1");
      
   }
   else digitalWrite(LEDpin, LOW);// turn off LED
   Serial.println("sensor1:0");

    
   photogateStatus = digitalRead(photogatePin2);//low when blocked
   if (photogateStatus == HIGH)
   { 
    digitalWrite(LEDpin, HIGH);// turn on LED
    Serial.println("Sensor2:1");   
   }
   else digitalWrite(LEDpin, LOW);// turn off LED
    Serial.println("Sensor2:0");
   }
   
// end of loop
