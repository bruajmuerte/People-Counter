{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import serial \n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "serial. __version__\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "sensor1=[]\n",
    "sensor2=[]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "there are -1 people in the room right now.\n",
      "there are 0 people in the room right now.\n",
      "there are 1 people in the room right now.\n",
      "there are 2 people in the room right now.\n",
      "there are 3 people in the room right now.\n",
      "there are 4 people in the room right now.\n",
      "there are 5 people in the room right now.\n"
     ]
    }
   ],
   "source": [
    "ser = serial.Serial('COM3', 9600) #Open the port to recive data from the aurdinuo board\n",
    "q=0 #variable to count how many people are in the room.\n",
    "for i in range(0,30): #the amount of time that the code will run.\n",
    "    b = ser.readline() # variable to save the data coming in from the board\n",
    "    data_str=bytes.decode(b) #Turning the bytes into strings\n",
    "    x=data_str.strip()# getting rid unwated characters\n",
    "    data=np.array(x) #saving data to an array to orginize that data.\n",
    "    y=x[0] #indexing all the data from senor 1\n",
    "    z=x[1] #indexing all the dtat from sensor 2 \n",
    "    sensor1.insert(0,y) #putting the newest data from sensor 1 at the start\n",
    "    sensor2.insert(0,z) #puting the newest data from sensore 2 at the top of the list\n",
    "    if sensor1[0]==sensor2[0]: #if statement if both lazers are in the same state\n",
    "        time.sleep(.1) #we done want anything to happen if they are both in the same state.\n",
    "    if sensor1[0]>sensor2[0]:#if statement if sensor 1 is triped and sensor 2 is not\n",
    "        q=q+1 #adding a person to the count in the room\n",
    "        print(f'there are {q} people in the room right now.') #printing the current total in the room     \n",
    "        while not sensor1[0]==sensor2[0]: # building the conditions for the dealy\n",
    "            time.sleep(.5) # building a delay \n",
    "            break #break out of the loop\n",
    "    if sensor1[0]<sensor2[0]: # if statement for when someone is leaving\n",
    "        q=q-1 #removing a person from the room\n",
    "        print(f'there are {q} people in the room right now.') #printing how many people are in the room\n",
    "        while not sensor1[0]==sensor2[0]:#building conditions to let someone walk trough\n",
    "            time.sleep(.5) # break\n",
    "            break # get out of the loop\n",
    "    time.sleep(.2) # sleep\n",
    "\n",
    "ser.close() # close the loop to the board."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "ser.close()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
