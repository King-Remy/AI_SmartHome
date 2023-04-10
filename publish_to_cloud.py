import sys
import threading
import time
import json
import board
import adafruit_dht
import random
import sys
import time
from Adafruit_IO import MQTTClient


from secret import user, password
import  binascii
import base64
from PIL import  Image 
import os  


dhtDevice = adafruit_dht.DHT11(board.D4)
dhtDevice = adafruit_dht.DHT11(board.D4, use_pulseio=False)
# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = password

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = user


# Define callback functions which will be called when certain events happen.
def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to feed changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.
    print('Connected to Adafruit IO!  Listening for DemoFeed changes...')
    # Subscribe to changes on a feed named DemoFeed.
    # client.subscribe('DemoFeed')

def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, payload):
    # Message function will be called when a subscribed feed has a new value.
    # The feed_id parameter identifies the feed, and the payload parameter has
    # the new value.
    print('Feed {0} received new value: {1}'.format(feed_id, payload))

def compressMe(file, verbose = False):
    
      # Get the path of the file
    filepath = os.path.join(os.getcwd(), 
                            file)
      
    # open the image
    picture = Image.open(filepath)
      
    # Save the picture with desired quality
    # To change the quality of image,
    # set the quality variable at
    # your desired level, The more 
    # the value of quality variable 
    # and lesser the compression
    picture.save("compressed_person.jpeg", 
                 "JPEG", 
                 optimize = True, 
                 quality = 10)
    return

# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message

# Connect to the Adafruit IO server.
client.connect()

# Now the program needs to use a client loop function to ensure messages are
# sent and received.  There are a few options for driving the message loop,
# depending on what your program needs to do.

# The first option is to run a thread in the background so you can continue
# doing things in your program.
client.loop_background()
# Now send new values every 10 seconds.
print('Publishing a new message every 10 seconds (press Ctrl-C to quit)...')


while True:
   try: 
    #   value = random.randint(0, 100)
      temperature_c = dhtDevice.temperature
      humidity = dhtDevice.humidity
      compressMe("inference/person.jpeg")
      with open("compressed_person.jpeg", "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())
        print(converted_string)
    #   client.publish('image', converted_string.decode("utf-8").strip())
      client.publish('image', converted_string.decode("utf-8").strip())
      client.publish('humid_reading', humidity)
      client.publish('temp_reading', temperature_c)
      time.sleep(5)
   
   except RuntimeError as error:
      # Errors happen fairly often, DHT's are hard to read, just keep going
      print(error.args[0])
      time.sleep(5.0)
      continue


# Another option is to pump the message loop yourself by periodically calling
# the client loop function.  Notice how the loop below changes to call loop
# continuously while still sending a new message every 10 seconds.  This is a
# good option if you don't want to or can't have a thread pumping the message
# loop in the background.
#last = 0
#print('Publishing a new message every 10 seconds (press Ctrl-C to quit)...')
#while True:
#   # Explicitly pump the message loop.
#   client.loop()
#   # Send a new message every 10 seconds.
#   if (time.time() - last) >= 10.0:
#       value = random.randint(0, 100)
#       print('Publishing {0} to DemoFeed.'.format(value))
#       client.publish('DemoFeed', value)
#       last = time.time()

# The last option is to just call loop_blocking.  This will run a message loop
# forever, so your program will not get past the loop_blocking call.  This is
# good for simple programs which only listen to events.  For more complex programs
# you probably need to have a background thread loop or explicit message loop like
# the two previous examples above.
#client.loop_blocking()

