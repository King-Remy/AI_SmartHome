import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BOARD)

GPIO.setup(40,GPIO.OUT)
GPIO.output(40,GPIO.HIGH)
person_state = None 

def  fan_off():  
    GPIO.output(40,GPIO.HIGH)
    return 

def  fan_on(): 
     GPIO.output(40,GPIO.LOW)
     return 


def fan_control_with_image(temp):
    number_of_person = len(os.listdir("inference"))
    print(number_of_person)
    if number_of_person == 0: 
        fan_off()
        print("off")
    else:
        fan_on()
        print("on")
        person_state = True  
        # time.sleep(10)
        os.system("rm -rf inference/person.jpeg")
    return f"The total number of people: {number_of_person}"


while True: 
    try:
        fan_control_with_image(30)
        time.sleep(2)
        # GPIO.cleanup()
        print("ALL OFF.....GOOD Bye !!!")

    except KeyboardInterrupt:
        print("QUIT")
        GPIO.cleanup()


