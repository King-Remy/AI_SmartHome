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

try:
    # GPIO.output(40,GPIO.LOW)
    fan_on()
    print("Fourth Relay ON")
    time.sleep(5)
    # fan_off()
    GPIO.cleanup()
    print("ALL OFF.....GOOD Bye !!!")

except KeyboardInterrupt:
    print("QUIT")
    GPIO.cleanup()
