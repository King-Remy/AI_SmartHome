import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(40,GPIO.OUT)
GPIO.output(40,GPIO.HIGH)


def  fan_off():  
    GPIO.output(40,GPIO.HIGH)
    return 

def  fan_on(): 
     GPIO.output(40,GPIO.LOW)
     return 


def fan_control(number_person, temp):

    if number_person == 0:  
        fan_off()
        print("off")
    else:
        fan_on()
        print("on")

    return f"The total number of people: {number_person}"

try:
    fan_control(0, 30)
    time.sleep(2)
    GPIO.cleanup()
    print("ALL OFF.....GOOD Bye !!!")

except KeyboardInterrupt:
    print("QUIT")
    GPIO.cleanup()
